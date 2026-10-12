# arrays.py — numpy: a grid of numbers of one type
import numpy as np

prices = np.array([[185.0, 188.2, 190.5],
                   [104.1, 103.0, 102.3],
                   [505.0, 509.9, 512.0]])
shares = np.array([10, 4, 2])
print(prices.shape, prices.dtype, prices.ndim)
print(prices[1, 2], prices[1], prices[:, -1])
print(prices[:2, 1:])

values = shares * prices[:, -1]
print(values, values.sum())
print(prices.mean(axis=1).round(2), prices.max(axis=0))
history = shares[:, None] * prices
print(history.sum(axis=0))
returns = prices[:, 1:] / prices[:, :-1] - 1
print(returns.round(4))
print(values[values > 1000], (returns > 0).sum())
