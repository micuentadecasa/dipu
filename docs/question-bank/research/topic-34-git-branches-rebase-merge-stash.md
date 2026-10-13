# Topic 34 — Git: ramas, rebase, merge frente a rebase y stash

**Research date:** 2026-10-13 UTC
**Primary source:** [`GIT-2.50`](../source-register.json), Git project documentation, verified entry point `https://git-scm.com/docs`
**Environment/version:** `git version 2.50.1 (Apple Git-155)`; source register records this stable reference and verification date 2026-10-12.
**Syllabus boundary:** This artifact covers local branches, switching and branch references; merge and conflict recovery; rebase and its history consequences; stash and temporary work. Remote transport, pull requests and branch strategies are reserved for topic 35.

## Source map

- [`gitglossary`](https://git-scm.com/docs/gitglossary): branches, refs, HEAD, commits and pathspec vocabulary.
- [`git-branch`](https://git-scm.com/docs/git-branch), [`git-switch`](https://git-scm.com/docs/git-switch), [`git-checkout`](https://git-scm.com/docs/git-checkout): branch creation, movement, listing, deletion and detached HEAD.
- [`git-merge`](https://git-scm.com/docs/git-merge) and [`git-merge-base`](https://git-scm.com/docs/git-merge-base): fast-forward/three-way merge, strategies, conflict states and recovery.
- [`git-rebase`](https://git-scm.com/docs/git-rebase): upstream/onto selection, interactive todo, conflict recovery, merge preservation and empty commits.
- [`git-stash`](https://git-scm.com/docs/git-stash): temporary work, index/untracked/ignored inclusion, apply/pop, branches and cleanup.
- [`git-reflog`](https://git-scm.com/docs/git-reflog), [`git-add`](https://git-scm.com/docs/git-add), [`git-status`](https://git-scm.com/docs/git-status): local recovery and recording conflict resolutions.

## Verified propositions and objective map

The 100 objective statements below were checked against the cited section of the official Git reference on the research date. Candidate questions are split into five sequential lots of 20; independent review checks the answer and citation before import.

- `t34-lo-001` — Una rama es una referencia que puede avanzar cuando se crean commits, mientras comparte la base de objetos del repositorio. *(citation: gitglossary — branch; ref)*
- `t34-lo-002` — La forma simple de git branch crea una referencia nueva en el punto indicado, que por defecto es HEAD. *(citation: git-branch — DESCRIPTION)*
- `t34-lo-003` — --create (o -c) crea la rama y cambia a ella en una sola operación. *(citation: git-switch — -c/--create)*
- `t34-lo-004` — La consulta de la rama actual identifica el nombre de la rama asociada a HEAD y no enumera todo el historial. *(citation: git-branch — --show-current)*
- `t34-lo-005` — La opción de movimiento renombra la referencia y actualiza la configuración asociada cuando corresponde. *(citation: git-branch — -m/--move)*
- `t34-lo-006` — El borrado normal con -d exige que la rama esté fusionada de forma alcanzable desde la rama actual u otra condición segura documentada. *(citation: git-branch — -d/--delete)*
- `t34-lo-007` — -D combina el borrado con la fuerza y permite quitar una rama cuya punta no está fusionada según la comprobación normal. *(citation: git-branch — -D)*
- `t34-lo-008` — El cambio de rama actualiza HEAD y normalmente el índice y el working tree para reflejar la rama destino. *(citation: git-switch — DESCRIPTION)*
- `t34-lo-009` — --list muestra las ramas que coinciden con el patrón indicado o todas si no se da patrón. *(citation: git-branch — --list)*
- `t34-lo-010` — La opción --contains selecciona las ramas cuya punta alcanza el commit especificado. *(citation: git-branch — --contains)*
- `t34-lo-011` — --merged muestra referencias alcanzables desde el punto indicado y ayuda a distinguir ramas integradas. *(citation: git-branch — --merged)*
- `t34-lo-012` — --no-merged invierte la selección de --merged y muestra las ramas aún no integradas en el punto consultado. *(citation: git-branch — --no-merged)*
- `t34-lo-013` — --copy crea una nueva referencia de rama basada en la existente y mantiene intacta la referencia original. *(citation: git-branch — -c/--copy)*
- `t34-lo-014` — La forma de git branch -f mueve la referencia nombrada al start-point especificado, sujeta a las restricciones documentadas. *(citation: git-branch — -f/--force)*
- `t34-lo-015` — Al comprobar un commit directamente, HEAD apunta al commit y no a una referencia de rama que avance con nuevos commits. *(citation: git-switch — --detach; gitglossary — detached HEAD)*
- `t34-lo-016` — checkout -b combina creación y cambio; switch -c expresa la misma intención con la interfaz dedicada a ramas. *(citation: git-checkout — -b; git-switch — -c/--create)*
- `t34-lo-017` — En el estado normal HEAD es simbólico y nombra la rama comprobada, cuya ref señala la punta del historial. *(citation: gitrepository-layout — HEAD; git-symbolic-ref)*
- `t34-lo-018` — Las ramas son referencias ligeras dentro del repositorio y comparten la base de objetos alcanzable. *(citation: gitglossary — branch; gitrepository-layout — refs)*
- `t34-lo-019` — Git evita perder modificaciones locales incompatibles con el estado que tendría la rama destino. *(citation: git-switch — DESCRIPTION; git-checkout — DESCRIPTION)*
- `t34-lo-020` — El reflog registra actualizaciones locales de referencias y HEAD, por lo que puede revelar la posición anterior durante su retención. *(citation: git-reflog — DESCRIPTION; git-branch — -d/--delete)*
- `t34-lo-021` — git merge incorpora en la rama actual la historia de uno o más commits nombrados. *(citation: git-merge — DESCRIPTION)*
- `t34-lo-022` — Si la punta actual es ancestro de la otra, Git puede mover la referencia directamente y no necesita un commit de integración. *(citation: git-merge — FAST-FORWARD MERGE)*
- `t34-lo-023` — --no-ff fuerza un commit de merge, lo que conserva explícitamente la existencia de la rama integrada en la topología. *(citation: git-merge — --ff/--no-ff)*
- `t34-lo-024` — --ff-only aborta si la integración no puede representarse como fast-forward. *(citation: git-merge — --ff-only)*
- `t34-lo-025` — El merge base es un ancestro común usado por los algoritmos de integración, especialmente en una fusión de tres vías. *(citation: git-merge-base — DESCRIPTION; git-merge — MERGE STRATEGIES)*
- `t34-lo-026` — La fusión de tres vías compara las dos puntas con un ancestro común cuando no basta mover una referencia. *(citation: git-merge — DESCRIPTION; git-merge-base — DESCRIPTION)*
- `t34-lo-027` — Un conflicto indica que la combinación automática no puede elegir una interpretación única para cambios solapados o estructuralmente incompatibles. *(citation: git-merge — TRUE MERGE; git-merge — HOW CONFLICTS ARE PRESENTED)*
- `t34-lo-028` — Tras resolver manualmente las marcas, git add registra la versión resuelta en el índice para que la fusión pueda continuar. *(citation: git-merge — HOW CONFLICTS ARE PRESENTED; git-add — DESCRIPTION)*
- `t34-lo-029` — MERGE_HEAD permite a Git saber qué commit o commits se están fusionando al completar el merge. *(citation: git-merge — TRUE MERGE; gitrepository-layout — MERGE_HEAD)*
- `t34-lo-030` — git status muestra las rutas no fusionadas y orienta sobre las acciones de resolución pendientes. *(citation: git-status — DESCRIPTION; git-merge — HOW CONFLICTS ARE PRESENTED)*
- `t34-lo-031` — git add sustituye las entradas de conflicto de la ruta por la versión resuelta preparada para el commit de merge. *(citation: git-add — DESCRIPTION; git-merge — HOW CONFLICTS ARE PRESENTED)*
- `t34-lo-032` — La continuación usa el índice resuelto y permite finalizar la fusión conforme al mensaje y opciones pendientes. *(citation: git-merge — --continue)*
- `t34-lo-033` — --abort intenta reconstruir el estado previo a la operación de merge y abandona la integración pendiente. *(citation: git-merge — --abort)*
- `t34-lo-034` — --quit olvida la operación de merge en curso, pero deja el índice y el working tree tal como están. *(citation: git-merge — --quit)*
- `t34-lo-035` — La terminología distingue el lado checkout de la rama que se está integrando, aunque el significado contextual debe comprobarse en la operación concreta. *(citation: git-merge — HOW CONFLICTS ARE PRESENTED)*
- `t34-lo-036` — Una fusión de múltiples heads puede crear un commit que registra más de dos padres y la integración conjunta. *(citation: git-merge — MERGING MULTIPLE HEADS)*
- `t34-lo-037` — git merge admite -s o --strategy para escoger el algoritmo de integración, además de sus opciones de estrategia. *(citation: git-merge — -s/--strategy)*
- `t34-lo-038` — Para impedir también el avance rápido y asegurar una pausa previa al commit de merge debe combinarse con --no-ff. *(citation: git-merge — --no-commit)*
- `t34-lo-039` — La edición afecta al mensaje del commit de integración, no al algoritmo que calcula sus árboles. *(citation: git-merge — --edit)*
- `t34-lo-040` — El flujo documentado separa la resolución y su registro en el índice de la decisión final de continuar o abandonar. *(citation: git-merge — HOW CONFLICTS ARE PRESENTED; git-merge — --continue; --abort)*
- `t34-lo-041` — Rebase toma commits seleccionados y los vuelve a aplicar sobre una base distinta, generando una historia reescrita. *(citation: git-rebase — DESCRIPTION)*
- `t34-lo-042` — La forma básica usa upstream como nueva base y aplica sobre ella los commits que están en la rama actual y no en upstream. *(citation: git-rebase — DESCRIPTION)*
- `t34-lo-043` — --onto separa la nueva base de la referencia que determina qué commits se reaplican. *(citation: git-rebase — --onto)*
- `t34-lo-044` — El cambio de padre altera la identidad criptográfica de los commits recreados. *(citation: git-rebase — DESCRIPTION; gitrevisions — commit object)*
- `t34-lo-045` — La reescritura puede obligar a reconciliar historias divergentes y complica la colaboración sobre commits publicados. *(citation: git-rebase — DESCRIPTION; git-rebase — RECOVERING FROM UPSTREAM REBASE)*
- `t34-lo-046` — La opción puede emplear el reflog de upstream para evitar reaplicar commits que ya fueron descartados de su historia visible. *(citation: git-rebase — --fork-point)*
- `t34-lo-047` — Rebase detiene la secuencia para que se resuelva el parche que no aplica limpiamente. *(citation: git-rebase — DESCRIPTION; git-rebase — CONFLICTS)*
- `t34-lo-048` — --continue retoma la secuencia usando la solución registrada en el índice. *(citation: git-rebase — --continue)*
- `t34-lo-049` — --skip descarta el commit conflictivo de la secuencia y pasa al siguiente. *(citation: git-rebase — --skip)*
- `t34-lo-050` — --abort detiene la operación y procura devolver HEAD y la rama al estado previo. *(citation: git-rebase — --abort)*
- `t34-lo-051` — --quit termina el seguimiento de la operación sin restablecer HEAD, índice ni working tree. *(citation: git-rebase — --quit)*
- `t34-lo-052` — -i o --interactive abre una lista de tareas en la que pueden reordenarse, combinarse o editarse commits. *(citation: git-rebase — -i/--interactive)*
- `t34-lo-053` — squash une el cambio con el commit anterior y solicita editar el mensaje combinado. *(citation: git-rebase — INTERACTIVE MODE)*
- `t34-lo-054` — --autosquash reconoce los prefijos de commits auxiliares y prepara el todo para combinarlos con su commit objetivo. *(citation: git-rebase — --autosquash)*
- `t34-lo-055` — --exec añade líneas exec al todo para ejecutar una orden después de cada commit creado durante la secuencia. *(citation: git-rebase — --exec)*
- `t34-lo-056` — --rebase-merges reconstruye commits de merge para preservar la topología en vez de aplanarla completamente. *(citation: git-rebase — --rebase-merges)*
- `t34-lo-057` — --keep-base selecciona la base de fork original como punto de reaplicación y evita moverla simplemente a la punta upstream. *(citation: git-rebase — --keep-base)*
- `t34-lo-058` — Las opciones de commits vacíos controlan la política cuando una reaplicación no introduce diferencias nuevas. *(citation: git-rebase — --empty)*
- `t34-lo-059` — La fusión conserva las líneas y añade una relación de integración, mientras rebase cambia los padres de commits recreados. *(citation: git-merge — DESCRIPTION; git-rebase — DESCRIPTION)*
- `t34-lo-060` — La resolución debe reflejarse en el índice, normalmente mediante git add, antes de continuar la secuencia. *(citation: git-rebase — CONFLICTS; git-add — DESCRIPTION)*
- `t34-lo-061` — Stash crea objetos y una referencia para apartar modificaciones locales y dejar limpio el estado de trabajo. *(citation: git-stash — DESCRIPTION)*
- `t34-lo-062` — stash push guarda el estado sucio del working tree y devuelve el árbol de trabajo al estado de la base, según las opciones. *(citation: git-stash — push)*
- `t34-lo-063` — stash list presenta las entradas de la pila y sus mensajes resumidos. *(citation: git-stash — list)*
- `t34-lo-064` — stash show muestra por defecto un resumen de las diferencias y puede recibir opciones para más detalle. *(citation: git-stash — show)*
- `t34-lo-065` — stash apply restaura cambios sin eliminar la referencia de stash, a diferencia del comportamiento adicional de pop. *(citation: git-stash — apply)*
- `t34-lo-066` — pop combina aplicación y eliminación, aunque si hay conflictos la entrada puede conservarse para permitir otro intento. *(citation: git-stash — pop)*
- `t34-lo-067` — --index intenta recuperar el estado staged además de las modificaciones del working tree. *(citation: git-stash — --index)*
- `t34-lo-068` — --include-untracked añade archivos no seguidos al contenido guardado, además de los cambios seguidos. *(citation: git-stash — -u/--include-untracked)*
- `t34-lo-069` — --all incluye archivos sin seguimiento e ignorados en el stash, con las precauciones correspondientes. *(citation: git-stash — -a/--all)*
- `t34-lo-070` — -m permite asociar un texto al stash para identificar su propósito en la lista. *(citation: git-stash — -m/--message)*
- `t34-lo-071` — stash branch crea una rama desde el commit donde se realizó el stash y aplica allí los cambios guardados. *(citation: git-stash — branch)*
- `t34-lo-072` — stash drop retira de la referencia de stash la entrada indicada. *(citation: git-stash — drop)*
- `t34-lo-073` — stash clear elimina todas las entradas de la colección de stashes; debe usarse con cuidado. *(citation: git-stash — clear)*
- `t34-lo-074` — Las entradas se nombran mediante la referencia especial stash y sus índices reflog, donde {0} es la más reciente. *(citation: git-stash — DESCRIPTION; gitrevisions — reflog selectors)*
- `t34-lo-075` — La inclusión de no seguidos requiere --include-untracked o --all; el comportamiento predeterminado se centra en cambios seguidos. *(citation: git-stash — DESCRIPTION; git-stash — -u/--include-untracked)*
- `t34-lo-076` — El pathspec permite elegir qué partes del working tree se guardan en la operación. *(citation: git-stash — push; gitglossary — pathspec)*
- `t34-lo-077` — Opciones como --keep-index permiten dejar intacto el estado preparado mientras se guarda el resto. *(citation: git-stash — --keep-index)*
- `t34-lo-078` — --include-untracked y --all tienen alcances distintos y el segundo incluye también las rutas ignoradas. *(citation: git-stash — -u/--include-untracked; -a/--all)*
- `t34-lo-079` — Cuando la aplicación no termina limpiamente, Git no elimina de forma normal la entrada para evitar perder el estado guardado. *(citation: git-stash — pop)*
- `t34-lo-080` — Los stashes usan referencias y objetos locales; tras borrarlos, el reflog o la recuperación de objetos puede ser una oportunidad temporal. *(citation: git-stash — DESCRIPTION; git-reflog — DESCRIPTION)*
- `t34-lo-081` — La fusión conserva la topología y el rebase cambia los padres de los commits reaplicados. *(citation: git-merge — DESCRIPTION; git-rebase — DESCRIPTION)*
- `t34-lo-082` — Las operaciones de branch sobre refs deben distinguir cambiar un nombre o puntero existente de copiarlo. *(citation: git-branch — -m/--move; git-branch — -c/--copy)*
- `t34-lo-083` — Rebase cambia identificadores y puede romper referencias de colaboradores; merge añade integración sin reemplazar esos commits. *(citation: git-merge — DESCRIPTION; git-rebase — DESCRIPTION)*
- `t34-lo-084` — Rebase es más seguro antes de publicar porque los commits recreados aún no son referencias compartidas por otros. *(citation: git-rebase — DESCRIPTION; git-rebase — RECOVERING FROM UPSTREAM REBASE)*
- `t34-lo-085` — La consulta de ramas fusionadas ofrece una señal de alcanzabilidad, pero la eliminación debe seguir una revisión explícita. *(citation: git-branch — --merged; git-branch — -d/--delete)*
- `t34-lo-086` — Renombrar una rama cambia el nombre de la ref, no la secuencia de commits que señala. *(citation: git-branch — -m/--move; gitrepository-layout — HEAD)*
- `t34-lo-087` — La entrada no fusionada indica que aún debe elegirse y añadir una versión resolviendo el conflicto. *(citation: git-merge — HOW CONFLICTS ARE PRESENTED; git-add — DESCRIPTION)*
- `t34-lo-088` — Las operaciones mantienen metadatos y secuencias distintas, por lo que sus comandos de abortar actúan sobre su propia operación pendiente. *(citation: git-merge — --abort; git-rebase — --abort)*
- `t34-lo-089` — Stash permite limpiar el working tree temporalmente y luego aplicar o extraer el trabajo en el contexto adecuado. *(citation: git-stash — DESCRIPTION; git-switch — DESCRIPTION)*
- `t34-lo-090` — La rama nombra una posición de historial; el checkout o switch actualiza un único working tree para reflejarla. *(citation: gitglossary — branch; git-switch — DESCRIPTION)*
- `t34-lo-091` — Un merge commit registra la relación entre las líneas integradas mediante múltiples padres. *(citation: git-merge — TRUE MERGE; gitglossary — commit object)*
- `t34-lo-092` — Rebase genera commits equivalentes con padres distintos, por eso sus identificadores cambian. *(citation: git-rebase — DESCRIPTION)*
- `t34-lo-093` — Un avance rápido actualiza la referencia y deja la secuencia existente sin un nuevo commit de merge. *(citation: git-merge — FAST-FORWARD MERGE)*
- `t34-lo-094` — --no-ff impide el fast-forward; --no-commit puede añadir una pausa antes de crear el merge commit. *(citation: git-merge — --ff/--no-ff; git-merge — --no-commit)*
- `t34-lo-095` — La edición cambia el working tree, pero git add comunica a Git que la ruta ya tiene una resolución preparada. *(citation: git-merge — HOW CONFLICTS ARE PRESENTED; git-add — DESCRIPTION)*
- `t34-lo-096` — El stash está pensado para posponer cambios locales, mientras el commit forma parte del historial nombrado por una rama o tag. *(citation: git-stash — DESCRIPTION; gitglossary — commit object)*
- `t34-lo-097` — La eliminación de la ref no implica de inmediato la desaparición de los objetos y el reflog puede conservar la posición anterior. *(citation: git-branch — -d/--delete; git-reflog — DESCRIPTION)*
- `t34-lo-098` — La opción normal comprueba la alcanzabilidad; la forzada permite borrar incluso una rama no fusionada. *(citation: git-branch — -d/--delete; git-branch — -D)*
- `t34-lo-099` — La operación pop combina aplicación y eliminación, mientras apply deja la entrada disponible para reutilizarla. *(citation: git-stash — apply; git-stash — pop)*
- `t34-lo-100` — La documentación advierte que iniciar un merge con modificaciones locales puede hacer imposible reconstruir exactamente el estado anterior. *(citation: git-merge — --abort)*

## Coverage and verification boundary

- Lots contain four-option A–D records with one keyed answer and source-backed explanations.
- The first 80 objectives cover definitions, mechanisms and recovery procedures; objectives 81–100 explicitly compare merge/rebase/branch/stash choices and recovery implications.
- No remote operation, pull request, or GitFlow/trunk-based claim is used here; those are reserved for topic 35.
- `GIT-2.50` is the only source ID used. Its version/as-of, URL, retrieval date and verification date remain attached to every imported record through the native additive schema.
