import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

returns = pd.read_csv("universe.csv", index_col="Date")
stocks = returns.drop(columns="VOO")
Z = ((stocks - stocks.mean()) / stocks.std()).to_numpy()

C = Z.T @ Z / (len(Z) - 1)            # 34 x 34 correlations
values, vectors = np.linalg.eigh(C)   # eigenvalues, ascending
order = np.argsort(values)[::-1]      # largest first
values, vectors = values[order], vectors[:, order]
share = values / values.sum()
print("share of variance:", share[:5].round(3))

pc1 = Z @ vectors[:, 0]               # PC1 on each day
pc1 = pc1 * np.sign(vectors[:, 0].sum())   # sign: up = up
r = np.corrcoef(pc1, returns["VOO"])[0, 1]
print("corr(PC1, VOO):", round(r, 3))

ratio = PCA().fit(Z).explained_variance_ratio_
print("scikit-learn:", ratio[:5].round(3))
