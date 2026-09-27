# Session 2 demo — one position, every line explained

| File | Role |
|---|---|
| position.py | the script pinned on the left of every lecture slide |

The deck is generated: edit `../slides.src.md`, then rebuild with

    uv run --python 3.12 --with pyyaml --with pygments python tools/codewalk/build.py content/weeks/week-02/slides.src.md

(from the repo root). The build runs `position.py` and every
```` ```python run ```` block on the slides, so every output shown is from a
real run. Do not edit `slides.md` by hand.

The crashes and wrong answers on the slides are this script with one or two
lines changed on that slide only (`edit:` in `slides.src.md`); the build runs
each changed copy for real.
