# Question-bank quality report — checkpoint 1

**As of:** 2026-10-12 UTC
**Scope:** topic 1 lot 1 is reviewed and import-validated as an artifact; no runtime publication has occurred.

## Current counts

| Measure | Count | Interpretation |
|---|---:|---|
| Legacy runtime records | 1,200 | Preserved baseline; not validated or counted toward the target |
| Objective slots | 8,000 | 200 per topic; 20 topic-1 statements researched, 7,980 slots pending |
| Topic 1 lot 1 candidates | 20 | Generated only after BOE source verification |
| Reviewed accepted artifact | 20 | All topic-1 lot-1 records passed the independent review matrix |
| Quarantined candidate audit | 20 | The original candidate lot remains unchanged as the audit trail |
| Deterministic duplicate matches | 0 | Exact, lexical and near-lexical checks against legacy/topic-lot records |
| Semantic/concept decisions | 20 unique | Independently reviewed against the objective and proposition |
| New static export/import | 0 | Import validation was a dry run; `frontend/src/questions.js` remains untouched |

## Lot 1 distributions

Topic 1, lot 1 uses 4 basic, 10 intermediate and 6 advanced candidates. It covers objective IDs `t01-lo-001` through `t01-lo-020`; every candidate cites the verified official BOE Constitution source with an article/structure citation. The independent review pass accepted all 20 records after answer, explanation, semantic and concept checks.

The original candidate lot is recorded in [`lots/topic-01-lot-01.json`](./lots/topic-01-lot-01.json), the reviewed artifact in [`accepted/topic-01-lot-01.json`](./accepted/topic-01-lot-01.json), the review audit in [`reviews/topic-01-lot-01.json`](./reviews/topic-01-lot-01.json), and the append-only checkpoint in [`checkpoints/topic-01-lot-01.jsonl`](./checkpoints/topic-01-lot-01.jsonl). Re-running the lot/review/import stages is idempotent.

## Source and scope status

- The official call and `temario.md` match exactly on topics 1–40.
- BOE, IETF, W3C, PostgreSQL, Microsoft, OASIS, Git and the resolved DOCM/EU CELEX sources are recorded with retrieval/verification dates in [`source-register.json`](./source-register.json).
- The reviewed batch contains 20 `official_primary` records and 0 `secondary_reputable` records; every question source now carries an explicit tier in the record schema.
- Topics 37–39 remain source-gated. The exact attempted URLs, HTTP/WAF observations and dispositions are in `source_blocker_log` in the source register. No questions were generated for those topics.
- SedipuAlba has public manuals for several modules, but Segra and AdminSedeElectrónica lack public authoritative specifications; claims about them remain quarantined.
- Topic 40 remains gated for the exact EN 301 549 edition. Other accessibility sources do not authorize silently substituting an unverified edition.

## Validation status

- `python3 -m unittest discover -s tests -v`: 10 passed.
- `python3 tools/validate_question_bank.py docs/question-bank/lots/topic-01-lot-01.json`: passed for 20 candidates.
- `python3 tools/validate_question_bank.py docs/question-bank/accepted/topic-01-lot-01.json`: passed for 20 reviewed records.
- `python3 tools/validate_accepted_batch.py`: import dry-run passed; legacy snapshot 1,200 preserved, 20 stable/numeric IDs collision-free, zero writes.
- JSON parsing, Python compilation and `git diff --check`: passed.
- `cd frontend && npm run lint`: passed.
- `cd frontend && npm run build`: passed; the build uses the unchanged runtime artifact.

The reviewed artifact passes answer, explanation, five-level duplicate review and source checks. Publication is blocked because `.github/workflows/deploy.yml` deploys on a push to `main` (or an authorized manual dispatch), while this worker is forbidden to push or merge without captain/firstmate authority. No runtime artifact was changed; the accepted batch is ready for an authorized native import/export. Therefore there is no published URL to report for this milestone.
