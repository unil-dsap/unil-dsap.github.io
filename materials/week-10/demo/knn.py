import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

history = pd.read_csv("history.csv", index_col="Date")
returns = history.pct_change().dropna() * 100   # in %
X = returns[["VOO", "MSFT"]]
y = (returns["AAPL"] < -2).astype(int)
train = returns.index < "2025-11-17"
test = ~train

scaler = StandardScaler().fit(X[train])   # mean and sd: train
Z = scaler.transform(X)                   # every column: sd 1

print("k, train error, test error, caught, false alarms")
for k in [1, 5, 15, 51, 151]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(Z[train], y[train])
    err_train = (knn.predict(Z[train]) != y[train]).mean()
    guess = knn.predict(Z[test])
    err_test = (guess != y[test]).mean()
    caught = ((guess == 1) & (y[test] == 1)).sum()
    wrong = ((guess == 1) & (y[test] == 0)).sum()
    print(k, round(err_train, 3), round(err_test, 3),
          caught, wrong)
