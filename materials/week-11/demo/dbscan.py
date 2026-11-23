import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

returns = pd.read_csv("universe.csv", index_col="Date")
market = returns["VOO"]
stocks = returns.drop(columns="VOO")      # GME included
beta = stocks.corrwith(market) * stocks.std() / market.std()
features = pd.DataFrame({"beta": beta, "vol": stocks.std()})
Z = StandardScaler().fit_transform(features)

print("eps, groups, noise")
for eps in [0.3, 0.5, 0.8]:
    labels = DBSCAN(eps=eps, min_samples=3).fit(Z).labels_
    noise = features.index[labels == -1]
    print(eps, labels.max() + 1, " ".join(noise))
