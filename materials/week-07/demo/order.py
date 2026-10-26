# order.py — an office-supplies order, with one planted lie (review item 3)
prices = {"pen": 1.5, "pad": 3.0, "ink": 4.0}
qty = {"pen": 4, "pad": 2, "ink": 1}

total = 0
for item in prices:
    total = total + prices[item] * qty["pen"]

print(f"order total: {total:.2f} CHF")
