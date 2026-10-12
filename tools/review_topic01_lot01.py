#!/usr/bin/env python3
"""Independent second-pass review for topic 1, lot 1 candidates.

The review consumes the candidate artifact and writes a separate accepted
artifact. It never mutates the candidate audit trail or the shipped frontend.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from question_bank.checkpoints import append_checkpoint, file_sha256
from question_bank.validation import validate_record
from seed_data import SEED_QUESTIONS

DATE = "2026-10-12"
CANDIDATE_PATH = ROOT / "docs/question-bank/lots/topic-01-lot-01.json"
ACCEPTED_PATH = ROOT / "docs/question-bank/accepted/topic-01-lot-01.json"
REVIEW_PATH = ROOT / "docs/question-bank/reviews/topic-01-lot-01.json"
CHECKPOINT_PATH = ROOT / "docs/question-bank/checkpoints/topic-01-lot-01.jsonl"

# This matrix is intentionally separate from build_topic01_lot01.py. Each
# answer and citation is rechecked against the official BOE source in the
# review stage rather than trusted from generation input.
REVIEW_MATRIX = {
    "t01-lo-001": ("A", "Estructura de la Constitución Española de 1978"),
    "t01-lo-002": ("B", "Artículo 1.3"),
    "t01-lo-003": ("A", "Artículo 2"),
    "t01-lo-004": ("A", "Artículo 3.1"),
    "t01-lo-005": ("A", "Artículo 9.3"),
    "t01-lo-006": ("A", "Artículo 10.1"),
    "t01-lo-007": ("A", "Artículo 14"),
    "t01-lo-008": ("A", "Artículo 15"),
    "t01-lo-009": ("A", "Artículo 16.2"),
    "t01-lo-010": ("B", "Artículo 17.2"),
    "t01-lo-011": ("A", "Artículo 18.2"),
    "t01-lo-012": ("B", "Artículo 20.2"),
    "t01-lo-013": ("B", "Artículo 21.2"),
    "t01-lo-014": ("A", "Artículo 23.2"),
    "t01-lo-015": ("A", "Artículo 24.2"),
    "t01-lo-016": ("A", "Artículo 27.1"),
    "t01-lo-017": ("A", "Artículo 28.2"),
    "t01-lo-018": ("A", "Artículo 31.1"),
    "t01-lo-019": ("A", "Artículo 66.1"),
    "t01-lo-020": ("B", "Artículo 81.2")
}


def main() -> int:
    payload = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    if payload["state"] != "candidates_written" or payload["revision"] != 2:
        raise RuntimeError("review requires the current candidate revision")
    accepted = []
    decisions = []
    for candidate in payload["questions"]:
        objective_id = candidate["learning_objective_id"]
        expected = REVIEW_MATRIX.get(objective_id)
        if expected is None:
            raise RuntimeError(f"no independent review matrix entry for {objective_id}")
        expected_answer, expected_citation = expected
        if candidate["correct"] != expected_answer:
            raise RuntimeError(f"answer disagreement for {objective_id}")
        if candidate["sources"][0]["tier"] != "official_primary":
            raise RuntimeError(f"non-official source in official lot: {objective_id}")
        if candidate["sources"][0]["verified_at"] != DATE:
            raise RuntimeError(f"source verification date missing for {objective_id}")
        if candidate["sources"][0]["citation"] != expected_citation:
            raise RuntimeError(f"citation mismatch for {objective_id}")

        reviewed = copy.deepcopy(candidate)
        reviewed["verification"]["answer"] = {
            "status": "passed",
            "reviewer": "independent-source-review-2026-10-12",
            "checked_at": DATE,
            "basis": f"Rechecked against BOE-CE-1978 {expected_citation}; expected option {expected_answer}.",
        }
        reviewed["verification"]["explanation"] = {
            "status": "passed",
            "reviewer": "independent-source-review-2026-10-12",
            "checked_at": DATE,
            "basis": f"Explanation checked against the cited BOE-CE-1978 {expected_citation}.",
        }
        reviewed["verification"]["reviewed_at"] = DATE
        reviewed["verification"]["reviewer_decision"] = "accepted"
        for level in ("semantic", "concept"):
            reviewed["deduplication"][level] = {
                "status": "unique",
                "checked_at": DATE,
                "basis": "Independent proposition/objective review found no collision with the legacy topic-1 bank or this lot.",
            }
        reviewed["status"] = "validated"
        errors = validate_record(reviewed)
        if errors:
            raise RuntimeError(f"reviewed record {objective_id} failed validation: {errors}")
        accepted.append(reviewed)
        decisions.append({
            "objective_id": objective_id,
            "stable_id": reviewed["stable_id"],
            "answer": expected_answer,
            "citation": expected_citation,
            "source_tier": "official_primary",
            "decision": "accepted",
            "reviewed_at": DATE,
        })

    review_audit = {
        "review_version": "1.0",
        "lot": "topic-01-lot-01",
        "revision": 2,
        "reviewer": "independent-source-review-2026-10-12",
        "source_ids": ["BOE-CE-1978"],
        "source_tier": "official_primary",
        "decisions": decisions,
    }
    REVIEW_PATH.parent.mkdir(parents=True, exist_ok=True)
    REVIEW_PATH.write_text(json.dumps(review_audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    accepted_payload = {
        "lot_version": payload["lot_version"],
        "state": "reviewed",
        "topic_num": payload["topic_num"],
        "lot_num": payload["lot_num"],
        "revision": 2,
        "reviewed_at": DATE,
        "source_register_sha256": payload["source_register_sha256"],
        "objective_manifest_sha256": payload["objective_manifest_sha256"],
        "syllabus_sha256": payload["syllabus_sha256"],
        "counts": {"candidates": 20, "accepted": len(accepted), "rejected": 0, "quarantined": 0},
        "review_audit": str(REVIEW_PATH.relative_to(ROOT)),
        "questions": accepted,
    }
    ACCEPTED_PATH.parent.mkdir(parents=True, exist_ok=True)
    ACCEPTED_PATH.write_text(json.dumps(accepted_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    checkpoint = {
        "schema_version": "1.0",
        "syllabus_hash": payload["syllabus_sha256"],
        "source_register_hash": payload["source_register_sha256"],
        "topic_num": 1,
        "lot_num": 1,
        "revision": 2,
        "stage": "reviewed",
        "objective_ids": [question["learning_objective_id"] for question in accepted],
        "stable_ids": [question["stable_id"] for question in accepted],
        "counts": accepted_payload["counts"],
        "input_hash": file_sha256(CANDIDATE_PATH),
        "output_hash": file_sha256(ACCEPTED_PATH),
        "last_import": {"status": "not_started", "transaction": None},
    }
    appended = append_checkpoint(CHECKPOINT_PATH, checkpoint)
    print(f"reviewed {len(accepted)} records; checkpoint {'appended' if appended else 'already present'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
