import numpy as np
import pandas as pd

returns = pd.read_csv("universe.csv", index_col="Date")
market = returns["VOO"]
stocks = returns.drop(columns="VOO")
resid = pd.DataFrame(index=stocks.index)  # minus the market
for t in stocks.columns:
    beta = stocks[t].cov(market) / market.var()   # session 9
    resid[t] = stocks[t] - beta * market
D = 1 - resid.corr()                      # distance table

def closest_pair(groups):
    """Closest pair of groups, by average linkage."""
    best = (np.inf, 0, 0)
    for i in range(len(groups)):
        for j in range(i + 1, len(groups)):
            block = D.loc[groups[i], groups[j]]   # all pairs
            d = block.to_numpy().mean()
            if d < best[0]:
                best = (d, i, j)
    return best

cut = 0.9                     # the dendrogram's dashed line
groups = [[t] for t in stocks.columns]   # one per stock
d, i, j = closest_pair(groups)
while d < cut:                # below the cut: merge
    groups[i] = groups[i] + groups[j]
    del groups[j]
    d, i, j = closest_pair(groups)

print(len(groups), "groups at cut", cut)
for g in groups:
    print(" ".join(g))
