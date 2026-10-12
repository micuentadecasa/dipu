#!/usr/bin/env python3
"""Build the deterministic 200-objective-per-topic planning manifest.

This command creates objective *slots*, not accepted evidence-backed objectives.
A slot must receive a researched statement, exact citations, and independent
review before it can be used by a question lot.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTER = ROOT / "docs/question-bank/source-register.json"
DEFAULT_OUTPUT = ROOT / "docs/question-bank/objective-manifest.json"
KNOWLEDGE_TARGETS = {
    "definitions_concepts": 35,
    "mechanisms": 45,
    "practical_application": 55,
    "error_scenario_analysis": 40,
    "relationships": 25,
}


def build(register: dict) -> dict:
    topics = register["topic_coverage"]
    if [topic["topic_num"] for topic in topics] != list(range(1, 41)):
        raise ValueError("source register must contain exactly topics 1-40 in order")
    objectives = []
    for topic in topics:
        objective_index = 1
        scopes = topic["knowledge_map"]
        for knowledge_type, count in KNOWLEDGE_TARGETS.items():
            for offset in range(count):
                objectives.append({
                    "objective_id": f"t{topic['topic_num']:02d}-lo-{objective_index:03d}",
                    "topic_num": topic["topic_num"],
                    "objective_index": objective_index,
                    "knowledge_type": knowledge_type,
                    "scope_hint": scopes[offset % len(scopes)],
                    "source_ids": topic["primary_sources"],
                    "statement": None,
                    "coverage_state": "planned_pending_source_verification",
                    "reviewer_decision": "not_reviewed",
                })
                objective_index += 1
    return {
        "manifest_version": "1.0",
        "created_at": "2026-10-12",
        "status": "planning_slots_only",
        "warning": "These are deterministic objective slots. They are not accepted learning objectives until statement, exact source citation, current-version check, and independent review are recorded.",
        "syllabus_source": "CALL-2691",
        "topic_count": 40,
        "objectives_per_topic": 200,
        "objective_count": len(objectives),
        "knowledge_type_targets_per_topic": KNOWLEDGE_TARGETS,
        "difficulty_target_per_topic": {"basic": 40, "intermediate": 100, "advanced": 60},
        "objectives": objectives,
    }


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--register", type=Path, default=DEFAULT_REGISTER)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    register = json.loads(args.register.read_text(encoding="utf-8"))
    manifest = build(register)
    manifest["source_register_sha256"] = _sha256(args.register)
    manifest["syllabus_sha256"] = _sha256(ROOT / "temario.md")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    objectives = manifest.pop("objectives")
    metadata = json.dumps(manifest, ensure_ascii=False, indent=2)
    metadata = metadata.rsplit("\n}", 1)[0]
    objective_lines = [json.dumps(objective, ensure_ascii=False, separators=(",", ":")) for objective in objectives]
    content = metadata + ',\n  "objectives": [\n' + ",\n".join(f"    {line}" for line in objective_lines) + "\n  ]\n}\n"
    args.output.write_text(content, encoding="utf-8")
    print(f"wrote {manifest['objective_count']} objective slots to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
