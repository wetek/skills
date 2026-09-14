# Refresh

Refresh has two depths. Full reads the whole codebase. Incremental reads only what changed since the last capture. The stamp decides.

## Stamp

Every capture leaves one line in `docs/architecture.md`, directly under the title:

```
<!-- capture-architecture: commit <full sha> date <YYYY-MM-DD> depth <full|incremental> -->
```

If the capture wrote no `docs/architecture.md`, put the line under the overview diagram in the root README instead.

Write the stamp last. Replace the old line, never append a second one. Use `git rev-parse HEAD` for the sha and today's date.

The stamp records HEAD, not the working tree. Uncommitted changes you document now show up again in the next diff. That is expected.

## Depth rules

Read the stamp before you read code. Then pick:

- **No stamp**: full.
- **Sha not an ancestor**: `git merge-base --is-ancestor <sha> HEAD` fails (rebase, squash, force-push, or a different history). Full. Say so in the report.
- **Large diff**: `git diff --name-only <sha> | wc -l` is more than a third of `git ls-files | wc -l`. Full.
- **Topology moved**: the diff adds, removes, or renames a product or package directory. Full.
- **Otherwise**: incremental.

## Incremental read scope

Read all docs as usual. For code, read only:

- `git log --oneline <sha>..HEAD`, for the intent behind the changes
- Every file in `git diff --name-only <sha>`, the whole file, not the hunk
- Every contract, schema, or enum that a changed file imports

Do not open other code files during inventory. The next section checks them by symbol.

## Re-verify existing claims

The existing docs already hold claims. Turn every diagram node, diagram edge, and architecture paragraph into a claim and find its file and symbol. Check that each symbol still resolves, with grep or by opening the file, even when the diff did not touch that file. A deleted caller or a renamed enum value elsewhere can strand a claim in an untouched file.

Then add new claims from the changed files, using the categories in [CLAIMS.md](CLAIMS.md).

If an existing claim's evidence cannot be found again, read that product or package at full depth before you move on. Do not drop a claim on the strength of the diff alone. List every claim that failed re-verification in the report, with the file that used to hold it.
