# Question-bank quality report — checkpoint 1

**As of:** 2026-10-12 UTC
**Scope:** topics 1, 2 and 3 lot 1 are reviewed, imported and published incrementally.

## Current counts

| Measure | Count | Interpretation |
|---|---:|---|
| Legacy runtime records | 1,200 | Preserved baseline; not validated or counted toward the target |
| Objective slots | 8,000 | 200 per topic; 100 topic-1-to-5 statements researched, 7,900 slots pending |
| Topics 1--3 lot 1 candidates | 60 | Generated only after official-source verification |
| Reviewed accepted artifacts | 60 | Topics 1--3 records passed independent review matrices |
| Quarantined candidate audits | 60 | Original candidate lots remain unchanged as audit trails |
| Deterministic duplicate matches | 0 | Exact, lexical and near-lexical checks against legacy/topic-lot records |
| Semantic/concept decisions | 20 unique | Independently reviewed against the objective and proposition |
| Native import/export | 60 | Accepted topics 1--3 are imported through `seed_data.py`; `frontend/src/questions.js` contains 1,260 records |
| Published batches | 3 | Topics 1--3 are live at `https://micuentadecasa.github.io/dipu/` |

## Lot 1 distributions

Topics 1--3 lot 1 each use 4 basic, 10 intermediate and 6 advanced records. Topic 1 covers `t01-lo-001` through `t01-lo-020`; topic 2 covers `t02-lo-001` through `t02-lo-020`; topic 3 covers `t03-lo-001` through `t03-lo-020`. All three independent review passes accepted 60 official-primary records after answer, explanation, semantic and concept checks. All three batches are live at `https://micuentadecasa.github.io/dipu/`; the deployed JavaScript returned HTTP 200 and contains representative questions from topics 1, 2 and 3.

Candidate, reviewed, audit and checkpoint artifacts are recorded under `lots/`, `accepted/`, `reviews/` and `checkpoints/` for both topics. Re-running the lot/review/import stages is idempotent.

## Source and scope status

- The official call and `temario.md` match exactly on topics 1–40.
- BOE, IETF, W3C, PostgreSQL, Microsoft, OASIS, Git and the resolved DOCM/EU CELEX sources are recorded with retrieval/verification dates in [`source-register.json`](./source-register.json).
- The reviewed batches contain 40 `official_primary` records and 0 `secondary_reputable` records; every question source carries an explicit tier in the record schema.
- Topics 37–39 remain source-gated. The exact attempted URLs, HTTP/WAF observations and dispositions are in `source_blocker_log` in the source register. No questions were generated for those topics.
- SedipuAlba has public manuals for several modules, but Segra and AdminSedeElectrónica lack public authoritative specifications; claims about them remain quarantined.
- Topic 40 remains gated for the exact EN 301 549 edition. Other accessibility sources do not authorize silently substituting an unverified edition.

## Validation status

- `python3 -m unittest discover -s tests -v`: 10 passed.
- `python3 tools/validate_question_bank.py docs/question-bank/lots/topic-01-lot-01.json`: passed for 20 candidates.
- `python3 tools/validate_question_bank.py docs/question-bank/accepted/topic-01-lot-01.json` and topic 2 equivalent: passed for 40 reviewed records.
- Topic 1 and topic 2 import validation passed; legacy snapshot 1,200 preserved, 40 stable/numeric IDs collision-free, followed by native seed/static import.
- JSON parsing, Python compilation and `git diff --check`: passed.
- `cd frontend && npm run lint`: passed.
- `cd frontend && npm run build`: passed; the build uses the unchanged runtime artifact.

The reviewed artifact passes answer, explanation, five-level duplicate review and source checks. Publication milestone: topics 1--3, lot 1, 20 accepted records each, are live at `https://micuentadecasa.github.io/dipu/`; workflow run `38252486326` completed successfully for commit `a59d45f`. No provisional or secondary sources are in these batches. Continue topics 4--5 sequentially.
