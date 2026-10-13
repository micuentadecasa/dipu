"""Deep validation and deterministic duplicate screening for question records.

The public interface deliberately separates deterministic checks from reviewer
work. Exact, lexical, and near-lexical checks are reproducible here; semantic
and concept-level checks remain ``uncertain`` until an independent reviewer
records a decision in the question record.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import date
import difflib
import hashlib
import json
from pathlib import Path
import re
import unicodedata
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "docs/question-bank/question-record.schema.json"
_OPTIONS = ("option_a", "option_b", "option_c", "option_d")
_CONTENT_FIELDS = ("topic_num", "learning_objective_id", "question", *_OPTIONS, "correct")


class QuestionRecordError(ValueError):
    """Raised when a candidate cannot satisfy the validated-record contract."""


def canonical_text(value: str) -> str:
    """Normalize content for stable identity without deleting punctuation."""
    if not isinstance(value, str):
        raise TypeError("question content must be text")
    normalized = unicodedata.normalize("NFKC", value).casefold()
    return " ".join(normalized.split())


def lexical_key(value: str) -> str:
    """Normalize text for accent-insensitive lexical duplicate screening."""
    decomposed = unicodedata.normalize("NFKD", canonical_text(value))
    without_marks = "".join(c for c in decomposed if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "", without_marks)


def _word_tokens(value: str) -> list[str]:
    decomposed = unicodedata.normalize("NFKD", canonical_text(value))
    without_marks = "".join(c for c in decomposed if not unicodedata.combining(c))
    return re.findall(r"[a-z0-9]+", without_marks)


def answer_leakage_errors(record: dict[str, Any]) -> list[str]:
    """Reject stems that disclose an option verbatim or near-verbatim.

    Short tokens such as ``JSON`` or ``GET`` are intentionally ignored: they
    are domain vocabulary, not answer text. Longer option phrases must not be
    repeated in the question, including after accent/punctuation folding.
    """
    question = canonical_text(record.get("question", ""))
    question_lexical = lexical_key(question)
    errors = []
    for name in _OPTIONS:
        option = canonical_text(record.get(name, ""))
        option_lexical = lexical_key(option)
        if len(option_lexical) < 12:
            continue
        if option in question or option_lexical in question_lexical:
            errors.append(f"answer leakage: {name} is repeated in the question")
            continue
        similarity = difflib.SequenceMatcher(None, option_lexical, question_lexical).ratio()
        option_words = _word_tokens(option)
        question_words = _word_tokens(question)
        longest_window_match = max(
            (
                difflib.SequenceMatcher(None, option_words, question_words[start : start + size]).find_longest_match(
                    0, len(option_words), 0, min(size, len(question_words[start : start + size]))
                ).size
                for size in range(max(1, len(option_words) - 2), len(option_words) + 3)
                for start in range(max(1, len(question_words) - size + 1))
            ),
            default=0,
        )
        if (len(option_lexical) >= 18 and similarity >= 0.86) or (len(option_words) >= 5 and longest_window_match / len(option_words) >= 0.9):
            errors.append(f"answer leakage: {name} is near-verbatim in the question")
    return errors


def _content_payload(record: dict[str, Any]) -> dict[str, Any]:
    return {
        field: record[field] if field == "topic_num" else canonical_text(record[field])
        for field in _CONTENT_FIELDS
    }


def stable_id_for(record: dict[str, Any]) -> str:
    """Return the idempotent stable key for a record's tested proposition."""
    topic = int(record["topic_num"])
    objective = str(record["learning_objective_id"])
    match = re.fullmatch(r"t[0-9]{2}-lo-(.+)", objective)
    if topic not in range(1, 41) or not match:
        raise QuestionRecordError("stable IDs require topic 1-40 and a tNN-lo-* objective")
    digest = hashlib.sha256(
        json.dumps(_content_payload(record), ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()[:24]
    slug = re.sub(r"[^a-z0-9._-]+", "-", match.group(1).casefold()).strip("-")
    if not slug:
        raise QuestionRecordError("learning objective has no stable slug")
    return f"qb-t{topic:02d}-{slug}-{digest}"


def _schema_errors(record: dict[str, Any], schema_path: Path) -> list[str]:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = []
    for error in sorted(validator.iter_errors(record), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in error.path) or "$"
        errors.append(f"{location}: {error.message}")
    return errors


def validate_record(record: dict[str, Any], schema_path: Path = SCHEMA_PATH) -> list[str]:
    """Return all structural and validated-state errors; an empty list is valid."""
    errors = _schema_errors(record, schema_path)
    if errors:
        return errors

    errors.extend(answer_leakage_errors(record))

    option_values = [canonical_text(record[name]) for name in _OPTIONS]
    if len(set(option_values)) != len(option_values):
        errors.append("options must be distinct after canonical normalization")
    correct_value = canonical_text(record[f"option_{record['correct'].lower()}"])
    if not correct_value:
        errors.append("the selected correct option must be non-empty")

    expected_stable_id = stable_id_for(record)
    if record["stable_id"] != expected_stable_id:
        errors.append(f"stable_id does not match canonical content: expected {expected_stable_id}")

    if record["status"] == "validated":
        verification = record["verification"]
        if verification["reviewer_decision"] != "accepted":
            errors.append("validated records require reviewer_decision=accepted")
        for name in ("answer", "explanation"):
            if verification[name]["status"] != "passed":
                errors.append(f"validated records require verification.{name}.status=passed")
        for name, result in record["deduplication"].items():
            if result["status"] != "unique":
                errors.append(f"validated records require deduplication.{name}.status=unique")
        if any(source["verified_at"] is None for source in record["sources"]):
            errors.append("validated records cannot cite a source without verified_at")
        if record["question_type"] in ("code", "sql"):
            execution = verification.get("code_or_sql")
            if not execution or execution["status"] != "passed":
                errors.append("validated code/sql records require a passed code_or_sql check")

    return errors


@dataclass(frozen=True)
class DuplicateResult:
    status: str
    checked_at: str
    basis: str
    matched_stable_id: str | None = None
    score: float | None = None

    def as_dict(self) -> dict[str, Any]:
        return {key: value for key, value in asdict(self).items() if value is not None}


@dataclass(frozen=True)
class DuplicateScreen:
    exact: DuplicateResult
    lexical: DuplicateResult
    near_lexical: DuplicateResult
    semantic: DuplicateResult
    concept: DuplicateResult

    def as_dict(self) -> dict[str, dict[str, Any]]:
        return {name: getattr(self, name).as_dict() for name in ("exact", "lexical", "near_lexical", "semantic", "concept")}


def _best_match(
    candidate: str,
    existing: Iterable[dict[str, Any]],
    key,
    threshold: float = 1.0,
) -> tuple[dict[str, Any] | None, float]:
    best_record = None
    best_score = 0.0
    for record in existing:
        score = 1.0 if key(candidate) == key(record["question"]) else difflib.SequenceMatcher(None, key(candidate), key(record["question"])).ratio()
        if score > best_score:
            best_record, best_score = record, score
    return (best_record if best_score >= threshold else None), best_score


def screen_duplicates(
    candidate: dict[str, Any],
    existing: Iterable[dict[str, Any]],
    checked_at: str | None = None,
    near_threshold: float = 0.92,
) -> DuplicateScreen:
    """Screen five duplicate levels without pretending semantic review is automated."""
    checked_at = checked_at or date.today().isoformat()
    existing_records = list(existing)
    digest = stable_id_for(candidate)

    exact_match = next((record for record in existing_records if record.get("stable_id") == digest), None)
    exact = DuplicateResult(
        "duplicate" if exact_match else "unique",
        checked_at,
        "stable ID/content digest comparison",
        exact_match.get("stable_id") if exact_match else None,
        1.0 if exact_match else None,
    )

    candidate_lexical = lexical_key(candidate["question"])
    lexical_match = next(
        (record for record in existing_records if lexical_key(record["question"]) == candidate_lexical),
        None,
    )
    lexical = DuplicateResult(
        "duplicate" if lexical_match else "unique",
        checked_at,
        "accent-folded punctuation-free prompt key",
        lexical_match.get("stable_id") if lexical_match else None,
        1.0 if lexical_match else None,
    )

    near_match, near_score = _best_match(candidate["question"], existing_records, lexical_key, near_threshold)
    near = DuplicateResult(
        "duplicate" if near_match else "unique",
        checked_at,
        f"SequenceMatcher over lexical prompt keys; threshold={near_threshold:.2f}",
        near_match.get("stable_id") if near_match else None,
        round(near_score, 6) if near_match else None,
    )

    unresolved_basis = "requires independent semantic reviewer decision against the tested proposition"
    semantic = DuplicateResult("uncertain", checked_at, unresolved_basis)
    concept = DuplicateResult("uncertain", checked_at, "requires reviewer decision against the learning objective/concept")
    return DuplicateScreen(exact, lexical, near, semantic, concept)
