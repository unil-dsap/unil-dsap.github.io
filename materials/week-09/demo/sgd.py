import numpy as np
import pandas as pd

prices = pd.read_csv("prices.csv", index_col="Date")
returns = prices.pct_change().dropna() * 100   # in %
x = returns["VOO"].to_numpy()
y = returns["AAPL"].to_numpy()

rng = np.random.default_rng(9)
a, b, rate = 0.0, 0.0, 0.1
print("step, loss on all days, a, b")
for step in range(1, 201):
    days = rng.choice(len(x), size=20)   # 20 random days
    errors = (a + b * x[days]) - y[days]
    a = a - rate * 2 * errors.mean()
    b = b - rate * 2 * (errors * x[days]).mean()
    if step in [1, 5, 20, 50, 100, 150, 200]:
        loss = (((a + b * x) - y) ** 2).mean()
        print(step, round(loss, 3), round(a, 3), round(b, 3))
