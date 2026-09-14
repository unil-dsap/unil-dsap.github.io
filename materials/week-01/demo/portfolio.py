# portfolio.py — three positions, their total, and one share in percent.
# Workshop, part 4: the first version has `round(share, 2)` on its own
# line and prints the long number. This is the fixed version.
aapl = 10 * 190.50
nesn = 4 * 102.30
voo = 2 * 512.00

total = aapl + nesn + voo
print("total:", total)

share = nesn / total * 100
print("NESN share, in percent:", share)

share = round(share, 2)
print("rounded:", share)
