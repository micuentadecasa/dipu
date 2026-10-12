# Official-call syllabus comparison

**Status:** completed as a source-boundary gate; this does not authorize question generation.

**Compared on:** 2026-10-12 (UTC)

## Inputs

- Official call snapshot: [`official-call-2691.pdf`](./official-call-2691.pdf)
- Official call URL: <https://aplicaciones.dipualba.es/EmpleoPublico/docs/2691.PDF>
- Snapshot SHA-256: `bdb990f9eec61c98ef95b52aad5ee5b38868e5ad29acec26c8658fea72fceb8f`
- Repository syllabus: [`../../temario.md`](../../temario.md)

## Method

The local PDF was text-extracted with `pypdf` and compared with `temario.md` after NFC normalization, case folding, whitespace normalization, line-wrap removal, and dehyphenation. The comparison checked topic numbers 1--40 and the complete scope text, not just the topic count. The PDF's printed pages are 35--36 (PDF pages 11--12).

## Result

- The call contains exactly 40 syllabus topics numbered 1 through 40.
- `temario.md` contains exactly the same 40 topic numbers and no extras or omissions.
- All topic scopes match after normalization. Differences are presentation-only: PDF line wrapping, soft hyphens, capitalization in group headings, and spacing around punctuation.
- Topics 8, 37, and 39 span multiple PDF lines; their continuation lines were included in the comparison.
- The legal call snapshot is the authority for the boundary. `temario.md` is the repository transcription used by `temario.py` and must not be expanded during generation.

## Generation gate

Every candidate must carry one of `topic_num` 1--40 and an objective from the matching topic coverage plan. A source may support an item, but it may not add a new topic or silently broaden a topic beyond the scope recorded in the official call. Any apparent scope mismatch is quarantined for review rather than normalized into the question bank.
