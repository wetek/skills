---
name: reflect-and-learn
description: 'Reflect on the current session transcript to capture lessons from mistakes, user corrections, recurring friction, or newly discovered repository patterns. Use at the end of a non-trivial session, after fixing a tricky bug, after user feedback/corrections, or when the user asks to reflect or update agent instructions/skills.'
---

# Reflect and Learn

Turn session friction and discoveries into durable repository memory so future agents (OpenCode, Claude Code, Cursor) do not repeat the same mistakes.

## When to run

Trigger or offer this workflow when any of these happen in a session:

1. **User correction**: The user corrected an assumption, convention, command, or architectural boundary.
2. **Repeated failure / debugging loop**: A build, test, migration, or deployment failed because of a non-obvious repository quirk.
3. **New pattern or boundary**: A new module seam, scraper adapter pattern, or shared contract was introduced.
4. **Explicit request**: The user asks to reflect on the session, update `AGENTS.md`, or extract a new skill.

## Process

```
- [ ] Review session transcript
- [ ] Classify findings by destination layer
- [ ] Propose concise diffs to the user
- [ ] Apply approved updates and run unslop
```

### 1. Review session transcript

Scan the conversation history for:
- Commands that failed before the right invocation was found
- **Context bloat**: Commands or scripts (like `prettier`, `knip`, test runners, or `curl`/`gcloud` dumps) that printed dozens of unnecessary lines into the context window instead of using `--log-level warn`, `--quiet`, or targeted `jq` filters
- **Slow execution**: Shell commands, builds, or CI/CD steps that took longer than necessary and could be parallelized, cached, or scoped
- Wrong file paths, imports, or layer violations that had to be reworked
- Domain terms that were misused or newly coined
- Multi-step workflows that worked well and will be repeated by teammates

### 2. Classify findings by destination layer

Never dump everything into `AGENTS.md`. Put each lesson in the layer that owns it:

| Finding type | Target file | Rule |
| --- | --- | --- |
| Repo-wide coding rule, command, layout rule, or guardrail | `AGENTS.md` | Keep to 1-2 crisp sentences. Do not duplicate architecture docs. |
| New or sharpened domain term | `CONTEXT.md` | Use `domain-modeling` format (`**Term**: definition` + `_Avoid_`). |
| Changed system topology, data flow, or "where new code goes" | `docs/architecture.md` | Use `capture-architecture` rules; cite the file and symbol. |
| Expensive, hard-to-reverse technical decision | `docs/adr/NNNN-slug.md` | Must pass the ADR gate (hard to reverse, surprising, real trade-off). |
| Reusable multi-step workflow or specialized playbook | `.agents/skills/<skill-name>/SKILL.md` | Create or update a skill directory and symlink it in `.claude/skills/`. |

### 3. Propose before editing (unless asked to edit directly)

Present a short summary to the user:
- **What happened**: One sentence on the mistake, correction, or pattern.
- **Proposed change**: Which file (`AGENTS.md`, `CONTEXT.md`, or `.agents/skills/<name>/SKILL.md`) and the exact rule or skill update.
- Ask: *"Would you like me to apply these updates to the agent instructions / skills?"*

### 4. Apply and verify

- Keep `AGENTS.md` tight and scannable. Remove or merge outdated rules when adding new ones.
- When creating a new skill under `.agents/skills/<name>/SKILL.md`, also create the relative symlink `.claude/skills/<name> -> ../../.agents/skills/<name>` so OpenCode, Cursor, and Claude Code all discover it.
- Run the `unslop` pass on every sentence added to Markdown files.
