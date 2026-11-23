import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

returns = pd.read_csv("universe.csv", index_col="Date")
market = returns["VOO"]
stocks = returns.drop(columns=["VOO", "GME"])   # GME: Part 7

features = pd.DataFrame(index=stocks.columns)
for t in stocks.columns:
    beta = stocks[t].cov(market) / market.var()   # session 9
    features.loc[t, "beta"] = beta
    features.loc[t, "vol"] = stocks[t].std()

Z = StandardScaler().fit_transform(features)    # sd 1 each
model = KMeans(n_clusters=5, n_init=10, random_state=0)
features["group"] = model.fit(Z).labels_

for g in range(5):
    members = features[features["group"] == g].index
    print("group", g, ":", " ".join(members))
