# Topic 30 research — Blazor dependency injection and configuration

**Research date:** 2026-10-12.

The topic boundary is the official call's topic 30: **Blazor: inyección de dependencias y configuración**. The 100 researched objectives below are limited to primary Microsoft Learn documentation for ASP.NET Core 10.0 and Blazor 10.0:

- [Dependency injection in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection?view=aspnetcore-10.0) (`ASPNET-DI-10`): service registration, constructor injection, lifetimes, scopes, keyed services, disposal, scope validation, and DI guidelines.
- [Configuration in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-10.0) (`DOTNET-CONFIG-10`): providers, precedence, hierarchical keys, environment variables, command-line configuration, reload, connection strings, and options.
- [Dependency injection in ASP.NET Core Blazor](https://learn.microsoft.com/en-us/aspnet/core/blazor/fundamentals/dependency-injection?view=aspnetcore-10.0) (`BLAZOR-DI-10`): component injection, registration, lifetimes by hosting model, prerendering, and service scopes.
- [ASP.NET Core Blazor configuration](https://learn.microsoft.com/en-us/aspnet/core/blazor/fundamentals/configuration?view=aspnetcore-10.0) (`BLAZOR-CONFIG-10`): configuration access and public configuration in Blazor WebAssembly.

The source register pins each source to the ASP.NET Core 10.0 view and records retrieval and verification on 2026-10-12. Candidate generation is separate from independent review. The five candidate lots contain 20 records each (100 total), with distinct objective IDs and deterministic duplicate screening. No code or SQL execution is applicable to this topic; records use conceptual, procedural, comparison, and scenario questions.

## Knowledge map and coverage

- **Container and registration:** `IServiceCollection`, `IServiceProvider`, constructors, component injection, factories, instances, open generics, keyed services, `TryAdd`, and service resolution.
- **Lifetimes and scopes:** transient, scoped, singleton, disposal, scope validation, captive dependencies, thread safety, background-service scopes, and Blazor Server versus WebAssembly semantics.
- **Options and configuration:** providers, precedence, hierarchical keys, environment-variable mapping, command-line input, reload, binding, `IOptions<T>`, `IOptionsSnapshot<T>`, `IOptionsMonitor<T>`, named options, validation, and startup validation.
- **Blazor integration:** service registration in `Program`, `@inject`/`[Inject]`, `HttpClient`, circuit scope, prerendering, server configuration, WebAssembly configuration, and public configuration constraints.

The initial 100 statements map to these subtopics and are distributed across the five lots. Expansion lots 06–10 add 100 independently reviewed scenarios across DI registration/lifetimes, configuration providers and precedence, options, Blazor hosting integration and public-configuration safety. All records remain restricted to the pinned Microsoft Learn ASP.NET Core/Blazor 10.0 sources; no unsupported framework behavior is inferred.
