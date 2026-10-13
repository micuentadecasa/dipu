# Topic 31 research — Blazor state management

**Research date:** 2026-10-13.

The topic boundary is the official call's topic 31: **Blazor: gestión de estado**. The first 100 researched objectives are restricted to the primary Microsoft Learn ASP.NET Core 10.0 Blazor state-management documentation:

- [ASP.NET Core Blazor state management](https://learn.microsoft.com/en-us/aspnet/core/blazor/state-management?view=aspnetcore-10.0) (`BLAZOR-STATE-10`): component state, state containers, notification, browser storage, persistence, prerendering, circuits, and state-management guidance.

The source register pins the ASP.NET Core 10.0 view and records retrieval and verification on 2026-10-13. Candidate generation is separate from independent review. The five candidate lots contain 20 records each (100 total), each with a distinct objective ID and five-level duplicate metadata. No code or SQL execution is applicable; the records use conceptual, comparison, procedural, and scenario questions.

## Knowledge map and coverage

- **Component and render state:** component fields/properties, `StateHasChanged`, `InvokeAsync`, `ShouldRender`, external notifications, and render boundaries.
- **Shared state:** state-container services, subscription/unsubscription, scoped versus singleton state in Blazor Server and WebAssembly, and state ownership.
- **Browser persistence:** local storage versus session storage, serialization, JS interop boundaries, and client-visible data.
- **Prerendering and reconnection:** state unavailable during prerender-only execution, persistent component state, hydration, circuit lifetime, and reconstructing transient state.
- **Design and safety:** ephemeral UI state versus durable application data, avoiding cross-user leakage, immutable snapshots, and minimizing serialized state.

The 100 statements map to these subtopics and are distributed across the five lots. The remaining 100 objective slots for topic 31 remain planning-only and are not counted as validated questions.
