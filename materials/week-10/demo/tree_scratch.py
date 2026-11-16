import numpy as np
import pandas as pd

def entropy(p):
    if p == 0 or p == 1:
        return 0.0
    return -(p * np.log2(p) + (1 - p) * np.log2(1 - p))

def best_split(x, y):
    """The cut-off on x with the largest information gain."""
    best_cut, best_gain = None, 0.0
    values = np.sort(np.unique(x))
    for cut in (values[:-1] + values[1:]) / 2:   # midpoints
        left = x <= cut
        after = (left.mean() * entropy(y[left].mean())
                 + (~left).mean() * entropy(y[~left].mean()))
        gain = entropy(y.mean()) - after
        if gain > best_gain:
            best_cut, best_gain = cut, gain
    return best_cut, best_gain

history = pd.read_csv("history.csv", index_col="Date")
returns = history.pct_change().dropna() * 100   # in %
train = returns[returns.index < "2025-11-17"]
x = train["VOO"].to_numpy()
y = (train["AAPL"] < -2).astype(int).to_numpy()

cut, gain = best_split(x, y)                     # question 1
print("VOO <=", round(cut, 3), " gain", round(gain, 3))
yes = x <= cut
cut_yes, g_yes = best_split(x[yes], y[yes])      # 2a: if yes
cut_no, g_no = best_split(x[~yes], y[~yes])      # 2b: if no
print("  if yes: VOO <=", round(cut_yes, 3),
      " gain", round(g_yes, 3))
print("  if no:  VOO <=", round(cut_no, 3),
      " gain", round(g_no, 3))
