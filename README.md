# WeTek skills

Reusable agent skills for WeTek repositories. Skills are ordinary Markdown
directories that any coding agent can load.

This catalog is a snapshot you can install in one step. Skill files inside
this repository point at each other by name. They do not link out to the
projects the copies came from.

## Install

[skills.sh](https://skills.sh) copies selected skill directories into the
project. From the target repository:

```sh
npx skills@latest add wetek/skills
```

Install one skill:

```sh
npx skills@latest add wetek/skills --skill=capture-architecture
```

Update later with:

```sh
npx skills@latest update
```

Install only the skills you need. This command does not replace other
skills already in the repository.

`capture-architecture` expects `domain-modeling`, `codebase-design`, and
`unslop` to sit next to it after install. Install those three with it, or
install the whole catalog.

## Skills

### Engineering

- [capture-architecture](skills/engineering/capture-architecture/SKILL.md): write or refresh architecture docs from live code, incrementally after the first run
- [code-review](skills/engineering/code-review/SKILL.md): review a diff on standards and spec in parallel
- [codebase-design](skills/engineering/codebase-design/SKILL.md): deep modules, seams, and testable interfaces
- [diagnosing-bugs](skills/engineering/diagnosing-bugs/SKILL.md): diagnosis loop for hard bugs
- [domain-modeling](skills/engineering/domain-modeling/SKILL.md): glossary and ADRs
- [grill-with-docs](skills/engineering/grill-with-docs/SKILL.md): grill a plan while writing CONTEXT and ADRs
- [to-spec](skills/engineering/to-spec/SKILL.md): turn the current conversation into a spec
- [unslop](skills/engineering/unslop/SKILL.md): cut AI tells from writing

### Productivity

- [grill-me](skills/productivity/grill-me/SKILL.md): start a grilling session
- [grilling](skills/productivity/grilling/SKILL.md): interview until the design tree is empty
- [handoff](skills/productivity/handoff/SKILL.md): compact the conversation for the next agent

## Origins

These lines are the only origin notes in this repository.

- `capture-architecture` is a WeTek skill. It was written from a live
  documentation capture, then generalized.
- `code-review`, `codebase-design`, `diagnosing-bugs`, `domain-modeling`,
  `grill-with-docs`, `to-spec`, `grill-me`, `grilling`, and `handoff` are
  snapshots of [mattpocock/skills](https://github.com/mattpocock/skills).
- `unslop` is a snapshot of
  [backnotprop/pstack](https://github.com/backnotprop/pstack)
  (`skills/unslop`).

We keep copies here so a WeTek repo can install one catalog and stay on
those copies. Refresh a snapshot by copying the upstream skill directory
into this repository. Do not point skill files at the upstream trees.

## License

[MIT](LICENSE)
