# ledger_np.py — the same ledger, with numpy and pandas
import numpy as np
import pandas as pd

shares = np.array([10, 4, 2])
prices = np.array([190.5, 102.3, 512.0])
values = shares * prices
print(values, values.sum())
print([10, 4, 2] * 2, shares * 2)

ledger = pd.DataFrame({"ticker": ["AAPL", "NESN", "VOO"],
                       "shares": [10, 4, 2],
                       "price": [190.5, 102.3, 512.0]})
ledger["value"] = ledger["shares"] * ledger["price"]
print(ledger)
print(type(shares), type(ledger))
