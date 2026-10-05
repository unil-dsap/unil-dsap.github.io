# objects.py — every value is an object of some class
import numpy as np
import pandas as pd

shares = [10, 4, 2]
arr = np.array(shares)
print(sum(shares), arr.sum(), arr.mean())
print(type(shares), type(arr))
print(arr.shape, arr.dtype, len(arr))

ledger = pd.DataFrame({"ticker": ["AAPL", "NESN", "VOO"],
                       "shares": shares,
                       "price": [190.5, 102.3, 512.0]})
ledger["value"] = ledger["shares"] * ledger["price"]
print(ledger["value"].sum(), ledger.shape)
print(type(ledger), type(ledger["value"]))
print(ledger.sort_values("value", ascending=False).head(2))
