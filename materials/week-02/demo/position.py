# position.py — one position of the ledger
ticker = "NESN"
raw = "4"             # text, as read from a file
shares = int(raw)
price = 102.3
cash = 1000.0
last_sale = None
print(raw * 2, shares * 2, type(raw), type(shares))

shares = shares + 6   # buy 6 more
cash -= 6 * price
value = shares * price
weight = value / (value + cash)
can_buy = int(cash // price)
rest = cash % price
in_2y = value * 1.05 ** 2

valid = len(ticker) <= 5 and shares > 0
alert = weight > 0.5 or not valid

print(cash, cash == 386.2, abs(cash - 386.2) < 0.01)
print(f"{ticker}: {shares} shares, {value:,.2f} CHF")
print(f"cash {cash:.2f}, weight {weight:.2f}")
print(can_buy, rest, round(in_2y, 2))
print(valid, alert, last_sale)
