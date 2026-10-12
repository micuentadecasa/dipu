# Question-bank quality report — checkpoint 1

**As of:** 2026-10-12 UTC
**Scope:** topics 1--10 lot 1 are reviewed, imported and published; topic 11 lot 1 is reviewed and import-validated, ready for deployment.

## Current counts

| Measure | Count | Interpretation |
|---|---:|---|
| Legacy runtime records | 1,200 | Preserved baseline; not validated or counted toward the target |
| Objective slots | 8,000 | 200 per topic; 300 topic-1-to-15 statements researched, 7,700 slots pending |
| Topics 1--11 lot 1 candidates | 220 | Generated only after source verification |
| Reviewed accepted artifacts | 220 | Topics 1--11 records passed independent review matrices |
| Quarantined candidate audits | 220 | Original candidate lots remain unchanged as audit trails |
| Deterministic duplicate matches | 0 | Exact, lexical and near-lexical checks against legacy/topic-lot records |
| Semantic/concept decisions | 100 unique | Independently reviewed against the objective and proposition |
| Native import/export | 220 | Accepted topics 1--11 are imported through `seed_data.py`; `frontend/src/questions.js` contains 1,420 records |
| Published batches | 10 | Topics 1--10 are live at `https://micuentadecasa.github.io/dipu/`; topic 11 is deployment-ready |

## Lot 1 distributions

Topics 1--11 lot 1 each use 4 basic, 10 intermediate and 6 advanced records. Topics 1--10 use documented official sources; topic 11 uses the official BOE Real Decreto 311/2022 source. All eleven independent review passes accepted 220 official-primary records after answer, explanation, semantic and concept checks. Topics 1--10 are live at `https://micuentadecasa.github.io/dipu/`; topic 11 is ready for the next deployment.

Candidate, reviewed, audit and checkpoint artifacts are recorded under `lots/`, `accepted/`, `reviews/` and `checkpoints/` for topics 1--5. Re-running the lot/review/import stages is idempotent.

## Source and scope status

- The official call and `temario.md` match exactly on topics 1–40.
- BOE, IETF, W3C, PostgreSQL, Microsoft, OASIS, Git and the resolved DOCM/EU CELEX sources are recorded with retrieval/verification dates in [`source-register.json`](./source-register.json).
- The reviewed batches contain 220 `official_primary` records and 0 `secondary_reputable` records; every question source carries an explicit tier in the record schema.
- Topics 37–39 remain source-gated. The exact attempted URLs, HTTP/WAF observations and dispositions are in `source_blocker_log` in the source register. No questions were generated for those topics.
- SedipuAlba has public manuals for several modules, but Segra and AdminSedeElectrónica lack public authoritative specifications; claims about them remain quarantined.
- Topic 40 remains gated for the exact EN 301 549 edition. Other accessibility sources do not authorize silently substituting an unverified edition.

## Validation status

- `python3 -m unittest discover -s tests -v`: 10 passed.
- `python3 tools/validate_question_bank.py docs/question-bank/lots/topic-01-lot-01.json`: passed for 20 candidates.
- `python3 tools/validate_question_bank.py` passed for all five accepted artifacts (100 records).
- Topic 1--5 import validation passed; legacy snapshot 1,200 preserved, 100 stable/numeric IDs collision-free, followed by native seed/static import.
- JSON parsing, Python compilation and `git diff --check`: passed.
- `cd frontend && npm run lint`: passed.
- `cd frontend && npm run build`: passed; the build uses the unchanged runtime artifact.

The reviewed artifacts pass answer, explanation, five-level duplicate review and source checks. Publication milestone: topics 1--10, lot 1, 20 accepted records each, are live at `https://micuentadecasa.github.io/dipu/`; workflow run `38256919688` completed successfully for commit `db9d416`. Topic 11 has 20 accepted official-primary records from the official ENS source and is ready for deployment. AutoFirma facts remain limited to the official entry point and no version-sensitive claim. No secondary or provisional records are in these batches.
