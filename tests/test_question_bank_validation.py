from __future__ import annotations

import copy
import json
import tempfile
import unicodedata
import unittest
from pathlib import Path

from question_bank.checkpoints import CheckpointError, append_checkpoint, load_checkpoints
from question_bank.validation import screen_duplicates, stable_id_for, validate_record
from seed_data import SEED_QUESTIONS


ROOT = Path(__file__).resolve().parents[1]


def prompt_key(question: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", question).casefold().split())


def fingerprint(record: dict) -> tuple:
    return tuple(record[field] for field in ("topic_num", "question", "option_a", "option_b", "option_c", "option_d"))


def valid_record() -> dict:
    record = {
        "id": 2001,
        "stable_id": "",
        "topic_num": 10,
        "topic_title": "Cifrado, PKI, certificados, SSL/TLS y PGP",
        "group_name": "Grupo seguridad",
        "question": "¿Qué documento vincula una clave pública con la identidad de un sujeto?",
        "option_a": "Un certificado digital",
        "option_b": "Un registro DNS",
        "option_c": "Una tabla de auditoría",
        "option_d": "Un archivo de configuración",
        "correct": "A",
        "explanation": "Un certificado digital contiene una clave pública y la identidad que certifica la autoridad correspondiente.",
        "learning_objective_id": "t10-lo-certificados-identidad",
        "difficulty": "basic",
        "question_type": "definition",
        "sources": [{
            "source_id": "RFC-5280",
            "title": "Internet X.509 Public Key Infrastructure Certificate and CRL Profile",
            "authority": "IETF RFC Editor",
            "tier": "official_primary",
            "url": "https://www.rfc-editor.org/rfc/rfc5280",
            "citation": "section 3",
            "version_or_as_of": "RFC 5280",
            "retrieved_at": "2026-10-12",
            "verified_at": "2026-10-12",
        }],
        "verification": {
            "answer": {"status": "passed", "reviewer": "reviewer-1", "checked_at": "2026-10-12", "basis": "RFC 5280 section 3"},
            "explanation": {"status": "passed", "reviewer": "reviewer-2", "checked_at": "2026-10-12", "basis": "Explanation matches citation"},
            "reviewed_at": "2026-10-12",
            "reviewer_decision": "accepted",
            "code_or_sql": {"status": "not_applicable"},
        },
        "deduplication": {
            name: {"status": "unique", "checked_at": "2026-10-12", "basis": "No match in accepted/quarantine index"}
            for name in ("exact", "lexical", "near_lexical", "semantic", "concept")
        },
        "status": "validated",
    }
    record["stable_id"] = stable_id_for(record)
    return record


class QuestionRecordTests(unittest.TestCase):
    def test_validated_record_matches_schema_and_stable_identity(self):
        record = valid_record()
        self.assertEqual(validate_record(record), [])
        self.assertEqual(record["stable_id"], stable_id_for(record))

    def test_legacy_adapter_fields_are_additive(self):
        record = valid_record()
        self.assertEqual(validate_record(record), [])
        self.assertIn("topic_title", record)
        self.assertIn("group_name", record)

    def test_duplicate_options_and_wrong_identity_are_rejected(self):
        record = valid_record()
        record["option_d"] = record["option_c"]
        record["stable_id"] = "qb-t10-certificados-identidad-0000000000000000"
        errors = validate_record(record)
        self.assertTrue(any("options must be distinct" in error for error in errors))
        self.assertTrue(any("stable_id does not match" in error for error in errors))

    def test_duplicate_screen_keeps_semantic_review_honest(self):
        candidate = valid_record()
        existing = [copy.deepcopy(candidate)]
        screen = screen_duplicates(candidate, existing, checked_at="2026-10-12")
        self.assertEqual(screen.exact.status, "duplicate")
        self.assertEqual(screen.lexical.status, "duplicate")
        self.assertEqual(screen.near_lexical.status, "duplicate")
        self.assertEqual(screen.semantic.status, "uncertain")
        self.assertEqual(screen.concept.status, "uncertain")

    def test_near_lexical_screen_is_deterministic(self):
        candidate = valid_record()
        existing = [copy.deepcopy(candidate)]
        existing[0]["stable_id"] = "qb-t10-other-1111111111111111"
        existing[0]["question"] = "¿Qué documento vincula una clave pública a la identidad de un sujeto?"
        screen = screen_duplicates(candidate, existing, checked_at="2026-10-12")
        self.assertEqual(screen.near_lexical.status, "duplicate")
        self.assertGreaterEqual(screen.near_lexical.score, 0.92)


class RuntimeQuestionBankTests(unittest.TestCase):
    def test_runtime_bank_has_unique_prompts_and_fingerprints(self):
        artifact = (ROOT / "frontend/src/questions.js").read_text(encoding="utf-8")
        runtime = json.loads(artifact[artifact.index("["):])

        self.assertEqual(len(runtime), len(SEED_QUESTIONS))
        self.assertEqual([question["id"] for question in runtime], list(range(1, len(runtime) + 1)))
        self.assertEqual(len({prompt_key(question["question"]) for question in SEED_QUESTIONS}), len(SEED_QUESTIONS))
        self.assertEqual(len({fingerprint(question) for question in SEED_QUESTIONS}), len(SEED_QUESTIONS))
        self.assertEqual(len({prompt_key(question["question"]) for question in runtime}), len(runtime))
        self.assertEqual(len({fingerprint(question) for question in runtime}), len(runtime))


class CheckpointTests(unittest.TestCase):
    def manifest(self):
        return {
            "schema_version": "1.0",
            "syllabus_hash": "a" * 64,
            "source_register_hash": "b" * 64,
            "topic_num": 10,
            "lot_num": 1,
            "objective_ids": ["t10-lo-certificados-identidad"],
            "stable_ids": ["qb-t10-certificados-identidad-0000000000000000"],
            "counts": {"candidates": 1, "accepted": 0, "rejected": 0, "quarantined": 1},
            "input_hash": "c" * 64,
            "output_hash": "d" * 64,
            "last_import": {"status": "not_started", "transaction": None},
        }

    def test_retry_is_idempotent_and_conflicting_lot_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "checkpoints.jsonl"
            manifest = self.manifest()
            self.assertTrue(append_checkpoint(path, manifest))
            self.assertFalse(append_checkpoint(path, manifest))
            self.assertEqual(len(load_checkpoints(path)), 1)
            changed = dict(manifest, output_hash="e" * 64)
            with self.assertRaises(CheckpointError):
                append_checkpoint(path, changed)

    def test_invalid_topic_cannot_enter_checkpoint(self):
        with tempfile.TemporaryDirectory() as directory:
            manifest = dict(self.manifest(), topic_num=41)
            with self.assertRaises(CheckpointError):
                append_checkpoint(Path(directory) / "checkpoints.jsonl", manifest)


class SourceRegisterTests(unittest.TestCase):
    def test_register_has_exact_topic_boundary_and_explicit_open_gates(self):
        register = json.loads((ROOT / "docs/question-bank/source-register.json").read_text(encoding="utf-8"))
        topics = register["topic_coverage"]
        self.assertEqual([topic["topic_num"] for topic in topics], list(range(1, 41)))
        self.assertTrue(register["open_gates"])
        self.assertEqual(register["official_call"]["source_id"], "CALL-2691")
        self.assertEqual(register["captain_decisions"]["objective_target"], "200 distinct learning objectives per topic, 8,000 objective IDs across topics 1-40")

    def test_objective_manifest_has_200_gated_slots_per_topic(self):
        manifest = json.loads((ROOT / "docs/question-bank/objective-manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["objective_count"], 8000)
        self.assertEqual(manifest["objectives_per_topic"], 200)
        self.assertEqual(manifest["researched_objective_count"], 480)
        topic_counts = {}
        researched_count = 0
        for objective in manifest["objectives"]:
            topic_counts[objective["topic_num"]] = topic_counts.get(objective["topic_num"], 0) + 1
            if objective["statement"] is None:
                self.assertEqual(objective["coverage_state"], "planned_pending_source_verification")
            else:
                researched_count += 1
                self.assertEqual(objective["coverage_state"], "researched_pending_independent_review")
                self.assertTrue(objective["citation"])
            self.assertEqual(objective["reviewer_decision"], "not_reviewed")
        self.assertEqual(researched_count, 480)
        self.assertEqual(topic_counts, {topic: 200 for topic in range(1, 41)})

    def test_topic_one_lot_is_candidate_only_and_blockers_are_recorded(self):
        lot = json.loads((ROOT / "docs/question-bank/lots/topic-01-lot-01.json").read_text(encoding="utf-8"))
        register = json.loads((ROOT / "docs/question-bank/source-register.json").read_text(encoding="utf-8"))
        self.assertEqual(lot["state"], "candidates_written")
        self.assertEqual(lot["counts"]["accepted"], 0)
        self.assertEqual(lot["counts"]["quarantined"], 20)
        self.assertTrue(all(question["status"] == "quarantined" for question in lot["questions"]))
        accepted = json.loads((ROOT / "docs/question-bank/accepted/topic-01-lot-01.json").read_text(encoding="utf-8"))
        import_report = json.loads((ROOT / "docs/question-bank/imports/topic-01-lot-01-dry-run.json").read_text(encoding="utf-8"))
        self.assertEqual(accepted["state"], "reviewed")
        self.assertEqual(accepted["counts"]["accepted"], 20)
        self.assertTrue(all(question["status"] == "validated" for question in accepted["questions"]))
        self.assertEqual(import_report["status"], "passed")
        self.assertEqual(import_report["writes_performed"], 0)
        blocked_topics = {topic for entry in register["source_blocker_log"] for topic in entry["topic_nums"]}
        self.assertTrue({37, 38, 39}.issubset(blocked_topics))


if __name__ == "__main__":
    unittest.main()
