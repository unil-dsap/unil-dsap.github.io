# Session 4 demo — functions, methods and modules

| File | Role |
|---|---|
| portfolio.py | the script pinned on the left: session 3's ledger, organised into functions |
| objects.py | Part 7 of the lecture: lists, numpy arrays and pandas DataFrames as objects of classes |
| positions.py | our own class `Position`: constructor, attributes, a method, two instances |

The deck is generated: edit `../slides.src.md`, then rebuild from the repo root with

    uv run --python 3.12 --with pyyaml --with pygments --with numpy --with pandas python tools/codewalk/build.py content/weeks/week-04/slides.src.md

Every output on the slides comes from a real run; the errors are
`portfolio.py` with one or two lines changed on that slide only (`edit:` in
`slides.src.md`). Do not edit `slides.md` by hand.
