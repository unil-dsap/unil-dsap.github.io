# make_history.py — writes history.csv: five years of daily prices for the
# four positions of the ledger. The last year is session 9's prices.csv,
# unchanged. The four years before it are SIMULATED with the same model
# and another fixed seed, so every run gives the same file.
import numpy as np
import pandas as pd

last_year = pd.read_csv("../../week-09/demo/prices.csv",
                        index_col="Date", parse_dates=True)
days = pd.bdate_range(end=last_year.index[0], periods=1001)

rng = np.random.default_rng(2025)
n = len(days) - 1                      # returns up to the known year
market = rng.normal(0.0004, 0.0095, n)
returns = pd.DataFrame(index=days[1:])
returns["AAPL"] = 0.0003 + 1.25 * market + rng.normal(0, 0.011, n)
returns["NESN"] = 0.0001 + 0.55 * market + rng.normal(0, 0.008, n)
returns["VOO"] = market
returns["MSFT"] = 0.0002 + 1.10 * market + rng.normal(0, 0.010, n)

# price on an earlier day = first known price / growth since that day
growth = (1 + returns).iloc[::-1].cumprod().iloc[::-1]
earlier = (last_year.iloc[0] / growth).round(2)
earlier.index = days[:-1]

history = pd.concat([earlier, last_year])
history.index.name = "Date"
history.to_csv("history.csv")
print("wrote history.csv:", len(history), "days,",
      history.index[0].date(), "to", history.index[-1].date())
