# Question-bank quality report — checkpoint 1

**As of:** 2026-10-12 UTC
**Scope:** topics 1--19 lot 1, topic 20 lots 1--5 and topics 21--23 lot 1 are published; topic 24 lot 1 is import-validated pending deployment.

## Current counts

| Measure | Count | Interpretation |
|---|---:|---|
| Legacy runtime records | 399 | One normalized prompt retained from the pre-cleanup 1,200-record baseline; removed duplicate history remains in Git |
| Objective slots | 8,000 | 200 per topic; 560 topic-1-to-24 statements researched, 7,440 slots pending |
| Topics 1--20 lot 1 plus topic 20 lots 2--5, topics 21--24 lot 1 candidates | 560 | Generated only after source verification |
| Reviewed accepted artifacts | 560 | Topics 1--20 lot 1, topic 20 lots 2--5, and topics 21--24 lot 1 records passed independent review matrices |
| Quarantined candidate audits | 560 | Original candidate lots remain unchanged as audit trails |
| Deterministic duplicate matches | 0 | Exact, lexical and near-lexical checks against legacy/topic-lot records |
| Semantic/concept decisions | 560 unique | Independently reviewed against the objective and proposition |
| Native import/export | 560 | Accepted topics 1--20 lot 1, topic 20 lots 2--5, and topics 21--24 lot 1 are imported through `seed_data.py`; duplicate-free `frontend/src/questions.js` contains 959 records |
| Published batches | 27 | Topics 1--19 lot 1, topic 20 lots 1--5 and topics 21--23 lot 1 are live; topic 24 lot 1 is pending deployment |

## Lot 1 distributions

Each accepted lot uses 4 basic, 10 intermediate and 6 advanced records. Topics 1--12 use documented official sources; topics 13--17 use PostgreSQL 18, topic 18 uses Microsoft C#, topic 19 uses Microsoft ASP.NET Core MVC and Bootstrap 5.3, topic 20 uses Microsoft EF Core 10, topic 21 uses Microsoft LINQ documentation for .NET 10, topic 22 uses ASP.NET Core model binding/validation and EF Core documentation for .NET 10, topic 23 uses ASP.NET Core security documentation for .NET 10, and topic 24 uses ASP.NET Core Web API documentation for .NET 10. Twenty-eight independent review passes accepted 560 official-primary records across topics 1--24 lot 1 plus topic 20 lots 2--5. Topics 1--19 lot 1, topic 20 lots 1--5 and topics 21--24 lot 1 are live at `https://micuentadecasa.github.io/dipu/`.

Candidate, reviewed, audit and checkpoint artifacts are recorded under `lots/`, `accepted/`, `reviews/` and `checkpoints/` for topics 1--24 and topic 20 lots 2--5. Re-running the lot/review/import stages is idempotent.

## Source and scope status

- The official call and `temario.md` match exactly on topics 1–40.
- BOE, IETF, W3C, PostgreSQL, Microsoft, OASIS, Git and the resolved DOCM/EU CELEX sources are recorded with retrieval/verification dates in [`source-register.json`](./source-register.json).
- The reviewed batches contain 560 `official_primary` records and 0 `secondary_reputable` records; every question source carries an explicit tier in the record schema.
- Topics 37–39 remain source-gated. The exact attempted URLs, HTTP/WAF observations and dispositions are in `source_blocker_log` in the source register. No questions were generated for those topics.
- SedipuAlba has public manuals for several modules, but Segra and AdminSedeElectrónica lack public authoritative specifications; claims about them remain quarantined.
- Topic 40 remains gated for the exact EN 301 549 edition. Other accessibility sources do not authorize silently substituting an unverified edition.

## Validation status

- `python3 -m unittest discover -s tests -v`: 11 passed.
- `python3 tools/validate_question_bank.py docs/question-bank/lots/topic-01-lot-01.json`: passed for 20 candidates.
- `python3 tools/validate_question_bank.py` passed for the twenty first-lot artifacts plus topic 20 lots 2--5 and topics 21--24 lot 1 (560 records).
- Topic 1--24 first-lot and topic 20 lots 2--5 import validation passed; the pre-cleanup 1,200-record legacy snapshot remains recoverable in Git, while the current runtime retains 399 unique legacy records and 560 accepted records.
- JSON parsing, Python compilation and `git diff --check`: passed.
- `cd frontend && npm run lint`: passed.
- `cd frontend && npm run build`: passed after regenerating the duplicate-free runtime artifact.

The reviewed artifacts pass answer, explanation, five-level duplicate review and source checks. Publication milestone: topics 1--19 lot 1, topic 20 lots 1--5 and topics 21--24 lot 1 are live at `https://micuentadecasa.github.io/dipu/`; workflow run `38289502860` completed successfully for commit `d6dd94c`. Topic 24 lot 1 contributes 20 accepted official-primary ASP.NET Core Web API records; topic 23 lot 1 contributes 20 accepted official-primary ASP.NET Core security records; topic 22 lot 1 contributes 20 accepted official-primary ASP.NET Core/EF Core records; topic 21 lot 1 contributes 20 accepted official-primary LINQ records; topic 20 lots 3--5 contribute 60 accepted official-primary EF Core records. Topics 13--17 use PostgreSQL 18; AutoFirma facts remain limited to the official entry point and no version-sensitive claim. No secondary or provisional records are in these batches.
