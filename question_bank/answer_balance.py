"""Source-reviewed option reauthoring to prevent answer-length leakage.

The balancer never changes a question's correct proposition.  It replaces only
incorrect choices with already-reviewed correct propositions from other
questions, preferring the same source and topic and falling back to the
nearest reviewed proposition by length.  This keeps distractors factual,
source-backed, and semantically wrong for the current stem without adding
padding or truncating authored text.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
import re
import unicodedata
from typing import Any, Iterable

from .validation import canonical_text, stable_id_for

OPTION_NAMES = ("option_a", "option_b", "option_c", "option_d")
CORRECT_LETTERS = "ABCD"
DEFAULT_MAX_GAP = 10


def answer_length_gap(record: dict[str, Any]) -> float:
    """Return correct-option length minus the mean distractor length."""
    correct_index = CORRECT_LETTERS.index(record["correct"])
    lengths = [len(record[name]) for name in OPTION_NAMES]
    distractors = lengths[:correct_index] + lengths[correct_index + 1 :]
    return lengths[correct_index] - (sum(distractors) / len(distractors))


def answer_length_leakage_errors(
    record: dict[str, Any], max_gap: int = 20
) -> list[str]:
    """Reject a uniquely longest correct option when the gap is conspicuous.

    Ties are deliberately allowed: a learner cannot identify the correct
    proposition from length when several choices share the longest length.
    The threshold is a quality gate, not a request to make prose identical.
    """
    correct_index = CORRECT_LETTERS.index(record["correct"])
    lengths = [len(record[name]) for name in OPTION_NAMES]
    correct_length = lengths[correct_index]
    distractors = lengths[:correct_index] + lengths[correct_index + 1 :]
    if correct_length > max(distractors) and answer_length_gap(record) > max_gap:
        return [
            "answer-length leakage: the correct option is uniquely longer "
            f"than distractors by {answer_length_gap(record):.1f} characters"
        ]
    return []


def _lexical_key(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", canonical_text(value))
    without_marks = "".join(c for c in decomposed if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "", without_marks)


def _would_leak(question_key: str, option_key: str) -> bool:
    # Donors are already source-reviewed. The exact lexical check is the
    # relevant fast guard here; full answer-leakage validation runs after the
    # reauthoring and catches near-verbatim stems as a final gate.
    return len(option_key) >= 12 and option_key in question_key


def _source_ids(record: dict[str, Any]) -> tuple[str, ...]:
    return tuple(source["source_id"] for source in record.get("sources", []))


def _stable_key(record: dict[str, Any], index: int) -> str:
    return str(record.get("stable_id") or f"legacy-{record.get('topic_num', 0)}-{index:04d}")


@dataclass(frozen=True)
class _Prepared:
    index: int
    record: dict[str, Any]
    correct_text: str
    correct_length: int
    correct_lexical: str
    question_lexical: str
    source_ids: tuple[str, ...]
    objective: str | None
    topic: int | None
    stable_key: str


@dataclass(frozen=True)
class _Candidate:
    distance: int
    source_priority: int
    topic_priority: int
    stable_key: str
    text: str
    source_records: tuple[dict[str, Any], ...]
    source_ids: tuple[str, ...]


def _candidate_pool(
    target: _Prepared,
    prepared: list[_Prepared],
    source_priority: bool,
    topic_priority: bool,
) -> list[_Candidate]:
    target_record = target.record
    target_options = {target_record[name] for name in OPTION_NAMES}
    target_sources = set(target.source_ids)
    candidates: list[_Candidate] = []
    for donor in prepared:
        if donor.index == target.index or (
            target.objective and donor.objective == target.objective
        ):
            continue
        if donor.correct_text in target_options or _would_leak(
            target.question_lexical, donor.correct_lexical
        ):
            continue
        source_match = bool(target_sources.intersection(donor.source_ids))
        topic_match = donor.topic == target.topic
        if source_priority and not source_match and not topic_match:
            continue
        candidates.append(
            _Candidate(
                distance=abs(donor.correct_length - target.correct_length),
                source_priority=0 if source_match else 1,
                topic_priority=0 if topic_match else 1,
                stable_key=donor.stable_key,
                text=donor.correct_text,
                source_records=tuple(deepcopy(donor.record.get("sources", []))),
                source_ids=donor.source_ids,
            )
        )
    return sorted(
        candidates,
        key=lambda candidate: (
            candidate.distance,
            candidate.source_priority if source_priority else 0,
            candidate.topic_priority if topic_priority else 0,
            candidate.stable_key,
        ),
    )


def _choose_three(candidates: Iterable[_Candidate]) -> list[_Candidate]:
    chosen: list[_Candidate] = []
    seen: set[str] = set()
    for candidate in candidates:
        if candidate.text in seen:
            continue
        seen.add(candidate.text)
        chosen.append(candidate)
        if len(chosen) == 3:
            return chosen
    return chosen


def balance_records(
    records: Iterable[dict[str, Any]],
    *,
    max_local_gap: int = DEFAULT_MAX_GAP,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Balance choices using the original records as reviewed donor facts.

    Returns ``(balanced_records, audit_entries)``.  Every target's correct
    option text and letter are copied unchanged.  The returned records are
    deep copies and may include the donor source records required to preserve
    provenance for reauthored distractors.
    """
    originals = [deepcopy(record) for record in records]
    balanced = [deepcopy(record) for record in records]
    prepared = [
        _Prepared(
            index=index,
            record=record,
            correct_text=record[f"option_{record['correct'].lower()}"],
            correct_length=len(record[f"option_{record['correct'].lower()}"]),
            correct_lexical=_lexical_key(record[f"option_{record['correct'].lower()}"]),
            question_lexical=_lexical_key(record["question"]),
            source_ids=_source_ids(record),
            objective=record.get("learning_objective_id"),
            topic=record.get("topic_num"),
            stable_key=_stable_key(record, index),
        )
        for index, record in enumerate(originals)
    ]
    audit: list[dict[str, Any]] = []

    for index, target in enumerate(originals):
        target_info = prepared[index]
        preferred = _choose_three(
            _candidate_pool(
                target_info,
                prepared,
                source_priority=True,
                topic_priority=True,
            )
        )
        proposed = deepcopy(target)
        correct_name = f"option_{target['correct'].lower()}"
        if len(preferred) == 3:
            for name, candidate in zip(
                (option for option in OPTION_NAMES if option != correct_name), preferred
            ):
                proposed[name] = candidate.text
            if abs(answer_length_gap(proposed)) > max_local_gap:
                preferred = []

        if len(preferred) != 3:
            preferred = _choose_three(
                _candidate_pool(
                    target_info,
                    prepared,
                    source_priority=False,
                    topic_priority=False,
                )
            )
            if len(preferred) != 3:
                raise ValueError(
                    f"not enough reviewed donor propositions for {_stable_key(target, index)}"
                )
            proposed = deepcopy(target)
            for name, candidate in zip(
                (option for option in OPTION_NAMES if option != correct_name), preferred
            ):
                proposed[name] = candidate.text

        if len({proposed[name] for name in OPTION_NAMES}) != 4:
            raise ValueError(f"donor propositions are not distinct for {_stable_key(target, index)}")

        donor_sources: list[dict[str, Any]] = []
        seen_sources: set[tuple[str, str]] = set()
        for source in [*target.get("sources", []), *(source for candidate in preferred for source in candidate.source_records)]:
            key = (source["source_id"], source["citation"])
            if key not in seen_sources:
                seen_sources.add(key)
                donor_sources.append(deepcopy(source))
        if donor_sources:
            proposed["sources"] = donor_sources

        balanced[index] = proposed
        audit.append(
            {
                "target_key": _stable_key(target, index),
                "objective_id": target.get("learning_objective_id"),
                "topic_num": target.get("topic_num"),
                "correct": target["correct"],
                "correct_text_before": target[correct_name],
                "correct_text_after": proposed[correct_name],
                "before_lengths": [len(target[name]) for name in OPTION_NAMES],
                "after_lengths": [len(proposed[name]) for name in OPTION_NAMES],
                "donors": [
                    {
                        "stable_id": candidate.stable_key,
                        "source_ids": list(candidate.source_ids),
                        "length": len(candidate.text),
                    }
                    for candidate in preferred
                ],
                "gap_after": round(answer_length_gap(proposed), 6),
            }
        )
    return balanced, audit


def refresh_stable_identity(record: dict[str, Any]) -> dict[str, Any]:
    """Recompute the stable ID after an option reauthoring revision."""
    updated = deepcopy(record)
    updated["stable_id"] = stable_id_for(updated)
    return updated
