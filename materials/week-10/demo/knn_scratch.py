import numpy as np
import pandas as pd

history = pd.read_csv("history.csv", index_col="Date")
returns = history.pct_change().dropna() * 100   # in %
X = returns[["VOO", "MSFT"]].to_numpy()
y = (returns["AAPL"] < -2).astype(int).to_numpy()
train = (returns.index < "2025-11-17")
Z = (X - X[train].mean(axis=0)) / X[train].std(axis=0)

def knn_proba(new, Z_train, y_train, k):
    """Share of bad days among the k closest days."""
    d = np.sqrt(((Z_train - new) ** 2).sum(axis=1))
    closest = np.argsort(d)[:k]          # k smallest distances
    return y_train[closest].mean()

p = []
for new in Z[~train]:                    # every test day
    p.append(knn_proba(new, Z[train], y[train], k=15))
p = np.array(p)
alarm = p > 0.2
print("caught:", (alarm & (y[~train] == 1)).sum(), "of",
      y[~train].sum())
print("false alarms:", (alarm & (y[~train] == 0)).sum())
