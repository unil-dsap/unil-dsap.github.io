# ledger_history.py — builds the ledger's git history, sessions 1-6, and
# writes every command and its real output to transcript.txt.
#
# Every terminal output on the session-7 slides is copied from
# transcript.txt. The machine is a fresh, empty home folder; commit dates
# are fixed, so the commit hashes are the same on every machine and every
# run. Your own git settings are ignored on purpose.
#
# Run:  python ledger_history.py
import os
import shlex
import shutil
import subprocess
import sys
import tempfile

# ---- the six versions of the ledger (one per session) ------------------

CSV_3 = """ticker,shares,price
AAPL,10,190.50
NESN,4,102.30
VOO,2,512.00
"""

CSV_4 = CSV_3 + "UBSG,40,25.00\n"

S1 = """# ledger.py — your first program. Run it from the folder it lives in.
print("DSAP ledger, version 0")
line = open("ledger.csv").readline()
print("first line of the ledger:", line.strip())
print("done — this line always runs last")
"""

S2 = """# ledger.py — session 2: value one position
ticker = "AAPL"
shares = 10
price = 190.50
value = shares * price
print(f"{ticker}: {value:.2f} CHF")
"""

S3 = """# ledger.py — session 3: many positions, one total
prices = [190.50, 102.30, 512.00, 25.00]
shares = [10, 4, 2, 40]
total = 0
fees = 0
for i in range(len(prices)):
    value = shares[i] * prices[i]
    total = total + value
    if value >= 1000:
        fee = 0
    else:
        fee = 5
    fees = fees + fee
print(f"total: {total:.2f} CHF, fees: {fees} CHF")
"""

S4 = """# ledger.py — session 4: named steps
def position_value(shares, price):
    return shares * price

def fee(value):
    if value >= 1000:
        return 0
    return 5

prices = [190.50, 102.30, 512.00, 25.00]
shares = [10, 4, 2, 40]
total = 0
fees = 0
for i in range(len(prices)):
    value = position_value(shares[i], prices[i])
    total = total + value
    fees = fees + fee(value)
print(f"total: {total:.2f} CHF, fees: {fees} CHF")
"""

S5 = """# ledger.py — session 5: positions as dicts
def position_value(shares, price):
    return shares * price

def fee(value):
    if value >= 1000:
        return 0
    return 5

positions = [
    {"ticker": "AAPL", "shares": 10, "price": 190.50},
    {"ticker": "NESN", "shares": 4, "price": 102.30},
    {"ticker": "VOO", "shares": 2, "price": 512.00},
    {"ticker": "UBSG", "shares": 40, "price": 25.00},
]
total = 0
fees = 0
for p in positions:
    value = position_value(p["shares"], p["price"])
    total = total + value
    fees = fees + fee(value)
print(f"total: {total:.2f} CHF, fees: {fees} CHF")
"""

S6 = """# ledger.py — session 6: file in, report out
import csv

def position_value(shares, price):
    return shares * price

def fee(value):
    if value >= 1000:
        return 0
    return 5

with open("ledger.csv") as f:
    positions = list(csv.DictReader(f))
total = 0
fees = 0
for p in positions:
    value = position_value(int(p["shares"]), float(p["price"]))
    total = total + value
    fees = fees + fee(value)
with open("report.txt", "w") as out:
    out.write(f"positions: {len(positions)}\\n")
    out.write(f"total: {total:.2f} CHF\\n")
    out.write(f"fees: {fees} CHF\\n")
print("wrote report.txt")
"""

# The assistant was asked: "round the report totals to two decimals".
# It did that, and it also changed >= to > . Nobody asked for that.
S6_MODEL_EDIT = S6.replace(
    "    if value >= 1000:", "    if value > 1000:"
).replace(
    "    total = total + value\n",
    "    total = round(total + value, 2)\n",
)

NOTES = """git notes: status first, then add, then commit.
"""

README = """# ledger

The DSAP course ledger. Run `python ledger.py` in this folder.
"""

# (date with time zone, message, files)
SESSIONS = [
    ("2026-09-14T16:30:00+0200", "session 1: first run",
     {"ledger.py": S1, "ledger.csv": CSV_3}),
    ("2026-09-28T16:30:00+0200", "session 2: value one position",
     {"ledger.py": S2}),
    ("2026-10-05T16:30:00+0200", "session 3: loop and total",
     {"ledger.py": S3, "ledger.csv": CSV_4}),
    ("2026-10-12T16:30:00+0200", "session 4: functions",
     {"ledger.py": S4}),
    ("2026-10-19T16:30:00+0200", "session 5: positions as dicts",
     {"ledger.py": S5}),
    ("2026-10-26T16:30:00+0100", "session 6: read csv, write report",
     {"ledger.py": S6, ".gitignore": "report.txt\n"}),
]

# The hashes the slides and figures print. If this check fails, the
# history changed: re-read transcript.txt, then update slides.md, fig/,
# and this table.
EXPECTED = {
    "session 1": "916acb4",
    "session 2": "ee7054a",
    "session 3": "9de8ebc",
    "session 4": "003891f",
    "session 5": "3c6342e",
    "session 6": "cd81ebf",
    "laptop README": "11573a5",
    "notes": "18a82e7",
}

# ---- machinery --------------------------------------------------------

root = os.path.realpath(tempfile.mkdtemp())
home = os.path.join(root, "home")
os.makedirs(home)

log = []
base_env = dict(os.environ)
for key in list(base_env):
    if key.startswith("GIT_"):
        del base_env[key]
base_env.pop("EMAIL", None)
base_env.update({
    "HOME": home,                  # a fresh machine: no ~/.gitconfig yet
    "XDG_CONFIG_HOME": home,
    "GIT_CONFIG_NOSYSTEM": "1",
    "LANG": "C",
    "LC_ALL": "C",
    "TZ": "Europe/Zurich",
})
date = SESSIONS[0][0]


def run(cwd, cmd, show=True, may_fail=False):
    """Run one command line; record it and its output as a terminal would."""
    env = dict(base_env, GIT_AUTHOR_DATE=date, GIT_COMMITTER_DATE=date)
    args = shlex.split(cmd)
    if args[0] == "git":
        # never guess an identity from the computer's name: a fresh
        # machine must ask, the way Nuvolos does
        args = ["git", "-c", "color.ui=never", "-c", "core.pager=cat",
                "-c", "init.defaultBranch=main",
                "-c", "user.useConfigOnly=true"] + args[1:]
    if args[0] == "python":
        args[0] = sys.executable
    result = subprocess.run(args, cwd=cwd, env=env, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # the temporary folder stands in for the Nuvolos files folder
    output = result.stdout.rstrip().replace(root, "/files")
    if result.returncode != 0 and not may_fail:
        print(f"FAILED: {cmd}\n{output}")
        sys.exit(1)
    if show:
        log.append(f"$ {cmd}")
        if output:
            log.append(output)
    return result.stdout.strip()


def section(title):
    log.append("")
    log.append(f"#### {title}")


def write(folder, files):
    for name, text in files.items():
        with open(os.path.join(folder, name), "w") as f:
            f.write(text)


def cat(folder, name):
    log.append(f"$ cat {name}")
    with open(os.path.join(folder, name)) as f:
        log.append(f.read().rstrip())


def short(cwd, rev):
    return run(cwd, f"git rev-parse --short=7 {rev}", show=False)


# ---- the story ----------------------------------------------------------

nuvolos = os.path.join(root, "dsap")
os.makedirs(nuvolos)

section("the fingerprint: same content, same hash; one character, new hash")
scratch = os.path.join(root, "scratch")
os.makedirs(scratch)
write(scratch, {"ledger.csv": CSV_3})
run(scratch, "git hash-object ledger.csv")
run(scratch, "git hash-object ledger.csv")
write(scratch, {"ledger.csv": CSV_3.replace("190.50", "190.51")})
log.append("(changed 190.50 to 190.51 — one character)")
run(scratch, "git hash-object ledger.csv")

section("outside a repository")
run(scratch, "git status", may_fail=True)

section("session 1: a folder becomes a repository")
write(nuvolos, SESSIONS[0][2])
run(nuvolos, "git --version")
run(nuvolos, "git init")
run(nuvolos, "ls -a")
run(nuvolos, "git status")
run(nuvolos, "git add ledger.py ledger.csv")
run(nuvolos, "git status")

section("first commit on a fresh machine: who are you?")
run(nuvolos, 'git commit -m "session 1: first run"', may_fail=True)
run(nuvolos, 'git config --global user.name "Student"')
run(nuvolos, 'git config --global user.email "student@unil.ch"')
run(nuvolos, 'git commit -m "session 1: first run"')
run(nuvolos, "git status")

section("session 2: the everyday loop")
date, message, files = SESSIONS[1]
write(nuvolos, files)
run(nuvolos, "git status --short")
run(nuvolos, "git diff --stat")
run(nuvolos, "git add ledger.py")
run(nuvolos, f'git commit -m "{message}"')

section("sessions 3-5: the same loop, three more times")
for date, message, files in SESSIONS[2:5]:
    write(nuvolos, files)
    run(nuvolos, "git status --short")
    run(nuvolos, "git add .")
    run(nuvolos, f'git commit -m "{message}"')

section("session 6: three places, and choosing what goes in")
date, message, files = SESSIONS[5]
write(nuvolos, files)
write(nuvolos, {"notes.txt": NOTES})
run(nuvolos, "git status")
run(nuvolos, "git add .")
run(nuvolos, "git status")
run(nuvolos, "git restore --staged notes.txt")
run(nuvolos, "git status")
run(nuvolos, f'git commit -m "{message}"')
run(nuvolos, "python ledger.py")
cat(nuvolos, "report.txt")
run(nuvolos, "git status --short")
run(nuvolos, "rm notes.txt")
run(nuvolos, "git status")

section("reading history")
run(nuvolos, "git log --oneline")
run(nuvolos, "git log -2")
run(nuvolos, f"git show --stat {short(nuvolos, 'HEAD~3')}")
run(nuvolos, f"git diff {short(nuvolos, 'HEAD~5')} {short(nuvolos, 'HEAD~3')} -- ledger.csv")
run(nuvolos, "git log --oneline -- ledger.csv")

section("snapshots are cheap: an unchanged file is stored once")
run(nuvolos, f"git ls-tree {short(nuvolos, 'HEAD~2')}")
run(nuvolos, f"git ls-tree {short(nuvolos, 'HEAD')}")

section("the planted lie: the assistant edits ledger.py")
date = "2026-10-28T14:00:00+0100"
write(nuvolos, {"ledger.py": S6_MODEL_EDIT})
run(nuvolos, "git status --short")
run(nuvolos, "git diff")
run(nuvolos, "git diff -U1")
run(nuvolos, "python ledger.py")
cat(nuvolos, "report.txt")
run(nuvolos, "git restore ledger.py")
run(nuvolos, "git status --short")
run(nuvolos, "python ledger.py")
cat(nuvolos, "report.txt")

section("remote: push to GitHub (a bare repository stands in for it)")
github = os.path.join(root, "github")
os.makedirs(github)
run(github, "git init --quiet --bare ledger.git", show=False)
run(nuvolos, "git remote add origin ../github/ledger.git")
run(nuvolos, "git remote -v")
run(nuvolos, "git push -u origin main")
run(nuvolos, "git status")

section("remote: clone on a second machine, change, push")
run(root, "git clone github/ledger.git laptop")
laptop = os.path.join(root, "laptop")
run(laptop, "git log --oneline -1")
write(laptop, {"README.md": README})
run(laptop, "git add README.md")
date = "2026-10-28T20:15:00+0100"
run(laptop, 'git commit -m "add a README"')
run(laptop, "git push")

section("remote: fetch the news, then pull the change back on Nuvolos")
run(nuvolos, "git fetch")
run(nuvolos, "git status")
run(nuvolos, "git pull")
run(nuvolos, "git log --oneline")

section("remote: Nuvolos pushes; the laptop forgot to pull")
date = "2026-10-29T10:00:00+0100"
write(nuvolos, {"notes.txt": NOTES})
run(nuvolos, "git add notes.txt")
run(nuvolos, 'git commit -m "add git notes"')
run(nuvolos, "git push")
date = "2026-10-29T21:00:00+0100"
write(laptop, {"README.md": README + "\nOutput: report.txt\n"})
run(laptop, "git add README.md")
run(laptop, 'git commit -m "README: say where the output goes"')
run(laptop, "git push", may_fail=True)

# ---- check and write ------------------------------------------------------

hashes = {f"session {n}": short(nuvolos, f"HEAD~{8 - n}") for n in range(1, 7)}
hashes["laptop README"] = short(nuvolos, "HEAD~1")
hashes["notes"] = short(nuvolos, "HEAD")
shutil.rmtree(root)

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "transcript.txt"), "w") as f:
    f.write("\n".join(log).lstrip() + "\n")

print("hashes:", hashes)
for name, value in EXPECTED.items():
    if hashes[name] != value:
        print(f"HASH CHANGED for {name}: {hashes[name]} (slides say {value})")
        sys.exit(1)
print("wrote transcript.txt")
