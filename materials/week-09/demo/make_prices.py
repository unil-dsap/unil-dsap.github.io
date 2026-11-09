# make_prices.py — writes prices.csv: one year of daily closing prices
# for the four positions of the ledger. The prices are SIMULATED, from a
# fixed seed, so every run gives the same file. The last row matches the
# prices in ledger.csv.
import numpy as np
import pandas as pd

rng = np.random.default_rng(2026)
days = pd.bdate_range(end="2026-10-30", periods=250)

market = rng.normal(0.0004, 0.0095, len(days))      # VOO: the market itself
returns = pd.DataFrame(index=days)
returns["AAPL"] = 0.0003 + 1.25 * market + rng.normal(0, 0.011, len(days))
returns["NESN"] = 0.0001 + 0.55 * market + rng.normal(0, 0.008, len(days))
returns["VOO"] = market
returns["MSFT"] = 0.0002 + 1.10 * market + rng.normal(0, 0.010, len(days))
returns.iloc[0] = 0.0                               # day 1 is the starting point

growth = (1 + returns).cumprod()                    # 1.00 on day 1, then day by day
last_price = pd.Series({"AAPL": 190.50, "NESN": 102.30, "VOO": 512.00, "MSFT": 410.00})
prices = (growth / growth.iloc[-1] * last_price).round(2)

prices.index.name = "Date"
prices.to_csv("prices.csv")
print("wrote prices.csv:", len(prices), "days,", prices.index[0].date(), "to", prices.index[-1].date())

# A copy with one typo, as real files have: on one day, the decimal point
# of Apple's price moved one place to the left.
typo = prices.copy()
typo.loc["2026-03-16", "AAPL"] = round(typo.loc["2026-03-16", "AAPL"] / 10, 2)
typo.to_csv("prices_typo.csv")
print("wrote prices_typo.csv: AAPL on 2026-03-16 is", typo.loc["2026-03-16", "AAPL"])
