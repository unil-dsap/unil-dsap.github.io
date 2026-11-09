# Session 9 demo — fitting a line

| File | Role |
|---|---|
| make_prices.py | writes prices.csv (one year, simulated, seed 2026; the last row matches the ledger) and prices_typo.csv (one AAPL price with the decimal point moved) |
| prices.csv, prices_typo.csv | the data |
| beta.py | pinned on the left: returns, mean, sd, correlation, least-squares beta, R² |
| descent.py | the same line by gradient descent (all days per step) |
| sgd.py | mini-batch gradient descent (20 random days per step) |
| plot_first.py, anscombe.csv, datasaurus.csv | same statistics, different pictures (Anscombe 1973; Datasaurus Dozen, Matejka & Fitzmaurice 2017, from the datasauRus R package) |
| multi.py | AAPL on MSFT, on VOO, on both (scikit-learn) |
| onehot.py | weekday dummies with pd.get_dummies |
| overfit.py | train on 200 days, test on 49: polynomial degrees 0, 1, 3, 8, 15 |
| fig/*.svg | the figures, drawn by ../verify/figures.py |


The deck is generated: edit `../slides.src.md`, then rebuild from the repo root with

    uv run --python 3.12 --with numpy --with pandas --with matplotlib python content/weeks/week-09/verify/figures.py
    uv run --python 3.12 --with pyyaml --with pygments --with numpy --with pandas --with scikit-learn python tools/codewalk/build.py content/weeks/week-09/slides.src.md

Math slides (`<!-- math -->`) take every number from `../verify/values.py`
through `{{name}}` placeholders; code slides run the scripts. Do not edit
`slides.md` by hand.
