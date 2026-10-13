# Question-bank quality report — checkpoint 1

**As of:** 2026-10-13 UTC
**Scope:** topics 1--19 lot 1, topic 20 lots 1--5, topics 21--22 lot 1, and topics 23--30 lots 1--5 are published with duplicate-free runtime data.

## Current counts

| Measure | Count | Interpretation |
|---|---:|---|
| Legacy runtime records | 399 | One normalized prompt retained from the pre-cleanup 1,200-record baseline; removed duplicate history remains in Git |
| Objective slots | 8,000 | 200 per topic; 1,320 topic-1-to-30 statements researched, 6,680 slots pending |
| Topics 1--20 lot 1 plus topic 20 lots 2--5, topics 21--22 lot 1, topics 23--30 lots 1--5 candidates | 1,320 | Generated only after source verification |
| Reviewed accepted artifacts | 1,320 | Topics 1--20 lot 1, topic 20 lots 2--5, topics 21--22 lot 1, and topics 23--30 lots 1--5 records passed independent review matrices |
| Quarantined candidate audits | 1,320 | Original candidate lots remain audit trails; 460 answer-leaking records are archived with replacements |
| Deterministic duplicate matches | 0 | Exact, lexical and near-lexical checks against legacy/topic-lot records |
| Semantic/concept decisions | 1,320 unique | Independently reviewed against the objective and proposition |
| Native import/export | 1,320 | Accepted topics 1--20 lot 1, topic 20 lots 2--5, topics 21--22 lot 1, and topics 23--30 lots 1--5 are imported through `seed_data.py`; duplicate-free `frontend/src/questions.js` contains 1,719 records |
| Published batches | 61 | Topics 1--19 lot 1, topic 20 lots 1--5, topics 21--22 lot 1, and topics 23--30 lots 1--5 are published in the native artifacts |

## Lot 1 distributions

Each accepted lot uses 4 basic, 10 intermediate and 6 advanced records. Topics 1--12 use documented official sources; topics 13--17 use PostgreSQL 18, topic 18 uses Microsoft C#, topic 19 uses Microsoft ASP.NET Core MVC and Bootstrap 5.3, topic 20 uses Microsoft EF Core 10, topic 21 uses Microsoft LINQ documentation for .NET 10, topic 22 uses ASP.NET Core model binding/validation and EF Core documentation for .NET 10, topic 23 uses ASP.NET Core security documentation for .NET 10, topic 24 uses ASP.NET Core Web API documentation for .NET 10, topic 25 uses OData 4.01, and topics 26--30 use ASP.NET Core Blazor documentation for .NET 10. Sixty-six independent review passes accepted 1,320 official-primary records across topics 1--30 first lots plus topic 20 lots 2--5 and topics 23--30 expansion lots. Topic 30 contributes 100 records covering DI registration/lifetimes, options/configuration and Blazor hosting-model boundaries, with exactly 20 basic, 50 intermediate and 30 advanced records.

Candidate, reviewed, audit and checkpoint artifacts are recorded under `lots/`, `accepted/`, `reviews/` and `checkpoints/` for topics 1--30, topic 20 lots 2--5, and topics 23--30 lots 1--5. Re-running the lot/review/import stages is idempotent; topic 30 metadata/hash corrections are recorded through append-only revision 4 checkpoints without duplicating the native import markers.

## Source and scope status

- The official call and `temario.md` match exactly on topics 1–40.
- BOE, IETF, W3C, PostgreSQL, Microsoft, OASIS, Git and the resolved DOCM/EU CELEX sources are recorded with retrieval/verification dates in [`source-register.json`](./source-register.json).
- The reviewed batches contain 1,320 `official_primary` records and 0 `secondary_reputable` records; every question source carries an explicit tier in the record schema. Topic 30 adds 100 official-primary Blazor DI/configuration records backed by four version-pinned Microsoft Learn pages; topic 29 adds 100 forms/validation records; topic 28 adds 100 advanced component/style records; the answer-leakage audit found 460 affected records across topics 23--27 and replacements passed independent correction review.
- Topics 37–39 remain source-gated. The exact attempted URLs, HTTP/WAF observations and dispositions are in `source_blocker_log` in the source register. No questions were generated for those topics.
- SedipuAlba has public manuals for several modules, but Segra and AdminSedeElectrónica lack public authoritative specifications; claims about them remain quarantined.
- Topic 40 remains gated for the exact EN 301 549 edition. Other accessibility sources do not authorize silently substituting an unverified edition.

## Validation status

- `python3 -m unittest discover -s tests -v`: 13 passed.
- `python3 tools/validate_question_bank.py docs/question-bank/lots/topic-01-lot-01.json`: passed for 20 candidates.
- `python3 tools/validate_question_bank.py` passed for the twenty first-lot artifacts plus topic 20 lots 2--5, topics 21--22 lot 1, and topics 23--30 lots 1--5 (1,320 records).
- Topics 1--30 first-lot, topic 20 lots 2--5, and topics 23--30 expansion lots import validation passed; the pre-cleanup 1,200-record legacy snapshot remains recoverable in Git, while the current runtime retains 399 unique legacy records and 1,320 accepted records.
- JSON parsing, Python compilation and `git diff --check`: passed.
- `cd frontend && npm run lint`: passed.
- `cd frontend && npm run build`: passed after regenerating the duplicate-free runtime artifact; the answer-leakage audit found 0 remaining affected records.

The reviewed artifacts pass answer, explanation, five-level duplicate review, source checks, and the answer-leakage regression. Topics 23--29 lots 1--5 remain represented by the prior Pages publication; topic 30 is imported and regenerated locally on this branch pending the normal delivery pipeline. Topic 30 contributes 100 accepted official-primary Blazor DI/configuration records, with 0 deterministic duplicate matches and 100 independent semantic/concept decisions. Topic 28 contributes 100 advanced component/style records and topic 29 contributes 100 forms/validation records. Topic 23 contributes 100 accepted official-primary ASP.NET Core security records, topic 24 contributes 100 accepted official-primary ASP.NET Core Web API records, topic 25 contributes 100 accepted official-primary OData records, and topic 26 contributes 100 accepted official-primary Blazor hosting records. Topic 22 lot 1 contributes 20 accepted official-primary ASP.NET Core/EF Core records; topic 21 lot 1 contributes 20 accepted official-primary LINQ records; topic 20 lots 3--5 contribute 60 accepted official-primary EF Core records. Topics 13--17 use PostgreSQL 18; AutoFirma facts remain limited to the official entry point and no version-sensitive claim. No secondary or provisional records are in these batches.
