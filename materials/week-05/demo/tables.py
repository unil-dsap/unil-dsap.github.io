# tables.py — pandas: a table with names
import pandas as pd

df = pd.DataFrame({"ticker": ["AAPL", "MSFT", "NESN", "VOO"],
                   "sector": ["tech", "tech", "food", "fund"],
                   "shares": [10, 3, 4, 2],
                   "price": [190.5, 410.0, 102.3, 512.0]})
df["value"] = df["shares"] * df["price"]
print(df)
print(df.shape, df["value"].sum())
print(df.loc[2, "ticker"], df.iloc[0, 3])

big = df[df["value"] > 1000]
print(big[["ticker", "value"]])
df["size"] = df["value"].apply(
    lambda v: "large" if v > 1500 else "small")
print(df.groupby("sector")["value"].sum())
