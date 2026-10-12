# Question-bank quality report — checkpoint 1

**As of:** 2026-10-12 UTC
**Scope:** candidate lot only; no candidate is accepted or shipped.

## Current counts

| Measure | Count | Interpretation |
|---|---:|---|
| Legacy runtime records | 1,200 | Preserved baseline; not validated or counted toward the target |
| Objective slots | 8,000 | 200 per topic; 20 topic-1 statements researched, 7,980 slots pending |
| Topic 1 lot 1 candidates | 20 | Generated only after BOE source verification |
| Accepted new records | 0 | No record has passed independent answer/explanation review |
| Quarantined candidates | 20 | All lot-1 candidates remain quarantined |
| Deterministic duplicate matches | 0 | Exact, lexical and near-lexical checks against legacy/topic-lot records |
| Semantic/concept decisions | 20 uncertain | Must be decided independently; uncertainty is never counted as unique |
| New static export/import | 0 | `frontend/src/questions.js` and runtime storage are untouched |

## Lot 1 distributions

Topic 1, lot 1 uses 4 basic, 10 intermediate and 6 advanced candidates. It covers objective IDs `t01-lo-001` through `t01-lo-020`; every candidate cites the verified BOE Constitution source with an article/structure citation. All answer and explanation reviews are `uncertain` pending a second reviewer.

The lot is recorded in [`lots/topic-01-lot-01.json`](./lots/topic-01-lot-01.json) and checkpointed in [`checkpoints/topic-01-lot-01.jsonl`](./checkpoints/topic-01-lot-01.jsonl). Re-running its builder is idempotent and does not append a second checkpoint line.

## Source and scope status

- The official call and `temario.md` match exactly on topics 1–40.
- BOE, IETF, W3C, PostgreSQL, Microsoft, OASIS, Git and the resolved DOCM/EU CELEX sources are recorded with retrieval/verification dates in [`source-register.json`](./source-register.json).
- Topics 37–39 remain source-gated. The exact attempted URLs, HTTP/WAF observations and dispositions are in `source_blocker_log` in the source register. No questions were generated for those topics.
- SedipuAlba has public manuals for several modules, but Segra and AdminSedeElectrónica lack public authoritative specifications; claims about them remain quarantined.
- Topic 40 remains gated for the exact EN 301 549 edition. Other accessibility sources do not authorize silently substituting an unverified edition.

## Validation status

- `python3 -m unittest discover -s tests -v`: 10 passed.
- `python3 tools/validate_question_bank.py docs/question-bank/lots/topic-01-lot-01.json`: passed for 20 records.
- JSON parsing, Python compilation and `git diff --check`: passed.
- Frontend lint/build baseline remains green; no frontend data changed.

The next gate is independent review of topic 1 lot 1. Only records that pass answer, explanation, five-level duplicate review and source checks may transition from quarantined to validated and later be imported.
