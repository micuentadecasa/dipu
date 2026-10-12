# Question-bank milestone 1: source coverage and validation seam

**Status:** source-boundary comparison and pre-generation validation seam completed; no new questions were generated or imported.

**Verified at:** 2026-10-12 (UTC)

## Completed

1. [`syllabus-comparison.md`](./syllabus-comparison.md) compares the preserved official call PDF with `temario.md`. It confirms the exact 40-topic boundary and records the PDF pages and SHA-256 used for the comparison.
2. [`source-register.json`](./source-register.json) records the official source plan, source URLs, version/as-of policy, retrieval and verification dates, topic knowledge-map coverage, and explicit blocked/pending entries. It has one topic-coverage record for every topic 1--40.
3. `docs/question-bank/question-record.schema.json` now accepts the optional `topic_title` and `group_name` context emitted by the legacy Flask adapter without changing the required static-frontend fields.
4. `question_bank/validation.py` provides the pre-export seam: JSON Schema/format validation, option/correct-answer checks, deterministic stable IDs, exact/lexical/near-lexical screening, and explicit `uncertain` results for semantic/concept review that cannot be automated honestly.
5. `question_bank/checkpoints.py` provides append-only lot checkpoints. A retry of the same `(topic_num, lot_num)` and content hashes is a no-op; a conflicting retry is rejected.
6. `tools/validate_question_bank.py` provides a command-line validation entry point. `tests/test_question_bank_validation.py` covers schema acceptance, legacy context fields, malformed records, five-level screening semantics, checkpoint idempotence/conflict handling, and exact 1--40 source coverage.

## Validation run

- `python3 -m unittest discover -s tests -v`: 8 tests passed.
- `python3 -m json.tool docs/question-bank/question-record.schema.json`: passed.
- `python3 -m json.tool docs/question-bank/source-register.json`: passed.
- `uv lock`: passed; `jsonschema` is now declared and locked.
- Existing frontend lint/build remain the milestone-0 baseline; no frontend data was changed.

## Deliberately not done

- No topic lot, objective set, candidate, legacy migration, or `frontend/src/questions.js` export was generated.
- The existing 1,200 records remain untouched and are not counted as validated records.
- Semantic and concept-level duplicate decisions remain reviewer work; the validator does not label them unique automatically.

## Blocking decisions before topic 1, lot 1

- Confirm the pinned versions for PostgreSQL, .NET/C#, ASP.NET Core, EF Core, Blazor, and related technical documentation. The register uses .NET 10/PostgreSQL 18 as a clearly marked proposal, not an accepted assumption.
- Supply the numerical difficulty/question-type target percentages; the repository and task text available to this worker do not contain them.
- Clarify whether “200 distinct learning objectives” means 200 across the bank or 200 per topic.
- Resolve official DOCM URLs/effective versions for Castilla-La Mancha Laws 12/2010 and 4/2018, EUR-Lex edge responses, Administración Electrónica WAF blocks, and public authoritative SedipuAlba module specifications. A missing source remains a quarantine condition.

The next implementation milestone is therefore **source-resolution and objective-map approval**, followed by topic 1, lot 1 only after these gates are resolved. The 8,000 count remains a target, never a padding requirement.
