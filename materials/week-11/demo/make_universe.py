# make_universe.py — writes universe.csv: five years of daily returns (in %)
# for 34 stocks and VOO. VOO is the market of sessions 9 and 10
# (history.csv), unchanged. The 34 stocks are SIMULATED from that market
# plus one shared factor per sector and their own noise, with a fixed
# seed, so every run gives the same file. The ledger's stocks keep their
# betas of session 9: AAPL 1.25, MSFT 1.10, NESN 0.55.
import numpy as np
import pandas as pd

history = pd.read_csv("history.csv", index_col="Date")
market = (history["VOO"].pct_change().dropna() * 100).to_numpy()
dates = history.index[1:]
n = len(market)
rng = np.random.default_rng(2027)

factor = {}                              # one shared factor per sector
for sector in ["tech", "staples", "banks", "energy", "pharma"]:
    factor[sector] = rng.normal(0, 1, n)

# ticker: sector, beta, sector loading, own noise (all in %)
stocks = {
    "AAPL": ("tech", 1.25, 0.60, 0.90), "MSFT": ("tech", 1.10, 0.55, 0.80),
    "NESN": ("staples", 0.55, 0.45, 0.55),
    "NVDA": ("tech", 1.40, 0.70, 1.10), "GOOGL": ("tech", 1.20, 0.60, 0.90),
    "META": ("tech", 1.35, 0.65, 1.00), "AMZN": ("tech", 1.30, 0.60, 0.90),
    "ORCL": ("tech", 1.15, 0.55, 0.85),
    "KO": ("staples", 0.50, 0.45, 0.50), "PG": ("staples", 0.55, 0.45, 0.50),
    "PEP": ("staples", 0.55, 0.40, 0.55), "ULVR": ("staples", 0.50, 0.45, 0.55),
    "CL": ("staples", 0.60, 0.40, 0.50), "DGE": ("staples", 0.60, 0.45, 0.60),
    "UBSG": ("banks", 1.00, 0.65, 0.60), "JPM": ("banks", 0.95, 0.60, 0.55),
    "BAC": ("banks", 1.05, 0.65, 0.60), "GS": ("banks", 1.00, 0.60, 0.60),
    "HSBA": ("banks", 0.95, 0.60, 0.55), "BNP": ("banks", 1.00, 0.65, 0.60),
    "XOM": ("energy", 0.75, 1.30, 0.80), "CVX": ("energy", 0.70, 1.25, 0.80),
    "SHEL": ("energy", 0.75, 1.35, 0.85), "BP": ("energy", 0.80, 1.40, 0.90),
    "TTE": ("energy", 0.70, 1.30, 0.85), "COP": ("energy", 0.80, 1.45, 0.90),
    "ROG": ("pharma", 0.60, 0.60, 0.80), "NOVN": ("pharma", 0.65, 0.60, 0.75),
    "PFE": ("pharma", 0.70, 0.65, 0.85), "JNJ": ("pharma", 0.60, 0.55, 0.75),
    "MRK": ("pharma", 0.65, 0.60, 0.80), "AZN": ("pharma", 0.70, 0.65, 0.85),
}
returns = pd.DataFrame(index=dates)
for t in stocks:
    sector, beta, load, own = stocks[t]
    returns[t] = (beta * market + load * factor[sector]
                  + rng.normal(0, own, n))
# between two sectors: a payments company (tech and banks)
returns["V"] = (1.15 * market + 0.45 * factor["tech"]
                + 0.45 * factor["banks"] + rng.normal(0, 0.8, n))
# a "meme stock": barely follows anything, moves a lot
returns["GME"] = 1.3 * market + rng.normal(0, 4.5, n)
returns["VOO"] = market
returns.round(4).to_csv("universe.csv")
print("wrote universe.csv:", returns.shape[1], "columns,", n, "days")
