# Session 5 demo — reading data code

| File | Role |
|---|---|
| prices.py | Parts 1–3, pinned on the left: nested data, comprehensions, lambda |
| arrays.py | Part 4: numpy 2-D arrays, indexing, slicing, axis, broadcasting, masks |
| tables.py | Part 5: pandas DataFrame, loc/iloc, filters, apply, groupby |

The deck is generated: edit `../slides.src.md`, then rebuild from the repo root with

    uv run --python 3.12 --with pyyaml --with pygments --with numpy --with pandas python tools/codewalk/build.py content/weeks/week-05/slides.src.md

Every output on the slides comes from a real run; variants and errors are
these scripts with lines changed on that slide only (`edit:` in
`slides.src.md`). Do not edit `slides.md` by hand.
