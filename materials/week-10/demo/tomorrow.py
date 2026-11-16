import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

history = pd.read_csv("history.csv", index_col="Date")
returns = history.pct_change().dropna() * 100   # in %
bad = (returns["AAPL"] < -2).astype(int)

data = pd.DataFrame({"today_VOO": returns["VOO"],
                     "tomorrow_bad": bad.shift(-1)}).dropna()
X = data[["today_VOO"]]
y = data["tomorrow_bad"].astype(int)
train = data.index < "2025-11-17"
test = ~train

model = LogisticRegression().fit(X[train], y[train])
p = model.predict_proba(X[test])[:, 1]
print("test days:", test.sum(), " bad:", y[test].sum())
print("test AUC:", round(roc_auc_score(y[test], p), 3))
