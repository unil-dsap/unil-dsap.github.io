import numpy as np
import pandas as pd

def entropy(p):
    """Bits of uncertainty in a yes/no with P(yes) = p."""
    if p == 0 or p == 1:
        return 0.0
    return -(p * np.log2(p) + (1 - p) * np.log2(1 - p))

history = pd.read_csv("history.csv", index_col="Date")
returns = history.pct_change().dropna() * 100   # in %
train = returns[returns.index < "2025-11-17"]
x = train["VOO"]
y = (train["AAPL"] < -2).astype(int)

print("before any question:", round(entropy(y.mean()), 3))
print("question, left days, right days, entropy after, gain")
for cut in [-2.0, -1.0, -0.359, 0.0]:
    left = x <= cut                   # the question's "yes"
    h_left = entropy(y[left].mean())
    h_right = entropy(y[~left].mean())
    after = left.mean() * h_left + (~left).mean() * h_right
    gain = entropy(y.mean()) - after
    print("VOO <=", cut, left.sum(), (~left).sum(),
          round(after, 3), round(gain, 3))
