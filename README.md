# WeTek skills

Reusable agent skills for WeTek repositories. This catalog starts with one
engineering skill and can grow. Skills are ordinary Markdown directories that
any coding agent can load.

## Capture architecture

`capture-architecture` reconstructs or refreshes system documentation from
live code. It writes a README-first reading path, current-state architecture
diagrams, a domain glossary, ADRs only when they earn their keep, and a
deferred-work page. Use it to create those files from scratch, or to run
periodically so `docs/` and related `*.md` files match the codebase.

Source: [skills/engineering/capture-architecture](skills/engineering/capture-architecture)

## Install

[skills.sh](https://skills.sh) copies selected skill directories into the
project. From the target repository:

```sh
npx skills@latest add wetek/skills --skill=capture-architecture
```

Update later with:

```sh
npx skills@latest update capture-architecture
```

Install only the skills you need. This command does not replace other skills
already in the repository.

## Companion skills

`capture-architecture` is standalone. If these skills from
[mattpocock/skills](https://github.com/mattpocock/skills) are already
installed, it may hand glossary, ADR, or module-seam work to them:

```sh
npx skills@latest add mattpocock/skills --skill=domain-modeling
npx skills@latest add mattpocock/skills --skill=codebase-design
```

Do not install those companions again in a repo that already has them.

## License

[MIT](LICENSE)
