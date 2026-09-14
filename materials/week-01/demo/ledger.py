# ledger.py — value one position, then watch the price change.
ticker = "AAPL"
shares = 10
price = 190.50

value = shares * price
print("value at", price, "is", value)

# the price feed corrects itself: it was 200.00 all along
price = 200.00
print("price is now", price)
print("value is still", value)
