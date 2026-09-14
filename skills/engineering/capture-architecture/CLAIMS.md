# Claims

A claim is one sentence about the current system plus the file and symbol that proves it. Write the list before you touch a doc. Use `CONTEXT.md` terms.

Skip a category the repo does not have. Do not add a row to make the list look complete.

## Actors and external systems

Who calls the system, and what the system calls. Evidence: entry points (HTTP routers, CLI commands, message consumers, scheduled jobs), client SDK imports, outbound HTTP clients, webhook handlers.

## Runtime topology

Which processes run, and what connects them. Evidence: process entry files, `Dockerfile` and compose files, queue and topic names, scheduler config, deploy manifests.

## Stores and write ownership

Every database, cache, bucket, and index, and which module may write each one. Evidence: schema files, migrations, ORM models, repository modules, bucket names in config. A read path does not count as ownership.

## Trust boundaries

Where a request is authenticated and authorized, and which paths are public. Evidence: auth middleware, token verification, role checks, route lists with and without guards, CORS and network policy.

## Main write paths

The two or three operations that change the system of record, in order. Evidence: the handler, the validation it runs, the transaction, the events or jobs it emits, and the idempotency key or dedupe check if there is one.

## Module dependency direction

Which modules or packages may import which, and what enforces it. Evidence: workspace layout, package manifests, import lint rules (`eslint-plugin-boundaries`, `import/no-restricted-paths`, `dependency-cruiser`, `ArchUnit`, `import-linter`), build graph config. If nothing enforces it, write "convention only".

## Workflows and legal states

Entities with a lifecycle, and the transitions the code allows. Evidence: enums, state machines, transition maps, status columns with a check constraint, guard clauses that reject a transition.

## Cross-cutting concerns

How the code handles errors, logging, configuration, and feature flags. Evidence: error base classes and global handlers, logger setup and request context, config loaders and env schemas, flag providers. One claim per concern. Skip a concern that has no shared mechanism.

## Deployment and configuration

What runs where, and which secrets each part needs by name. Evidence: CI and deploy pipelines, infrastructure definitions, environment schemas, cron definitions. Names only, never a value.

## Test boundaries

What the suite treats as a unit, what runs against real infrastructure, and what it fakes. Evidence: test config, fixtures, fakes and test doubles, containers started in tests, contract tests.

## Extension points

Where the code expects new variants: plugin registries, strategy maps, handler tables, adapter interfaces with more than one implementation. Evidence: the registry and two existing entries. These claims feed the "where new code goes" section.
