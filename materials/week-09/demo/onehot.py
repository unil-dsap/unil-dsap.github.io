import pandas as pd
from sklearn.linear_model import LinearRegression

prices = pd.read_csv("prices.csv", index_col="Date")
returns = prices.pct_change().dropna() * 100   # in %

day = pd.to_datetime(returns.index).day_name()  # "Monday"
dummies = pd.get_dummies(day, drop_first=True, dtype=int)
dummies.index = returns.index

X = pd.concat([returns[["VOO"]], dummies], axis=1)
print(X.head(3))
model = LinearRegression().fit(X, returns["AAPL"])
print("b:", model.coef_.round(3))
print("R2:", round(model.score(X, returns["AAPL"]), 3))
