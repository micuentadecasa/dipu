#!/usr/bin/env python3
"""Validate one reviewed lot against the native static import contract."""

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
from seed_data import SEED_QUESTIONS


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("topic_num", type=int, choices=(2, 3, 4, 5))
    args = parser.parse_args()
    stem = f"topic-{args.topic_num:02d}-lot-01"
    accepted_path = ROOT / "docs/question-bank/accepted" / f"{stem}.json"
    checkpoint_path = ROOT / "docs/question-bank/checkpoints" / f"{stem}.jsonl"
    payload = json.loads(accepted_path.read_text(encoding="utf-8"))
    if payload["state"] != "reviewed":
        raise RuntimeError("import validation requires reviewed state")
    records = payload["questions"]
    errors = [(record["stable_id"], error) for record in records for error in validate_record(record)]
    if errors:
        raise RuntimeError(f"reviewed records failed validation: {errors}")
    stable_ids = [record["stable_id"] for record in records]
    numeric_ids = [record["id"] for record in records]
    if len(set(stable_ids)) != len(stable_ids) or len(set(numeric_ids)) != len(numeric_ids):
        raise RuntimeError("accepted batch contains an ID collision")
    runtime_before_batch = 1200 + 20 * (args.topic_num - 1)
    if any(record["id"] <= 1200 for record in records):
        raise RuntimeError("accepted numeric ID collides with legacy snapshot")
    if any(record["id"] <= 1200 + 20 * (args.topic_num - 1) for record in records):
        raise RuntimeError("accepted numeric ID collides with an earlier accepted topic batch")
    tier_counts = {"official_primary": 0, "secondary_reputable": 0}
    for record in records:
        for source in record["sources"]:
            tier_counts[source["tier"]] += 1
    report = {"validation_version":"1.0","status":"passed","mode":"dry_run","lot":stem,"revision":payload["revision"],"validated_at":"2026-10-12","writes_performed":0,"legacy_snapshot_total":1200,"prior_accepted_topics":args.topic_num - 1,"runtime_records_before_batch":runtime_before_batch,"accepted_delta":len(records),"stable_id_collisions":0,"numeric_id_collisions":0,"source_tier_counts":tier_counts,"artifact_to_import":"existing seed_data.py -> frontend/src/questions.js path","frontend_artifact_replaced":False,"stable_ids":stable_ids}
    report_path = ROOT / "docs/question-bank/imports" / f"{stem}-dry-run.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    checkpoint = {"schema_version":"1.0","syllabus_hash":payload["syllabus_sha256"],"source_register_hash":payload["source_register_sha256"],"topic_num":args.topic_num,"lot_num":1,"revision":payload["revision"],"stage":"import_validated","objective_ids":[x["learning_objective_id"] for x in records],"stable_ids":stable_ids,"counts":{"candidates":20,"accepted":len(records),"rejected":0,"quarantined":0},"input_hash":file_sha256(accepted_path),"output_hash":file_sha256(report_path),"last_import":{"status":"dry_run_passed","transaction":"not_written"}}
    appended=append_checkpoint(checkpoint_path,checkpoint)
    print(f"topic {args.topic_num}: import dry-run passed for {len(records)} records; checkpoint {'appended' if appended else 'already present'}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
