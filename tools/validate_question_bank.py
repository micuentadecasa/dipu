#!/usr/bin/env python3
"""Validate an enriched question-bank JSON array before export/import."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from question_bank.validation import validate_record


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="JSON array or object with a questions array")
    parser.add_argument("--schema", type=Path, default=None, help="Optional schema path")
    args = parser.parse_args()

    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"cannot read JSON: {exc}", file=sys.stderr)
        return 2
    records = payload.get("questions") if isinstance(payload, dict) else payload
    if not isinstance(records, list):
        print("input must be a JSON array or an object containing questions[]", file=sys.stderr)
        return 2

    errors = []
    for index, record in enumerate(records):
        record_errors = validate_record(record, args.schema) if args.schema else validate_record(record)
        errors.extend((index, message) for message in record_errors)
    if errors:
        for index, message in errors:
            print(f"record[{index}]: {message}", file=sys.stderr)
        print(f"invalid: {len(errors)} error(s) across {len(records)} record(s)", file=sys.stderr)
        return 1
    print(f"valid: {len(records)} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
