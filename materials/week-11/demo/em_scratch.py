import numpy as np
import pandas as pd

returns = pd.read_csv("universe.csv", index_col="Date")
vol = returns.drop(columns=["VOO", "GME"]).std()
x = vol.to_numpy()                       # one number a stock

def normal(x, mu, sd):                   # the bell curve
    z = (x - mu) / sd
    return np.exp(-z ** 2 / 2) / (sd * np.sqrt(2 * np.pi))

mu = np.array([0.8, 1.2, 1.9])           # three first guesses
sd = np.array([0.3, 0.3, 0.3])
w = np.array([1 / 3, 1 / 3, 1 / 3])      # mixing weights
for step in range(100):
    dens = w * normal(x[:, None], mu, sd)        # E-step
    r = dens / dens.sum(axis=1, keepdims=True)   # memberships
    n_k = r.sum(axis=0)                          # M-step
    w = n_k / len(x)
    mu = (r * x[:, None]).sum(axis=0) / n_k
    dev = (x[:, None] - mu) ** 2
    sd = np.sqrt((r * dev).sum(axis=0) / n_k)

print("means:", mu.round(2), " sds:", sd.round(2))
print("weights:", w.round(2))
for t in ["NESN", "JPM", "MSFT", "AAPL"]:
    i = list(vol.index).index(t)
    print(t, round(x[i], 2), "memberships:", r[i].round(2))
