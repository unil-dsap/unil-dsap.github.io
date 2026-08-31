# Session 1 workshop — files, folders, and your first run

*Ungraded, self-checked. You leave with a working setup, your first
program run, your first error survived, and your first commit.*

## Setup (10 min)

1. Log into Nuvolos and open the **VS Code** app.
2. In the left sidebar (the Explorer), find your files. The
   `session-01` folder was distributed to you. **Copy it** into a new
   folder called `dsap` — right-click → Copy, right-click → Paste.
   You work on your copy; the original stays untouched.
3. Open a terminal: menu → Terminal → New Terminal.
4. Plumbing check — type exactly this and press Enter:
   ```
   python check.py
   ```
   You should see: `setup OK — you can run Python files. ...`
   If you see anything else, **raise your hand now.** Nothing later
   works until this does.

## Paper first (10 min — keyboard closed)

Draw this tree on your worksheet, then answer in writing:

```
files/
└── dsap/
    ├── check.py
    ├── hello.py
    ├── ledger.csv
    └── ledger.py
```

- P1. Write the **absolute path** of `ledger.csv`.
- P2. You stand in `dsap`. Write the **relative path** of `ledger.csv`.
- P3. You stand in `files`. Write the relative path of `ledger.csv` now.
- P4. A program standing in `files` runs `open("ledger.csv")`.
  Will it find the file? One word, and one reason.

## The tasks (45 min)

**T1 — run.** In the terminal: `python hello.py`, then
`python ledger.py`. Write down the *first* printed line of each.

**T2 — break it on purpose.** Go one folder up (`cd ..`), run
`python dsap/ledger.py`. It fails. Copy the **last line** of the error
onto your worksheet, word for word. This error means the program stood
in the wrong folder — you will never fear it again.
Return with `cd dsap`.

**T3 — the unsaved-dot trap.** Open `hello.py` in the editor. Change
the message text. **Do not save.** Run it. Old message! Look at the
tab: the white dot means unsaved. Save (Cmd/Ctrl-S), run again.
Write one sentence: what does the dot mean?

**T4 — edit for real.** In `ledger.py`, change `version 0` to
`version 0.1`. Save. Run. Confirm the output changed.

**T5 — ask your assistant.** Open any free chatbot in a second browser
tab (create an account now if you don't have one — you need it all
semester). Paste the FULL error text from T2 and ask: *"Explain this
error to a complete beginner."* Read the answer. Does it agree with
what the lecture said (the error is about WHERE, not wrong code)?

**T6 — your first commit.** Left sidebar → Source Control icon.
1. Click **Initialize Repository** (choose your `dsap` folder).
2. In the terminal, paste these two lines with YOUR details:
   ```
   git config --global user.name "Your Name"
   git config --global user.email "your.name@unil.ch"
   ```
3. Back in Source Control: type the message `session 1: first run`,
   press **Commit** (stage all when asked).
4. Readiness check: the file list in Source Control is now empty, and
   `git status` in the terminal says "nothing to commit". You will
   commit like this at the end of every workshop.

## Self-check — write before you peek

Answer on the worksheet FIRST, then unfold.

- S1. What is printed first when `ledger.py` runs correctly?
- S2. What is the exact error *type* from T2 (the word before the colon)?
- S3. True or false: after T3's first run, the file on disk had your
  new text.

<details><summary>Answers (only after writing yours)</summary>

- S1: `DSAP ledger, version 0`
- S2: `FileNotFoundError`
- S3: False — the editor had it; the disk still held the old text.
  The dot on the tab told you so.

</details>

## The bridge — before Sep 28 (no class Sep 21)

Two short visits, twenty minutes each. The goal is only this:
your hands stay warm.

**Visit 1 (this week):** open Nuvolos again. In `dsap`, make a new
file `notes.py` that prints one line about your day. Run it. Commit it
(`bridge: notes`).

**Visit 2 (next week):** do the first two pages of
[futurecoder.io](https://futurecoder.io) — in the browser, nothing to
install. Then make `notes.py` print a second line, run, commit.

If either visit fails somewhere, that's *useful* — write down where it
stopped, bring it Sep 28, you will not be alone.

## Stretch (optional)

In the terminal, try `pwd` (print working directory) and `ls`
(list files). Then predict: what does `python ../dsap/hello.py` do —
and why does it work?
