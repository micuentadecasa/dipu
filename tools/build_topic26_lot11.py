#!/usr/bin/env python3
"""Generate the source-gated supplemental topic-26 render-mode lot 11.

This lot is intentionally outside the 200-objective target manifest: it records
an independently researched coverage gap without inflating target statistics.
Generation only writes quarantined candidates; review and import are separate
commands/stages.
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

DATE = "2026-10-15"
TOPIC = 26
LOT = 11
REVISION = 1
SOURCE_REGISTER = ROOT / "docs/question-bank/source-register.json"
OBJECTIVE_MANIFEST = ROOT / "docs/question-bank/objective-manifest.json"
SYLLABUS = ROOT / "temario.md"
RESEARCH_ARTIFACT = ROOT / "docs/question-bank/research/questions/topics-26-lot-11.json"
LOT_PATH = ROOT / "docs/question-bank/lots/topic-26-lot-11.json"
CHECKPOINT_PATH = ROOT / "docs/question-bank/checkpoints/topic-26-lot-11.jsonl"

RENDER_MODES_URL = "https://learn.microsoft.com/en-us/aspnet/core/blazor/components/render-modes?view=aspnetcore-10.0"

SPECS = [
    {
        "objective_id": "t26-lo-supp-001",
        "question": "¿Qué límite tienen los modos de renderizado descritos para Blazor?",
        "options": [
            "Se aplican a una Blazor Web App; una WebAssembly standalone solo renderiza en el cliente y no tiene concepto de render mode.",
            "Se aplican únicamente a aplicaciones MVC que devuelven vistas.",
            "Obligan a que toda aplicación WebAssembly mantenga un circuito SignalR.",
            "Solo controlan el formato de los archivos CSS publicados.",
        ],
        "correct": "A",
        "explanation": "La documentación limita los render modes a Blazor Web Apps; una aplicación Blazor WebAssembly standalone renderiza en el cliente y no usa el concepto de render mode.",
        "difficulty": "basic",
        "question_type": "concept",
        "citation": "Render modes — scope and standalone WebAssembly",
    },
    {
        "objective_id": "t26-lo-supp-002",
        "question": "En una Blazor Web App que no asigna otro modo, ¿qué comportamiento predeterminado recibe un componente?",
        "options": [
            "InteractiveServer",
            "Static",
            "InteractiveWebAssembly",
            "InteractiveAuto",
        ],
        "correct": "B",
        "explanation": "La tabla de render modes y las reglas de propagación de Microsoft Learn establecen Static como modo predeterminado.",
        "difficulty": "basic",
        "question_type": "concept",
        "citation": "Render-mode propagation — default render mode",
    },
    {
        "objective_id": "t26-lo-supp-003",
        "question": "¿Qué responsabilidad tiene AddInteractiveServerComponents en la configuración de una Blazor Web App?",
        "options": [
            "Añade los servicios necesarios para representar componentes Interactive Server.",
            "Publica el proyecto cliente WebAssembly como archivos estáticos.",
            "Desactiva el prerendering de todos los componentes.",
            "Convierte automáticamente todos los componentes en Static.",
        ],
        "correct": "A",
        "explanation": "La guía de habilitación separa la adición de servicios para Interactive Server de la configuración de los endpoints del modo.",
        "difficulty": "basic",
        "question_type": "procedure",
        "citation": "Enable support for interactive render modes — AddInteractiveServerComponents",
    },
    {
        "objective_id": "t26-lo-supp-004",
        "question": "¿Qué API configura el endpoint de renderizado Interactive Server después de registrar sus servicios?",
        "options": [
            "AddInteractiveWebAssemblyComponents",
            "UseStaticFiles",
            "AddInteractiveServerRenderMode",
            "MapFallbackToFile",
        ],
        "correct": "C",
        "explanation": "AddInteractiveServerRenderMode configura el modo de renderizado del endpoint; AddInteractiveServerComponents cubre el registro de servicios.",
        "difficulty": "basic",
        "question_type": "procedure",
        "citation": "Enable support for interactive render modes — AddInteractiveServerRenderMode",
    },
    {
        "objective_id": "t26-lo-supp-005",
        "question": "Para habilitar componentes Interactive WebAssembly en una Blazor Web App, ¿qué frontera de proyecto documenta Microsoft?",
        "options": [
            "Un proyecto de base de datos separado que aloje el circuito.",
            "Un proyecto cliente separado que configure el host WebAssembly y el runtime .NET del navegador.",
            "Una segunda aplicación MVC que sustituya a Components.",
            "Un servicio Windows que ejecute el runtime del navegador.",
        ],
        "correct": "B",
        "explanation": "La documentación requiere un proyecto cliente separado para el host WebAssembly y señala que los componentes deben compilarse desde ese proyecto para entrar en el paquete descargado.",
        "difficulty": "basic",
        "question_type": "concept",
        "citation": "Enable support for interactive render modes — client project",
    },
    {
        "objective_id": "t26-lo-supp-006",
        "question": "¿Qué diferencia documenta Microsoft entre la directiva @rendermode de una definición y el atributo @rendermode de una instancia?",
        "options": [
            "La definición requiere una instancia estática del modo; el atributo de instancia puede recibir cualquier instancia de modo.",
            "La definición solo funciona con CSS y el atributo solo con JavaScript.",
            "La definición se ejecuta en SQL y el atributo en el servidor HTTP.",
            "No hay diferencia semántica ni de ubicación entre ambos usos.",
        ],
        "correct": "A",
        "explanation": "En una definición de componente la directiva exige una instancia de render mode estática, mientras que el atributo aplicado a una instancia admite cualquier instancia de modo.",
        "difficulty": "intermediate",
        "question_type": "comparison",
        "citation": "Apply a render mode — component definition versus component instance",
    },
    {
        "objective_id": "t26-lo-supp-007",
        "question": "¿Qué restricción existe al intentar hacer interactivo el componente raíz App?",
        "options": [
            "App solo puede usar InteractiveWebAssembly.",
            "App debe estar dentro de una carpeta .Client.",
            "Hacer interactivo un componente raíz como App no está soportado.",
            "App requiere siempre un circuito por cada archivo CSS.",
        ],
        "correct": "C",
        "explanation": "La guía de aplicación a toda la aplicación indica que un componente raíz como App no puede hacerse interactivo directamente.",
        "difficulty": "intermediate",
        "question_type": "concept",
        "citation": "Apply a render mode to the entire app — root component restriction",
    },
    {
        "objective_id": "t26-lo-supp-008",
        "question": "¿Dónde se suele asignar el modo global cuando una Blazor Web App usa el componente Routes?",
        "options": [
            "En cada archivo de estilos aislados.",
            "En la llamada a la base de datos de la aplicación.",
            "En el proyecto de pruebas únicamente.",
            "En la instancia de Routes usada por App.razor, no directamente en App como raíz interactiva.",
        ],
        "correct": "D",
        "explanation": "El ejemplo oficial asigna el modo a Routes dentro de Components/App.razor; Router propaga después ese modo a las páginas que enruta.",
        "difficulty": "intermediate",
        "question_type": "procedure",
        "citation": "Apply a render mode to the entire app — Routes component",
    },
    {
        "objective_id": "t26-lo-supp-009",
        "question": "¿Qué efecto tiene Router cuando recibe el modo de renderizado aplicado al componente Routes?",
        "options": [
            "Propaga el modo a las páginas que enruta.",
            "Elimina las rutas que no sean estáticas.",
            "Traslada todas las páginas al proyecto de base de datos.",
            "Desactiva la navegación del navegador.",
        ],
        "correct": "A",
        "explanation": "La documentación señala que Router propaga el render mode a las páginas que enruta.",
        "difficulty": "intermediate",
        "question_type": "concept",
        "citation": "Apply a render mode to the entire app — Router propagation",
    },
    {
        "objective_id": "t26-lo-supp-010",
        "question": "Cuando se habilita la interactividad global de una Blazor Web App, ¿qué componente suele recibir también el mismo modo que Routes?",
        "options": [
            "DbContext",
            "HeadOutlet",
            "HttpClientFactory",
            "ErrorBoundary del navegador exclusivamente",
        ],
        "correct": "B",
        "explanation": "El ejemplo de aplicación global indica que normalmente también se asigna el mismo modo interactivo a HeadOutlet.",
        "difficulty": "intermediate",
        "question_type": "concept",
        "citation": "Apply a render mode to the entire app — HeadOutlet",
    },
    {
        "objective_id": "t26-lo-supp-011",
        "question": "¿Qué decisión describe con precisión el modo Interactive Auto mientras un componente permanece en la página?",
        "options": [
            "Cambia continuamente de servidor a WebAssembly en cada evento.",
            "Usa siempre WebAssembly y nunca evalúa el contexto de la página.",
            "Toma una decisión inicial y mantiene ese tipo de interactividad mientras el componente siga en la página.",
            "Desactiva la interactividad después del prerendering.",
        ],
        "correct": "C",
        "explanation": "La documentación aclara que Auto no cambia dinámicamente el modo de un componente ya presente: decide inicialmente y conserva ese tipo de interactividad mientras permanece en la página.",
        "difficulty": "intermediate",
        "question_type": "concept",
        "citation": "Interactive Auto render mode — initial decision",
    },
    {
        "objective_id": "t26-lo-supp-012",
        "question": "¿Por qué Interactive Auto prefiere coincidir con un modo interactivo ya presente en la página?",
        "options": [
            "Para evitar introducir otro runtime interactivo que no comparta estado con el existente.",
            "Para obligar a todas las páginas a usar Static.",
            "Para impedir que se descargue cualquier recurso WebAssembly.",
            "Para convertir el circuito en una base de datos distribuida.",
        ],
        "correct": "A",
        "explanation": "La guía explica que Auto prefiere el modo ya existente para evitar introducir un runtime interactivo nuevo que no comparta estado con el runtime existente.",
        "difficulty": "intermediate",
        "question_type": "scenario",
        "citation": "Interactive Auto render mode — existing interactivity",
    },
    {
        "objective_id": "t26-lo-supp-013",
        "question": "En una misma jerarquía de componentes, ¿qué combinación describe una posibilidad documentada?",
        "options": [
            "Todos los hermanos deben compartir obligatoriamente el mismo modo.",
            "Un hermano puede ser Static, pero ningún otro puede ser interactivo.",
            "Solo se permiten dos componentes si ambos usan InteractiveServer.",
            "Los hermanos pueden usar distintos modos interactivos, si la jerarquía lo permite.",
        ],
        "correct": "D",
        "explanation": "Las reglas de propagación permiten usar los modos interactivos desde componentes, incluidos modos diferentes para componentes hermanos.",
        "difficulty": "intermediate",
        "question_type": "scenario",
        "citation": "Render-mode propagation — sibling components",
    },
    {
        "objective_id": "t26-lo-supp-014",
        "question": "¿Qué ocurre si un componente hijo intenta cambiar a otro modo interactivo distinto del modo interactivo de su padre?",
        "options": [
            "El hijo siempre hereda silenciosamente el nuevo modo.",
            "La combinación no está soportada; por ejemplo, un componente Server no puede ser hijo de uno WebAssembly.",
            "El framework convierte ambos componentes en MVC.",
            "Solo se cambia el color del componente.",
        ],
        "correct": "B",
        "explanation": "La regla de propagación prohíbe cambiar a otro modo interactivo en un hijo; la documentación da como ejemplo que Server no puede ser hijo de WebAssembly.",
        "difficulty": "intermediate",
        "question_type": "scenario",
        "citation": "Render-mode propagation — child components with different interactive modes",
    },
    {
        "objective_id": "t26-lo-supp-015",
        "question": "¿Por qué puede fallar al pasar ChildContent como parámetro a un componente con un render mode interactivo?",
        "options": [
            "Porque RenderFragment representa código arbitrario que no se puede serializar.",
            "Porque ChildContent solo se admite en componentes Static.",
            "Porque el parámetro siempre se convierte en una consulta SQL.",
            "Porque los layouts no pueden recibir parámetros.",
        ],
        "correct": "A",
        "explanation": "La documentación muestra InvalidOperationException: un parámetro RenderFragment es un delegado con código arbitrario y no se puede serializar al cruzar la frontera del modo.",
        "difficulty": "advanced",
        "question_type": "scenario",
        "citation": "Render-mode propagation — RenderFragment serialization",
    },
    {
        "objective_id": "t26-lo-supp-016",
        "question": "¿Qué solución propone la guía para el límite de serialización de ChildContent al aplicar un modo interactivo?",
        "options": [
            "Convertir el fragmento en una consulta SQL.",
            "Eliminar todos los parámetros del componente.",
            "Envolver el contenido en otro componente que no tenga ese parámetro en la frontera del modo.",
            "Cambiar siempre a un proyecto MVC.",
        ],
        "correct": "C",
        "explanation": "La solución documentada es envolver el componente hijo en otro componente sin el parámetro que cruza la frontera; el template usa este patrón con WrapperComponent y Routes.",
        "difficulty": "advanced",
        "question_type": "procedure",
        "citation": "Render-mode propagation — wrapper component workaround",
    },
    {
        "objective_id": "t26-lo-supp-017",
        "question": "Una página de Identity necesita leer o escribir cookies en una aplicación con interactividad global. ¿Qué enfoque documentado permite mantenerla en estático?",
        "options": [
            "Forzar InteractiveWebAssembly en la página.",
            "Usar ExcludeFromInteractiveRouting para que adopte static SSR y fuerce una recarga completa.",
            "Mover las cookies a localStorage durante el prerender.",
            "Desactivar el middleware de autorización del servidor.",
        ],
        "correct": "B",
        "explanation": "La guía usa [ExcludeFromInteractiveRouting] para páginas que deben trabajar en el ciclo petición/respuesta, como las que gestionan cookies; la navegación a ellas fuerza una recarga completa.",
        "difficulty": "advanced",
        "question_type": "scenario",
        "citation": "Static SSR pages in an interactive app — ExcludeFromInteractiveRouting",
    },
    {
        "objective_id": "t26-lo-supp-018",
        "question": "Durante el prerendering de un componente interactivo, ¿qué valor debe esperarse normalmente en RendererInfo.IsInteractive?",
        "options": [
            "Siempre true, porque el modo asignado ya es interactivo.",
            "El valor depende solo de si existe un archivo .Client.",
            "false, porque el componente aún se está prerenderizando y no está interactivo en ese momento.",
            "Un valor que representa el estado de una conexión SQL.",
        ],
        "correct": "C",
        "explanation": "RendererInfo.IsInteractive es false durante el prerendering y true cuando el componente ya se está renderizando interactivamente.",
        "difficulty": "advanced",
        "question_type": "concept",
        "citation": "Detect rendering location and interactivity — RendererInfo.IsInteractive",
    },
    {
        "objective_id": "t26-lo-supp-019",
        "question": "Si un componente usa static SSR sin un modo asignado, ¿qué expone AssignedRenderMode según la guía?",
        "options": [
            "InteractiveServerRenderMode siempre.",
            "InteractiveWebAssemblyRenderMode siempre.",
            "Una instancia de InteractiveAutoRenderMode.",
            "null, porque no tiene un render mode asignado.",
        ],
        "correct": "D",
        "explanation": "AssignedRenderMode expone null cuando no se ha asignado un render mode; los modos interactivos exponen sus tipos correspondientes.",
        "difficulty": "advanced",
        "question_type": "concept",
        "citation": "Detect rendering location and interactivity — AssignedRenderMode",
    },
    {
        "objective_id": "t26-lo-supp-020",
        "question": "Durante static SSR, ¿qué mecanismo procesa normalmente la autorización de una solicitud de página?",
        "options": [
            "El componente NotAuthorized de Blazor siempre se renderiza antes del middleware.",
            "Un circuito WebAssembly creado durante la solicitud.",
            "El pipeline middleware de ASP.NET Core, porque los componentes no se renderizan durante ese procesamiento.",
            "El almacenamiento local del navegador sin una solicitud al servidor.",
        ],
        "correct": "C",
        "explanation": "La documentación indica que durante static SSR las solicitudes de páginas se procesan por el pipeline middleware de ASP.NET Core; las características dedicadas del Router, como NotAuthorized, no operan porque los componentes no se renderizan durante ese procesamiento.",
        "difficulty": "advanced",
        "question_type": "scenario",
        "citation": "Static server-side rendering — routing and authorization",
    },
]


def source_for(spec: dict) -> dict:
    return {
        "source_id": "BLAZOR-10",
        "title": "ASP.NET Core Blazor render modes",
        "authority": "Microsoft Learn",
        "tier": "official_primary",
        "url": RENDER_MODES_URL,
        "citation": spec["citation"],
        "version_or_as_of": "ASP.NET Core 10.0, current stable reference at research time",
        "retrieved_at": DATE,
        "verified_at": DATE,
    }


def load_accepted_records() -> list[dict]:
    records = []
    for path in sorted((ROOT / "docs/question-bank/accepted").glob("topic-*-lot-*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        records.extend(payload.get("questions", []))
    return records


def make_record(spec: dict, numeric_id: int) -> dict:
    record = {
        "id": numeric_id,
        "stable_id": "",
        "topic_num": TOPIC,
        "question": spec["question"],
        "option_a": spec["options"][0],
        "option_b": spec["options"][1],
        "option_c": spec["options"][2],
        "option_d": spec["options"][3],
        "correct": spec["correct"],
        "explanation": spec["explanation"],
        "learning_objective_id": spec["objective_id"],
        "difficulty": spec["difficulty"],
        "question_type": spec["question_type"],
        "sources": [source_for(spec)],
        "verification": {
            "answer": {"status": "uncertain", "reviewer": "awaiting-independent-review", "checked_at": DATE, "basis": "Candidate answer requires an independent second pass against the cited official source."},
            "explanation": {"status": "uncertain", "reviewer": "awaiting-independent-review", "checked_at": DATE, "basis": "Candidate explanation requires an independent second pass against the cited official source."},
            "reviewed_at": DATE,
            "reviewer_decision": "quarantined",
        },
        "deduplication": {},
        "status": "quarantined",
    }
    record["stable_id"] = stable_id_for(record)
    return record


def main() -> int:
    if len(SPECS) != 20:
        raise RuntimeError("supplemental lot must contain exactly 20 questions")
    accepted_records = load_accepted_records()
    supplement_objectives = {spec["objective_id"] for spec in SPECS}
    supplement_questions = {spec["question"] for spec in SPECS}
    # A retry after native import must screen against every prior lot while
    # excluding this lot's own already-published representation.
    existing = [question for question in SEED_QUESTIONS if question.get("question") not in supplement_questions]
    existing.extend(record for record in accepted_records if record.get("learning_objective_id") not in supplement_objectives)
    accepted_ids = [record["id"] for record in accepted_records]
    start_id = max([1200, *accepted_ids]) + 1
    records = []
    for offset, spec in enumerate(SPECS):
        record = make_record(spec, start_id + offset)
        record["deduplication"] = screen_duplicates(record, existing + records, checked_at=DATE).as_dict()
        errors = validate_record(record)
        if errors:
            raise RuntimeError(f"candidate {record['stable_id']} failed validation: {errors}")
        records.append(record)

    research_payload = {
        "generated_at": DATE,
        "research_artifact": "docs/question-bank/research/topic-26-lot-11-render-mode-boundaries.md",
        "topic_num": TOPIC,
        "lot_num": LOT,
        "revision": REVISION,
        "source_ids": ["BLAZOR-10"],
        "supplemental": True,
        "excluded_from_target_manifest": True,
        "batches": [{"topic_num": TOPIC, "lot_num": LOT, "source_ids": ["BLAZOR-10"], "questions": SPECS}],
    }
    RESEARCH_ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    RESEARCH_ARTIFACT.write_text(json.dumps(research_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    payload = {
        "lot_version": "1.0",
        "state": "candidates_written",
        "topic_num": TOPIC,
        "lot_num": LOT,
        "revision": REVISION,
        "generated_at": DATE,
        "supplemental": True,
        "excluded_from_target_manifest": True,
        "source_register_sha256": file_sha256(SOURCE_REGISTER),
        "objective_manifest_sha256": file_sha256(OBJECTIVE_MANIFEST),
        "syllabus_sha256": file_sha256(SYLLABUS),
        "source_verification": {"source_ids": ["BLAZOR-10"], "verified_at": DATE, "pages": [RENDER_MODES_URL]},
        "counts": {"candidates": len(records), "accepted": 0, "rejected": 0, "quarantined": len(records)},
        "questions": records,
    }
    LOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    LOT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    checkpoint = {
        "schema_version": "1.0",
        "syllabus_hash": payload["syllabus_sha256"],
        "source_register_hash": payload["source_register_sha256"],
        "topic_num": TOPIC,
        "lot_num": LOT,
        "revision": REVISION,
        "stage": "candidates_written",
        "objective_ids": [record["learning_objective_id"] for record in records],
        "stable_ids": [record["stable_id"] for record in records],
        "counts": payload["counts"],
        "input_hash": hashlib.sha256((payload["source_register_sha256"] + payload["objective_manifest_sha256"]).encode()).hexdigest(),
        "output_hash": file_sha256(LOT_PATH),
        "last_import": {"status": "not_started", "transaction": None},
    }
    appended = append_checkpoint(CHECKPOINT_PATH, checkpoint)
    print(f"topic {TOPIC} supplemental lot {LOT}: wrote {len(records)} quarantined candidates; checkpoint {'appended' if appended else 'already present'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
