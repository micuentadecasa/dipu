"""Append-only, idempotent lot checkpoints for sequential question-bank work."""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

_REQUIRED_FIELDS = {
    "schema_version",
    "syllabus_hash",
    "source_register_hash",
    "topic_num",
    "lot_num",
    "objective_ids",
    "stable_ids",
    "counts",
    "input_hash",
    "output_hash",
    "last_import",
}


class CheckpointError(ValueError):
    """Raised when a checkpoint would make resumability ambiguous."""


def file_sha256(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def checkpoint_key(manifest: dict[str, Any]) -> tuple[int, int]:
    try:
        topic_num = int(manifest["topic_num"])
        lot_num = int(manifest["lot_num"])
    except (KeyError, TypeError, ValueError) as exc:
        raise CheckpointError("checkpoint requires numeric topic_num and lot_num") from exc
    if topic_num not in range(1, 41) or lot_num < 1:
        raise CheckpointError("checkpoint topic_num must be 1-40 and lot_num must be positive")
    return topic_num, lot_num


def validate_manifest(manifest: dict[str, Any]) -> None:
    missing = _REQUIRED_FIELDS - manifest.keys()
    if missing:
        raise CheckpointError(f"checkpoint missing fields: {', '.join(sorted(missing))}")
    checkpoint_key(manifest)
    if not isinstance(manifest["objective_ids"], list) or not isinstance(manifest["stable_ids"], list):
        raise CheckpointError("objective_ids and stable_ids must be lists")
    if len(set(manifest["stable_ids"])) != len(manifest["stable_ids"]):
        raise CheckpointError("stable_ids must be unique within a lot")
    if not isinstance(manifest["counts"], dict):
        raise CheckpointError("counts must be an object")
    if not isinstance(manifest["last_import"], dict):
        raise CheckpointError("last_import must be an object")
    for field in ("syllabus_hash", "source_register_hash", "input_hash", "output_hash"):
        if not isinstance(manifest[field], str) or not manifest[field]:
            raise CheckpointError(f"{field} must be a non-empty content hash")


def manifest_digest(manifest: dict[str, Any]) -> str:
    payload = {key: value for key, value in manifest.items() if key not in {"recorded_at"}}
    return hashlib.sha256(json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")).hexdigest()


def append_checkpoint(path: str | Path, manifest: dict[str, Any]) -> bool:
    """Append a lot once; return False for an identical retry, reject conflicts."""
    validate_manifest(manifest)
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    key = checkpoint_key(manifest)
    digest = manifest_digest(manifest)
    if target.exists():
        for line_number, line in enumerate(target.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                previous = json.loads(line)
            except json.JSONDecodeError as exc:
                raise CheckpointError(f"invalid checkpoint JSON on line {line_number}") from exc
            if checkpoint_key(previous) != key:
                continue
            if manifest_digest(previous) == digest:
                return False
            raise CheckpointError(f"checkpoint {key[0]}/{key[1]} already exists with different content")
    record = dict(manifest)
    record.setdefault("recorded_at", datetime.now(timezone.utc).date().isoformat())
    with target.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
    return True


def load_checkpoints(path: str | Path) -> list[dict[str, Any]]:
    target = Path(path)
    if not target.exists():
        return []
    records = []
    for line_number, line in enumerate(target.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            raise CheckpointError(f"invalid checkpoint JSON on line {line_number}") from exc
        validate_manifest(record)
        records.append(record)
    return records
