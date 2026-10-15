# Topic 27 supplemental research — advanced binding, events, and rendering

**Research/verification date:** 2026-10-15 UTC
**Primary authority:** Microsoft Learn, ASP.NET Core 10.0 Blazor documentation (`BLAZOR-10`)
**Scope:** supplemental coverage-gap lot for exact event, binding, and rendering behavior not represented precisely in published topic-27 lots 1–10.

## Verified pages

- [ASP.NET Core Blazor event handling](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/event-handling?view=aspnetcore-10.0), retrieved and checked 2026-10-15. Sections used: delegate event handlers, EventCallback, custom event arguments, prevent-default, and event rendering.
- [ASP.NET Core Blazor data binding](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/data-binding?view=aspnetcore-10.0), retrieved and checked 2026-10-15. Sections used: `@bind:after`, `@bind:get`/`@bind:set`, multiple select, unparsable values, format strings, and component-parameter binding.
- [ASP.NET Core Blazor rendering](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/rendering?view=aspnetcore-10.0), retrieved and checked 2026-10-15. Sections used: automatic rendering, `ShouldRender`, `StateHasChanged`, streaming rendering, and external notifications.
- [Avoid overwriting parameters in ASP.NET Core Blazor](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/overwriting-parameters?view=aspnetcore-10.0), retrieved and checked 2026-10-15. Sections used: parameter overwrite hazards and private state fields.

## Coverage gap

Published topic-27 records cover ordinary event callbacks, basic binding, cascading values, `@key`, element references, and lifecycle scenarios. This lot isolates additional source-backed details: automatic event renders; custom event registration; `@bind:after` timing and restrictions; `@bind:get`/`@bind:set` synchronization; array binding for multiple select; invalid-value reversion; date format binding; the `Value`/`ValueChanged` component contract; `ShouldRender` and render-queue coalescing; external-event notifications; streaming-rendering requirements; and parameter-overwrite avoidance.

The lot is supplemental and does **not** change the captain-approved 200-objective-per-topic manifest or the 8,000-slot target. Its `t27-lo-supp-*` objective IDs are excluded from target-count statistics. Every item remains restricted to the exact official page and section cited in its record; no code execution is applicable.
