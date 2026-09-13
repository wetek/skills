---
name: capture-architecture
description: >-
  Capture or refresh system architecture documentation from live code.
  Builds a README-first reading path, current-state diagrams, a domain
  glossary, ADRs when they earn their keep, and a deferred-work page.
  Use when creating architecture docs from scratch, updating docs after
  the codebase changed, reconciling docs with ingestion or deployment,
  or running a periodic docs refresh.
disable-model-invocation: true
---

# Capture architecture

Reconstruct how the system works from code, then write or refresh the docs
so a first-time GitHub reader can follow them. Narrative never invents
behavior. Plans are history until code confirms them.

If [domain-modeling](https://github.com/mattpocock/skills/tree/main/skills/engineering/domain-modeling)
is installed, use it when a glossary term or ADR must be invented or
sharpened. If
[codebase-design](https://github.com/mattpocock/skills/tree/main/skills/engineering/codebase-design)
is installed, use its module and seam vocabulary inside a product. This
skill stays on system topology, write paths, and the reading path.

## Mode

**Create** when the repo has no architecture reading path.
**Refresh** when `README.md`, `docs/`, or product READMEs already exist.
Refresh is the common case. Do not wipe working docs. Diff claims against
them, then edit.

Copy this checklist and keep it current:

```
- [ ] Inventory
- [ ] Rank sources
- [ ] List claims
- [ ] Diff docs
- [ ] Edit layers
- [ ] Draw diagrams
- [ ] Link the path
- [ ] Verify
- [ ] Report
```

## 1. Inventory

Read, do not skim:

- Root `README.md`, `CONTEXT.md` or `CONTEXT-MAP.md`, everything under `docs/`
- Every product or package README
- ADRs, skipped-work or deferred pages, deploy notes, import or ops reports
- Cursor or agent plans (`.cursor/plans`, `docs/plans`, work logs)
- Live write paths: shared contracts, ingest or sync code, workflow machines,
  seed and delivery commands, schema, deploy config (`vercel.json`,
  Docker Compose, env examples)

Plans are suspect history. A later plan can reverse an earlier one. The
oldest plan is not current architecture.

## 2. Rank sources

On conflict, higher wins:

1. Compiled contracts, schemas, enums, and state machines
2. The write path that mutates the system of record
3. Source delivery (outbox, CLI deliver, seed)
4. Deploy config
5. ADRs (durable intent; if code diverged, fix code or supersede the ADR)
6. Product READMEs (how to run that product)
7. `docs/architecture.md` and the root README (narrative over the above)
8. Plans, work logs, skipped-work pages (historical or deferred)

`CONTEXT.md` is vocabulary, not behavior. Apply it as a filter on every
other layer.

Details: [DOC-LAYERS.md](DOC-LAYERS.md)

## 3. List claims

From code, write a claim list before editing docs:

- Actors and products
- Stores and who may write each one
- Trust boundaries (auth, tokens, public vs private)
- Write paths and their idempotency rules
- Workflows and illegal transitions
- Review or human-decision kinds
- Deployment topology and secrets
- Deferred work the code still does not do

Each claim needs a file and symbol. No claim without evidence.

## 4. Diff docs

Compare the claim list to existing docs. Record:

- Stale (docs say it, code does not)
- Missing (code does it, docs do not)
- Wrong layer (true, but in the wrong file)
- Superseded plans (plan still describes an older topology)

Edit only after this list exists.

## 5. Edit layers

Create a missing layer only when you have something to put in it. Keep
each fact in one place:

| Layer | Job |
| --- | --- |
| Root README | Picture, status, one overview diagram, reading order |
| CONTEXT / CONTEXT-MAP | Words. No schemas, routes, or tables |
| `docs/architecture.md` | How data moves now |
| `docs/adr/` | Why an expensive choice was made |
| Product README | How to run that product |
| Ops report | Dated, PII-free counts or fingerprints |
| Deploy notes | Projects, secrets, migrate, seed, cron |
| Skipped-work page | Noticed and not built. Not current architecture |

ADR gate: hard to reverse, surprising without context, and a real
trade-off. Skip the ADR if any of the three is missing.

Do not keep a "what's left" dump inside architecture. Point at the
skipped-work page.

Edit order: glossary terms if needed, architecture, ADR if warranted,
README overview, docs index, product See also blocks, deploy and ops
pages only if those claims changed, skipped-work for deferred items
removed from architecture.

## 6. Draw diagrams

Few diagrams. One reader question each. Labels use CONTEXT terms.
Map every node and edge to a claim from step 3.

Default set is in [DIAGRAM-CATALOG.md](DIAGRAM-CATALOG.md). Skip a
diagram that has nothing to show. Prefer a table for a small closed
enum. Do not draw future components. Do not use C4 section titles.

Root README gets one thin overview. Architecture gets the rest.

## 7. Link the path

A GitHub reader starts at `README.md`. State the reading order there
and in `docs/README.md` if that hub exists.

Every leaf ends with `## See also`: up to README or architecture,
sideways to peers, down only when the reader needs depth. ADRs link to
the architecture section that shows the decision in motion.

Relative Markdown links only. Sentence-case headings so GitHub fragment
IDs stay predictable. After a heading rename, grep the old slug.

## 8. Verify

Walk the path as a first-time reader. Spot-check each diagram against
one code symbol. Then run the checker from this skill directory:

```sh
python3 scripts/check-markdown-links.py --root <repo-root>
```

Fix every broken relative path and heading fragment before finishing.

More checks: [DRIFT-CHECKS.md](DRIFT-CHECKS.md)

Prose: short sentences, active voice, no em dashes. Do not commit unless
asked.

## 9. Report

When done, say:

- Create or refresh
- Files added or changed
- Claims that contradicted docs, and which source won
- ADRs offered or skipped, with the gate result
- Unknowns still unresolved
- Link-check result
- Remaining work, on the skipped-work page, not presented as current

A worked example from the Wellis capture: [WELLIS-EXAMPLE.md](WELLIS-EXAMPLE.md)
