# Topic 28 supplemental research — lifecycle, CSS, and template boundaries

**Research/verification date:** 2026-10-15 UTC
**Primary authority:** Microsoft Learn, ASP.NET Core 10.0 Blazor documentation (`BLAZOR-10`)
**Scope:** supplemental coverage-gap lot for exact lifecycle, CSS-isolation, and templated-component behavior not represented precisely in published topic-28 lots 1–10.

## Verified pages

- [ASP.NET Core Razor component lifecycle](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/lifecycle?view=aspnetcore-10.0), retrieved and checked 2026-10-15. Sections used: `SetParametersAsync`, initialization ordering, asynchronous valid state, prerendering, parameter-set callbacks, after-render callbacks, `firstRender`, and rerender behavior.
- [ASP.NET Core Blazor CSS isolation](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/css-isolation?view=aspnetcore-10.0), retrieved and checked 2026-10-15. Sections used: `::deep` descendant boundaries and scope placement.
- [ASP.NET Core Blazor templated components](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/templated-components?view=aspnetcore-10.0), retrieved and checked 2026-10-15. Sections used: generic render fragments, implicit context, explicit `Context`, and type inference.

## Coverage gap

The published topic-28 set covers the lifecycle names, basic prerendering/disposal, CSS isolation, templates, dynamic components, and ErrorBoundary scenarios. This lot isolates exact boundaries useful for implementation reasoning: `ParameterView` assignment and base calls; missing-parameter preservation; parent/child initialization ordering; valid state before asynchronous yields; prerender duplication and JS restrictions; unchanged parameter-set callbacks; after-render invocation and rerender suppression; CSS scope placement; and generic template context/type inference.

The lot is supplemental and does **not** change the captain-approved 200-objective-per-topic manifest or 8,000-slot target. Its `t28-lo-supp-*` objective IDs are excluded from target-count statistics. Every record cites the exact official page and section used; no code or SQL execution is applicable.
