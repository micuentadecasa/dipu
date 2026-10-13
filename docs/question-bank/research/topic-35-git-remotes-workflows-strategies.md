# Topic 35 — Git remoto, flujos de trabajo y estrategias de ramas

**Research date:** 2026-10-13 UTC
**Primary sources:** [`GIT-2.50`](../source-register.json), [`GITHUB-PULL-REQUESTS`](../source-register.json), [`GITHUB-FLOW`](../source-register.json) and [`ATLASSIAN-GIT-FLOW`](../source-register.json).
**Environment/version:** `git version 2.50.1 (Apple Git-155)`; Git command claims use the official Git reference entry point recorded in the source register.
**Evidence boundary:** This artifact covers remote names and refs, fetch/pull/push transport, pull-request collaboration as documented by GitHub, and branch-workflow comparisons. Local branches, merge/rebase conflict mechanics and stash behavior are covered by topic 34; SedipuAlba and other syllabus topics are out of scope.

## Source map

- [`git-remote`](https://git-scm.com/docs/git-remote), [`git-ls-remote`](https://git-scm.com/docs/git-ls-remote) and [`gitrepository-layout`](https://git-scm.com/docs/gitrepository-layout): remote configuration, URLs, remote-tracking refs and bare repositories.
- [`git-fetch`](https://git-scm.com/docs/git-fetch), [`git-pull`](https://git-scm.com/docs/git-pull) and [`git-push`](https://git-scm.com/docs/git-push): refspecs, transport, pruning, upstreams, fast-forward checks and guarded force updates.
- [`gitworkflows`](https://git-scm.com/docs/gitworkflows): topic branches, integration/stable branches and distributed workflow principles.
- [`GitHub pull requests`](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests): base/head branches, review, checks, protected branches, merge methods and conflict updates.
- [`GitHub flow`](https://docs.github.com/en/get-started/using-github/github-flow) and [`Atlassian Gitflow`](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow): short-lived branch flow and Gitflow branch roles used for the strategy comparison objectives.

## Verified propositions and objective map

The 100 objective statements below were checked against the cited official documentation on the research date. Five sequential lots contain 20 records each; the independent review key checks both the answer position and the cited source before native import.

- `t35-lo-001` — Un remoto es un nombre local asociado a una o más URLs y a reglas de seguimiento para intercambiar objetos y referencias. *(citation: git-remote — DESCRIPTION; source: GIT-2.50)*
- `t35-lo-002` — La forma detallada de git remote muestra los nombres y las URLs fetch/push configuradas. *(citation: git-remote — -v/--verbose; source: GIT-2.50)*
- `t35-lo-003` — remote add crea la configuración que vincula el nombre del remoto con la URL indicada. *(citation: git-remote — add; source: GIT-2.50)*
- `t35-lo-004` — rename actualiza el nombre del remoto y las referencias de seguimiento relacionadas. *(citation: git-remote — rename; source: GIT-2.50)*
- `t35-lo-005` — remove quita el remoto de la configuración local; no equivale a borrar el repositorio remoto. *(citation: git-remote — remove; source: GIT-2.50)*
- `t35-lo-006` — get-url devuelve la URL asociada al remoto y admite opciones para consultar sus variantes. *(citation: git-remote — get-url; source: GIT-2.50)*
- `t35-lo-007` — remote show presenta información de seguimiento, ramas locales y referencias remotas conocidas. *(citation: git-remote — show; source: GIT-2.50)*
- `t35-lo-008` — set-url modifica la URL configurada para el remoto, con modos específicos para fetch o push. *(citation: git-remote — set-url; source: GIT-2.50)*
- `t35-lo-009` — Las remote-tracking refs se organizan bajo refs/remotes y reflejan el estado conocido de otros repositorios. *(citation: gitrepository-layout — refs; gitglossary — remote-tracking branch; source: GIT-2.50)*
- `t35-lo-010` — Una remote-tracking branch se actualiza mediante operaciones de red y sirve como referencia local, no como canal directo de escritura. *(citation: gitglossary — remote-tracking branch; source: GIT-2.50)*
- `t35-lo-011` — clone usa origin como nombre remoto predeterminado salvo que se indique otro con sus opciones. *(citation: git-clone — -o/--origin; source: GIT-2.50)*
- `t35-lo-012` — get-url --all enumera las URLs configuradas en lugar de limitarse a la primera. *(citation: git-remote — get-url --all; source: GIT-2.50)*
- `t35-lo-013` — set-head permite configurar o consultar la rama simbólica HEAD asociada a un remoto. *(citation: git-remote — set-head; source: GIT-2.50)*
- `t35-lo-014` — remote prune elimina referencias de seguimiento que ya no aparecen en el remoto, sin borrar por ello las ramas locales. *(citation: git-remote — prune; source: GIT-2.50)*
- `t35-lo-015` — ls-remote lista referencias y object IDs disponibles en otro repositorio sin crear ni actualizar remote-tracking refs. *(citation: git-ls-remote — DESCRIPTION; source: GIT-2.50)*
- `t35-lo-016` — remote update ejecuta operaciones de obtención para los remotos o grupos definidos en la configuración. *(citation: git-remote — update; source: GIT-2.50)*
- `t35-lo-017` — Un repositorio bare omite el working tree y está pensado para intercambio, por ejemplo como destino central. *(citation: git-clone — --bare; gitrepository-layout — bare repository; source: GIT-2.50)*
- `t35-lo-018` — La configuración de un remoto es local al clon; remove no realiza una operación destructiva en el servidor. *(citation: git-remote — remove; source: GIT-2.50)*
- `t35-lo-019` — Git permite configurar por separado la URL usada para obtener y las URLs usadas para enviar. *(citation: git-remote — get-url; git-remote — set-url; source: GIT-2.50)*
- `t35-lo-020` — remote add solo registra la relación local; el intercambio de objetos se hace con fetch o push de forma explícita. *(citation: git-remote — add; source: GIT-2.50)*
- `t35-lo-021` — fetch actualiza la información local sobre otro repositorio, pero deja separada la decisión de integrar sus cambios. *(citation: git-fetch — DESCRIPTION; source: GIT-2.50)*
- `t35-lo-022` — fetch origin descarga y actualiza las referencias de seguimiento según la configuración y refspec aplicables. *(citation: git-fetch — <repository>; source: GIT-2.50)*
- `t35-lo-023` — --prune limpia las remote-tracking refs que dejaron de existir en el remoto consultado. *(citation: git-fetch — --prune; source: GIT-2.50)*
- `t35-lo-024` — --tags incorpora tags desde el remoto; no significa publicar los tags locales. *(citation: git-fetch — --tags; source: GIT-2.50)*
- `t35-lo-025` — --depth limita los commits obtenidos y puede crear o ampliar un repositorio shallow. *(citation: git-fetch — --depth; git-clone — --depth; source: GIT-2.50)*
- `t35-lo-026` — pull ejecuta una obtención y luego integra los cambios en la rama actual conforme a sus opciones. *(citation: git-pull — DESCRIPTION; source: GIT-2.50)*
- `t35-lo-027` — --rebase pide usar rebase para integrar la historia obtenida, con las advertencias normales de reescritura. *(citation: git-pull — --rebase; source: GIT-2.50)*
- `t35-lo-028` — --ff-only permite actualizar solo si la punta actual es ancestro de la historia obtenida. *(citation: git-pull — --ff-only; source: GIT-2.50)*
- `t35-lo-029` — --no-rebase selecciona la integración mediante merge en el flujo de pull. *(citation: git-pull — --no-rebase; source: GIT-2.50)*
- `t35-lo-030` — Un refspec describe qué refs se obtienen y dónde se almacenan o mapean localmente. *(citation: git-fetch — REFSPEC; gitglossary — refspec; source: GIT-2.50)*
- `t35-lo-031` — origin/main es una remote-tracking ref local y solo representa el estado conocido tras las actualizaciones realizadas. *(citation: gitglossary — remote-tracking branch; git-fetch — DESCRIPTION; source: GIT-2.50)*
- `t35-lo-032` — fetch actualiza refs/remotes y el almacén de objetos; la rama checkout queda sin fusionar. *(citation: git-fetch — DESCRIPTION; source: GIT-2.50)*
- `t35-lo-033` — FETCH_HEAD registra las refs obtenidas por fetch y puede ser usado por comandos de integración. *(citation: git-fetch — DESCRIPTION; gitrepository-layout — FETCH_HEAD; source: GIT-2.50)*
- `t35-lo-034` — --all selecciona todos los remotos configurados para la operación de obtención. *(citation: git-fetch — --all; source: GIT-2.50)*
- `t35-lo-035` — pull combina fetch con una integración, mientras fetch deja el análisis y la integración para una orden posterior. *(citation: git-fetch — DESCRIPTION; git-pull — DESCRIPTION; source: GIT-2.50)*
- `t35-lo-036` — Las opciones de poda de tags amplían el alcance de --prune y deben usarse entendiendo qué refs locales eliminarán. *(citation: git-fetch — --prune-tags; source: GIT-2.50)*
- `t35-lo-037` — --autostash usa un stash temporal para permitir la operación y lo intenta aplicar después. *(citation: git-pull — --autostash; source: GIT-2.50)*
- `t35-lo-038` — Separar obtención e integración permite inspeccionar la referencia de seguimiento antes de modificar la rama checkout. *(citation: git-fetch — DESCRIPTION; git-pull — DESCRIPTION; source: GIT-2.50)*
- `t35-lo-039` — La política fast-forward-only rechaza la divergencia para evitar que pull elija automáticamente merge o rebase. *(citation: git-pull — --ff-only; source: GIT-2.50)*
- `t35-lo-040` — La separación mejora el control sobre la revisión, la resolución de conflictos y la estrategia de integración. *(citation: git-fetch — DESCRIPTION; git-merge — DESCRIPTION; git-rebase — DESCRIPTION; source: GIT-2.50)*
- `t35-lo-041` — push transfiere objetos necesarios y propone actualizar refs en el repositorio receptor. *(citation: git-push — DESCRIPTION; source: GIT-2.50)*
- `t35-lo-042` — El refspec simple main pide actualizar la rama homónima del remoto origin con la rama local. *(citation: git-push — <repository> <refspec>; source: GIT-2.50)*
- `t35-lo-043` — --set-upstream registra la relación de seguimiento para que futuras operaciones puedan omitir referencias explícitas. *(citation: git-push — -u/--set-upstream; source: GIT-2.50)*
- `t35-lo-044` — La comprobación non-fast-forward protege la historia remota frente a actualizar una ref con una línea no descendiente. *(citation: git-push — NOTE ABOUT FAST-FORWARDS; source: GIT-2.50)*
- `t35-lo-045` — force-with-lease limita la sobrescritura a un estado remoto esperado y reduce el riesgo de borrar trabajo ajeno no observado. *(citation: git-push — --force-with-lease; source: GIT-2.50)*
- `t35-lo-046` — --force permite ignorar comprobaciones de avance y puede hacer inalcanzables commits publicados por otros. *(citation: git-push — --force; source: GIT-2.50)*
- `t35-lo-047` — La refspec de borrado envía una petición para eliminar la referencia feature en origin. *(citation: git-push — --delete; source: GIT-2.50)*
- `t35-lo-048` — --tags pide enviar todas las refs bajo refs/tags, independientemente de que apunten a commits alcanzables por ramas. *(citation: git-push — --tags; source: GIT-2.50)*
- `t35-lo-049` — --follow-tags limita la publicación automática a tags anotados alcanzables relacionados con las refs que se envían. *(citation: git-push — --follow-tags; source: GIT-2.50)*
- `t35-lo-050` — push.default configura qué ramas o referencias se consideran destino implícito en un push sencillo. *(citation: git-config — push.default; git-push — DESCRIPTION; source: GIT-2.50)*
- `t35-lo-051` — La refspec HEAD:main usa la revisión actual como origen y main como destino remoto. *(citation: git-push — REFSPEC; source: GIT-2.50)*
- `t35-lo-052` — --dry-run informa del resultado previsto sin realizar las actualizaciones remotas. *(citation: git-push — --dry-run; source: GIT-2.50)*
- `t35-lo-053` — --atomic solicita una actualización transaccional del conjunto de refs, si el servidor la admite. *(citation: git-push — --atomic; source: GIT-2.50)*
- `t35-lo-054` — La relación upstream aporta el destino predeterminado y la referencia de comparación para el flujo normal. *(citation: git-push — -u/--set-upstream; gitglossary — upstream branch; source: GIT-2.50)*
- `t35-lo-055` — --signed pide una transacción firmada cuando el servidor y el transporte soportan esa capacidad. *(citation: git-push — --signed; source: GIT-2.50)*
- `t35-lo-056` — --push-option transmite opciones de proceso al lado receptor, sujeto a su configuración y hooks. *(citation: git-push — --push-option; source: GIT-2.50)*
- `t35-lo-057` — La protección depende de la expectativa remota conocida y no sustituye la coordinación sobre reescrituras. *(citation: git-push — --force-with-lease; source: GIT-2.50)*
- `t35-lo-058` — --set-upstream registra origin/feature como upstream de la rama local feature al publicar. *(citation: git-push — -u/--set-upstream; source: GIT-2.50)*
- `t35-lo-059` — Una ref local y una ref en otro repositorio tienen operaciones y efectos distintos. *(citation: git-branch — -d/--delete; git-push — --delete; source: GIT-2.50)*
- `t35-lo-060` — Actualizar la expectativa y usar una fuerza condicionada evita sobrescribir silenciosamente cambios remotos desconocidos. *(citation: git-push — --force-with-lease; source: GIT-2.50)*
- `t35-lo-061` — La pull request es una unidad de colaboración de la plataforma para discutir, revisar y proponer integración. *(citation: Pull request overview — about pull requests; source: GITHUB-PULL-REQUESTS)*
- `t35-lo-062` — La plataforma superpone el flujo de revisión al intercambio de referencias que Git por sí solo proporciona. *(citation: About pull requests — differences from Git commands; source: GITHUB-PULL-REQUESTS)*
- `t35-lo-063` — La base define el contexto de destino de los cambios propuestos. *(citation: About pull requests — base and head branches; source: GITHUB-PULL-REQUESTS)*
- `t35-lo-064` — La rama head es la fuente cuyos cambios se comparan con la base. *(citation: About pull requests — base and head branches; source: GITHUB-PULL-REQUESTS)*
- `t35-lo-065` — Los nuevos pushes a la rama de origen actualizan la propuesta y sus comprobaciones. *(citation: Updating a pull request — push to the head branch; source: GITHUB-PULL-REQUESTS)*
- `t35-lo-066` — La revisión permite comentar líneas y aprobar, solicitar cambios o comentar la propuesta. *(citation: Reviewing proposed changes in a pull request; source: GITHUB-PULL-REQUESTS)*
- `t35-lo-067` — Las reglas de protección pueden exigir checks y revisiones antes de permitir la combinación. *(citation: About protected branches — required status checks and reviews; source: GITHUB-PULL-REQUESTS)*
- `t35-lo-068` — Las plataformas pueden exponer distintas estrategias, cada una con efectos de topología e identificadores. *(citation: Merging a pull request — merge methods; source: GITHUB-PULL-REQUESTS)*
- `t35-lo-069` — Cerrar la propuesta cambia su estado de colaboración, no equivale a integrar ni necesariamente a borrar la rama. *(citation: Closing a pull request; source: GITHUB-PULL-REQUESTS)*
- `t35-lo-070` — El estado draft comunica que el trabajo está en preparación y evita tratarlo como propuesta lista. *(citation: Changing the status of a pull request — draft; source: GITHUB-PULL-REQUESTS)*
- `t35-lo-071` — La plataforma mantiene revisores y sus solicitudes como parte de la colaboración de la propuesta. *(citation: Requesting a pull request review; source: GITHUB-PULL-REQUESTS)*
- `t35-lo-072` — La protección limita actualizaciones directas y puede requerir revisiones, checks o historial lineal. *(citation: About protected branches; source: GITHUB-PULL-REQUESTS)*
- `t35-lo-073` — Los checks proporcionan señales automatizadas que las políticas de integración pueden requerir. *(citation: About status checks; source: GITHUB-PULL-REQUESTS)*
- `t35-lo-074` — La comparación delimita exactamente el conjunto de cambios propuestos para revisión. *(citation: About pull requests — comparing changes; source: GITHUB-PULL-REQUESTS)*
- `t35-lo-075` — La protección de rama desplaza la integración hacia una propuesta revisable y controlada. *(citation: About protected branches; source: GITHUB-PULL-REQUESTS)*
- `t35-lo-076` — La conversación y las revisiones son metadatos colaborativos que acompañan a la comparación. *(citation: Reviewing proposed changes in a pull request; source: GITHUB-PULL-REQUESTS)*
- `t35-lo-077` — Una revisión puede bloquear la aceptación hasta que el autor corrija y publique nuevos cambios. *(citation: Submitting a pull request review; source: GITHUB-PULL-REQUESTS)*
- `t35-lo-078` — Revertir conserva el historial y añade una corrección que deshace los cambios integrados. *(citation: Reverting a pull request; source: GITHUB-PULL-REQUESTS)*
- `t35-lo-079` — La propuesta necesita actualizar o resolver cambios solapados antes de poder integrarse. *(citation: About merge conflicts in pull requests; source: GITHUB-PULL-REQUESTS)*
- `t35-lo-080` — Actualizar la rama de trabajo y enviar la resolución permite recalcular checks y la comparación de la propuesta. *(citation: Updating a pull request branch; source: GITHUB-PULL-REQUESTS)*
- `t35-lo-081` — Una topic branch aísla una línea de trabajo enfocada hasta que se integra en una rama de desarrollo o estable. *(citation: gitworkflows — Topic branches; source: GIT-2.50)*
- `t35-lo-082` — Gitworkflows separa integración y estabilidad para ordenar la incorporación de contribuciones. *(citation: gitworkflows — Integration branches; source: GIT-2.50)*
- `t35-lo-083` — La separación proporciona una frontera de calidad entre trabajo en integración y código estable. *(citation: gitworkflows — Integration branches; source: GIT-2.50)*
- `t35-lo-084` — Git distribuido permite múltiples repositorios y roles de integración mediante fetch, push y selección de refs. *(citation: gitworkflows — Distributed workflows; source: GIT-2.50)*
- `t35-lo-085` — La estabilidad de referencias compartidas reduce el coste de coordinación y evita divergencias artificiales. *(citation: gitworkflows — Public history; git-rebase — DESCRIPTION; source: GIT-2.50)*
- `t35-lo-086` — GitHub flow documenta un flujo ligero basado en rama, commit, pull request, revisión y despliegue. *(citation: GitHub flow — Understanding the GitHub flow; source: GITHUB-FLOW)*
- `t35-lo-087` — La pull request convierte la rama corta en una propuesta revisable contra la rama base. *(citation: GitHub flow — Creating a branch; opening a pull request; source: GITHUB-FLOW)*
- `t35-lo-088` — Las guías distinguen la simplicidad de ramas cortas de la estructura explícita de Gitflow. *(citation: GitHub flow — Understanding the GitHub flow; Gitflow workflow — overview; source: GITHUB-FLOW)*
- `t35-lo-089` — Gitflow usa develop como línea donde se integran funcionalidades antes de preparar una release. *(citation: Gitflow workflow — develop branch; source: ATLASSIAN-GIT-FLOW)*
- `t35-lo-090` — La rama release aísla la estabilización de una versión mientras el desarrollo futuro puede continuar. *(citation: Gitflow workflow — release branches; source: ATLASSIAN-GIT-FLOW)*
- `t35-lo-091` — Hotfix se reserva para correcciones urgentes sobre la línea de producción y después se integra donde corresponda. *(citation: Gitflow workflow — hotfix branches; source: ATLASSIAN-GIT-FLOW)*
- `t35-lo-092` — El cierre de una release conserva la versión en producción y sincroniza la línea de desarrollo. *(citation: Gitflow workflow — release branches; source: ATLASSIAN-GIT-FLOW)*
- `t35-lo-093` — La estructura formal de Gitflow ofrece roles claros, pero aumenta la coordinación y la divergencia potencial. *(citation: Gitflow workflow — comparing workflows; source: ATLASSIAN-GIT-FLOW)*
- `t35-lo-094` — Trunk-based development reduce el tiempo de vida de ramas y favorece la integración frecuente sobre el tronco. *(citation: GitHub flow — Understanding the GitHub flow; source: GITHUB-FLOW)*
- `t35-lo-095` — El flujo de GitHub es una realización ligera compatible con la idea de mantener corta la divergencia respecto al tronco. *(citation: GitHub flow — Understanding the GitHub flow; source: GITHUB-FLOW)*
- `t35-lo-096` — La estrategia debe responder al ritmo de entrega, controles y necesidades de mantenimiento, no a una receta universal. *(citation: Gitflow workflow — comparing workflows; GitHub flow — understanding the flow; source: ATLASSIAN-GIT-FLOW)*
- `t35-lo-097` — La secuencia limita la divergencia, conserva la revisión y usa checks antes de modificar la línea principal. *(citation: GitHub flow — understanding the GitHub flow; git-fetch — DESCRIPTION; source: GITHUB-FLOW)*
- `t35-lo-098` — Una estrategia es un proceso de colaboración y calidad, no solo una nomenclatura de refs. *(citation: gitworkflows — Workflow; About protected branches; source: GIT-2.50)*
- `t35-lo-099` — Las protecciones combinan control de acceso y señales de calidad antes de integrar cambios. *(citation: About protected branches; About status checks; source: GITHUB-PULL-REQUESTS)*
- `t35-lo-100` — La colaboración segura hace visibles los límites entre trabajo local, referencias compartidas, revisión e integración. *(citation: gitworkflows — Workflow; About pull requests; git-push — NOTE ABOUT FAST-FORWARDS; source: GIT-2.50)*

## Coverage and verification boundary

- Lots use balanced A/B/C/D positions and the established 4 basic / 10 intermediate / 6 advanced shape.
- GitHub and Atlassian documentation are used only for platform workflow and named strategy claims; Git command behavior remains sourced to the official Git project documentation.
- No claims about Diputación-specific remotes, hosting credentials or an unverified server policy are introduced.
