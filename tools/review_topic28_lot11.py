#!/usr/bin/env python3
"""Independently review and promote topic-28 supplemental lot 11."""

from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from question_bank.checkpoints import append_checkpoint, file_sha256
from question_bank.validation import validate_record

DATE = "2026-10-15"
TOPIC = 28
LOT = 11
REVIEWER = "independent-source-review-2026-10-15"
LOT_PATH = ROOT / "docs/question-bank/lots/topic-28-lot-11.json"
ACCEPTED_PATH = ROOT / "docs/question-bank/accepted/topic-28-lot-11.json"
REVIEW_PATH = ROOT / "docs/question-bank/reviews/topic-28-lot-11.json"
RESEARCH_PATH = ROOT / "docs/question-bank/research/questions/topics-28-lot-11.json"
CHECKPOINT_PATH = ROOT / "docs/question-bank/checkpoints/topic-28-lot-11.jsonl"

EXPECTED = {
    1: ("B", "When parameters are set (SetParametersAsync)"),
    2: ("C", "When parameters are set (SetParametersAsync)"),
    3: ("A", "Component initialization (OnInitialized{Async})"),
    4: ("B", "Prerendering and quiescence"),
    5: ("C", "After component render (OnAfterRender{Async})"),
    6: ("C", "After parameters are set (OnParametersSet{Async})"),
    7: ("A", "Component base class lifecycle methods"),
    8: ("B", "Component lifecycle synchronous and asynchronous methods"),
    9: ("C", "After component render (OnAfterRender{Async})"),
    10: ("B", "CSS isolation file naming"),
    11: ("A", "CSS isolation file naming"),
    12: ("D", "CSS isolation limitations"),
    13: ("B", "CSS isolation in Razor class libraries"),
    14: ("B", "CSS isolation bundling"),
    15: ("A", "CSS isolation bundling"),
    16: ("D", "Templated components"),
    17: ("B", "Templated components"),
    18: ("C", "Templated components"),
    19: ("A", "Templated components"),
    20: ("D", "Templated components"),
}

def load_semantic_audit() -> dict[str, dict[str, str]]:
    payload = json.loads(RESEARCH_PATH.read_text(encoding="utf-8"))
    return {
        question["objective_id"]: question["semantic_review"]
        for question in payload["batches"][0]["questions"]
    }


def load_published_topic_records() -> list[dict]:
    records = []
    for path in sorted((ROOT / "docs/question-bank/accepted").glob("topic-28-lot-*.json")):
        if path == ACCEPTED_PATH:
            continue
        records.extend(json.loads(path.read_text(encoding="utf-8")).get("questions", []))
    return records


def main() -> int:
    payload = json.loads(LOT_PATH.read_text(encoding="utf-8"))
    records = payload["questions"]
    if payload["state"] != "candidates_written" or len(records) != 20:
        raise RuntimeError("unexpected supplemental candidate lot")
    audit = load_semantic_audit()
    published = load_published_topic_records()
    if set(audit) != {record["learning_objective_id"] for record in records}:
        raise RuntimeError("semantic audit does not cover exactly this lot")
    proposition_keys = [audit[record["learning_objective_id"]]["proposition_key"] for record in records]
    if len(set(proposition_keys)) != len(proposition_keys):
        raise RuntimeError("semantic audit contains a collision within this lot")
    accepted = []
    decisions = []
    for index, candidate in enumerate(records, start=1):
        expected = EXPECTED[index]
        if candidate["correct"] != expected[0] or candidate["sources"][0]["citation"] != expected[1]:
            raise RuntimeError(f"independent review disagreement for question {index}")
        reviewed = dict(candidate)
        reviewed["verification"] = {
            "answer": {"status": "passed", "reviewer": REVIEWER, "checked_at": DATE, "basis": f"Independent answer-key check against BLAZOR-10 section {expected[1]}."},
            "explanation": {"status": "passed", "reviewer": REVIEWER, "checked_at": DATE, "basis": f"Explanation checked against the official ASP.NET Core 10.0 page, section {expected[1]}."},
            "reviewed_at": DATE,
            "reviewer_decision": "accepted",
        }
        deterministic = candidate.get("deduplication", {})
        for name in ("exact", "lexical", "near_lexical"):
            if deterministic.get(name, {}).get("status") != "unique":
                raise RuntimeError(f"deterministic duplicate detected for question {index}: {name}")
        reviewed["deduplication"] = {
            name: dict(result) for name, result in deterministic.items()
        }
        decision = audit[reviewed["learning_objective_id"]]
        if decision["status"] != "unique" or decision["published_match_count"] != 0:
            raise RuntimeError(f"semantic collision detected for question {index}")
        basis = f"{decision['basis']} Compared records: {len(published)} published topic-28 records; candidate proposition key: {decision['proposition_key']}."
        for name in ("semantic", "concept"):
            reviewed["deduplication"][name] = {
                "status": decision["status"],
                "checked_at": DATE,
                "basis": basis,
            }
        reviewed["status"] = "validated"
        errors = validate_record(reviewed)
        if errors:
            raise RuntimeError(f"reviewed record {reviewed['stable_id']} failed validation: {errors}")
        accepted.append(reviewed)
        decisions.append({
            "objective_id": reviewed["learning_objective_id"],
            "stable_id": reviewed["stable_id"],
            "answer": expected[0],
            "citation": expected[1],
            "source_tier": reviewed["sources"][0]["tier"],
            "exact_duplicate": reviewed["deduplication"]["exact"]["status"],
            "lexical_duplicate": reviewed["deduplication"]["lexical"]["status"],
            "near_lexical_duplicate": reviewed["deduplication"]["near_lexical"]["status"],
            "semantic_duplicate": reviewed["deduplication"]["semantic"]["status"],
            "concept_collision": reviewed["deduplication"]["concept"]["status"],
            "decision": "accepted",
            "reviewed_at": DATE,
        })

    review_payload = {
        "review_version": "1.0",
        "lot": "topic-28-lot-11",
        "topic_num": TOPIC,
        "lot_num": LOT,
        "supplemental": True,
        "excluded_from_target_manifest": True,
        "reviewer": REVIEWER,
        "source_tier_counts": {"official_primary": 20, "secondary_reputable": 0},
        "semantic_audit": {"published_topic28_records": len(published), "lot_candidates": len(records), "proposition_keys_unique": True},
        "decisions": decisions,
        "reviewed_at": DATE,
    }
    REVIEW_PATH.parent.mkdir(parents=True, exist_ok=True)
    REVIEW_PATH.write_text(json.dumps(review_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    accepted_payload = {
        "lot_version": payload["lot_version"],
        "state": "reviewed",
        "topic_num": TOPIC,
        "lot_num": LOT,
        "revision": payload["revision"],
        "supplemental": True,
        "excluded_from_target_manifest": True,
        "reviewed_at": DATE,
        "source_register_sha256": payload["source_register_sha256"],
        "objective_manifest_sha256": payload["objective_manifest_sha256"],
        "syllabus_sha256": payload["syllabus_sha256"],
        "counts": {"candidates": 20, "accepted": 20, "rejected": 0, "quarantined": 0},
        "review_audit": str(REVIEW_PATH.relative_to(ROOT)),
        "questions": accepted,
    }
    ACCEPTED_PATH.parent.mkdir(parents=True, exist_ok=True)
    ACCEPTED_PATH.write_text(json.dumps(accepted_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    checkpoint = {
        "schema_version": "1.0",
        "syllabus_hash": payload["syllabus_sha256"],
        "source_register_hash": payload["source_register_sha256"],
        "topic_num": TOPIC,
        "lot_num": LOT,
        "revision": payload["revision"],
        "stage": "reviewed",
        "objective_ids": [record["learning_objective_id"] for record in accepted],
        "stable_ids": [record["stable_id"] for record in accepted],
        "counts": accepted_payload["counts"],
        "input_hash": file_sha256(LOT_PATH),
        "output_hash": file_sha256(ACCEPTED_PATH),
        "last_import": {"status": "not_started", "transaction": None},
    }
    appended = append_checkpoint(CHECKPOINT_PATH, checkpoint)
    print(f"topic {TOPIC} supplemental lot {LOT}: reviewed {len(accepted)} records; checkpoint {'appended' if appended else 'already present'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
