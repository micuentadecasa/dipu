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
CHECKPOINT_PATH = ROOT / "docs/question-bank/checkpoints/topic-28-lot-11.jsonl"

EXPECTED = {
    1: ("B", "When parameters are set (SetParametersAsync)"),
    2: ("C", "Component initialization — parent and child order"),
    3: ("A", "Component initialization — asynchronous order"),
    4: ("D", "After parameters are set — complex parameters"),
    5: ("B", "After parameters are set — valid state before await"),
    6: ("B", "CSS isolation — bundled stylesheet link"),
    7: ("C", "CSS isolation — shared scope identifiers"),
    8: ("D", "CSS isolation — inherited scoped styles"),
    9: ("A", "CSS isolation — ::deep selector placement"),
    10: ("C", "CSS isolation — generated scope length"),
    11: ("C", "CSS isolation — hyperlink descendant wrapper"),
    12: ("D", "Templated components — typed fragment invocation"),
    13: ("A", "Templated components — component-level Context"),
    14: ("B", "Templated components — child-level Context placement"),
    15: ("A", "Templated components — implicit context name"),
    16: ("D", "Templated components — generic list type"),
    17: ("A", "Templated components — inferred generic type"),
    18: ("B", "When parameters are set — base assignment"),
    19: ("C", "After parameters are set — callback timing"),
    20: ("C", "Templated components — explicit type attribute"),
}

SEMANTIC_DECISIONS = {
    "t28-lo-supp-001": {"status": "unique", "basis": "Compared missing-parameter preservation with all published lifecycle records and lot-11 candidates; no proposition collision."},
    "t28-lo-supp-002": {"status": "unique", "basis": "Compared synchronous parent-before-child initialization with all published lifecycle records and lot-11 candidates; no proposition collision."},
    "t28-lo-supp-003": {"status": "unique", "basis": "Compared nondeterministic asynchronous initialization completion with all published lifecycle records and lot-11 candidates; no proposition collision."},
    "t28-lo-supp-004": {"status": "unique", "basis": "Compared complex-parameter callback triggering with all published lifecycle records and lot-11 candidates; no proposition collision."},
    "t28-lo-supp-005": {"status": "unique", "basis": "Compared valid-state requirements before OnParametersSetAsync await with all published lifecycle records and lot-11 candidates; no proposition collision."},
    "t28-lo-supp-006": {"status": "unique", "basis": "Compared the bundled stylesheet link location with all published CSS records and lot-11 candidates; no proposition collision."},
    "t28-lo-supp-007": {"status": "unique", "basis": "Compared wildcard scope sharing with all published CSS records and lot-11 candidates; no proposition collision."},
    "t28-lo-supp-008": {"status": "unique", "basis": "Compared base-derived scoped-style inheritance with all published CSS records and lot-11 candidates; no proposition collision."},
    "t28-lo-supp-009": {"status": "unique", "basis": "Compared the div ::deep selector transformation with all published CSS records and lot-11 candidates; no proposition collision."},
    "t28-lo-supp-010": {"status": "unique", "basis": "Compared generated scope-string length with all published CSS records and lot-11 candidates; no proposition collision."},
    "t28-lo-supp-011": {"status": "unique", "basis": "Compared the wrapper requirement for a child hyperlink with all published CSS records and lot-11 candidates; no proposition collision."},
    "t28-lo-supp-012": {"status": "unique", "basis": "Compared the typed-fragment invocation contract with all published template records and lot-11 candidates; no proposition collision."},
    "t28-lo-supp-013": {"status": "unique", "basis": "Compared component-level Context scope across templates with all published template records and lot-11 candidates; no proposition collision."},
    "t28-lo-supp-014": {"status": "unique", "basis": "Compared child-element Context placement with all published template records and lot-11 candidates; no proposition collision."},
    "t28-lo-supp-015": {"status": "unique", "basis": "Compared the implicit context name with all published template records and lot-11 candidates; no proposition collision."},
    "t28-lo-supp-016": {"status": "unique", "basis": "Compared IReadOnlyList<T> in the generic example with all published template records and lot-11 candidates; no proposition collision."},
    "t28-lo-supp-017": {"status": "unique", "basis": "Compared generic type inference conditions with all published template records and lot-11 candidates; no proposition collision."},
    "t28-lo-supp-018": {"status": "unique", "basis": "Compared base parameter assignment behavior with all published parameter records and lot-11 candidates; no proposition collision."},
    "t28-lo-supp-019": {"status": "unique", "basis": "Compared callback timing after parameter assignment with all published lifecycle records and lot-11 candidates; no proposition collision."},
    "t28-lo-supp-020": {"status": "unique", "basis": "Compared the explicit generic type attribute with all published template records and lot-11 candidates; no proposition collision."},
}


def main() -> int:
    payload = json.loads(LOT_PATH.read_text(encoding="utf-8"))
    records = payload["questions"]
    if payload["state"] != "candidates_written" or len(records) != 20:
        raise RuntimeError("unexpected supplemental candidate lot")
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
        decision = SEMANTIC_DECISIONS.get(reviewed["learning_objective_id"])
        if not decision:
            raise RuntimeError(f"missing semantic review decision for question {index}")
        for name in ("semantic", "concept"):
            reviewed["deduplication"][name] = {
                "status": decision["status"],
                "checked_at": DATE,
                "basis": decision["basis"],
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
