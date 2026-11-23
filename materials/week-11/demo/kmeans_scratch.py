import numpy as np
import pandas as pd

returns = pd.read_csv("universe.csv", index_col="Date")
market = returns["VOO"]
stocks = returns.drop(columns=["VOO", "GME"])
beta = stocks.corrwith(market) * stocks.std() / market.std()
X = np.column_stack([beta, stocks.std()])
Z = (X - X.mean(axis=0)) / X.std(axis=0)

rng = np.random.default_rng(0)
centres = Z[rng.choice(len(Z), size=5, replace=False)]
for step in range(1, 11):
    d = ((Z[:, None] - centres[None]) ** 2).sum(axis=2)
    group = d.argmin(axis=1)               # 1. nearest centre
    J = d.min(axis=1).sum()                # distortion
    for g in range(5):                     # 2. move centres
        centres[g] = Z[group == g].mean(axis=0)
    print("step", step, " J =", round(J, 2))
