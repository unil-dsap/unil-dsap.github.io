import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

history = pd.read_csv("history.csv", index_col="Date")
returns = history.pct_change().dropna() * 100   # in %
X = returns[["VOO", "MSFT"]]
y = (returns["AAPL"] < -2).astype(int)
train = returns.index < "2025-11-17"
test = ~train

models = {
    "one deep tree": DecisionTreeClassifier(
        criterion="entropy", random_state=0),
    "100 bagged trees": BaggingClassifier(
        DecisionTreeClassifier(criterion="entropy"),
        n_estimators=100, random_state=0),
    "random forest": RandomForestClassifier(
        n_estimators=300, min_samples_leaf=5, random_state=0),
}
for name in models:
    m = models[name].fit(X[train], y[train])
    p = m.predict_proba(X[test])[:, 1]
    auc = roc_auc_score(y[test], p)
    print(name, "test AUC:", round(auc, 3))
