import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

history = pd.read_csv("history.csv", index_col="Date")
returns = history.pct_change().dropna() * 100   # in %
X = returns[["VOO", "MSFT"]]
y = (returns["AAPL"] < -2).astype(int).to_numpy()
train = returns.index < "2025-11-17"
model = LogisticRegression().fit(X[train], y[train])
p = model.predict_proba(X[~train])[:, 1]
y_te = y[~train]

alarm = p > 0.2
tp = (alarm & (y_te == 1)).sum()
fp = (alarm & (y_te == 0)).sum()
fn = (~alarm & (y_te == 1)).sum()
print("recall:", round(tp / (tp + fn), 3),
      " precision:", round(tp / (tp + fp), 3))

wins = 0              # AUC: bad day vs normal day, all pairs
for p_bad in p[y_te == 1]:
    for p_normal in p[y_te == 0]:
        wins = wins + (p_bad > p_normal)
pairs = (y_te == 1).sum() * (y_te == 0).sum()
print("AUC, counting pairs:", round(wins / pairs, 3))
auc = roc_auc_score(y_te, p)
print("AUC, scikit-learn:  ", round(auc, 3))
