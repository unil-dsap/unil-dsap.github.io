# report.py — ledger.csv in, report.txt out
from pathlib import Path

def load(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        header = f.readline()
        for line in f:
            parts = line.strip().split(",")
            ticker, name, shares, price = parts
            try:
                rows.append((name, int(shares), float(price)))
            except ValueError:
                print(f"skipped {ticker}: bad number")
    return rows

def write_report(rows, path):
    total = 0.0
    with open(path, "w", encoding="utf-8") as out:
        for name, shares, price in rows:
            out.write(f"{name:<9}{shares * price:>10,.2f}\n")
            total += shares * price
        out.write(f"{'total':<9}{total:>10,.2f}\n")
    return total

rows = load(Path("ledger.csv"))
total = write_report(rows, Path("report.txt"))
assert total > 0, "an empty report?"
print(len(rows), "positions, total", round(total, 2))
print(Path("report.txt").read_text())
