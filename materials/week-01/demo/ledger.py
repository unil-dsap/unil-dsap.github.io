# ledger.py — your first program. Run it from the folder it lives in.
print("DSAP ledger, version 0")
line = open("ledger.csv").readline()
print("first line of the ledger:", line.strip())
print("done — this line always runs last")
