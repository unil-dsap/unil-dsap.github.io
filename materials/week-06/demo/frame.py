# frame.py — the same ledger, the pandas way
import pandas as pd

df = pd.read_csv("ledger.csv")
print(df)
print(df["shares"].dtype, df["shares"].isna().sum())
df = df.dropna()
df["value"] = df["shares"] * df["price"]
print(df["value"].sum())
df.to_csv("report.csv", index=False)
print(open("report.csv").read())
