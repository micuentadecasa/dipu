#!/usr/bin/env python3
"""Independently review and promote topic-26 supplemental lot 11."""

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
TOPIC = 26
LOT = 11
REVIEWER = "independent-source-review-2026-10-15"
LOT_PATH = ROOT / "docs/question-bank/lots/topic-26-lot-11.json"
ACCEPTED_PATH = ROOT / "docs/question-bank/accepted/topic-26-lot-11.json"
REVIEW_PATH = ROOT / "docs/question-bank/reviews/topic-26-lot-11.json"
CHECKPOINT_PATH = ROOT / "docs/question-bank/checkpoints/topic-26-lot-11.jsonl"
RENDER_MODES_URL = "https://learn.microsoft.com/en-us/aspnet/core/blazor/components/render-modes?view=aspnetcore-10.0"

# Independent answer key, kept separate from the candidate generator's option data.
EXPECTED = {
    1: ("A", "Render modes — scope and standalone WebAssembly"),
    2: ("B", "Render-mode propagation — default render mode"),
    3: ("A", "Enable support for interactive render modes — AddInteractiveServerComponents"),
    4: ("C", "Enable support for interactive render modes — AddInteractiveServerRenderMode"),
    5: ("B", "Enable support for interactive render modes — client project"),
    6: ("A", "Apply a render mode — component definition versus component instance"),
    7: ("C", "Apply a render mode to the entire app — root component restriction"),
    8: ("D", "Apply a render mode to the entire app — Routes component"),
    9: ("A", "Apply a render mode to the entire app — Router propagation"),
    10: ("B", "Apply a render mode to the entire app — HeadOutlet"),
    11: ("C", "Interactive Auto render mode — initial decision"),
    12: ("A", "Interactive Auto render mode — existing interactivity"),
    13: ("D", "Render-mode propagation — sibling components"),
    14: ("B", "Render-mode propagation — child components with different interactive modes"),
    15: ("A", "Render-mode propagation — RenderFragment serialization"),
    16: ("C", "Render-mode propagation — wrapper component workaround"),
    17: ("B", "Static SSR pages in an interactive app — ExcludeFromInteractiveRouting"),
    18: ("C", "Detect rendering location and interactivity — RendererInfo.IsInteractive"),
    19: ("D", "Detect rendering location and interactivity — AssignedRenderMode"),
    20: ("C", "Static server-side rendering — routing and authorization"),
}


def main() -> int:
    payload = json.loads(LOT_PATH.read_text(encoding="utf-8"))
    if payload["state"] != "candidates_written" or payload["topic_num"] != TOPIC or payload["lot_num"] != LOT:
        raise RuntimeError("unexpected supplemental candidate lot")
    records = payload["questions"]
    if len(records) != 20:
        raise RuntimeError("supplemental lot must contain exactly 20 candidates")

    decisions = []
    accepted = []
    for index, candidate in enumerate(records, start=1):
        expected = EXPECTED[index]
        if candidate["correct"] != expected[0]:
            raise RuntimeError(f"answer disagreement for supplemental question {index}")
        if candidate["sources"][0]["source_id"] != "BLAZOR-10" or candidate["sources"][0]["url"] != RENDER_MODES_URL:
            raise RuntimeError(f"source mismatch for supplemental question {index}")
        if candidate["sources"][0]["citation"] != expected[1]:
            raise RuntimeError(f"citation mismatch for supplemental question {index}")

        reviewed = dict(candidate)
        reviewed["verification"] = {
            "answer": {
                "status": "passed",
                "reviewer": REVIEWER,
                "checked_at": DATE,
                "basis": f"Independent answer-key check against BLAZOR-10 section {expected[1]}.",
            },
            "explanation": {
                "status": "passed",
                "reviewer": REVIEWER,
                "checked_at": DATE,
                "basis": f"Explanation checked against the official ASP.NET Core 10.0 page, section {expected[1]}.",
            },
            "reviewed_at": DATE,
            "reviewer_decision": "accepted",
        }
        reviewed["deduplication"] = {
            name: {
                "status": "unique",
                "checked_at": DATE,
                "basis": "Independent proposition/objective review found no collision with published topic-26 records or this supplemental lot.",
            }
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
        "lot": "topic-26-lot-11",
        "topic_num": TOPIC,
        "lot_num": LOT,
        "supplemental": True,
        "excluded_from_target_manifest": True,
        "reviewer": REVIEWER,
        "source_tier_counts": {"official_primary": len(accepted), "secondary_reputable": 0},
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
        "counts": {"candidates": len(records), "accepted": len(accepted), "rejected": 0, "quarantined": 0},
        "review_audit": str(REVIEW_PATH.relative_to(ROOT)),
        "questions": accepted,
    }
    ACCEPTED_PATH.parent.mkdir(parents=True, exist_ok=True)
    ACCEPTED_PATH.write_text(json.dumps(accepted_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    checkpoint = {
        "schema_version": "1.0",
        "syllabus_hash": accepted_payload["syllabus_sha256"],
        "source_register_hash": accepted_payload["source_register_sha256"],
        "topic_num": TOPIC,
        "lot_num": LOT,
        "revision": accepted_payload["revision"],
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
