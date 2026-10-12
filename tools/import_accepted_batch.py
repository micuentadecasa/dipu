#!/usr/bin/env python3
"""Apply one reviewed batch to the existing seed_data.py authoring path."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from question_bank.checkpoints import append_checkpoint, file_sha256
from question_bank.validation import validate_record

SEED_PATH = ROOT / "seed_data.py"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("topic_num", type=int, choices=tuple(range(1, 17)))
    args = parser.parse_args()
    stem = f"topic-{args.topic_num:02d}-lot-01"
    accepted_path = ROOT / "docs/question-bank/accepted" / f"{stem}.json"
    checkpoint_path = ROOT / "docs/question-bank/checkpoints" / f"{stem}.jsonl"
    payload = json.loads(accepted_path.read_text(encoding="utf-8"))
    if payload["state"] != "reviewed":
        raise RuntimeError("only reviewed batches can be imported")
    records = payload["questions"]
    for record in records:
        errors = validate_record(record)
        if errors:
            raise RuntimeError(f"invalid accepted record {record['stable_id']}: {errors}")
    marker = f"QUESTION_BANK_ACCEPTED_TOPIC_{args.topic_num:02d}_LOT_01"
    seed = SEED_PATH.read_text(encoding="utf-8")
    if marker in seed:
        raise RuntimeError(f"batch already imported: {marker}")
    for previous in range(1, args.topic_num):
        if f"QUESTION_BANK_ACCEPTED_TOPIC_{previous:02d}_LOT_01" not in seed:
            raise RuntimeError(f"sequential import requires topic {previous} first")
    native = [{
        "topic_num": record["topic_num"],
        "question": record["question"],
        "option_a": record["option_a"],
        "option_b": record["option_b"],
        "option_c": record["option_c"],
        "option_d": record["option_d"],
        "correct": record["correct"],
        "explanation": record["explanation"],
    } for record in records]
    block = (
        f"\n\n# {marker}_START\n"
        "SEED_QUESTIONS.extend("
        + json.dumps(native, ensure_ascii=False, indent=4)
        + f")\n# {marker}_END\n"
    )
    SEED_PATH.write_text(seed.rstrip() + block, encoding="utf-8")
    checkpoint = {
        "schema_version": "1.0",
        "syllabus_hash": payload["syllabus_sha256"],
        "source_register_hash": payload["source_register_sha256"],
        "topic_num": args.topic_num,
        "lot_num": 1,
        "revision": payload["revision"],
        "stage": "import_applied",
        "objective_ids": [record["learning_objective_id"] for record in records],
        "stable_ids": [record["stable_id"] for record in records],
        "counts": {"candidates": 20, "accepted": len(records), "rejected": 0, "quarantined": 0},
        "input_hash": file_sha256(accepted_path),
        "output_hash": file_sha256(SEED_PATH),
        "last_import": {"status": "applied_to_seed_data", "transaction": marker},
    }
    appended = append_checkpoint(checkpoint_path, checkpoint)
    print(f"topic {args.topic_num}: imported {len(records)} records into seed_data.py; checkpoint {'appended' if appended else 'already present'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
