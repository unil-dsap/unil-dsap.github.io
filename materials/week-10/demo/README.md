# Session 10 demo — classification: bad days

| File | Role |
|---|---|
| make_history.py | writes history.csv: five years; the last is session 9's prices.csv, the four before simulated the same way (seed 2025) |
| history.csv | the data; train on 2022-01 to 2025-11-14, test on session 9's year |
| classify.py | pinned on the left: logistic regression on VOO and MSFT, threshold 0.2, confusion matrix |
| knn.py | k-nearest neighbours, k = 1, 5, 15, 51, 151, standardised on the training years |
| logit_gd.py | logistic regression by gradient descent, checked against scikit-learn |
| entropy.py | entropy and information gain of four cut-offs |
| tree.py | a depth-2 tree as text; train and test AUC by depth |
| forest.py | one deep tree, bagging, random forest |
| knn_scratch.py | k-nearest neighbours from scratch (numpy), same result as scikit-learn |
| tree_scratch.py | a depth-2 tree from scratch: entropy, best split, two levels |
| metrics_scratch.py | recall, precision, and AUC by counting every pair of bad and normal days |
| bagging_scratch.py | bagging from scratch: 100 trees on bootstrap samples, averaged |
| tomorrow.py | predicting tomorrow's bad day (the honest version of "spot the lie") |
| fig/*.svg | the figures, drawn by ../verify/figures.py |

Rebuild from the repo root:

    uv run --python 3.12 --with numpy --with pandas --with matplotlib --with scikit-learn python content/weeks/week-10/verify/figures.py
    uv run --python 3.12 --with pyyaml --with pygments --with numpy --with pandas --with scikit-learn python tools/codewalk/build.py content/weeks/week-10/slides.src.md
