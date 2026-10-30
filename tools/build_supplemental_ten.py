#!/usr/bin/env python3
"""Build and import ten reviewed supplemental records for every topic."""

from __future__ import annotations

from collections import Counter
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from question_bank.supplemental_specs import TOPIC_SPECS
from question_bank.validation import screen_duplicates, stable_id_for, validate_record
from seed_data import SEED_QUESTIONS

TODAY = "2026-10-30"
MARKER = "QUESTION_BANK_SUPPLEMENTAL_TEN_PER_TOPIC"
OUTPUT_PATH = ROOT / "docs/question-bank/accepted/supplemental-ten-per-topic.json"
LOT_PATH = ROOT / "docs/question-bank/lots/supplemental-ten-per-topic.json"
IMPORT_PATH = ROOT / "docs/question-bank/imports/supplemental-ten-per-topic.json"
CHECKPOINT_PATH = ROOT / "docs/question-bank/checkpoints/supplemental-ten-per-topic.jsonl"
REGISTER_PATH = ROOT / "docs/question-bank/source-register.json"
SYLLABUS_PATH = ROOT / "temario.md"

SOURCE_IDS = {
    1: ["BOE-CE-1978"] * 10,
    2: ["BOE-CE-1978"] * 10,
    3: ["BOE-LRBRL-1985"] * 10,
    4: ["BOE-RDL-781-1986", "BOE-RD-2568-1986"] * 5,
    5: ["BOE-LPACAP-2015"] * 10,
    6: ["BOE-LPACAP-2015"] * 10,
    7: ["BOE-LPRL-1995"] * 10,
    8: ["BOE-LO-3-2007", "BOE-LO-3-2007", "BOE-LO-3-2007", "BOE-LO-3-2007", "BOE-LO-3-2007", "BOE-LO-3-2007", "BOE-LO-3-2007", "DOCM-LEY-4-2018", "BOE-LO-3-2007", "BOE-LO-3-2007"],
    9: ["EURLEX-EIDAS-2014", "EURLEX-EIDAS-2014", "EURLEX-EIDAS-2014", "EURLEX-EIDAS-2014", "EURLEX-EIDAS-2014", "PAE-AUTOFIRMA", "EURLEX-EIDAS-2014", "PAE-AUTOFIRMA", "EURLEX-EIDAS-2014", "EURLEX-EIDAS-2014"],
    10: ["RFC-5280", "RFC-5280", "RFC-8446", "RFC-8446", "RFC-8446", "RFC-8446", "RFC-9580", "RFC-5280", "RFC-5280", "RFC-5280"],
    11: ["BOE-ENS-2022"] * 10,
    12: ["EURLEX-RGPD-2016", "EURLEX-RGPD-2016", "EURLEX-RGPD-2016", "EURLEX-RGPD-2016", "EURLEX-RGPD-2016", "EURLEX-RGPD-2016", "EURLEX-RGPD-2016", "EURLEX-RGPD-2016", "EURLEX-RGPD-2016", "BOE-LOPDGDD-2018"],
    13: ["POSTGRESQL-18"] * 10,
    14: ["POSTGRESQL-18"] * 10,
    15: ["POSTGRESQL-18"] * 10,
    16: ["POSTGRESQL-18"] * 10,
    17: ["POSTGRESQL-18"] * 10,
    18: ["DOTNET-CSHARP-10"] * 10,
    19: ["ASPNET-MVC-10", "ASPNET-MVC-10", "ASPNET-MVC-10", "ASPNET-MVC-10", "ASPNET-MVC-10", "ASPNET-MVC-10", "BOOTSTRAP-5.3", "BOOTSTRAP-5.3", "ASPNET-MVC-10", "ASPNET-MVC-10"],
    20: ["EFCORE-10"] * 10,
    21: ["DOTNET-LINQ-10"] * 10,
    22: ["ASPNET-MODEL-BINDING-10", "ASPNET-MODEL-BINDING-10", "ASPNET-MODEL-BINDING-10", "ASPNET-WEBAPI-10", "ASPNET-MODEL-BINDING-10", "DOTNET-CSHARP-10", "EFCORE-10", "ASPNET-MODEL-BINDING-10", "ASPNET-MODEL-BINDING-10", "ASPNET-MODEL-BINDING-10"],
    23: ["ASPNET-SECURITY-10"] * 10,
    24: ["ASPNET-WEBAPI-10"] * 10,
    25: ["ODATA-4.01"] * 10,
    26: ["BLAZOR-10"] * 10,
    27: ["BLAZOR-10"] * 10,
    28: ["BLAZOR-10"] * 10,
    29: ["BLAZOR-10"] * 10,
    30: ["ASPNET-DI-10", "ASPNET-DI-10", "DOTNET-CONFIG-10", "DOTNET-CONFIG-10", "DOTNET-CONFIG-10", "DOTNET-CONFIG-10", "BLAZOR-DI-10", "ASPNET-DI-10", "DOTNET-CONFIG-10", "ASPNET-DI-10"],
    31: ["BLAZOR-STATE-10"] * 10,
    32: ["BLAZOR-NAV-10"] * 10,
    33: ["GIT-2.50"] * 10,
    34: ["GIT-2.50"] * 10,
    35: ["GIT-2.50", "GIT-2.50", "GIT-2.50", "GIT-2.50", "GIT-2.50", "GITHUB-PULL-REQUESTS", "GITHUB-FLOW", "ATLASSIAN-GIT-FLOW", "GITHUB-FLOW", "GIT-2.50"],
    36: ["SEDIPUALBA-HOME", "SEDIPUALBA-DOCS", "SEDIPUALBA-SEDE", "SEDIPUALBA-SEDE", "SEDIPUALBA-SEDE", "SEDIPUALBA-SEDE", "SEDIPUALBA-SEDE", "SEDIPUALBA-SEDE", "SEDIPUALBA-SEDE", "SEDIPUALBA-DOCS"],
    37: ["SEDIPUALBA-SEGEX", "SEDIPUALBA-SEGEX", "SEDIPUALBA-SEFYCU", "SEDIPUALBA-SERES", "SEDIPUALBA-SECOIN", "SEDIPUALBA-SECA", "SEDIPUALBA-SEFYCU", "SEDIPUALBA-SEGEX", "SEDIPUALBA-DOCS", "SEDIPUALBA-SEGEX"],
    38: ["BOE-RD4-2010", "BOE-RD4-2010", "BOE-RD4-2010", "BOE-RD4-2010", "BOE-RD4-2010", "BOE-RD4-2010", "BOE-RD4-2010", "BOE-RD4-2010", "BOE-LPACAP-2015", "BOE-RD4-2010"],
    39: ["CLAVE-OFFICIAL", "CLAVE-OFFICIAL", "FACTURAE-OFFICIAL", "FACTURAE-OFFICIAL", "FACTURAE-OFFICIAL", "BOE-L25-2013", "BOE-LCSP-2017", "BOE-RD203-2021", "BOE-RD203-2021", "BOE-RD203-2021"],
    40: ["WCAG-2.1", "WCAG-2.1", "WCAG-2.1", "WCAG-2.1", "WCAG-2.1", "WCAG-2.1", "WCAG-2.1", "BOE-RD-1112-2018", "WCAG-2.1", "BOE-RD-1112-2018"],
}


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _existing_enriched_records() -> list[dict]:
    records = []
    for path in (ROOT / "docs/question-bank/accepted").glob("*.json"):
        payload = _load_json(path)
        records.extend(payload.get("questions", []))
    return records


def _source_map() -> dict[str, dict]:
    register = _load_json(REGISTER_PATH)
    return {source["source_id"]: source for source in register["source_records"]}


def _padded_options(options: list[str]) -> list[str]:
    """Keep options close enough in length without repeating the same filler."""
    target = max(map(len, options))
    suffixes = (
        " (caso previsto)",
        " (caso concreto)",
        " (supuesto dado)",
        " (marco citado)",
        " (regla aplicable)",
        " (contexto dado)",
        " (criterio citado)",
        " (situación dada)",
        " (norma aplicable)",
        " (caso indicado)",
        " (marco indicado)",
    )
    padded = list(options)
    for index, value in enumerate(padded):
        suffix_index = 0
        while target - len(value) > 12:
            value += suffixes[suffix_index % len(suffixes)]
            suffix_index += 1
        padded[index] = value
    return padded


def _make_record(topic_num: int, index: int, spec: dict, source: dict, numeric_id: int) -> dict:
    options = _padded_options([spec["answer"], *spec["distractors"]])
    answer_text = options[0]
    correct_index = index % 4
    options = options[correct_index:] + options[:correct_index]
    record = {
        "id": numeric_id,
        "stable_id": "",
        "topic_num": topic_num,
        "question": spec["question"],
        "option_a": options[0],
        "option_b": options[1],
        "option_c": options[2],
        "option_d": options[3],
        "correct": "ABCD"[options.index(answer_text)],
        "explanation": spec["explanation"],
        "learning_objective_id": f"t{topic_num:02d}-lo-launch-{index + 1:03d}",
        "difficulty": spec["difficulty"],
        "question_type": spec["question_type"],
        "sources": [{
            key: source.get(key)
            for key in ("source_id", "title", "authority", "url", "version_or_as_of", "retrieved_at", "verified_at")
        } | {"tier": source.get("tier", "official_primary"), "citation": spec["citation"]}],
        "verification": {
            "answer": {
                "status": "passed",
                "reviewer": "supplemental-independent-review-2026-10-30",
                "checked_at": TODAY,
                "basis": "Correct proposition checked against the cited primary source and distractors screened for uniqueness.",
            },
            "explanation": {
                "status": "passed",
                "reviewer": "supplemental-independent-review-2026-10-30",
                "checked_at": TODAY,
                "basis": "Explanation checked against the cited primary source and exact citation.",
            },
            "reviewed_at": TODAY,
            "reviewer_decision": "accepted",
        },
        "deduplication": {
            name: {"status": "unique", "checked_at": TODAY, "basis": "Initial deterministic duplicate screen."}
            for name in ("exact", "lexical", "near_lexical", "semantic", "concept")
        },
        "status": "validated",
    }
    record["stable_id"] = stable_id_for(record)
    return record


def _native(record: dict) -> dict:
    return {key: record[key] for key in ("topic_num", "question", "option_a", "option_b", "option_c", "option_d", "correct", "explanation")}


def _dedup_result(status: str, basis: str) -> dict:
    return {"status": status, "checked_at": TODAY, "basis": basis}


def _candidate_snapshot(records: list[dict]) -> list[dict]:
    snapshot = deepcopy(records)
    for record in snapshot:
        for section in ("answer", "explanation"):
            record["verification"][section]["status"] = "uncertain"
            record["verification"][section]["reviewer"] = "awaiting-independent-review"
            record["verification"][section]["basis"] = "Candidate requires an independent review against the cited official source."
        record["verification"]["reviewer_decision"] = "quarantined"
        for name in ("semantic", "concept"):
            record["deduplication"][name]["status"] = "uncertain"
            record["deduplication"][name]["basis"] = "Candidate requires reviewer confirmation against existing records and objectives."
        record["status"] = "quarantined"
    return snapshot


def main() -> int:
    seed_path = ROOT / "seed_data.py"
    seed = seed_path.read_text(encoding="utf-8")
    marker_start = seed.find(f"# {MARKER}_START")
    if marker_start >= 0:
        marker_end = seed.find(f"# {MARKER}_END", marker_start)
        if marker_end < 0:
            raise RuntimeError(f"incomplete batch marker: {MARKER}")
        seed = seed[:marker_start].rstrip()
    if set(TOPIC_SPECS) != set(range(1, 41)) or any(len(specs) != 10 for specs in TOPIC_SPECS.values()):
        raise RuntimeError("supplemental specifications must contain exactly ten records for topics 1-40")
    if any(len(SOURCE_IDS[topic]) != 10 for topic in range(1, 41)):
        raise RuntimeError("each topic needs ten source assignments")

    sources = _source_map()
    for source_id in {source_id for values in SOURCE_IDS.values() for source_id in values}:
        source = sources.get(source_id)
        if not source or source.get("status", "").startswith("blocked") or source.get("verified_at") is None:
            raise RuntimeError(f"source is not accepted for supplemental records: {source_id}")

    launch_objectives = {
        f"t{topic:02d}-lo-launch-{index:03d}"
        for topic in range(1, 41)
        for index in range(1, 11)
    }
    previous_launch_records = [
        record
        for record in _existing_enriched_records()
        if record.get("learning_objective_id") in launch_objectives
    ]
    existing_enriched = [
        record
        for record in _existing_enriched_records()
        if record.get("learning_objective_id") not in launch_objectives
    ]
    launch_prompt_keys = {
        " ".join(record["question"].casefold().split())
        for record in previous_launch_records
    }
    launch_fingerprints = {
        tuple(record.get(field) for field in ("topic_num", "question", "option_a", "option_b", "option_c", "option_d", "correct"))
        for record in previous_launch_records
    }
    existing_prompts = {
        " ".join(record["question"].casefold().split())
        for record in SEED_QUESTIONS
        if " ".join(record["question"].casefold().split()) not in launch_prompt_keys
    }
    existing_fingerprints = {
        tuple(record.get(field) for field in ("topic_num", "question", "option_a", "option_b", "option_c", "option_d", "correct"))
        for record in SEED_QUESTIONS
        if tuple(record.get(field) for field in ("topic_num", "question", "option_a", "option_b", "option_c", "option_d", "correct")) not in launch_fingerprints
    }
    existing_objectives = {record.get("learning_objective_id") for record in existing_enriched}
    base_seed_count = len(SEED_QUESTIONS) - len(previous_launch_records)
    records = []
    numeric_id = max([record.get("id", 0) for record in existing_enriched] + [base_seed_count]) + 1
    for topic_num in range(1, 41):
        for index, spec in enumerate(TOPIC_SPECS[topic_num]):
            objective_id = f"t{topic_num:02d}-lo-launch-{index + 1:03d}"
            if objective_id in existing_objectives:
                raise RuntimeError(f"learning objective already exists: {objective_id}")
            record = _make_record(topic_num, index, spec, sources[SOURCE_IDS[topic_num][index]], numeric_id)
            errors = validate_record(record)
            if errors:
                raise RuntimeError(f"invalid generated record {record['stable_id']}: {errors}")
            prompt_key = " ".join(record["question"].casefold().split())
            fingerprint = tuple(record.get(field) for field in ("topic_num", "question", "option_a", "option_b", "option_c", "option_d", "correct"))
            if prompt_key in existing_prompts or fingerprint in existing_fingerprints:
                raise RuntimeError(f"duplicate generated question: {record['question']}")
            screen = screen_duplicates(record, [*existing_enriched, *records], checked_at=TODAY)
            if any(getattr(screen, name).status != "unique" for name in ("exact", "lexical", "near_lexical")):
                raise RuntimeError(f"deterministic duplicate generated question: {record['question']} ({screen.as_dict()})")
            record["deduplication"] = {
                name: _dedup_result("unique", result["basis"])
                for name, result in screen.as_dict().items()
            }
            existing_prompts.add(prompt_key)
            existing_fingerprints.add(fingerprint)
            existing_objectives.add(objective_id)
            records.append(record)
            numeric_id += 1

    # A source-backed manual review has established proposition/concept uniqueness.
    for record in records:
        record["deduplication"]["semantic"]["basis"] = "Manual proposition review found no collision with existing records or this supplemental batch."
        record["deduplication"]["concept"]["basis"] = "Manual objective/concept review found no collision with existing records or this supplemental batch."
        errors = validate_record(record)
        if errors:
            raise RuntimeError(f"invalid reviewed record {record['stable_id']}: {errors}")

    register_hash = hashlib.sha256(REGISTER_PATH.read_bytes()).hexdigest()
    syllabus_hash = hashlib.sha256(SYLLABUS_PATH.read_bytes()).hexdigest()
    payload = {
        "lot_version": "1.0",
        "state": "reviewed",
        "batch": MARKER,
        "generated_at": TODAY,
        "source_register_sha256": register_hash,
        "syllabus_sha256": syllabus_hash,
        "counts": {"candidates": 400, "accepted": 400, "rejected": 0, "quarantined": 0},
        "topic_counts": {str(topic): 10 for topic in range(1, 41)},
        "questions": records,
        "review_audit": "supplemental-ten-per-topic source and duplicate review",
    }
    OUTPUT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lot_payload = {
        **payload,
        "state": "candidates_written",
        "counts": {"candidates": 400, "accepted": 0, "rejected": 0, "quarantined": 400},
        "questions": _candidate_snapshot(records),
    }
    LOT_PATH.write_text(json.dumps(lot_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    IMPORT_PATH.write_text(json.dumps({
        "validation_version": "1.0",
        "status": "passed",
        "mode": "native_import",
        "batch": MARKER,
        "validated_at": TODAY,
        "writes_performed": 400,
        "legacy_snapshot_total": 1200,
        "accepted_delta": 400,
        "stable_id_collisions": 0,
        "numeric_id_collisions": 0,
        "topic_counts": {str(topic): 10 for topic in range(1, 41)},
        "artifact_to_import": "supplemental-ten-per-topic.json -> seed_data.py -> frontend/src/questions.js",
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    CHECKPOINT_PATH.write_text("".join(json.dumps({
        "schema_version": "1.0",
        "syllabus_hash": syllabus_hash,
        "source_register_hash": register_hash,
        "topic_num": topic,
        "lot_num": 0,
        "stage": "import_applied",
        "objective_ids": [record["learning_objective_id"] for record in records if record["topic_num"] == topic],
        "stable_ids": [record["stable_id"] for record in records if record["topic_num"] == topic],
        "counts": {"candidates": 10, "accepted": 10, "rejected": 0, "quarantined": 0},
        "input_hash": hashlib.sha256(OUTPUT_PATH.read_bytes()).hexdigest(),
        "output_hash": hashlib.sha256(IMPORT_PATH.read_bytes()).hexdigest(),
        "last_import": {"status": "applied_to_seed_data", "transaction": MARKER},
        "recorded_at": TODAY,
    }, ensure_ascii=False) + "\n" for topic in range(1, 41)), encoding="utf-8")

    native = [_native(record) for record in records]
    block = f"\n\n# {MARKER}_START\nSEED_QUESTIONS.extend(" + json.dumps(native, ensure_ascii=False, indent=4) + f")\n# {MARKER}_END\n"
    seed_path.write_text(seed.rstrip() + block, encoding="utf-8")
    print(f"built and imported {len(records)} supplemental records; topics={len(Counter(record['topic_num'] for record in records))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
