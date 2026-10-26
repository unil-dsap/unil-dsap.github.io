# Session 7 demo — git from zero, and the review

Build the deck (from the repository root):

    uv run --python 3.12 --with pyyaml --with pygments --with numpy --with pandas \
      python tools/codewalk/build.py content/weeks/week-07/slides.src.md

Edit `slides.src.md`, never `slides.md` (generated).

## Part 1 · Git

| File | Role |
|---|---|
| ledger_history.py | builds a ledger repository on a fresh "machine" (no git identity), one commit per session, pushes to a stand-in "GitHub", clones to a "laptop", ends with a rejected push; records every command and its real output |
| transcript.txt | that record. Every `<!-- term -->` block in the deck is checked against it at build time |
| prompt.md | the ask for the planted lie (the agent that changes `>=` to `>`) |
| fig/ | `idea-*` pictures; `vscode-*` stylized VS Code (Light Modern); `agent-*` a generic agent panel; `term-diff.svg` is generated from transcript.txt |

Hashes are fixed: author, dates and config are pinned, so `916acb4 … cd81ebf … 11573a5 … 18a82e7` are the same on every machine. The script stops with `HASH CHANGED` if the history changes; then update the slides, the figures in `fig/`, and `EXPECTED` in the script.

The git demo's ledger code (`S1` … `S6` in ledger_history.py) is its own small story (a fee rule, a UBSG row) for the git part. It is not the code of sessions 2–6.

VS Code views are drawings, not screenshots. Button labels and messages follow current VS Code wording; check them against Nuvolos before the lecture.

## Part 2 · Review

The review pins each session's own script: `../week-02/demo/position.py`, `../week-03/demo/ledger.py`, `../week-04/demo/portfolio.py`, `../week-05/demo/prices.py`, `arrays.py`, `tables.py`, `../week-06/demo/report.py`. Every output is a real run at build time.

| File | Role |
|---|---|
| growth.py | session 2's position.py with its planted lie (line 16) — item 2 |
| order.py | an office-supplies order with one planted lie (line 7) — item 3 |
| regions.py | sales totals by region, read as a whole program — item 11 |

They are copies so that the question slide does not mark the changed line.
