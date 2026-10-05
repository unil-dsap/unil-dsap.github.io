# positions.py — our own class for one position of the ledger
class Position:
    """One position: a ticker, a number of shares, a price."""

    def __init__(self, ticker, shares, price):
        self.ticker = ticker
        self.shares = shares
        self.price = price

    def value(self):
        return self.shares * self.price

nesn = Position("NESN", 4, 102.3)
aapl = Position("AAPL", 10, 190.5)
print(nesn.ticker, nesn.shares, nesn.value())
print(aapl.ticker, aapl.value())
print(type(nesn), isinstance(nesn, Position))
print(type(4), type("NESN"), type([10, 4, 2]))
