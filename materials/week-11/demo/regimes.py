import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

returns = pd.read_csv("universe.csv", index_col="Date")
days = StandardScaler().fit_transform(returns[["VOO", "MSFT"]])

model = KMeans(n_clusters=4, n_init=10, random_state=0)
labels = model.fit(days).labels_
for g in range(4):
    print("regime", g, ":", (labels == g).sum(), "days")
print("silhouette:", round(silhouette_score(days, labels), 2))
