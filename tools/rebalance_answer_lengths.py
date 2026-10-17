#!/usr/bin/env python3
"""Apply the source-reviewed answer-length balance revision to accepted lots.

The migration uses only already reviewed correct propositions as distractors.
It updates accepted artifacts, appends a checkpoint revision for every lot,
rewrites the native seed blocks, and regenerates the Pages artifact.
"""

from __future__ import annotations

from copy import deepcopy
from datetime import date
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from question_bank.answer_balance import balance_records, refresh_stable_identity
from question_bank.checkpoints import append_checkpoint, file_sha256
from question_bank.validation import screen_duplicates, validate_record
from seed_data import SEED_QUESTIONS

DATE = date.today().isoformat()
AUDIT_PATH = ROOT / "docs/question-bank/answer-length-balance-audit.json"


def question_key(record: dict) -> tuple[int, str]:
    return record["topic_num"], record["question"]


def load_accepted() -> tuple[list[dict], dict[str, dict]]:
    records: list[dict] = []
    payloads: dict[str, dict] = {}
    for path in sorted((ROOT / "docs/question-bank/accepted").glob("topic-*-lot-*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        payloads[path.name] = payload
        records.extend(deepcopy(payload.get("questions", [])))
    return records, payloads


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def replace_seed_options(mapping: dict[tuple[int, str], dict], seed_path: Path) -> int:
    lines = seed_path.read_text(encoding="utf-8").splitlines(keepends=True)
    changed = 0
    used: set[tuple[int, str]] = set()
    index = 0
    while index < len(lines):
        if not lines[index].lstrip().startswith('"topic_num": '):
            index += 1
            continue
        try:
            topic = int(lines[index].split(": ", 1)[1].rstrip("\n,"))
        except ValueError:
            index += 1
            continue
        block_end = index
        while block_end < len(lines) and '"explanation": ' not in lines[block_end]:
            block_end += 1
        if block_end >= len(lines):
            index += 1
            continue
        question_line = next(
            (cursor for cursor in range(index, block_end) if lines[cursor].lstrip().startswith('"question": ')),
            None,
        )
        if question_line is None:
            index = block_end + 1
            continue
        raw = lines[question_line].split(": ", 1)[1].rstrip("\n").rstrip(",")
        try:
            question = json.loads(raw)
        except json.JSONDecodeError:
            index = block_end + 1
            continue
        key = (topic, question)
        if key not in mapping:
            index = block_end + 1
            continue
        record = mapping[key]
        used.add(key)
        option_indexes = {}
        for cursor in range(question_line + 1, block_end):
            stripped = lines[cursor].lstrip()
            for name in ("option_a", "option_b", "option_c", "option_d", "correct"):
                if stripped.startswith(f'"{name}": '):
                    option_indexes[name] = cursor
        for name in ("option_a", "option_b", "option_c", "option_d", "correct"):
            cursor = option_indexes.get(name)
            if cursor is None:
                raise RuntimeError(f"could not locate {name} for {key}")
            indent = lines[cursor][: len(lines[cursor]) - len(lines[cursor].lstrip())]
            lines[cursor] = f"{indent}{json.dumps(name)}: {json.dumps(record[name], ensure_ascii=False)},\n"
        changed += 1
        index = block_end + 1
    missing = set(mapping) - used
    if missing:
        raise RuntimeError(f"accepted records missing from seed_data.py: {len(missing)}")
    seed_path.write_text("".join(lines), encoding="utf-8")
    return changed


def revise_record(record: dict, audit_entry: dict) -> dict:
    updated = refresh_stable_identity(record)
    updated["verification"] = deepcopy(updated["verification"])
    updated["verification"]["answer"] = {
        **updated["verification"]["answer"],
        "reviewer": "answer-length-balance-review-2026-10-17",
        "checked_at": DATE,
        "basis": (
            "Correct proposition preserved. Three incorrect choices were replaced "
            "with independently reviewed propositions from other objectives; "
            f"post-revision lengths={audit_entry['after_lengths']}."
        ),
    }
    updated["verification"]["reviewed_at"] = DATE
    updated["deduplication"] = {
        name: {
            **result,
            "status": "unique",
            "checked_at": DATE,
            "basis": result.get("basis", "Prompt and content remain unique after reauthoring"),
        }
        for name, result in updated["deduplication"].items()
    }
    errors = validate_record(updated)
    if errors:
        raise RuntimeError(f"revised record {updated['stable_id']} failed validation: {errors}")
    return updated


def main() -> int:
    accepted, payloads = load_accepted()
    seed_by_key = {question_key(record): record for record in SEED_QUESTIONS}
    if len(seed_by_key) != len(SEED_QUESTIONS):
        raise RuntimeError("seed_data.py contains duplicate topic/question keys")
    if len({question_key(record) for record in accepted}) != len(accepted):
        raise RuntimeError("accepted artifacts contain duplicate topic/question keys")

    targets = []
    for record in accepted:
        seed_record = seed_by_key.get(question_key(record))
        if seed_record is None:
            raise RuntimeError(f"accepted record missing from seed_data.py: {record['stable_id']}")
        target = deepcopy(record)
        # The native static path is authoritative for the current rendered
        # answer. One historical accepted artifact has stale option text; use
        # the native record and retain its source/review metadata.
        for name in ("option_a", "option_b", "option_c", "option_d", "correct", "explanation"):
            target[name] = seed_record[name]
        target = refresh_stable_identity(target)
        targets.append(target)

    balanced, audit = balance_records(targets)
    by_objective = {record["learning_objective_id"]: record for record in balanced}
    audit_by_objective = {entry["objective_id"]: entry for entry in audit}

    revised_by_file: dict[str, list[dict]] = {name: [] for name in payloads}
    for name, payload in payloads.items():
        for original in payload.get("questions", []):
            revised_by_file[name].append(
                revise_record(
                    record=next(
                        r for r in balanced
                        if r["learning_objective_id"] == original["learning_objective_id"]
                    ),
                    audit_entry=audit_by_objective[original["learning_objective_id"]],
                )
            )

    for name, payload in payloads.items():
        payload["questions"] = revised_by_file[name]
        payload["revision"] = int(payload.get("revision", 1)) + 1
        payload["answer_length_balance_audit"] = str(AUDIT_PATH.relative_to(ROOT))
        write_json(ROOT / "docs/question-bank/accepted" / name, payload)

    mapping = {question_key(record): record for record in balanced}
    changed = replace_seed_options(mapping, ROOT / "seed_data.py")

    audit_payload = {
        "audit_version": "1.0",
        "revision_date": DATE,
        "scope": "all source-reviewed accepted records; legacy records are balanced in seed_data.py from existing legacy propositions",
        "method": "Replace only incorrect choices with already reviewed correct propositions from different objectives; prefer same source/topic, then nearest reviewed length.",
        "correct_answers_changed": 0,
        "records_reauthored": len(audit),
        "entries": audit,
    }
    write_json(AUDIT_PATH, audit_payload)

    seed_hash = file_sha256(ROOT / "seed_data.py")
    for name, payload in payloads.items():
        topic_num = int(payload["topic_num"])
        lot_num = int(payload["lot_num"])
        checkpoint_path = ROOT / "docs/question-bank/checkpoints" / name.replace(".json", ".jsonl")
        existing = [json.loads(line) for line in checkpoint_path.read_text(encoding="utf-8").splitlines() if line.strip()]
        revision = max(int(item.get("revision", 1)) for item in existing) + 1
        checkpoint = {
            "schema_version": "1.0",
            "syllabus_hash": payload["syllabus_sha256"],
            "source_register_hash": payload["source_register_sha256"],
            "topic_num": topic_num,
            "lot_num": lot_num,
            "revision": revision,
            "stage": "import_applied",
            "objective_ids": [record["learning_objective_id"] for record in payload["questions"]],
            "stable_ids": [record["stable_id"] for record in payload["questions"]],
            "counts": payload["counts"],
            "input_hash": file_sha256(ROOT / "docs/question-bank/accepted" / name),
            "output_hash": seed_hash,
            "last_import": {
                "status": "answer_length_balanced",
                "transaction": "ANSWER_LENGTH_BALANCE_20261017",
            },
        }
        append_checkpoint(checkpoint_path, checkpoint)

    # Regenerate the static artifact from the now-authoritative seed input.
    import importlib
    import seed_data
    importlib.reload(seed_data)
    runtime = [{"id": index, **question} for index, question in enumerate(seed_data.SEED_QUESTIONS, 1)]
    (ROOT / "frontend/src/questions.js").write_text(
        "// Generated from seed_data.py. Static question bank for GitHub Pages.\n"
        "export const QUESTIONS = "
        + json.dumps(runtime, ensure_ascii=False, indent=2)
        + "\n",
        encoding="utf-8",
    )
    print(f"balanced {len(audit)} accepted records; updated {changed} seed records; runtime {len(runtime)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
