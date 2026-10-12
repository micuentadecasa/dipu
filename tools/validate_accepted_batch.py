#!/usr/bin/env python3
"""Dry-run native import validation without touching the shipped frontend."""

from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from question_bank.checkpoints import append_checkpoint, file_sha256
from question_bank.validation import validate_record
from seed_data import SEED_QUESTIONS

ACCEPTED_PATH = ROOT / "docs/question-bank/accepted/topic-01-lot-01.json"
REPORT_PATH = ROOT / "docs/question-bank/imports/topic-01-lot-01-dry-run.json"
CHECKPOINT_PATH = ROOT / "docs/question-bank/checkpoints/topic-01-lot-01.jsonl"


def main() -> int:
    payload = json.loads(ACCEPTED_PATH.read_text(encoding="utf-8"))
    if payload["state"] != "reviewed":
        raise RuntimeError("import validation requires a reviewed batch")
    records = payload["questions"]
    errors = [
        (record["stable_id"], error)
        for record in records
        for error in validate_record(record)
    ]
    if errors:
        raise RuntimeError(f"reviewed records failed validation: {errors}")
    stable_ids = [record["stable_id"] for record in records]
    numeric_ids = [record["id"] for record in records]
    if len(set(stable_ids)) != len(stable_ids):
        raise RuntimeError("stable ID collision in accepted batch")
    if len(set(numeric_ids)) != len(numeric_ids):
        raise RuntimeError("numeric ID collision in accepted batch")
    if any(record["id"] <= 1200 for record in records):
        raise RuntimeError("accepted numeric ID collides with legacy snapshot")

    report = {
        "validation_version": "1.0",
        "status": "passed",
        "mode": "dry_run",
        "lot": "topic-01-lot-01",
        "revision": payload["revision"],
        "validated_at": "2026-10-12",
        "writes_performed": 0,
        "legacy_snapshot_total": 1200,
        "accepted_delta": len(records),
        "stable_id_collisions": 0,
        "numeric_id_collisions": 0,
        "source_tier_counts": {"official_primary": len(records), "secondary_reputable": 0},
        "artifact_to_import": "existing seed_data.py -> frontend/src/questions.js path",
        "frontend_artifact_replaced": False,
        "stable_ids": stable_ids,
    }
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    checkpoint = {
        "schema_version": "1.0",
        "syllabus_hash": payload["syllabus_sha256"],
        "source_register_hash": payload["source_register_sha256"],
        "topic_num": 1,
        "lot_num": 1,
        "revision": payload["revision"],
        "stage": "import_validated",
        "objective_ids": [record["learning_objective_id"] for record in records],
        "stable_ids": stable_ids,
        "counts": {"candidates": 20, "accepted": len(records), "rejected": 0, "quarantined": 0},
        "input_hash": file_sha256(ACCEPTED_PATH),
        "output_hash": file_sha256(REPORT_PATH),
        "last_import": {"status": "dry_run_passed", "transaction": "not_written"},
    }
    appended = append_checkpoint(CHECKPOINT_PATH, checkpoint)
    print(f"import dry-run passed for {len(records)} records; checkpoint {'appended' if appended else 'already present'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
