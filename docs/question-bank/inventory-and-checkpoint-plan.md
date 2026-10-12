# Diputest question-bank milestone 0: inventory, source plan, schema, and checkpoints

**Status:** planning gate only. No new questions have been generated or promoted.
**Scope:** the existing Diputest application in this repository; no second application or runtime storage is proposed.
**Verified at:** 2026-10-12T10:57:49Z (UTC), unless a row says otherwise.

## 1. Baseline and source evidence

The official call supplied for this work was fetched without credentials and preserved as:

- URL: <https://aplicaciones.dipualba.es/EmpleoPublico/docs/2691.PDF>
- Local snapshot: `docs/question-bank/official-call-2691.pdf`
- HTTP content type: `application/pdf`
- HTTP size: `311233` bytes
- HTTP `Last-Modified`: `Fri, 10 Apr 2026 07:10:35 GMT`
- HTTP `ETag`: `"9669020b9c8dc1:0"`
- SHA-256: `bdb990f9eec61c98ef95b52aad5ee5b38868e5ad29acec26c8658fea72fceb8f`
- Retrieval date: `2026-10-12`

`temario.md` is the repository's syllabus transcription. `temario.py::parse_temario` parses **40** topics (numbers 1--40), and the runtime question source has one topic number for each of those 40 numbers. The PDF snapshot and `temario.md` must still be compared topic-by-topic with a PDF text/signature-capable tool before any item is generated; this milestone deliberately does not claim that comparison is complete.

### Existing data inventory

| Area | Current implementation | Baseline finding | Risk / implication |
|---|---|---|---|
| Deployed app | `frontend/src/App.jsx` + Vite/React | Static GitHub Pages app; imports `QUESTIONS` and shows 30 random items | This is the active product path, not Flask/SQLite |
| Canonical authoring input | `seed_data.py` | `SEED_QUESTIONS` is built from a base list plus generated extra/direct filler; runtime total is 1,200, exactly 30/topic | Dynamic filler makes provenance and stable identity difficult; do not treat the filler as validated |
| Generated frontend data | `frontend/src/questions.js` | 1,200 records, numeric IDs 1--1,200, 30/topic | Generated artifact must remain compatible with the current field names |
| Legacy backend | `app.py`, `db.py`, `generator.py`, `templates/` | Flask API and SQLite table exist, but README says production does not use them | Preserve as legacy compatibility; do not introduce a parallel question service |
| SQLite schema | `db.py::init_db` | `questions` has topic/group, prompt, four options, answer, explanation, created timestamp; only topic index | No source, objective, difficulty, type, review state, stable key, or uniqueness constraint |
| Backend import/generation | `app.py::api_generate*`, `generator.py`, `db.py::insert_questions` | Generator slices seed data and inserts blindly; repeated calls can duplicate rows | Never use current generation endpoints for a bulk import without an idempotency layer |
| Static export | Procedure in `guide_dev.md` | Imports Python source and rewrites `frontend/src/questions.js` with sequential IDs | Keep this native path, but make identity/content validation and atomic export explicit before bulk lots |
| Frontend contract | `App.jsx::optionText`, `question.id`, `question.correct`, `question.explanation` | Uses `topic_num`, `question`, `option_a..d`, `correct`, `explanation`; ignores additional properties | Add metadata without removing or renaming existing fields; preserve numeric `id` for UI compatibility |
| Tests | Repository-wide test search | No Python test suite, frontend test script, Playwright setup, or bank validator is present | Validation gates must be added before importing lots |
| Existing duplicate state | Runtime `seed_data.SEED_QUESTIONS` and generated JS | 1,200 total; only 399 normalized prompt texts; 801 repeated prompt occurrences; 480 exact full-record duplicate groups with 560 extra occurrences | Existing records are a legacy baseline, not 1,200 validated learning objectives |
| Existing field validity | Runtime `seed_data.SEED_QUESTIONS` | All 1,200 have four non-empty distinct options, a valid A--D answer, and a non-empty explanation | Structural validity is not evidence validity or conceptual distinctness |

The duplicate counts above use Unicode accent folding, lower-casing, punctuation removal, and whitespace collapse for prompt comparison. They are screening counts, not a semantic-review verdict.

## 2. Exact 40-topic boundary

The source of truth for the topic boundary remains `temario.md`, with the official call snapshot above as the legal source to re-check. The groups and scopes are:

| # | Group | Scope as transcribed in `temario.md` | Primary authority to verify before generation |
|---:|---|---|---|
| 1 | General | Constitución de 1978: estructura, Título Preliminar, Título I y Título III | BOE consolidated Constitution |
| 2 | General | Constitución: Títulos IV, V y VIII | BOE consolidated Constitution |
| 3 | General | Ley 7/1985: municipio (Título II, Cap. II) y provincia (Título III, Cap. I) | BOE consolidated LRBRL |
| 4 | General | RDL 781/1986, Títulos I y III; RD 2568/1986, Título II, Cap. II | BOE consolidated texts |
| 5 | General | Ley 39/2015: disposiciones generales e interesados, Título I, Caps. I--II | BOE consolidated LPACAP |
| 6 | General | Ley 39/2015: actividad administrativa, actos, requisitos, eficacia, nulidad y anulabilidad | BOE consolidated LPACAP |
| 7 | General | Ley 31/1995: definiciones, protección, principios preventivos y obligaciones de trabajadores | BOE consolidated LPRL |
| 8 | General | LO 3/2007; Ley 12/2010 CLM; Ley 4/2018 CLM | BOE and DOCM consolidated texts |
| 9 | Seguridad | Firma electrónica, métodos y AutoFirma del MINHAP | EUR-Lex eIDAS and official AutoFirma/PAe docs |
| 10 | Seguridad | Cifrado, PKI, certificados, SSL/TLS y PGP | IETF RFCs and official security standards |
| 11 | Seguridad | Esquema Nacional de Seguridad | BOE RD 311/2022 and its current guidance |
| 12 | Seguridad | Protección de datos | EUR-Lex RGPD and BOE LOPDGDD |
| 13 | Base de datos | PostgreSQL: arquitectura de servidor | PostgreSQL official docs, pinned major version |
| 14 | Base de datos | PostgreSQL: jerarquía de objetos y funciones | PostgreSQL official docs, pinned major version |
| 15 | Base de datos | PostgreSQL: transacciones | PostgreSQL official docs, pinned major version |
| 16 | Base de datos | PostgreSQL: herramientas cliente e importación/exportación | PostgreSQL official docs, pinned major version |
| 17 | Base de datos | PostgreSQL: optimización SQL y del servidor | PostgreSQL official docs, pinned major version |
| 18 | .NET Core/MVC | Fundamentos de programación C# | Microsoft Learn C# language reference, pinned .NET version |
| 19 | .NET Core/MVC | Sitios web MVC y Bootstrap | Microsoft ASP.NET Core docs and Bootstrap docs, pinned versions |
| 20 | .NET Core/MVC | Datos con Entity Framework Core | Microsoft EF Core docs, pinned major version |
| 21 | .NET Core/MVC | Manipulación y consultas LINQ | Microsoft .NET LINQ docs, pinned .NET version |
| 22 | .NET Core/MVC | Model binding, validación, modificar datos con EF y asincronía | Microsoft ASP.NET Core/EF Core docs |
| 23 | .NET Core/MVC | Autenticación, autorización y filtros | Microsoft ASP.NET Core security/filter docs |
| 24 | .NET Core/MVC | Creación/consumo de servicios Web y Web API | Microsoft ASP.NET Core Web API docs |
| 25 | .NET Core/MVC | Estándar de exposición de datos OData | OASIS OData standard and Microsoft OData docs |
| 26 | Blazor | Modelos de alojamiento y solución Blazor | Microsoft Learn Blazor docs, pinned .NET version |
| 27 | Blazor | Componentes básicos, binding, parámetros y valores en cascada | Microsoft Learn Blazor component docs |
| 28 | Blazor | Componentes avanzados y estilos | Microsoft Learn Blazor component/CSS docs |
| 29 | Blazor | Formularios y validación | Microsoft Learn Blazor forms/validation docs |
| 30 | Blazor | Inyección de dependencias y configuración | Microsoft Learn .NET/Blazor DI/configuration docs |
| 31 | Blazor | Gestión de estado | Microsoft Learn Blazor state-management docs |
| 32 | Blazor | Navegación y enrutado | Microsoft Learn Blazor navigation/routing docs |
| 33 | Git | Teoría, instalación/configuración y trabajo local | git-scm official documentation / Pro Git |
| 34 | Git | Ramas, rebase, merge frente a rebase y stash | git-scm official documentation / Pro Git |
| 35 | Git | Remoto, flujos de trabajo y estrategias de ramas | git-scm official documentation / Pro Git |
| 36 | Administración electrónica | SedipuAlba: definiciones, conceptos y sede electrónica | SedipuAlba/Diputación de Albacete official docs |
| 37 | Administración electrónica | SedipuAlba: módulos para tramitadores (Segex, Sefycu, Segra, Seres, Secoin, Seface, Seca y AdminSedeElectrónica) | SedipuAlba/Diputación de Albacete official docs |
| 38 | Administración electrónica | Interoperabilidad estatal, SCSP y Red SARA | PAe/administracionelectronica.gob.es official docs |
| 39 | Administración electrónica | Cl@ve, DNIe, FIRe, Carpeta ciudadana, SIR, PID y public-sector platforms | Each service's official documentation and PAe |
| 40 | Administración electrónica | Accesibilidad Web | W3C WCAG, ETSI EN 301 549, EUR-Lex and BOE transpositions |

No item may be assigned to a topic outside this table. A source register must pin a URL, title, issuing authority, version or effective date, retrieval date, verification date, and the exact citation/article/section used.

## 3. Source register and research gate

The official call is the only source fetched in this milestone. Before generation, research must create a source-register entry for every authority used. The minimum primary-source set is:

- Legal topics 1--8, 11--12: consolidated BOE records and official DOCM records where applicable. Record the law version/effective date and article/section; do not rely on an unofficial summary.
- Topic 9: Regulation (EU) 910/2014 (EUR-Lex) plus the official AutoFirma/PAe documentation.
- Topic 10: IETF RFC 5280, RFC 8446, and the current OpenPGP RFC, plus any explicitly used official standard.
- Topics 13--17: PostgreSQL documentation with a pinned major release and retrieval date; no unversioned answer is accepted for version-sensitive behavior.
- Topics 18--32: Microsoft Learn and the standards/vendor documentation for the exact .NET, ASP.NET Core, EF Core, Bootstrap, OData, and Blazor versions used.
- Topics 33--35: git-scm documentation/Pro Git and versioned command documentation.
- Topics 36--39: official SedipuAlba/Diputación and Spanish public-administration service documentation; if a module or service has no public authoritative description, quarantine it rather than infer behavior.
- Topic 40: W3C WCAG, ETSI EN 301 549, the EU directive, and the Spanish BOE transposition as applicable.

Initial authoritative entry points (the final register must pin the exact document/page/article used) are:

- BOE: <https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229>, <https://www.boe.es/buscar/act.php?id=BOE-A-1985-5392>, <https://www.boe.es/buscar/act.php?id=BOE-A-2015-10565>, <https://www.boe.es/buscar/act.php?id=BOE-A-1995-24292>, <https://www.boe.es/buscar/act.php?id=BOE-A-2007-6115>, <https://www.boe.es/buscar/act.php?id=BOE-A-2022-7191>, and the BOE search for the remaining cited texts.
- DOCM: <https://docm.jccm.es/portaldocm/> for Laws 12/2010 and 4/2018 of Castilla-La Mancha.
- EUR-Lex: <https://eur-lex.europa.eu/eli/reg/2014/910/oj>, <https://eur-lex.europa.eu/eli/reg/2016/679/oj>, and <https://eur-lex.europa.eu/eli/dir/2016/2102/oj>.
- IETF: <https://www.rfc-editor.org/rfc/rfc5280>, <https://www.rfc-editor.org/rfc/rfc8446>, and the current OpenPGP RFC at <https://www.rfc-editor.org/>.
- PostgreSQL: <https://www.postgresql.org/docs/current/>; record the resolved major-version URL rather than leaving `current` in an item citation.
- Microsoft/.NET, Bootstrap, OData, and Blazor: <https://learn.microsoft.com/dotnet/>, <https://getbootstrap.com/docs/>, and <https://www.oasis-open.org/standards/odata/> with versioned pages recorded per item.
- Git: <https://git-scm.com/docs> and <https://git-scm.com/book/en/v2>.
- SedipuAlba and public administration: <https://sedipualba.es/> and <https://administracionelectronica.gob.es/>; absence of a public module specification is a quarantine condition.
- Accessibility: <https://www.w3.org/TR/WCAG21/> and <https://www.etsi.org/standards/harmonised-standards/accessibility>.

The source register should record `verified_at` separately from `retrieved_at`: a downloaded page is not proof that a citation was checked. Any source that cannot be retrieved or whose version/effective date cannot be established is a blocker for the affected objectives, not a reason to invent questions.

## 4. Schema decision: extend the native static record, do not add a storage system

The active product path is the static React application. The safe decision is:

1. Keep `seed_data.py` as the authoring input and `frontend/src/questions.js` as its generated, shipped artifact, using the existing export procedure as the only application data path.
2. Preserve all existing fields and numeric `id` behavior required by `App.jsx` and the legacy API. New metadata is additive, so the current UI can continue to render records while later UI work can expose evidence and classification.
3. Add an immutable `stable_id` for idempotence; it is derived from topic, learning-objective ID, and a canonical content digest, not from array order. Numeric `id` remains a compatibility/export field.
4. Add `learning_objective_id`, `difficulty`, `question_type`, `sources[]`, `verification`, `deduplication`, and `status` to the record. Their contract is machine-readable in `docs/question-bank/question-record.schema.json`.
5. Existing records are retained but marked `quarantined`/legacy-unverified until they receive citations, objective mapping, independent answer verification, and duplicate screening. They must not be counted toward the validated target merely because they pass the old shape checks.
6. The legacy SQLite table remains available for old callers. If that API must be populated, use an additive migration and a stable-key uniqueness constraint; never delete the existing rows or use `delete_questions_for_topic` as a migration mechanism. SQLite is not the canonical store for the deployed app.

### Required record contract

A validated record has exactly four non-empty, distinct options, one `correct` value in `A`--`D`, a source-backed explanation, one or more learning-objective and source references, a difficulty/type classification, an immutable stable key, and independent verification. The verification object distinguishes answer verification from explanation/source verification and records safe code/SQL execution when applicable. A record with unresolved source, answer, ambiguity, or duplicate status is quarantined.

### Five-level duplicate policy

Every candidate is screened against accepted and quarantined records at five levels:

1. exact canonical record (all content and answer fields),
2. normalized/lexical prompt and option text,
3. near-duplicate lexical similarity (token/character similarity),
4. semantic similarity of the tested proposition, and
5. concept/objective collision (same fact, operation, or learning objective even when phrased differently).

Levels 1--3 are deterministic and must emit reproducible keys/scores. Levels 4--5 require a reviewer decision and a retained rationale. A duplicate or uncertain result is rejected or quarantined, never silently counted.

## 5. Checkpoint and resumability design

Generation, verification, and review are logically separate stages. They are sequential by topic and never run overlapping generators.

### Unit of work

- One topic is processed at a time.
- Each topic has ten nominal lots of up to 20 accepted records, with the actual accepted count allowed to remain below 200 when evidence cannot support more.
- Each lot has a research/source snapshot, a knowledge map, distinct learning-objective IDs, candidates, validation results, reviewer decisions, and an import digest.
- The 200/topic figure is a target, not permission to pad with invented, stale, ambiguous, or concept-duplicate questions.

### State machine

`research_ready -> objectives_ready -> candidates_written -> structural_validated -> duplicates_screened -> independently_verified -> reviewed -> imported`.

Any unresolved evidence, answer disagreement, unsafe code/SQL, or duplicate uncertainty transitions to `quarantined` or `rejected` with a reason and reviewer identity. No later state may hide a rejection.

### Checkpoint manifest

Each checkpoint records at least:

- schema version, syllabus hash, source-register hash, topic number, lot number, and stable IDs;
- objective IDs and coverage counts by subtopic, difficulty, and question type;
- candidates, accepted, rejected, quarantined, and duplicate counts;
- exact/lexical/near-duplicate keys and semantic/concept review decisions;
- source IDs, versions/effective dates, citations, retrieval and verification dates;
- independent answer/explanation review results and code/SQL execution result where relevant;
- input/output content hashes and the last successful import transaction.

Checkpoints are append-only and resumable. A rerun must recompute the same stable IDs, skip already imported IDs, and refuse a changed source/syllabus hash unless the checkpoint is explicitly superseded. Export to `frontend/src/questions.js` is atomic: validate the complete accepted set first, write a temporary file, then replace the generated artifact. The existing data snapshot remains recoverable through Git and is never overwritten by an unvalidated lot.

### Import and rollback safety

The importer must be a dry-run first, report per-topic deltas and collisions, and then use an idempotent transaction keyed by `stable_id`. It must preserve legacy records and reject malformed records before touching the generated artifact. A failed lot leaves its checkpoint and audit trail intact; retrying the same lot cannot double its records. The frontend export must be regenerated only from accepted records, while quarantined/rejected records stay in the audit stream and never ship as practice questions.

## 6. Validation and acceptance gates before any bulk lot

Before the first generation lot, add tests/tools for:

- JSON/schema validation and required citation/version/date fields;
- exactly four unique options and exactly one correct answer;
- topic numbers 1--40 and objective coverage;
- five-level duplicate screening and rejection-audit persistence;
- independent answer verification, including an explicit disagreement/quarantine path;
- safe, bounded code/SQL execution for items marked executable, with version and output captured;
- idempotent import/export and preservation of the 1,200-record legacy snapshot;
- static build (`npm run build`) and lint (`npm run lint`);
- Flask legacy API compatibility if the old backend remains supported;
- browser flow: load a round, answer an item, reveal the explanation, start a new round, and ensure duplicate stable IDs are not emitted.

The quality report must show per-topic accepted counts, objective coverage, difficulty/type distributions, source/version coverage, duplicate/rejection/quarantine counts, verification completion, and all test results. It must explicitly report a real validated count below 8,000 if any topic cannot support 200 evidence-backed distinct records.

### Milestone checks run

- `python3 -m json.tool docs/question-bank/question-record.schema.json`: passed.
- `cd frontend && npm run lint`: passed.
- `cd frontend && npm run build`: passed; Vite emitted only its existing large-chunk warning.
- `npm ci` reported 8 dependency audit findings (1 low, 1 moderate, 6 high); this is recorded as a baseline follow-up and is not silently treated as question-bank validation.

## 7. Immediate next gate

Do not generate or import thousands of questions from this milestone. The follow-up comparison, source register, and pre-generation validator/checkpoint seam are recorded in `docs/question-bank/milestone-1-source-and-validation-report.md`, `docs/question-bank/syllabus-comparison.md`, `docs/question-bank/source-register.json`, and `question_bank/`. Topic 1, lot 1 remains gated until the open source/version and objective-map decisions in that report are resolved and its checkpoint is recorded.

The brief requires difficulty/type targets but does not state their numerical percentages in the repository or in the milestone evidence. Before generation, copy the authoritative percentages from the complete captain specification into the checkpoint manifest; do not infer or silently choose a distribution.
