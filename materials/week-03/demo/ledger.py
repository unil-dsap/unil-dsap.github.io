# ledger.py — the whole ledger: lists, a dict, loops
tickers = ["AAPL", "NESN", "VOO"]
shares = [10, 4, 2]
price = {"AAPL": 190.5, "NESN": 102.3, "VOO": 512.0}
print(tickers[0], tickers[-1], tickers[1:], price["NESN"])

total = 0.0
for i in range(len(tickers)):
    value = shares[i] * price[tickers[i]]
    total += value
    if value >= 1500:
        size = "large"
    elif value >= 500:
        size = "medium"
    else:
        size = "small"
    print(f"{tickers[i]:<5} {value:>9,.2f}  {size}")

years = 0
grown = total
while grown < 2 * total:
    grown *= 1.05
    years += 1
print(f"total {total:,.2f}, doubles in {years} years")
