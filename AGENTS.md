# Project agent memory

This file is the project's committed home for project-intrinsic agent knowledge: build, test, release, architecture, and sharp-edge notes that should travel with the code.

- Add durable project-specific notes here as they are discovered through real work.

## Maintaining this file

Keep this file for knowledge useful to almost every future agent session in this project.
Do not repeat what the codebase already shows; point to the authoritative file or command instead.
Prefer rewriting or pruning existing entries over appending new ones.
When updating this file, preserve this bar for all agents and keep entries concise.

## Durable architecture notes

- The deployed product path is the static React app: `seed_data.py` is the authoring input and `frontend/src/questions.js` is the generated artifact consumed by `frontend/src/App.jsx`; `app.py`, `db.py`, `generator.py`, and `templates/` are legacy Flask/SQLite paths. See `README.md` and `guide_dev.md`.
- Question-bank milestone constraints, source evidence, metadata schema, and resumable checkpoint design are recorded in `docs/question-bank/inventory-and-checkpoint-plan.md`; the machine-readable record contract is `docs/question-bank/question-record.schema.json`.
- Source boundary/completeness evidence is in `docs/question-bank/syllabus-comparison.md` and `docs/question-bank/source-register.json`; the captain-approved 200-per-topic objective-slot manifest is `docs/question-bank/objective-manifest.json`; the current candidate-only metrics/blockers are in `docs/question-bank/quality-report.md`; pre-generation validation and append-only lot checkpoints live in `question_bank/` with tests under `tests/test_question_bank_validation.py`.
