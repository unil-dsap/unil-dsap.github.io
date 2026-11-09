import pandas as pd

prices = pd.read_csv("prices.csv", index_col="Date")
returns = prices.pct_change().dropna() * 100   # in %

x = returns["VOO"]       # the market
y = returns["AAPL"]      # one stock from the ledger

b = x.cov(y) / x.var()               # the slope: beta
a = y.mean() - b * x.mean()          # the intercept

fitted = a + b * x
residuals = y - fitted
r2 = 1 - (residuals ** 2).sum() / ((y - y.mean()) ** 2).sum()

print("days:", len(returns))
print("mean, VOO, AAPL:", round(x.mean(), 3), round(y.mean(), 3))
print("sd,   VOO, AAPL:", round(x.std(), 3), round(y.std(), 3))
print("correlation:", round(x.corr(y), 3))
print("slope b:", round(b, 3), " intercept a:", round(a, 3))
print("R squared:", round(r2, 3))
