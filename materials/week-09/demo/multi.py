import pandas as pd
from sklearn.linear_model import LinearRegression

prices = pd.read_csv("prices.csv", index_col="Date")
returns = prices.pct_change().dropna() * 100   # in %
y = returns["AAPL"]

for columns in [["MSFT"], ["VOO"], ["VOO", "MSFT"]]:
    X = returns[columns]                # one column, or two
    model = LinearRegression().fit(X, y)
    print(columns, "b:", model.coef_.round(3),
          "a:", round(model.intercept_, 3),
          "R2:", round(model.score(X, y), 3))
