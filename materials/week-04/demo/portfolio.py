# portfolio.py — the ledger, organised into functions
import math

def position_value(shares, price):
    """Value of one position, in CHF."""
    return shares * price

def total_value(tickers, shares, price):
    total = 0.0
    for i in range(len(tickers)):
        total += position_value(shares[i], price[tickers[i]])
    return total

def years_to_double(rate=0.05):
    return math.ceil(math.log(2) / math.log(1 + rate))

tickers = ["AAPL", "NESN", "VOO"]
shares = [10, 4, 2]
price = {"AAPL": 190.5, "NESN": 102.3, "VOO": 512.0}

total = total_value(tickers, shares, price)
print(f"total {total:,.2f}", round(total, 1))
print(years_to_double(), years_to_double(rate=0.07))
print(position_value(price=102.3, shares=4), sum(shares))
print(", ".join(tickers).lower(), type(total_value))
