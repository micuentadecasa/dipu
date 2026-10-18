# Diputest topic-balance audit

**Status:** implemented in `frontend/src/round.js` and covered by `frontend/test/round.test.js`.

## Baseline

The generated runtime artifact contains 4,469 unique, normalized visible questions across official topics 1–40. The source bank is intentionally uneven because accepted records are still being expanded by topic: topics 1–19 and 21–22 have 29–30 records, topics 20 and 23 have 110, and the expanded topics have 200–230 records.

The previous uniform all-bank sampler therefore produced an expected 30-question round of approximately:

- **1.6 questions from topics 1–8**, including the two Constitution topics;
- **4.2 Git questions** from topics 33–35; and
- **10.3 Blazor/Razor-family questions** from topics 26–32.

This was a composition problem, not permission to delete reviewed records or pad underrepresented topics with unsupported material.

## Published round policy

For a full eligible bank, every 30-question round now selects:

- four questions from topics **1–2** combined (Constitution);
- one question from each topic **3–8**;
- one question from each topic **9–12**;
- four questions from distinct topics in **13–17**;
- four questions from distinct topics in **18–25**;
- two questions from distinct topics in **26–32**;
- one question from topics **33–35 combined**;
- one question from each topic **36–40**.

Thus Constitution receives four questions, the other general-syllabus topics are always represented, Git is capped at one question per round, and the Blazor/Razor family is capped at two questions in a full bank. Topic selection and question selection remain randomized within each policy group.

If cooldown state makes a policy group short, the sampler fills available non-Git, non-Blazor questions first and then uses remaining Blazor questions only up to the same cap. It never fills a shortage with a second Git question. A small eligible pool may consequently produce fewer than 30 questions, consistent with the app's existing “up to 30” contract.

The current accepted artifacts contain 20 independently reviewed, source-backed records for each topic 1–8, while the remaining 180 objective slots per topic are still planned pending source verification:

| Topics | Runtime records | Accepted validated records | Researched objectives | Planned pending source verification |
|---|---:|---:|---:|---:|
| 1–8, each topic | 30 | 20 | 20 | 180 |

The accepted source register covers Constitution topics 1–2 with `BOE-CE-1978`, regime local topics 3–4 with `BOE-LRBRL-1985`, `BOE-RDL-781-1986` and `BOE-RD-2568-1986`, LPACAP topics 5–6 with `BOE-LPACAP-2015`, prevention topic 7 with `BOE-LPRL-1995`, and equality topic 8 with `BOE-LO-3-2007`. The sampler therefore improves coverage without promoting unreviewed candidates or inventing unsupported legal questions; further bank expansion must pass the existing source, answer, duplicate, and quarantine gates before publication.

## Preserved gates

The change is limited to runtime composition. It does not alter `seed_data.py`, accepted or quarantined artifacts, source citations, correctness, topic metadata, or generated question IDs. `uniqueQuestions()` still applies NFKC, Spanish case folding, whitespace normalization, and ID filtering before composition. The Python bank validation and the frontend build remain independent gates; deterministic composition tests use the generated runtime artifact.
