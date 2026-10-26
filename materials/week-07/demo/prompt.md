# The live AI moment — session 7

The planted lie: an assistant changes more than it was asked to, and
`git diff` shows it.

Setup: the `dsap` folder at commit `cd81ebf` (session 6), working tree
clean. Show `git status` first — "nothing to commit" — so the room sees
the starting point.

Ask a harness, verbatim:

> Round the report totals to two decimals.

Then, before anything else:

1. `git status --short` — which files did it touch?
2. `git diff` — read every `-` and `+` line out loud.
3. `python ledger.py` and `cat report.txt` — compare with the last commit.
4. Keep or throw away: `git restore ledger.py` (↶ Discard Changes).

Fallback (and the slides): the staged edit `S6_MODEL_EDIT` in
`ledger_history.py`; its diff and both reports are in `transcript.txt`.
