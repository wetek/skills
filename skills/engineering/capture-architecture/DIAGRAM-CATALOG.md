# Diagram Catalog

Ask a reader question, then pick the smallest diagram that answers it. One concern per figure. Labels use CONTEXT terms.

## Default set

| Reader question | Kind | Put it in |
| --- | --- | --- |
| What is the whole system, in one glance? | `flowchart LR` | root README |
| Who talks to whom, including external services? | `flowchart LR` | architecture |
| Where does data live, and who may write it? | `flowchart TB` | architecture |
| What happens on the main write path? | `sequenceDiagram` | architecture |
| Which modules may depend on which? | `flowchart TD` | architecture |
| How does a request cross the trust boundary? | `flowchart TD` | architecture |
| What states are legal? | `stateDiagram-v2` | architecture |
| What runs where? | `flowchart TB` | architecture |

Skip any row that has nothing to show in this repo. A table beats a diagram when the set is a small closed enum.

## Rules

- Map every node and edge to a claim from [CLAIMS.md](CLAIMS.md).
- Prefer `flowchart`, `sequenceDiagram`, and `stateDiagram-v2`.
- Keep node IDs free of spaces. Quote labels that contain punctuation.
- Name sections by the reader question, not "Context" or "Containers".
- Do not draw a payload, database, queue, or service that does not exist.
- Do not restyle nodes with colors. The renderer picks the theme.

## Anti-patterns

- One diagram that mixes actors, tables, and deploy targets
- Edges with no verb
- A second overview that repeats the README figure
- A box added so the picture looks complete
