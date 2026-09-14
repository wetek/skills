# Drift Checks

Run these after every capture. Fail closed on broken links.

## Link check

From this skill directory, with `--root` set to the repository being documented:

```sh
python3 scripts/check-markdown-links.py --root <repo-root>
```

The script resolves relative Markdown targets and GitHub-style heading fragments. It ignores `http`, `https`, and `mailto` links. A missing file or unknown fragment is a failure.

After a heading rename, grep the old slug before you rely on the script. A hand-written `#whats-next` will not match `What runs where`.

## Stamp

Grep the repo for `capture-architecture: commit`. Exactly one line must match, in `docs/architecture.md` or, failing that, the root README. Two matches mean a capture appended instead of replacing.

On that line:

- The sha is 40 hex characters and `git cat-file -e <sha>` succeeds
- The sha equals `git rev-parse HEAD` at the time you wrote it
- The date is today in `YYYY-MM-DD`
- The depth is `full` or `incremental`

## Code to docs

Build a matrix for this repo. Typical rows:

| Claim | Doc location | Code symbol |
| --- | --- | --- |
| Legal states | state diagram | enum or transition map |
| Who may write the system of record | architecture paragraph | auth guard and handler |
| Module dependency direction | dependency diagram | lint rule or package manifest |
| Public vs guarded routes | trust boundary diagram | router and middleware |
| Where new code goes | closing table | the example file named in each row |
| Deploy secrets and cron | deploy notes | deploy config |

If a cell disagrees, the ranking in [DOC-LAYERS.md](DOC-LAYERS.md) decides.

Every "where new code goes" row must name a file that exists. Open each one.

## Phrase traps

Grep and delete or rewrite:

- topology the code already left behind
- a retired service described as the live path
- plan language presented as current topology
- CONTEXT `_Avoid_` terms used as primary names
- future tense about components ("will handle", "is planned to")

## Plan supersession

If a plan still describes an older topology, say so in the report. Do not promote the plan into architecture. Do not edit the plan unless the user asked.

## Vocabulary

Primary terms in diagrams and headings must exist in CONTEXT, or CONTEXT must gain them in the same pass. Use the `domain-modeling` companion when you add a term.
