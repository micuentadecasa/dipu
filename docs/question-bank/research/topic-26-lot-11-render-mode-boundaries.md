# Topic 26 supplemental research — render-mode boundaries

**Research/verification date:** 2026-10-15 UTC
**Primary authority:** Microsoft Learn, ASP.NET Core 10.0 Blazor documentation (`BLAZOR-10`)
**Scope:** a supplemental, non-target lot covering render-mode boundaries and runtime observability that are not represented precisely in the published topic-26 lots 1–10.

## Verified pages

- [ASP.NET Core Blazor render modes](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/render-modes?view=aspnetcore-10.0), retrieved and checked 2026-10-15. Sections used: scope and render-mode table, enabling interactive render modes, applying modes, application-level modes, prerendering, runtime detection, static SSR, Interactive Server/WebAssembly/Auto, propagation, and static SSR pages in an interactive app.
- [ASP.NET Core Blazor project structure](https://learn.microsoft.com/en-us/aspnet/core/blazor/project-structure?view=aspnetcore-10.0), retrieved and checked 2026-10-15. Used to cross-check the generated `App.razor`, client-project, and published-script boundaries.

## Coverage gap and source notes

The published 200-record topic-26 set covers the broad hosting-model comparison, common render modes, prerendering, deployment, circuits, payload, APIs, and Hybrid. This lot is deliberately narrower: standalone WebAssembly's lack of render modes; the services/render-mode registration seam; the `.Client` project boundary; directive-versus-directive-attribute semantics; root-component restrictions; `Routes`/`HeadOutlet` propagation; Auto's initial decision; cross-mode child restrictions; serializable parameter boundaries; static-SSR routing; and `RendererInfo`/`AssignedRenderMode` observability.

The lot is supplemental and does **not** change the captain-approved 200-objective-per-topic manifest or its 8,000-slot target. It is retained as an independently reviewed coverage-gap artifact. Its objective IDs use the `t26-lo-supp-*` namespace and are excluded from the target-count statistics.

Every candidate uses `BLAZOR-10` with the exact official page URL and section citation. No code or SQL execution is applicable to this documentation lot.
