---
name: capture-architecture
description: 'Write or refresh architecture docs from live code. Builds a README-first reading path, a domain glossary, current-state diagrams, ADRs that pass a gate, and a "where new code goes" section. Refreshes incrementally from the last captured commit when a stamp exists. Use when a repo has no architecture docs, when docs drifted from code, or on a periodic docs refresh.'
disable-model-invocation: true
---

# Capture Architecture

Read the code, then write or refresh the docs so a first-time reader can follow them. Docs describe the current state. Every claim points at a file and a symbol. Plans are history until code confirms them.

## Modes

- **Create**: the repo has no architecture reading path. Read everything.
- **Full refresh**: docs exist, but there is no stamp or the stamp is unusable. Read everything, then diff against the docs.
- **Incremental refresh**: docs exist and carry a usable stamp. Read what changed since that commit. Rules in [REFRESH.md](REFRESH.md).

Refresh is the common case. Never wipe working docs. Diff, then edit.

## Companions

Skills sit as siblings after install (`.agents/skills/<name>/`; in this repository, `skills/engineering/` and `skills/productivity/`).

- **domain-modeling** when a glossary term or ADR needs writing (`CONTEXT-FORMAT.md`, `ADR-FORMAT.md`)
- **codebase-design** when "where new code goes" needs module and seam vocabulary
- **unslop** on every sentence you write to a `*.md` file
- **grilling** when the user wants to stress-test the picture first

If a companion is missing, do that slice with the rules in this folder and say so in the report. Do not clone another repository to fetch it.

## Process

Copy this checklist and keep it current:

```
- [ ] Scope
- [ ] Inventory
- [ ] Claims
- [ ] Diff docs
- [ ] Write
- [ ] Verify and report
```

### Scope

Pick the mode with the stamp rules in [REFRESH.md](REFRESH.md). Tell the user which mode you are in before you read code.

### Inventory

Docs are cheap. Read all of them, in every mode:

- Root `README.md`, `CONTEXT.md` or `CONTEXT-MAP.md`, everything under `docs/`
- Every product or package README
- ADRs, deploy notes, contributing guides
- Agent plans (`.cursor/plans`, `docs/plans`, work logs)

Code is the expensive part. In Create and Full refresh, read the files that prove each category in [CLAIMS.md](CLAIMS.md): contracts, schemas, entry points, handlers, workers, boundary configs, deploy config, test setup. In Incremental refresh, read only what REFRESH.md scopes.

Plans are suspect history. A later plan can reverse an earlier one.

### Claims

Before you edit any doc, write a claim list from code. One claim per line, with the file and symbol that proves it. Categories and the evidence to look for are in [CLAIMS.md](CLAIMS.md).

When two sources disagree, the ranking in [DOC-LAYERS.md](DOC-LAYERS.md) decides. `CONTEXT.md` is vocabulary, not behavior. Use its terms in every claim. If you cannot name the symbol, drop the claim or record it as an unknown for the report.

### Diff docs

Compare the claim list to the existing docs. Record each finding as:

- **Stale**: docs say it, code does not
- **Missing**: code does it, docs do not
- **Wrong layer**: true, but in the wrong file
- **Superseded plan**: a plan still describes an older topology

Edit only after this list exists.

### Write

Each fact lives in one layer. The layer table and what belongs where are in [DOC-LAYERS.md](DOC-LAYERS.md). Create a missing layer only when you have something to put in it.

Edit order: glossary terms, `docs/architecture.md`, ADRs that pass the gate, root README overview, docs index, product `## See also` blocks.

ADR gate: hard to reverse, surprising without context, and a real trade-off. Skip the ADR if any of the three is missing. Use the domain-modeling format.

Diagrams answer one reader question each and map every node and edge to a claim. Default set in [DIAGRAM-CATALOG.md](DIAGRAM-CATALOG.md). The root README gets one thin overview. Architecture gets the rest.

"Where new code goes" closes `docs/architecture.md`. Every entry names an existing file that already follows the pattern, and the check that enforces it or the words "convention only". Rules in DOC-LAYERS.md.

Reading path: state the reading order in the root README and in `docs/README.md` if that hub exists. Every leaf ends with `## See also`: up to README or architecture, sideways to peers, down only when the reader needs depth. Relative links only. Sentence-case headings.

Run unslop on every paragraph you add or rewrite. Write the stamp last. The format is in REFRESH.md.

### Verify and report

Walk the path as a first-time reader. Spot-check each diagram against one symbol. Run the link checker from this skill directory:

```sh
python3 -B scripts/check-markdown-links.py --root <repo-root>
```

`-B` is PYTHONDONTWRITEBYTECODE. Same check, no `__pycache__` next to the script. The verify step must not leave skill-directory artifacts.

Fix every broken path and fragment, then run the checks in [DRIFT-CHECKS.md](DRIFT-CHECKS.md). Do not commit unless asked. Report:

- **Mode**: for incremental, the commit range and file count; for a forced full refresh, the rule that forced it
- **Files** added or changed
- **Contradictions**: claims that disagreed with docs, and which source won
- **ADRs** written or declined, with the gate result
- **Companions** loaded, and any missing
- **Checks**: link-check and drift-check results
- **Unknowns**: claims you could not prove
- **Not built**: work the code does not do. It stays in this report and appears in no doc
