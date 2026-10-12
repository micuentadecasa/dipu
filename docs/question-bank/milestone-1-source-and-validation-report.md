# Question-bank milestone 1: source coverage and validation seam

**Status:** source-boundary comparison and validation seam completed; topics 1--19 lot 1, topic 20 lots 1--5, topics 21--22 lot 1, and topics 23--27 lots 1--5 are published; topic 28 lots 1--5 are staged pending deployment.

**Verified at:** 2026-10-12 (UTC)

## Completed

1. [`syllabus-comparison.md`](./syllabus-comparison.md) compares the preserved official call PDF with `temario.md`. It confirms the exact 40-topic boundary and records the PDF pages and SHA-256 used for the comparison.
2. [`source-register.json`](./source-register.json) records the official source plan, source URLs, version/as-of policy, retrieval and verification dates, topic knowledge-map coverage, and explicit blocked/pending entries. It has one topic-coverage record for every topic 1--40 and records the captain-approved target policy: 200 objectives/topic, 40/100/60 difficulty counts, and 35/45/55/40/25 knowledge-type counts.
3. [`objective-manifest.json`](./objective-manifest.json) records exactly 200 deterministic objective slots per topic (8,000 total), with the approved knowledge-type allocation and source IDs. One thousand one hundred twenty statements for topics 1--28 are researched and independently reviewable; the remaining 6,880 slots have `statement: null` and `planned_pending_source_verification`.
4. `docs/question-bank/question-record.schema.json` now accepts the optional `topic_title` and `group_name` context emitted by the legacy Flask adapter without changing the required static-frontend fields.
5. `question_bank/validation.py` provides the pre-export seam: JSON Schema/format validation, option/correct-answer checks, deterministic stable IDs, exact/lexical/near-lexical screening, and explicit `uncertain` results for semantic/concept review that cannot be automated honestly.
6. `question_bank/checkpoints.py` provides append-only lot-stage checkpoints. A retry of the same topic/lot/revision/stage and content hashes is a no-op; a conflicting retry is rejected.
7. `tools/validate_question_bank.py` provides a command-line validation entry point. `tools/build_objective_manifest.py` rebuilds the objective-slot artifact from the source register. `tests/test_question_bank_validation.py` covers schema acceptance, legacy context fields, malformed records, five-level screening semantics, checkpoint idempotence/conflict handling, and exact 1--40 source coverage.
8. `docs/question-bank/research/objectives/topic-01.json` through `topic-05.json`, `topics-06-15.json`, `topic-16.json` through `topic-28.json` record 1,120 primary-source-backed objective statements. The topic-1 and generic topic-2--28 pipelines produced quarantined candidate audits; separate review artifacts contain 20 accepted records per first lot plus topic 20 lots 2--5, topics 23--28 expansion lots, and topics 21--22 lot 1 after answer, explanation, semantic-duplicate, concept-collision, and answer-leakage correction review. Native imports use `tools/import_accepted_batch.py`.
9. Every question source now carries `official_primary` or `secondary_reputable` tier metadata. The current accepted set contains 1,120 official-primary records and no secondary-source records; 460 affected records are archived and replaced in `quarantine/answer-leakage-audit.json`.

## Validation run

- `python3 -m unittest discover -s tests -v`: 13 tests passed after the schema/review/import, runtime-uniqueness, and answer-leakage additions.
- `python3 -m json.tool docs/question-bank/question-record.schema.json`: passed.
- `python3 -m json.tool docs/question-bank/source-register.json`: passed.
- `python3 tools/build_objective_manifest.py` followed by JSON validation: passed; 8,000 slots, 200 per topic, with source-register and syllabus hashes.
- `python3 tools/validate_question_bank.py docs/question-bank/lots/topic-01-lot-01.json`: passed for 20 candidate records.
- The twenty first-lot artifacts plus topic 20 lots 2--5, topics 21--22 lot 1, topics 23--28 expansion lots and the answer-leakage replacement review passed `python3 tools/validate_question_bank.py`: 1,120 reviewed records.
- Topic 1 and topics 2--28 first-lot imports plus topic 20 lots 2--5, topics 23--28 expansion lots, and the answer-leakage replacements passed validation; the historical 1,200-record baseline remains recoverable in Git, while the current duplicate-free runtime retains 399 unique legacy records and 1,120 collision-free additions.
- Re-running lot, review and import stages produced no duplicate checkpoint stage; checkpoint retries are idempotent.
- `uv lock`: passed; `jsonschema` is now declared and locked.
- Frontend lint/build passed after each native import; the current duplicate-free `frontend/src/questions.js` contains 1,519 runtime records with no detected answer leakage.

## Deliberately not done

- Topics 1--28 first lots, topic 20 lots 2--5, topics 23--28 expansion lots are imported through `seed_data.py` and regenerated into a duplicate-free `frontend/src/questions.js` (1,519 runtime records). The original affected records remain archived in `quarantine/answer-leakage-audit.json`; each separate reviewed artifact contains 20 accepted records. The remaining 6,880 objective slots stay source-gated. The objective manifest is not question content.
- The pre-cleanup 1,200-record baseline remains recoverable in Git but is no longer published wholesale; 399 unique legacy records remain in the runtime and are not counted as validated records.
- Semantic and concept-level duplicate decisions for topics 1--26 first lots, topic 20 lots 2--5, topic 23 lots 2--5, topic 24 lots 2--5 and topics 25--26 lots 1--5 are recorded as independently reviewed unique; future lots still require the same reviewer decision and the validator does not label them unique automatically.

## Blocking decisions before topic 1, lot 1

- The captain-approved current-stable technical-version policy is now recorded; version-sensitive stems must name the version. PostgreSQL 18 and .NET/ASP.NET/EF Core/Blazor 10 are the research-time references.
- Difficulty and knowledge-type targets are recorded per topic; adaptation requires a documented evidence-based reason.
- The objective target is 200 distinct objectives per topic, not 200 objectives reused across lots. The slot manifest is complete, but every statement still needs source research and independent review.
- The official DOCM ELI URLs and Publications Office CELEX fallbacks are now recorded; verify current legal vigency/article amendments before acceptance. Administración Electrónica service pages remain WAF-blocked, and public SedipuAlba evidence remains incomplete for Segra and AdminSedeElectrónica. Missing or unverifiable claims remain quarantined.

Topics 23--26 lots 1--5 are published at `https://micuentadecasa.github.io/dipu/` after successful workflow run `38298599980` for commit `c220179`; topics 23--24 use official ASP.NET Core 10 documentation, topic 25 uses the OData 4.01 OASIS Standard, and topic 26 uses official ASP.NET Core Blazor 10 documentation. Continue with later topics sequentially under the same provenance and quarantine policy. The 8,000 count remains a target, never a padding requirement.
