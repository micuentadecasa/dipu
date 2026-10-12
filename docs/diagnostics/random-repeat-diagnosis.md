# Diputest random-repeat diagnosis

**Status:** diagnosis complete; no product code or question data was changed.

## Conclusion

The repeat is a **question-bank content problem, amplified by an otherwise correct random sampler**. `App.jsx` shuffles the 1,500 runtime records with an in-place Fisher–Yates pass over a copy and takes the first 30. It cannot select the same array element twice in one round. The artifact has only **699 distinct normalized prompts** and **940 distinct prompt+options fingerprints**: many legacy records are repeated copies or repeated stems with option permutations. A 30-record sample therefore sometimes renders the same stem, and less often the same stem and options, more than once.

The newly accepted records (IDs 1201–1500) are clean in this respect: 300 distinct prompts and 300 distinct fingerprints, with no overlap with the legacy set. They do not remove the repeated legacy records from the runtime pool.

## Reproduction setup and end-user path

- Published URL: `https://micuentadecasa.github.io/dipu/`.
- Published `main` during capture: commit `f4c4a8c` (`Record topic fifteen publication`); the successful GitHub Pages workflow uses `npm ci`, `npm run build`, and publishes `frontend/dist`. The default branch advanced to topic 16 after this capture; all counts below are explicitly for the published `f4c4a8c` snapshot.
- Local path: production build (`cd frontend && npm run build`) served at `http://127.0.0.1:4173/` with `npm run preview -- --host 127.0.0.1`.
- Browser tool: `chrome-devtools-axi`, opening each URL and exercising the visible `Nueva ronda` button.
- Configuration observed in both paths: **30 questions per round**, all **1,500 records**, topics 1–40 mixed; there are no topic, pool, length, pagination, or seed controls.
- Each initial load and each `Nueva ronda` rendered 30 cards. DOM fingerprints from the live rounds all matched records in the `f4c4a8c` `frontend/src/questions.js` artifact; no live-only or missing records were observed.

For each measured round, the browser captured topic, prompt, and all four displayed options. A prompt repeat means the prompt after NFKC/case/whitespace normalization appeared twice. A content-fingerprint repeat means the tuple `(topic_num, question, option_a, option_b, option_c, option_d)` appeared twice.

## Reproduction results

500 fresh rounds were generated per path by clicking `Nueva ronda` and waiting for the React render.

| Path | Prompt-repeat rounds | Prompt-repeat groups | Fingerprint-repeat rounds | Fingerprint-repeat groups | Maximum multiplicity |
|---|---:|---:|---:|---:|---:|
| Published live | 253/500 (**50.6%**) | 332 | 114/500 (**22.8%**) | 138 | prompt 3; fingerprint 3 |
| Local preview | 261/500 (**52.2%**) | 355 | 105/500 (**21.0%**) | 114 | prompt 3; fingerprint 2 |

Representative live round: cards 22 and 25 both rendered topic 4, `Que norma aprueba el texto refundido de disposiciones legales vigentes en materia de regimen local?`, with options `Real Decreto Legislativo 781/1986 / Ley 39/2015 / Ley Organica 3/2018 / Real Decreto 203/2021`. The local artifact maps that exact fingerprint to IDs **239, 251, and 263**; the fingerprint is `3828ba811d6aa2c1` (SHA-256 prefix). This is a content duplicate across distinct records, not evidence that one ID was returned twice.

Representative local round: cards 2 and 30 both rendered topic 12, `Como se llama la persona fisica identificada o identificable sobre la que trata la informacion?`, with the same options. The artifact maps that fingerprint to IDs **448, 460, and 472**, fingerprint `c042e6b38ec7d718`.

A fixed-runtime counterfactual also behaved deterministically: replacing `Math.random` temporarily with the same seeded generator produced the same 30-card DOM twice (`same: true`), with no prompt or fingerprint duplicate for that seed. This supports “random choice exposes existing duplicates,” not “randomness invents duplicates.”

## Bank and duplicate inventory

Computed from the `f4c4a8c` snapshot of `frontend/src/questions.js`:

| Set | Records | Distinct normalized prompts | Prompt duplicate groups / records in groups | Distinct fingerprints | Fingerprint duplicate groups / records in groups |
|---|---:|---:|---:|---:|---:|
| Legacy IDs 1–1200 | 1,200 | 399 | 240 / 1,041 | 640 | 480 / 1,040 |
| Accepted IDs 1201–1500 | 300 | 300 | 0 / 0 | 300 | 0 / 0 |
| Runtime total | 1,500 | 699 | 240 / 1,041 | 940 | 480 / 1,040 |

The legacy prompt duplicates include both exact full copies and same-stem variants with option permutations. For example, prompt `Que ley estatal regula la igualdad efectiva de mujeres y hombres?` occurs at IDs 95, 343, 349, 355, 361, and 367; IDs 343/355/367 share one fingerprint while 349/361 share another. These are visible/lexical duplicates; this inventory does not claim to classify every broader concept-level semantic collision.

The accepted-batch quality report's “0 deterministic duplicate matches” and “300 semantic/concept unique” refer to the new reviewed records screened against existing records. The validator does not retroactively deduplicate the pre-existing 1,200-record baseline. `tools/import_accepted_batch.py` appends accepted records and regenerates the static artifact, preserving the legacy records by design.

## Causal boundary and hypotheses

### Initiating trigger

A load or `Nueva ronda` calls `makeRound()`, which shuffles the complete runtime array and slices 30 records. Any repeated legacy record/stem in those 30 slots becomes visible.

### Masking condition

The user is sampling only 30 of 1,500 records, so the collision is probabilistic. The clean 300-record addition increases total size but does not change the 1,200-record legacy subset. Exact fingerprint collisions are less frequent than stem collisions because some repeated prompts have different option ordering.

### Visible symptom

The user sees the same question wording, sometimes with the same answer choices, in one 30-question round. The user does **not** see evidence of the same numeric record ID being selected twice in a round.

### Hypothesis assessment

| Hypothesis | Assessment | Evidence |
|---|---|---|
| Selection returns the same record twice | **Ruled out as primary cause** | Fisher–Yates swaps a copy of `QUESTIONS`; `slice` takes unique positions; IDs 1–1500 are unique. Repeated samples map to multiple distinct candidate IDs sharing a fingerprint. |
| Insufficient effective pool / duplicate records | **Confirmed** | Only 699 distinct prompts and 940 fingerprints; live and local rates match this distribution. |
| Client cache or React session state | **Ruled out for within-round repeats** | State is initialized on mount and replaced by `makeRound()`; no `localStorage`, `sessionStorage`, API, or pagination path exists. |
| Pagination/import/build loaded the wrong subset | **Ruled out** | Both paths show 30 cards; live DOM fingerprints match the checked-out 1,500-record artifact; Pages build publishes `frontend/dist`. |
| Incorrect shuffle or fixed/incorrect seed | **Ruled out as primary cause** | Fisher–Yates is structurally correct; a fixed-seed runtime replay is repeatable. The seed/order changes which duplicates appear, not whether duplicate records exist. |

## Refresh/session behavior

There is no cross-round or cross-refresh uniqueness guarantee. The app stores no used-question set. In one live refresh pair, the two 30-question rounds shared 2 exact fingerprints and 3 prompts; a local refresh pair shared 0 exact fingerprints and 2 prompts. This is expected from independent sampling and is separate from the within-round duplicate symptom.

## Counterfactuals (controlled model, one variable at a time)

These are deterministic simulations of the current Fisher–Yates shape over the `f4c4a8c` bank (2,000 seeded rounds), not claims about a new product mode.

### Requested length, all 1,500 records

| Length | Prompt-repeat rounds | Fingerprint-repeat rounds |
|---:|---:|---:|
| 10 | 6.7% | 2.5% |
| 30 (current) | 49.5% | 22.9% |
| 60 | 94.2% | 65.1% |
| 100 | 100.0% | 94.8% |
| 300 | 100.0% | 100.0% |

### Pool/topic mix, length 30

| Pool | Records | Prompt-repeat rounds | Fingerprint-repeat rounds |
|---|---:|---:|---:|
| Accepted IDs 1201–1500 only | 300 | 0.0% | 0.0% |
| Legacy IDs 1–1200 only | 1,200 | 66.5% | 33.0% |
| Topics 1–15 only | 750 | 64.8% | 31.6% |
| Topics 16–40 only | 750 | 82.8% | 45.5% |
| All records (current) | 1,500 | 49.5% | 22.9% |

These controls deliberately separate pool membership from the randomizer. A clean unique pool has no visible collision at length 30; increasing length or selecting the legacy-heavy pool sharply increases collisions.

## Smallest authorized follow-up

Do not change the shuffle or add a seed workaround. First decide the product invariant:

1. If “no repeat” means no identical visible stem, enforce a normalized-prompt uniqueness policy in the runtime artifact or filter by prompt while constructing a round.
2. If it means no identical stem **and** options, dedupe the content fingerprint at generation/import time.
3. Preserve legacy records and audit artifacts for history, but do not publish repeated legacy records into the runtime pool. The smallest data-side fix is to build a unique runtime view before `questions.js` generation; the current 1,500 records reduce to 940 unique fingerprints, or 699 unique normalized prompts for the stricter visible-stem invariant.
4. Only add persistent used-question state if the requirement is uniqueness across refreshes; that is not the current app contract and would be a separate UX/product decision.

## Regression-test design

- Unit-test the round constructor with an injected deterministic RNG: assert unique numeric IDs within every round across many seeds and assert that a fixture containing duplicate content cannot produce duplicate runtime fingerprints when the chosen invariant is enabled.
- Add a pre-build bank validation that reports both exact fingerprint duplicates and normalized-prompt duplicates, with an explicit allowlist if variants are intentional. Test that IDs remain unique and that the 300 accepted records do not overlap the runtime set.
- Add an end-to-end local production-build test that clicks `Nueva ronda` repeatedly, extracts a stable question identifier/fingerprint, and asserts the selected invariant. The current DOM does not expose numeric IDs, so use a test-only data attribute or a pure exported round-builder test rather than inferring IDs from rendered text.
- Keep refresh behavior as a separate test: document that overlap across reloads is allowed, or add persistent history only if the product decision changes.

## Unresolved uncertainty

- This investigation proves exact/lexical duplicate stems and exact content fingerprints. It does not classify all concept-level semantic duplicates among the legacy records.
- Rendered cards do not expose their numeric IDs, so browser evidence maps repeated content to candidate ID sets; the no-same-ID conclusion comes from the static unique-ID inventory plus the shuffle/slice implementation. A follow-up instrumentation/test seam can make IDs directly observable.
- The measured percentages describe this published build and 500-round samples, not every historical deployment or user-specific browser session.
