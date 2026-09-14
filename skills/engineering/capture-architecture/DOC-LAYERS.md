# Doc Layers

Put each fact in one file. Duplicate truth drifts.

## Source ranking

On conflict, higher wins:

1. Compiled contracts, schemas, enums, and state machines
2. The write path that mutates the system of record
3. Entry points and delivery (routers, CLI, consumers, cron)
4. Deploy and boundary config
5. ADRs. Durable intent. If code diverged, fix code or supersede the ADR
6. Product READMEs
7. `docs/architecture.md` and the root README
8. Plans and work logs. History, never current architecture

`CONTEXT.md` is not a behavior source. It is the vocabulary filter on every other layer.

If an ADR disagrees with code, do not rewrite current-state docs to match the ADR. Either the code is wrong, or the ADR is superseded. Say which in the report.

## Layers

| Layer | Job |
| --- | --- |
| Root README | One system sentence, status, one overview diagram, reading order |
| `CONTEXT.md` or `CONTEXT-MAP.md` | Terms. No schemas, routes, or tables |
| `docs/architecture.md` | How data moves now, who may write what, where new code goes |
| `docs/adr/` | Why an expensive choice was made |
| Product README | How to run that product |
| Deploy notes | Projects, secrets by name, migrate, cron |
| Ops report | Dated aggregate counts. No secrets or personal data |

## What belongs where

**Root README.** One short system sentence. One overview diagram. Status. Reading order. Pointers. No decision trees, env dumps, or change history.

**CONTEXT.md.** Term, definition, `_Avoid_` list. One or two sentences each. Define what the thing is, not what it does. No implementation. One context at the repo root, or a `CONTEXT-MAP.md` that points at several. Follow `CONTEXT-FORMAT.md` from the `domain-modeling` companion when you add or sharpen a term.

**docs/architecture.md.** Sections follow the reader questions in [DIAGRAM-CATALOG.md](DIAGRAM-CATALOG.md). Diagrams sit next to the prose that explains them. Point to ADRs for why and to product READMEs for how to run. The last section is "Where new code goes".

**Where new code goes.** A table or list. Each entry has the kind of change (a new endpoint, a new store, a new job, a new variant of an existing extension point), the directory it lands in, one existing file that already follows the pattern, and what enforces it: a lint rule, a package boundary, a CI check, or the words "convention only". No entry without an existing example. Do not describe a pattern the repo has not used yet. Use `codebase-design` vocabulary for modules and seams.

**docs/adr/.** Sequential `0001-slug.md`. A paragraph is enough. Considered options and consequences only when they add information. Follow `ADR-FORMAT.md` from the `domain-modeling` companion.

**Product README.** Setup, env, commands, owned schema. Intro line: this product is part of the system; read CONTEXT and architecture first.

**Deploy notes.** Projects, databases, secrets by name, migrate, cron. No domain lecture.

**Ops report.** Dated aggregate counts. No secrets or personal data. Do not copy those counts into architecture.

## Bans

- How-to-run steps in architecture
- Schemas, routes, or table names in CONTEXT
- Boxes on a diagram for components that do not exist
- Work the code does not do, in any doc layer. It goes in the report
- Treating a plan checkbox as a deployed fact
- Counts copied out of an ops report into architecture
