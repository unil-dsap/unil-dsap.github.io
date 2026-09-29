# slices.py — slicing, in many types
import numpy as np
import pandas as pd

ticker = "NESN.SW"
print(ticker[:4], ticker[-2:])

prices = [190.5, 102.3, 512.0, 410.0]
print(prices[1:3], prices[::-1])

table = np.array([[10, 190.5], [4, 102.3], [2, 512.0]])
print(table[1:, 0], table[:2, 1])

names = ["AAPL", "NESN", "VOO"]
ledger = pd.DataFrame({"shares": [10, 4, 2]}, index=names)
print(ledger.iloc[:2]["shares"].tolist())
print(ledger.loc["AAPL":"NESN", "shares"].tolist())

parts = "NESN,4,102.30".split(",")
print(parts[1:])
