import numpy as np
import pandas as pd

prices = pd.read_csv("prices.csv", index_col="Date")
returns = prices.pct_change().dropna() * 100   # in %
x = returns["VOO"].to_numpy()
y = returns["AAPL"].to_numpy()

x_train, y_train = x[:200], y[:200]     # the first 200 days
x_test, y_test = x[200:], y[200:]       # the last 49 days
print("degree, train error, test error")
for degree in [0, 1, 3, 8, 15]:
    c = np.polyfit(x_train, y_train, degree)    # 1 = a line
    train = ((np.polyval(c, x_train) - y_train) ** 2).mean()
    test = ((np.polyval(c, x_test) - y_test) ** 2).mean()
    print(degree, round(train, 3), round(test, 3))
