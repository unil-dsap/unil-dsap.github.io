import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

history = pd.read_csv("history.csv", index_col="Date")
returns = history.pct_change().dropna() * 100   # in %

X = returns[["VOO", "MSFT"]]            # the same day
y = (returns["AAPL"] < -2).astype(int)  # 1 = a bad day

train = returns.index < "2025-11-17"    # four years
test = ~train                           # session 9's year

model = LogisticRegression().fit(X[train], y[train])
p = model.predict_proba(X[test])[:, 1]  # P(bad day)
alarm = p > 0.2

print("test year:", test.sum(), "days,", y[test].sum(), "bad")
print(confusion_matrix(y[test], alarm))
hits = (alarm & (y[test] == 1)).sum()
print("caught:", hits, "of", y[test].sum())
