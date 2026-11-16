import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import roc_auc_score

history = pd.read_csv("history.csv", index_col="Date")
returns = history.pct_change().dropna() * 100   # in %
X = returns[["VOO", "MSFT"]]
y = (returns["AAPL"] < -2).astype(int)
train = returns.index < "2025-11-17"
test = ~train

small = DecisionTreeClassifier(criterion="entropy", max_depth=2)
small.fit(X[train], y[train])
print(export_text(small, feature_names=["VOO", "MSFT"],
                  show_weights=True))

print("depth, train AUC, test AUC")
for depth in [1, 2, 3, 5, 10, None]:
    tree = DecisionTreeClassifier(criterion="entropy",
                                  max_depth=depth,
                                  random_state=0)
    tree.fit(X[train], y[train])
    p_train = tree.predict_proba(X[train])[:, 1]
    p_test = tree.predict_proba(X[test])[:, 1]
    print(depth, round(roc_auc_score(y[train], p_train), 3),
          round(roc_auc_score(y[test], p_test), 3))
