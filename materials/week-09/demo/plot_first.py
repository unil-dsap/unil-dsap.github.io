import pandas as pd

anscombe = pd.read_csv("anscombe.csv")
dozen = pd.read_csv("datasaurus.csv")

def describe(name, x, y):
    b = x.cov(y) / x.var()
    a = y.mean() - b * x.mean()
    print(name.ljust(8), round(x.mean(), 2), round(y.mean(), 2),
          round(x.std(), 2), round(y.std(), 2),
          round(x.corr(y), 3), round(a, 2), round(b, 3))

print("set, mean x, mean y, sd x, sd y, corr, a, b")
for name in ["I", "II", "III", "IV"]:
    rows = anscombe[anscombe["set"] == name]
    describe(name, rows["x"], rows["y"])
for name in ["dino", "star", "x_shape", "circle"]:
    rows = dozen[dozen["dataset"] == name]
    describe(name, rows["x"], rows["y"])
