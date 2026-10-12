#!/usr/bin/env python3
"""Write topic 1, lot 1 candidates and its resumable checkpoint.

This is deliberately a candidate-only lot: all records remain quarantined until
an independent answer/explanation reviewer resolves the semantic/concept checks.
No static export or runtime import is performed here.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from question_bank.checkpoints import append_checkpoint, file_sha256
from question_bank.validation import screen_duplicates, stable_id_for, validate_record
from seed_data import SEED_QUESTIONS

DATE = "2026-10-12"
REGISTER_PATH = ROOT / "docs/question-bank/source-register.json"
OBJECTIVE_PATH = ROOT / "docs/question-bank/objective-manifest.json"
SYLLABUS_PATH = ROOT / "temario.md"
LOT_PATH = ROOT / "docs/question-bank/lots/topic-01-lot-01.json"
CHECKPOINT_PATH = ROOT / "docs/question-bank/checkpoints/topic-01-lot-01.jsonl"

# The specifications are generation input, separate from verification/review.
SPECS = [
    {
        "objective": "t01-lo-001", "difficulty": "basic", "type": "concept",
        "question": "¿Cuál de estas enumeraciones describe correctamente la estructura básica de la Constitución Española de 1978?",
        "options": ["Título Preliminar, diez Títulos y disposiciones adicionales, transitorias, derogatorias y final", "Doce Títulos, sin disposiciones adicionales", "Un único Título dividido en capítulos", "Diez Títulos, sin Título Preliminar ni disposiciones"], "correct": "A",
        "explanation": "La estructura constitucional comprende un Título Preliminar, los Títulos I a X y disposiciones adicionales, transitorias, derogatorias y final.", "citation": "Estructura de la Constitución Española de 1978"
    },
    {
        "objective": "t01-lo-002", "difficulty": "basic", "type": "legal_provision",
        "question": "Según el artículo 1.3 de la Constitución Española, ¿cuál es la forma política del Estado español?",
        "options": ["República federal", "Monarquía parlamentaria", "Monarquía absoluta", "República presidencialista"], "correct": "B",
        "explanation": "El artículo 1.3 establece literalmente que la forma política del Estado español es la Monarquía parlamentaria.", "citation": "Artículo 1.3"
    },
    {
        "objective": "t01-lo-003", "difficulty": "basic", "type": "concept",
        "question": "¿Qué combinación recoge los principios del artículo 2 de la Constitución Española?",
        "options": ["Unidad de la Nación, autonomía y solidaridad", "Soberanía de las provincias y subsidiariedad", "Confederación territorial y neutralidad", "Centralización, jerarquía y uniformidad"], "correct": "A",
        "explanation": "El artículo 2 se fundamenta en la indisoluble unidad de la Nación española y reconoce y garantiza la autonomía y la solidaridad entre sus partes.", "citation": "Artículo 2"
    },
    {
        "objective": "t01-lo-004", "difficulty": "basic", "type": "legal_provision",
        "question": "Conforme al artículo 3.1 de la Constitución, ¿qué afirmación es correcta sobre el castellano?",
        "options": ["Es la lengua oficial del Estado y todos tienen el deber de conocerla y el derecho a usarla", "Solo es oficial en la Administración General del Estado", "Su conocimiento es voluntario y no existe derecho de uso", "Solo puede utilizarse en las relaciones privadas"], "correct": "A",
        "explanation": "El artículo 3.1 declara el castellano lengua española oficial del Estado y establece el deber de conocerla y el derecho a usarla.", "citation": "Artículo 3.1"
    },
    {
        "objective": "t01-lo-005", "difficulty": "intermediate", "type": "comparison",
        "question": "¿Cuál de los siguientes principios aparece expresamente en el artículo 9.3 de la Constitución Española?",
        "options": ["Legalidad y seguridad jurídica", "Censura previa de las publicaciones", "Mandato imperativo de los parlamentarios", "Irretroactividad de toda norma favorable"], "correct": "A",
        "explanation": "El artículo 9.3 garantiza, entre otros, los principios de legalidad, jerarquía normativa, publicidad de las normas, irretroactividad de disposiciones sancionadoras no favorables o restrictivas, seguridad jurídica, responsabilidad e interdicción de la arbitrariedad.", "citation": "Artículo 9.3"
    },
    {
        "objective": "t01-lo-006", "difficulty": "intermediate", "type": "concept",
        "question": "¿Qué constituye, según el artículo 10.1, el fundamento del orden político y de la paz social?",
        "options": ["La dignidad de la persona y el libre desarrollo de la personalidad", "La potestad reglamentaria del Gobierno", "La autonomía financiera provincial", "La costumbre administrativa"], "correct": "A",
        "explanation": "El artículo 10.1 sitúa la dignidad de la persona, los derechos inviolables inherentes, el libre desarrollo de la personalidad y el respeto a la ley y a los derechos ajenos como fundamento del orden político y la paz social.", "citation": "Artículo 10.1"
    },
    {
        "objective": "t01-lo-007", "difficulty": "intermediate", "type": "scenario",
        "question": "Una norma establece un trato desfavorable por razón de nacimiento. ¿Qué parámetro constitucional resulta directamente aplicable?",
        "options": ["La igualdad ante la ley y la prohibición de discriminación del artículo 14", "La inviolabilidad del domicilio del artículo 18", "La libertad de empresa del artículo 38", "El derecho de petición del artículo 29"], "correct": "A",
        "explanation": "El artículo 14 proclama la igualdad ante la ley y prohíbe la discriminación, entre otros motivos, por razón de nacimiento, raza, sexo, religión, opinión o cualquier otra condición o circunstancia personal o social.", "citation": "Artículo 14"
    },
    {
        "objective": "t01-lo-008", "difficulty": "intermediate", "type": "legal_provision",
        "question": "¿Qué protege expresamente el artículo 15 de la Constitución Española?",
        "options": ["La vida y la integridad física y moral", "Solo la propiedad privada", "La libertad de empresa frente a toda regulación", "La autonomía universitaria exclusivamente"], "correct": "A",
        "explanation": "El artículo 15 reconoce el derecho a la vida y a la integridad física y moral y prohíbe la tortura y las penas o tratos inhumanos o degradantes.", "citation": "Artículo 15"
    },
    {
        "objective": "t01-lo-009", "difficulty": "intermediate", "type": "legal_provision",
        "question": "Según el artículo 16.2, ¿qué puede exigirse a una persona sobre su religión o creencias?",
        "options": ["Nada: nadie puede ser obligado a declarar sobre su religión o creencias", "Una declaración anual ante el Congreso", "Una declaración siempre que solicite una subvención", "Una declaración previa para ejercer cualquier derecho"], "correct": "A",
        "explanation": "El artículo 16.2 dispone que nadie podrá ser obligado a declarar sobre su ideología, religión o creencias.", "citation": "Artículo 16.2"
    },
    {
        "objective": "t01-lo-010", "difficulty": "intermediate", "type": "legal_provision",
        "question": "¿Cuál es el límite máximo ordinario de la detención preventiva previsto en el artículo 17.2?",
        "options": ["24 horas en todo caso", "72 horas, tras las cuales debe producirse la puesta en libertad o a disposición judicial", "15 días sin control judicial", "Un mes prorrogable por la policía"], "correct": "B",
        "explanation": "El artículo 17.2 establece que la detención preventiva no puede durar más del tiempo estrictamente necesario y, en todo caso, debe finalizar en un máximo de 72 horas con libertad o puesta a disposición judicial.", "citation": "Artículo 17.2"
    },
    {
        "objective": "t01-lo-011", "difficulty": "intermediate", "type": "scenario",
        "question": "La entrada en un domicilio sin consentimiento del titular exige, como regla constitucional, una resolución judicial o que exista flagrante delito. ¿Qué derecho fundamenta esta regla?",
        "options": ["La inviolabilidad del domicilio del artículo 18.2", "El derecho de reunión del artículo 21", "El derecho de petición del artículo 29", "La libertad de circulación del artículo 19"], "correct": "A",
        "explanation": "El artículo 18.2 declara inviolable el domicilio y solo permite la entrada o registro con consentimiento del titular, resolución judicial o en caso de flagrante delito.", "citation": "Artículo 18.2"
    },
    {
        "objective": "t01-lo-012", "difficulty": "intermediate", "type": "comparison",
        "question": "¿Qué límite establece el artículo 20.2 respecto del ejercicio de las libertades de expresión e información?",
        "options": ["No pueden restringirse mediante ningún procedimiento judicial", "No pueden someterse a ningún tipo de censura previa", "Solo pueden ejercerse con autorización administrativa", "Únicamente protegen comunicaciones oficiales"], "correct": "B",
        "explanation": "El artículo 20.2 dispone que el ejercicio de estos derechos no puede restringirse mediante ningún tipo de censura previa.", "citation": "Artículo 20.2"
    },
    {
        "objective": "t01-lo-013", "difficulty": "intermediate", "type": "scenario",
        "question": "Para una manifestación en un lugar de tránsito público, ¿qué exige el artículo 21.2 como regla general?",
        "options": ["Autorización previa del Gobierno", "Comunicación previa a la autoridad, sin autorización previa", "Autorización judicial en todos los casos", "Ninguna comunicación ni requisito"], "correct": "B",
        "explanation": "El artículo 21.2 exige comunicación previa para reuniones en lugares de tránsito público y manifestaciones; no establece un régimen de autorización previa.", "citation": "Artículo 21.2"
    },
    {
        "objective": "t01-lo-014", "difficulty": "intermediate", "type": "scenario",
        "question": "Una convocatoria para acceder a una función pública debe respetar, según el artículo 23.2, el derecho de la ciudadanía a acceder en condiciones de:",
        "options": ["Igualdad, con los requisitos que señalen las leyes", "Antigüedad sindical exclusivamente", "Designación discrecional sin requisitos legales", "Residencia en cualquier municipio concreto"], "correct": "A",
        "explanation": "El artículo 23.2 reconoce el derecho a acceder en condiciones de igualdad a las funciones y cargos públicos, con los requisitos que señalen las leyes.", "citation": "Artículo 23.2"
    },
    {
        "objective": "t01-lo-015", "difficulty": "advanced", "type": "scenario",
        "question": "En un proceso judicial, ¿qué garantía del artículo 24.2 protege a la persona frente a la obligación de declarar contra sí misma?",
        "options": ["El derecho a no declarar contra sí mismo y a no confesarse culpable", "El derecho a elegir siempre el órgano judicial", "La inmunidad parlamentaria", "La potestad de dictar reglamentos"], "correct": "A",
        "explanation": "El artículo 24.2 reconoce, entre las garantías del proceso, el derecho a no declarar contra sí mismo y a no confesarse culpable.", "citation": "Artículo 24.2"
    },
    {
        "objective": "t01-lo-016", "difficulty": "advanced", "type": "concept",
        "question": "¿Qué combinación recoge el artículo 27.1 de la Constitución Española?",
        "options": ["Derecho a la educación y libertad de enseñanza", "Derecho a la educación y prohibición de toda enseñanza privada", "Libertad de enseñanza sin derecho a la educación", "Solo derecho de acceso a la universidad"], "correct": "A",
        "explanation": "El artículo 27.1 reconoce el derecho de todos a la educación y la libertad de enseñanza.", "citation": "Artículo 27.1"
    },
    {
        "objective": "t01-lo-017", "difficulty": "advanced", "type": "scenario",
        "question": "Respecto del derecho de huelga, ¿qué prevé el artículo 28.2?",
        "options": ["Lo reconoce para la defensa de los intereses de los trabajadores y permite regular por ley el mantenimiento de servicios esenciales", "Lo prohíbe para todo el sector público", "Lo somete siempre a autorización judicial individual", "Lo reconoce solo para funcionarios electos"], "correct": "A",
        "explanation": "El artículo 28.2 reconoce el derecho a la huelga para la defensa de los intereses de los trabajadores y ordena que la ley regule las garantías para asegurar el mantenimiento de los servicios esenciales de la comunidad.", "citation": "Artículo 28.2"
    },
    {
        "objective": "t01-lo-018", "difficulty": "advanced", "type": "scenario",
        "question": "Un sistema tributario que ignore la capacidad económica y no respete la igualdad contradice directamente el artículo:",
        "options": ["31.1", "18.3", "21.1", "66.3"], "correct": "A",
        "explanation": "El artículo 31.1 exige que todos contribuyan al sostenimiento de los gastos públicos conforme a su capacidad económica, mediante un sistema tributario justo inspirado en igualdad y progresividad.", "citation": "Artículo 31.1"
    },
    {
        "objective": "t01-lo-019", "difficulty": "advanced", "type": "concept",
        "question": "¿Qué órganos integran las Cortes Generales según el artículo 66.1?",
        "options": ["Congreso de los Diputados y Senado", "Gobierno y Consejo de Estado", "Tribunal Constitucional y Tribunal Supremo", "Congreso y Consejo General del Poder Judicial"], "correct": "A",
        "explanation": "El artículo 66.1 establece que las Cortes Generales representan al pueblo español y están formadas por el Congreso de los Diputados y el Senado.", "citation": "Artículo 66.1"
    },
    {
        "objective": "t01-lo-020", "difficulty": "advanced", "type": "legal_provision",
        "question": "¿Qué mayoría exige el artículo 81.2 para aprobar, modificar o derogar una ley orgánica?",
        "options": ["Mayoría simple del Senado", "Mayoría absoluta del Congreso en una votación final sobre el conjunto del proyecto", "Unanimidad de las Cortes Generales", "Mayoría de tres quintos de ambas Cámaras en dos votaciones"], "correct": "B",
        "explanation": "El artículo 81.2 exige mayoría absoluta del Congreso, en una votación final sobre el conjunto del proyecto, para aprobar, modificar o derogar leyes orgánicas.", "citation": "Artículo 81.2"
    }
]


def source_record(register: dict) -> dict:
    return next(source for source in register["source_records"] if source["source_id"] == "BOE-CE-1978")


def make_record(spec: dict, source: dict, numeric_id: int) -> dict:
    record = {
        "id": numeric_id,
        "stable_id": "",
        "topic_num": 1,
        "question": spec["question"],
        "option_a": spec["options"][0],
        "option_b": spec["options"][1],
        "option_c": spec["options"][2],
        "option_d": spec["options"][3],
        "correct": spec["correct"],
        "explanation": spec["explanation"],
        "learning_objective_id": spec["objective"],
        "difficulty": spec["difficulty"],
        "question_type": spec["type"],
        "sources": [{
            "source_id": source["source_id"],
            "title": source["title"],
            "authority": source["authority"],
            "tier": source.get("tier", "official_primary"),
            "url": source["url"],
            "citation": spec["citation"],
            "version_or_as_of": source["version_or_as_of"],
            "retrieved_at": source["retrieved_at"],
            "verified_at": source["verified_at"],
        }],
        "verification": {
            "answer": {"status": "uncertain", "reviewer": "awaiting-independent-review", "checked_at": DATE, "basis": "Candidate answer requires an independent second pass against the cited BOE article."},
            "explanation": {"status": "uncertain", "reviewer": "awaiting-independent-review", "checked_at": DATE, "basis": "Candidate explanation requires an independent second pass against the cited BOE article."},
            "reviewed_at": DATE,
            "reviewer_decision": "quarantined",
        },
        "deduplication": {},
        "status": "quarantined",
    }
    record["stable_id"] = stable_id_for(record)
    return record


def main() -> int:
    register = json.loads(REGISTER_PATH.read_text(encoding="utf-8"))
    source = source_record(register)
    if source["status"] != "verified":
        raise RuntimeError("BOE-CE-1978 is not verified; refusing to write a lot")
    legacy = [question for question in SEED_QUESTIONS if question["topic_num"] == 1]
    records = []
    duplicate_counts = {name: 0 for name in ("exact", "lexical", "near_lexical")}
    for index, spec in enumerate(SPECS, start=1201):
        record = make_record(spec, source, index)
        screen = screen_duplicates(record, legacy + records, checked_at=DATE)
        record["deduplication"] = screen.as_dict()
        for name in duplicate_counts:
            duplicate_counts[name] += screen.as_dict()[name]["status"] == "duplicate"
        errors = validate_record(record)
        if errors:
            raise RuntimeError(f"record {record['stable_id']} failed validation: {errors}")
        records.append(record)

    payload = {
        "lot_version": "1.0",
        "state": "candidates_written",
        "topic_num": 1,
        "lot_num": 1,
        "revision": 2,
        "generated_at": DATE,
        "source_register_sha256": file_sha256(REGISTER_PATH),
        "objective_manifest_sha256": file_sha256(OBJECTIVE_PATH),
        "syllabus_sha256": file_sha256(SYLLABUS_PATH),
        "source_verification": {"source_ids": [source["source_id"]], "verified_at": source["verified_at"]},
        "counts": {"candidates": len(records), "accepted": 0, "rejected": 0, "quarantined": len(records), "deterministic_duplicates": duplicate_counts},
        "questions": records,
    }
    LOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    LOT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    stable_ids = [record["stable_id"] for record in records]
    checkpoint = {
        "schema_version": "1.0",
        "syllabus_hash": payload["syllabus_sha256"],
        "source_register_hash": payload["source_register_sha256"],
        "topic_num": 1,
        "lot_num": 1,
        "revision": 2,
        "stage": "candidates_written",
        "objective_ids": [record["learning_objective_id"] for record in records],
        "stable_ids": stable_ids,
        "counts": payload["counts"],
        "input_hash": hashlib.sha256((payload["source_register_sha256"] + payload["objective_manifest_sha256"]).encode()).hexdigest(),
        "output_hash": file_sha256(LOT_PATH),
        "last_import": {"status": "not_started", "transaction": None},
    }
    appended = append_checkpoint(CHECKPOINT_PATH, checkpoint)
    print(f"wrote {len(records)} quarantined candidates; checkpoint {'appended' if appended else 'already present'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
