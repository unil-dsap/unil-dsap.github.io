import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

history = pd.read_csv("history.csv", index_col="Date")
returns = history.pct_change().dropna() * 100   # in %
train = returns[returns.index < "2025-11-17"]
x = train["VOO"]
y = (train["AAPL"] < -2).astype(int)

a, b, rate = 0.0, 0.0, 0.5
print("step, log loss, a, b")
for step in range(1, 3001):
    p = 1 / (1 + np.exp(-(a + b * x)))     # the sigmoid
    a = a - rate * (p - y).mean()
    b = b - rate * ((p - y) * x).mean()
    if step in [1, 10, 100, 1000, 3000]:
        loss = -(y * np.log(p) + (1 - y) * np.log(1 - p))
        loss = round(loss.mean(), 4)
        print(step, loss, round(a, 3), round(b, 3))

m = LogisticRegression(C=np.inf).fit(train[["VOO"]], y)
print("sklearn:", m.intercept_.round(3), m.coef_.round(3))
