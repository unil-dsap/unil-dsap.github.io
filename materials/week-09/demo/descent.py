import pandas as pd

prices = pd.read_csv("prices.csv", index_col="Date")
returns = prices.pct_change().dropna() * 100   # in %
x = returns["VOO"]
y = returns["AAPL"]

a = 0.0                 # start anywhere: a flat line at zero
b = 0.0
rate = 0.1              # the learning rate: step size
print("step, loss, a, b")
for step in range(1, 61):
    errors = (a + b * x) - y
    loss = (errors ** 2).mean()          # mean squared error
    grad_a = 2 * errors.mean()           # rate of change in a
    grad_b = 2 * (errors * x).mean()     # rate of change in b
    a = a - rate * grad_a                # step downhill
    b = b - rate * grad_b
    if step in [1, 2, 3, 5, 10, 20, 40, 60]:
        print(step, round(loss, 3), round(a, 3), round(b, 3))
