# Session 3 demo — the whole ledger: lists, a dict, loops

| File | Role |
|---|---|
| ledger.py | the script pinned on the left of the lecture slides |
| ledger_np.py | the same ledger with numpy and pandas (Part 6 of the lecture) |
| slices.py | slicing six kinds of objects (the slicing warning slide) |

The deck is generated: edit `../slides.src.md`, then rebuild from the repo root with

    uv run --python 3.12 --with pyyaml --with pygments --with numpy --with pandas python tools/codewalk/build.py content/weeks/week-03/slides.src.md

(numpy and pandas are needed because the build runs `ledger_np.py`.) Every
output on the slides comes from a real run. Do not edit `slides.md` by hand.
