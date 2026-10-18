# Session 6 demo — real data, real errors

| File | Role |
|---|---|
| ledger.csv | the input, with one bad row on purpose (MSFT has no shares) |
| report.py | pinned on the left: load → check → compute → write, by hand |
| frame.py | the same with pandas (read_csv, NaN, dropna, to_csv) |
| report.txt, report.csv | the files the two scripts write |

The deck is generated: edit `../slides.src.md`, then rebuild from the repo root with

    uv run --python 3.12 --with pyyaml --with pygments --with numpy --with pandas python tools/codewalk/build.py content/weeks/week-06/slides.src.md

Every output on the slides comes from a real run; errors and variants are
these scripts with lines changed on that slide only (`edit:` in
`slides.src.md`). Do not edit `slides.md` by hand.
