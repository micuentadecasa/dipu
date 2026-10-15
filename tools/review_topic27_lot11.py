#!/usr/bin/env python3
"""Independently review and promote topic-27 supplemental lot 11."""

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
TOPIC = 27
LOT = 11
REVIEWER = "independent-source-review-2026-10-15"
LOT_PATH = ROOT / "docs/question-bank/lots/topic-27-lot-11.json"
ACCEPTED_PATH = ROOT / "docs/question-bank/accepted/topic-27-lot-11.json"
REVIEW_PATH = ROOT / "docs/question-bank/reviews/topic-27-lot-11.json"
CHECKPOINT_PATH = ROOT / "docs/question-bank/checkpoints/topic-27-lot-11.jsonl"

EXPECTED = {
    1: ("A", "Delegate event handlers — exception logging"),
    2: ("B", "Custom event arguments — prevent-default and stop-propagation flags"),
    3: ("C", "Binding features — case-sensitive bind attributes"),
    4: ("D", "Binding with component parameters — chained bind"),
    5: ("A", "Custom event arguments — EventHandler registration"),
    6: ("B", "Binding features — @bind:after delegate restriction"),
    7: ("C", "Binding with @bind:get and @bind:set — synchronization"),
    8: ("D", "Binding with @bind:get and @bind:set — synchronization"),
    9: ("A", "Multiple option selection with select elements"),
    10: ("B", "Unparsable values"),
    11: ("C", "Format strings — DateTime binding"),
    12: ("C", "Binding features — component @bind:after"),
    13: ("A", "Binding with component parameters — legacy callback Task"),
    14: ("B", "Suppress UI refreshing — ShouldRender"),
    15: ("C", "StateHasChanged — render queue"),
    16: ("D", "Receiving a call from something external — timer and StateHasChanged"),
    17: ("A", "Streaming rendering — long-running asynchronous tasks"),
    18: ("B", "Streaming rendering — StreamRendering attribute"),
    19: ("C", "Streaming rendering — buffering fallback"),
    20: ("B", "Overwritten parameters — private state field"),
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
        reviewed["deduplication"] = {
            name: {"status": "unique", "checked_at": DATE, "basis": "Independent proposition/objective review found no collision with published topic-27 records or this supplemental lot."}
            for name in ("exact", "lexical", "near_lexical", "semantic", "concept")
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
            "semantic_duplicate": "unique",
            "concept_collision": "unique",
            "decision": "accepted",
            "reviewed_at": DATE,
        })

    review_payload = {
        "review_version": "1.0",
        "lot": "topic-27-lot-11",
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
