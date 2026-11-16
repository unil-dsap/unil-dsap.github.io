import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score

history = pd.read_csv("history.csv", index_col="Date")
returns = history.pct_change().dropna() * 100   # in %
X = returns[["VOO", "MSFT"]].to_numpy()
y = (returns["AAPL"] < -2).astype(int).to_numpy()
train = returns.index < "2025-11-17"
X_tr, y_tr = X[train], y[train]
X_te, y_te = X[~train], y[~train]

rng = np.random.default_rng(0)
total = np.zeros(len(y_te))
for b in range(100):
    rows = rng.choice(len(y_tr), size=len(y_tr))  # bootstrap
    tree = DecisionTreeClassifier(criterion="entropy",
                                  random_state=b)
    tree.fit(X_tr[rows], y_tr[rows])
    total = total + tree.predict_proba(X_te)[:, 1]
    if b == 0:
        auc = roc_auc_score(y_te, total)
        print("1 tree,    test AUC:", round(auc, 3))
p = total / 100                        # the average vote
auc = roc_auc_score(y_te, p)
print("100 trees, test AUC:", round(auc, 3))
