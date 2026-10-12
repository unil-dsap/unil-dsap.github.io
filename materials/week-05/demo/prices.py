# prices.py — nested data, read in one line
ledger = {
    "AAPL": {"shares": 10, "prices": [185.0, 188.2, 190.5]},
    "NESN": {"shares": 4, "prices": [104.1, 103.0, 102.3]},
    "VOO": {"shares": 2, "prices": [505.0, 509.9, 512.0]},
}
print(ledger["NESN"]["prices"][-1])
print(ledger["AAPL"]["prices"][1:])

last = {t: d["prices"][-1] for t, d in ledger.items()}
values = [d["shares"] * last[t] for t, d in ledger.items()]
rising = [t for t, d in ledger.items()
          if d["prices"][-1] > d["prices"][0]]
print(last)
print(values, sum(values))
print(rising)

by_value = sorted(ledger, reverse=True,
                  key=lambda t: ledger[t]["shares"] * last[t])
print(by_value)
change = lambda p: (p[-1] - p[0]) / p[0]
print({t: round(change(d["prices"]), 4)
       for t, d in ledger.items()})
