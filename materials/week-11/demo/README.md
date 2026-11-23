# Session 11 demo — learning without labels

| File | Role |
|---|---|
| make_universe.py | writes universe.csv: 34 simulated stocks in five sectors (plus GME) on the market of history.csv |
| history.csv, universe.csv | the data |
| cluster.py | pinned on the left: beta and volatility per stock, k-means with 5 groups |
| kmeans_scratch.py | k-means by hand |
| em_scratch.py | a Gaussian mixture on volatility, fitted by EM by hand |
| hier_scratch.py | hierarchical clustering (average linkage) by hand, on correlations of returns minus the market |
| dbscan.py | DBSCAN with three radii |
| pca_scratch.py | principal components by hand (eigenvectors), checked against scikit-learn |
| regimes.py | "spot the lie": k-means finds four regimes in one cloud of days |
| fig/*.svg | the figures, drawn by ../verify/figures.py |

Rebuild from the repo root:

    uv run --python 3.12 --with numpy --with pandas --with matplotlib --with scikit-learn --with scipy python content/weeks/week-11/verify/figures.py
    uv run --python 3.12 --with pyyaml --with pygments --with numpy --with pandas --with scikit-learn python tools/codewalk/build.py content/weeks/week-11/slides.src.md
