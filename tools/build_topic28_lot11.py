#!/usr/bin/env python3
"""Generate topic-28 supplemental lot 11 from its researched question spec."""

from __future__ import annotations

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

DATE = "2026-10-15"
TOPIC = 28
LOT = 11
REVISION = 1
SOURCE_REGISTER = ROOT / "docs/question-bank/source-register.json"
OBJECTIVE_MANIFEST = ROOT / "docs/question-bank/objective-manifest.json"
SYLLABUS = ROOT / "temario.md"
RESEARCH_PATH = ROOT / "docs/question-bank/research/questions/topics-28-lot-11.json"
LOT_PATH = ROOT / "docs/question-bank/lots/topic-28-lot-11.json"
CHECKPOINT_PATH = ROOT / "docs/question-bank/checkpoints/topic-28-lot-11.jsonl"

SOURCE_TITLES = {
    "lifecycle": "ASP.NET Core Razor component lifecycle",
    "css-isolation": "ASP.NET Core Blazor CSS isolation",
    "templated-components": "ASP.NET Core Blazor templated components",
}


def load_specs() -> list[dict]:
    payload = json.loads(RESEARCH_PATH.read_text(encoding="utf-8"))
    return payload["batches"][0]["questions"]


def title_for(url: str) -> str:
    for slug, title in SOURCE_TITLES.items():
        if f"/blazor/components/{slug}?" in url:
            return title
    raise RuntimeError(f"unregistered source URL: {url}")


def load_accepted_records() -> list[dict]:
    records = []
    for path in sorted((ROOT / "docs/question-bank/accepted").glob("topic-*-lot-*.json")):
        records.extend(json.loads(path.read_text(encoding="utf-8")).get("questions", []))
    return records


def make_record(spec: dict, numeric_id: int) -> dict:
    source = {
        "source_id": "BLAZOR-10",
        "title": title_for(spec["url"]),
        "authority": "Microsoft Learn",
        "tier": "official_primary",
        "url": spec["url"],
        "citation": spec["citation"],
        "version_or_as_of": "ASP.NET Core 10.0, current stable reference at research time",
        "retrieved_at": DATE,
        "verified_at": DATE,
    }
    record = {
        "id": numeric_id,
        "stable_id": "",
        "topic_num": TOPIC,
        "question": spec["question"],
        "option_a": spec["options"][0],
        "option_b": spec["options"][1],
        "option_c": spec["options"][2],
        "option_d": spec["options"][3],
        "correct": spec["correct"],
        "explanation": spec["explanation"],
        "learning_objective_id": spec["objective_id"],
        "difficulty": spec["difficulty"],
        "question_type": spec["question_type"],
        "sources": [source],
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
    specs = load_specs()
    if len(specs) != 20:
        raise RuntimeError("supplemental lot must contain exactly 20 questions")
    accepted = load_accepted_records()
    own_objectives = {spec["objective_id"] for spec in specs}
    own_questions = {spec["question"] for spec in specs}
    existing = [question for question in SEED_QUESTIONS if question.get("question") not in own_questions]
    existing.extend(record for record in accepted if record.get("learning_objective_id") not in own_objectives)
    start_id = max([1200, *(record["id"] for record in accepted)]) + 1
    records = []
    for offset, spec in enumerate(specs):
        record = make_record(spec, start_id + offset)
        record["deduplication"] = screen_duplicates(record, existing + records, checked_at=DATE).as_dict()
        errors = validate_record(record)
        if errors:
            raise RuntimeError(f"candidate {record['stable_id']} failed validation: {errors}")
        records.append(record)

    source_hash = file_sha256(SOURCE_REGISTER)
    manifest_hash = file_sha256(OBJECTIVE_MANIFEST)
    syllabus_hash = file_sha256(SYLLABUS)
    payload = {
        "lot_version": "1.0",
        "state": "candidates_written",
        "topic_num": TOPIC,
        "lot_num": LOT,
        "revision": REVISION,
        "generated_at": DATE,
        "supplemental": True,
        "excluded_from_target_manifest": True,
        "source_register_sha256": source_hash,
        "objective_manifest_sha256": manifest_hash,
        "syllabus_sha256": syllabus_hash,
        "source_verification": {"source_ids": ["BLAZOR-10"], "verified_at": DATE},
        "counts": {"candidates": 20, "accepted": 0, "rejected": 0, "quarantined": 20},
        "questions": records,
    }
    LOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    LOT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    checkpoint = {
        "schema_version": "1.0",
        "syllabus_hash": syllabus_hash,
        "source_register_hash": source_hash,
        "topic_num": TOPIC,
        "lot_num": LOT,
        "revision": REVISION,
        "stage": "candidates_written",
        "objective_ids": [record["learning_objective_id"] for record in records],
        "stable_ids": [record["stable_id"] for record in records],
        "counts": payload["counts"],
        "input_hash": hashlib.sha256((source_hash + manifest_hash).encode()).hexdigest(),
        "output_hash": file_sha256(LOT_PATH),
        "last_import": {"status": "not_started", "transaction": None},
    }
    appended = append_checkpoint(CHECKPOINT_PATH, checkpoint)
    print(f"topic {TOPIC} supplemental lot {LOT}: wrote {len(records)} quarantined candidates; checkpoint {'appended' if appended else 'already present'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
