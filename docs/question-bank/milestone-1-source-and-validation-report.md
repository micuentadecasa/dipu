# Question-bank milestone 1: source coverage and validation seam

**Status:** source-boundary comparison and pre-generation validation seam completed; topic 1 lot 1 has 20 source-backed candidates, all quarantined pending independent review; no question was accepted, imported, or exported.

**Verified at:** 2026-10-12 (UTC)

## Completed

1. [`syllabus-comparison.md`](./syllabus-comparison.md) compares the preserved official call PDF with `temario.md`. It confirms the exact 40-topic boundary and records the PDF pages and SHA-256 used for the comparison.
2. [`source-register.json`](./source-register.json) records the official source plan, source URLs, version/as-of policy, retrieval and verification dates, topic knowledge-map coverage, and explicit blocked/pending entries. It has one topic-coverage record for every topic 1--40 and records the captain-approved target policy: 200 objectives/topic, 40/100/60 difficulty counts, and 35/45/55/40/25 knowledge-type counts.
3. [`objective-manifest.json`](./objective-manifest.json) records exactly 200 deterministic objective slots per topic (8,000 total), with the approved knowledge-type allocation and source IDs. Slots have `statement: null` and `planned_pending_source_verification`; they are not accepted objectives and cannot generate questions until researched and independently reviewed.
4. `docs/question-bank/question-record.schema.json` now accepts the optional `topic_title` and `group_name` context emitted by the legacy Flask adapter without changing the required static-frontend fields.
5. `question_bank/validation.py` provides the pre-export seam: JSON Schema/format validation, option/correct-answer checks, deterministic stable IDs, exact/lexical/near-lexical screening, and explicit `uncertain` results for semantic/concept review that cannot be automated honestly.
6. `question_bank/checkpoints.py` provides append-only lot checkpoints. A retry of the same `(topic_num, lot_num)` and content hashes is a no-op; a conflicting retry is rejected.
7. `tools/validate_question_bank.py` provides a command-line validation entry point. `tools/build_objective_manifest.py` rebuilds the objective-slot artifact from the source register. `tests/test_question_bank_validation.py` covers schema acceptance, legacy context fields, malformed records, five-level screening semantics, checkpoint idempotence/conflict handling, and exact 1--40 source coverage.
8. `docs/question-bank/research/objectives/topic-01.json` records 20 BOE-backed objective statements. `tools/build_topic01_lot01.py` produced `docs/question-bank/lots/topic-01-lot-01.json` with 20 candidates and an append-only checkpoint at `docs/question-bank/checkpoints/topic-01-lot-01.jsonl`; every candidate is quarantined until answer, explanation, semantic-duplicate, and concept-collision review is independently completed.

## Validation run

- `python3 -m unittest discover -s tests -v`: 8 tests passed.
- `python3 -m json.tool docs/question-bank/question-record.schema.json`: passed.
- `python3 -m json.tool docs/question-bank/source-register.json`: passed.
- `python3 tools/build_objective_manifest.py` followed by JSON validation: passed; 8,000 slots, 200 per topic, with source-register and syllabus hashes.
- `python3 tools/validate_question_bank.py docs/question-bank/lots/topic-01-lot-01.json`: passed for 20 candidate records.
- Re-running the lot builder produced no duplicate checkpoint line; checkpoint retry is idempotent.
- `uv lock`: passed; `jsonschema` is now declared and locked.
- Existing frontend lint/build remain the milestone-0 baseline; no frontend data was changed.

## Deliberately not done

- No question was accepted, legacy migration was run, or `frontend/src/questions.js` export was generated. The 20-record topic-1 lot is candidate-only and fully quarantined. Twenty topic-1 objective statements are researched but pending independent review; the remaining 7,980 slots stay source-gated. The objective manifest is not question content.
- The existing 1,200 records remain untouched and are not counted as validated records.
- Semantic and concept-level duplicate decisions remain reviewer work; the validator does not label them unique automatically.

## Blocking decisions before topic 1, lot 1

- The captain-approved current-stable technical-version policy is now recorded; version-sensitive stems must name the version. PostgreSQL 18 and .NET/ASP.NET/EF Core/Blazor 10 are the research-time references.
- Difficulty and knowledge-type targets are recorded per topic; adaptation requires a documented evidence-based reason.
- The objective target is 200 distinct objectives per topic, not 200 objectives reused across lots. The slot manifest is complete, but every statement still needs source research and independent review.
- The official DOCM ELI URLs and Publications Office CELEX fallbacks are now recorded; verify current legal vigency/article amendments before acceptance. Administración Electrónica service pages remain WAF-blocked, and public SedipuAlba evidence remains incomplete for Segra and AdminSedeElectrónica. Missing or unverifiable claims remain quarantined.

The next implementation milestone is therefore **independent verification/review of topic 1, lot 1**, followed by promotion only for records that pass all five duplicate levels and answer/explanation checks. Other topics remain sequential and source-gated; topics 37-39 have no generated lot. The 8,000 count remains a target, never a padding requirement.
