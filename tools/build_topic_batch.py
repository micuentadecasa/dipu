#!/usr/bin/env python3
"""Build one source-gated candidate lot for topics 2-5.

Generation is intentionally separate from review and import validation. The
candidate artifact remains quarantined until the review stage promotes records.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from question_bank.checkpoints import append_checkpoint, file_sha256
from question_bank.validation import screen_duplicates, stable_id_for, validate_record
from seed_data import SEED_QUESTIONS

DATE = "2026-10-13"
REGISTER_PATH = ROOT / "docs/question-bank/source-register.json"
OBJECTIVE_PATH = ROOT / "docs/question-bank/objective-manifest.json"
SYLLABUS_PATH = ROOT / "temario.md"
SPEC_PATHS = [
    ROOT / "docs/question-bank/research/questions/topics-02-05-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-06-15-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-16-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-17-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-18-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-19-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-20-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-20-lot-02.json",
    ROOT / "docs/question-bank/research/questions/topics-20-lot-03.json",
    ROOT / "docs/question-bank/research/questions/topics-20-lot-04.json",
    ROOT / "docs/question-bank/research/questions/topics-20-lot-05.json",
    ROOT / "docs/question-bank/research/questions/topics-21-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-22-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-23-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-24-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-24-lot-02.json",
    ROOT / "docs/question-bank/research/questions/topics-24-lot-03.json",
    ROOT / "docs/question-bank/research/questions/topics-24-lot-04.json",
    ROOT / "docs/question-bank/research/questions/topics-24-lot-05.json",
    ROOT / "docs/question-bank/research/questions/topics-23-lot-02.json",
    ROOT / "docs/question-bank/research/questions/topics-23-lot-03.json",
    ROOT / "docs/question-bank/research/questions/topics-23-lot-04.json",
    ROOT / "docs/question-bank/research/questions/topics-23-lot-05.json",
    ROOT / "docs/question-bank/research/questions/topics-25-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-25-lot-02.json",
    ROOT / "docs/question-bank/research/questions/topics-25-lot-03.json",
    ROOT / "docs/question-bank/research/questions/topics-25-lot-04.json",
    ROOT / "docs/question-bank/research/questions/topics-25-lot-05.json",
    ROOT / "docs/question-bank/research/questions/topics-26-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-26-lot-02.json",
    ROOT / "docs/question-bank/research/questions/topics-26-lot-03.json",
    ROOT / "docs/question-bank/research/questions/topics-26-lot-04.json",
    ROOT / "docs/question-bank/research/questions/topics-26-lot-05.json",
    ROOT / "docs/question-bank/research/questions/topics-27-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-27-lot-02.json",
    ROOT / "docs/question-bank/research/questions/topics-27-lot-03.json",
    ROOT / "docs/question-bank/research/questions/topics-27-lot-04.json",
    ROOT / "docs/question-bank/research/questions/topics-27-lot-05.json",
    ROOT / "docs/question-bank/research/questions/topics-28-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-28-lot-02.json",
    ROOT / "docs/question-bank/research/questions/topics-28-lot-03.json",
    ROOT / "docs/question-bank/research/questions/topics-28-lot-04.json",
    ROOT / "docs/question-bank/research/questions/topics-28-lot-05.json",
    ROOT / "docs/question-bank/research/questions/topics-29-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-29-lot-02.json",
    ROOT / "docs/question-bank/research/questions/topics-29-lot-03.json",
    ROOT / "docs/question-bank/research/questions/topics-29-lot-04.json",
    ROOT / "docs/question-bank/research/questions/topics-29-lot-05.json",
    ROOT / "docs/question-bank/research/questions/topics-30-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-30-lot-02.json",
    ROOT / "docs/question-bank/research/questions/topics-30-lot-03.json",
    ROOT / "docs/question-bank/research/questions/topics-30-lot-04.json",
    ROOT / "docs/question-bank/research/questions/topics-30-lot-05.json",
    ROOT / "docs/question-bank/research/questions/topics-31-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-31-lot-02.json",
    ROOT / "docs/question-bank/research/questions/topics-31-lot-03.json",
    ROOT / "docs/question-bank/research/questions/topics-31-lot-04.json",
    ROOT / "docs/question-bank/research/questions/topics-31-lot-05.json",
    ROOT / "docs/question-bank/research/questions/topics-32-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-32-lot-02.json",
    ROOT / "docs/question-bank/research/questions/topics-32-lot-03.json",
    ROOT / "docs/question-bank/research/questions/topics-32-lot-04.json",
    ROOT / "docs/question-bank/research/questions/topics-32-lot-05.json",
    ROOT / "docs/question-bank/research/questions/topics-33-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-33-lot-02.json",
    ROOT / "docs/question-bank/research/questions/topics-33-lot-03.json",
    ROOT / "docs/question-bank/research/questions/topics-33-lot-04.json",
    ROOT / "docs/question-bank/research/questions/topics-33-lot-05.json",
    ROOT / "docs/question-bank/research/questions/topics-34-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-34-lot-02.json",
    ROOT / "docs/question-bank/research/questions/topics-34-lot-03.json",
    ROOT / "docs/question-bank/research/questions/topics-34-lot-04.json",
    ROOT / "docs/question-bank/research/questions/topics-34-lot-05.json",
    ROOT / "docs/question-bank/research/questions/topics-35-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-35-lot-02.json",
    ROOT / "docs/question-bank/research/questions/topics-35-lot-03.json",
    ROOT / "docs/question-bank/research/questions/topics-35-lot-04.json",
    ROOT / "docs/question-bank/research/questions/topics-35-lot-05.json",
    ROOT / "docs/question-bank/research/questions/topics-36-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-36-lot-02.json",
    ROOT / "docs/question-bank/research/questions/topics-36-lot-03.json",
    ROOT / "docs/question-bank/research/questions/topics-36-lot-04.json",
    ROOT / "docs/question-bank/research/questions/topics-36-lot-05.json",
    ROOT / "docs/question-bank/research/questions/topics-37-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-37-lot-02.json",
    ROOT / "docs/question-bank/research/questions/topics-37-lot-03.json",
    ROOT / "docs/question-bank/research/questions/topics-37-lot-04.json",
    ROOT / "docs/question-bank/research/questions/topics-37-lot-05.json",
    ROOT / "docs/question-bank/research/questions/topics-38-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-38-lot-02.json",
    ROOT / "docs/question-bank/research/questions/topics-38-lot-03.json",
    ROOT / "docs/question-bank/research/questions/topics-38-lot-04.json",
    ROOT / "docs/question-bank/research/questions/topics-38-lot-05.json",
    ROOT / "docs/question-bank/research/questions/topics-38-lot-06.json",
    ROOT / "docs/question-bank/research/questions/topics-38-lot-07.json",
    ROOT / "docs/question-bank/research/questions/topics-38-lot-08.json",
    ROOT / "docs/question-bank/research/questions/topics-38-lot-09.json",
    ROOT / "docs/question-bank/research/questions/topics-38-lot-10.json",
    ROOT / "docs/question-bank/research/questions/topics-39-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-39-lot-02.json",
    ROOT / "docs/question-bank/research/questions/topics-39-lot-03.json",
    ROOT / "docs/question-bank/research/questions/topics-39-lot-04.json",
    ROOT / "docs/question-bank/research/questions/topics-39-lot-05.json",
    ROOT / "docs/question-bank/research/questions/topics-39-lot-06.json",
    ROOT / "docs/question-bank/research/questions/topics-39-lot-07.json",
    ROOT / "docs/question-bank/research/questions/topics-39-lot-08.json",
    ROOT / "docs/question-bank/research/questions/topics-39-lot-09.json",
    ROOT / "docs/question-bank/research/questions/topics-39-lot-10.json",
    ROOT / "docs/question-bank/research/questions/topics-40-lot-01.json",
    ROOT / "docs/question-bank/research/questions/topics-40-lot-02.json",
    ROOT / "docs/question-bank/research/questions/topics-40-lot-03.json",
    ROOT / "docs/question-bank/research/questions/topics-40-lot-04.json",
    ROOT / "docs/question-bank/research/questions/topics-40-lot-05.json",
    ROOT / "docs/question-bank/research/questions/topics-40-lot-06.json",
    ROOT / "docs/question-bank/research/questions/topics-40-lot-07.json",
    ROOT / "docs/question-bank/research/questions/topics-40-lot-08.json",
    ROOT / "docs/question-bank/research/questions/topics-40-lot-09.json",
    ROOT / "docs/question-bank/research/questions/topics-40-lot-10.json",
]


def load_batch(topic_num: int, lot_num: int) -> dict:
    for spec_path in SPEC_PATHS:
        if not spec_path.exists():
            continue
        payload = json.loads(spec_path.read_text(encoding="utf-8"))
        for batch in payload.get("batches", []):
            if batch["topic_num"] == topic_num and batch.get("lot_num", 1) == lot_num:
                return batch
    raise RuntimeError(f"no question specification for topic {topic_num}, lot {lot_num}")


def next_numeric_id(topic_num: int, lot_num: int) -> int:
    # Preserve established IDs for first lots through topic 20. New lots and
    # later topics continue after the highest accepted artifact ID.
    if topic_num <= 20 and lot_num == 1:
        return 1200 + (topic_num - 1) * 20 + 1
    ids = []
    for path in (ROOT / "docs/question-bank/accepted").glob("topic-*-lot-*.json"):
        payload = json.loads(path.read_text(encoding="utf-8"))
        ids.extend(record["id"] for record in payload.get("questions", []))
    return max([1200, *ids]) + 1


def make_record(spec: dict, source: dict, numeric_id: int) -> dict:
    record = {
        "id": numeric_id,
        "stable_id": "",
        "topic_num": spec["topic_num"],
        "question": spec["question"],
        "option_a": spec["options"][0],
        "option_b": spec["options"][1],
        "option_c": spec["options"][2],
        "option_d": spec["options"][3],
        "correct": spec["correct"],
        "explanation": spec["explanation"],
        "learning_objective_id": spec["objective_id"],
        "difficulty": spec["difficulty"],
        "question_type": spec["type"],
        "sources": [{
            "source_id": source["source_id"],
            "title": source["title"],
            "authority": source["authority"],
            "tier": source.get("tier", "official_primary"),
            "url": source["url"],
            "citation": spec["citation"],
            "version_or_as_of": source["version_or_as_of"],
            "retrieved_at": source["retrieved_at"],
            "verified_at": source["verified_at"],
        }],
        "verification": {
            "answer": {"status": "uncertain", "reviewer": "awaiting-independent-review", "checked_at": DATE, "basis": "Candidate answer requires an independent second pass against the cited official source."},
            "explanation": {"status": "uncertain", "reviewer": "awaiting-independent-review", "checked_at": DATE, "basis": "Candidate explanation requires an independent second pass against the cited official source."},
            "reviewed_at": DATE,
            "reviewer_decision": "quarantined",
        },
        "deduplication": {},
        "status": "quarantined",
    }
    record["stable_id"] = stable_id_for(record)
    return record


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("topic_num", type=int, choices=tuple(range(2, 41)))
    parser.add_argument("--lot-num", type=int, default=1, choices=tuple(range(1, 11)))
    args = parser.parse_args()
    batch = load_batch(args.topic_num, args.lot_num)
    register = json.loads(REGISTER_PATH.read_text(encoding="utf-8"))
    sources = {source["source_id"]: source for source in register["source_records"]}
    manifest = json.loads(OBJECTIVE_PATH.read_text(encoding="utf-8"))
    objectives = {objective["objective_id"]: objective for objective in manifest["objectives"]}
    records = []
    existing = list(SEED_QUESTIONS)
    start_id = next_numeric_id(args.topic_num, args.lot_num)
    for index, spec in enumerate(batch["questions"], start=start_id):
        objective = objectives.get(spec["objective_id"])
        if not objective or not objective["statement"]:
            raise RuntimeError(f"objective is not researched: {spec['objective_id']}")
        source = sources[spec["source_id"]]
        if source["status"] not in {"verified", "verified_with_correction_review", "verified_official_eli_entry", "verified_official_celex_fallback", "verified_entry_point", "verified_current_stable_reference", "verified_public_manual"}:
            raise RuntimeError(f"source is not verified for generation: {spec['source_id']}")
        record = make_record({**spec, "topic_num": args.topic_num}, source, index)
        screen = screen_duplicates(record, existing + records, checked_at=DATE)
        record["deduplication"] = screen.as_dict()
        errors = validate_record(record)
        if errors:
            raise RuntimeError(f"record {record['stable_id']} failed validation: {errors}")
        records.append(record)

    lot_dir = ROOT / "docs/question-bank/lots"
    lot_dir.mkdir(parents=True, exist_ok=True)
    stem = f"topic-{args.topic_num:02d}-lot-{args.lot_num:02d}"
    lot_path = lot_dir / f"{stem}.json"
    checkpoint_path = ROOT / "docs/question-bank/checkpoints" / f"{stem}.jsonl"
    payload = {
        "lot_version": "1.0",
        "state": "candidates_written",
        "topic_num": args.topic_num,
        "lot_num": args.lot_num,
        "revision": 1,
        "generated_at": DATE,
        "source_register_sha256": file_sha256(REGISTER_PATH),
        "objective_manifest_sha256": file_sha256(OBJECTIVE_PATH),
        "syllabus_sha256": file_sha256(SYLLABUS_PATH),
        "source_verification": {"source_ids": batch["source_ids"], "verified_at": DATE},
        "counts": {"candidates": len(records), "accepted": 0, "rejected": 0, "quarantined": len(records)},
        "questions": records,
    }
    lot_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    checkpoint = {
        "schema_version": "1.0",
        "syllabus_hash": payload["syllabus_sha256"],
        "source_register_hash": payload["source_register_sha256"],
        "topic_num": args.topic_num,
        "lot_num": args.lot_num,
        "revision": 1,
        "stage": "candidates_written",
        "objective_ids": [record["learning_objective_id"] for record in records],
        "stable_ids": [record["stable_id"] for record in records],
        "counts": payload["counts"],
        "input_hash": hashlib.sha256((payload["source_register_sha256"] + payload["objective_manifest_sha256"]).encode()).hexdigest(),
        "output_hash": file_sha256(lot_path),
        "last_import": {"status": "not_started", "transaction": None},
    }
    appended = append_checkpoint(checkpoint_path, checkpoint)
    print(f"topic {args.topic_num}: wrote {len(records)} quarantined candidates; checkpoint {'appended' if appended else 'already present'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
