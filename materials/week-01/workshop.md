# Session 1 workshop — your workspace, your first program, your first error

*Ungraded, self-checked. You leave with a working workspace, a program
you typed and ran, an error you read and fixed, and — if there is time —
your first commit. Nothing else today.*

**Why this session is only this.** The next session is two weeks away
(no class on 21 September). If your workspace does not work today, you
have no way to find out until 28 September. So today we make sure it
does, and we prove it by using it.

**How to ask for help.** Raise your hand and keep working on the next
step you can do. Three of us are walking the room for 250 people. If you
are stuck at a checkpoint, say which one — "I'm stuck at checkpoint 2"
tells us everything.

---

## Checkpoint 1 — Get in (until about 14:55)

You pass this checkpoint when you can see **a folder called `dsap`** in
the left-hand panel of VS Code, inside your browser.

1. **Enrol in the course workspace.** Use the Nuvolos link on Moodle.
   Sign in with your UNIL email. If it asks you to create an account,
   create it with the same email.
2. **Open the app called "VSCode".** Not "Terminal", not "Claude Code",
   not "Codex" — those exist and we will meet them later. VSCode. It
   takes up to a minute to start the first time.
3. You now see an editor in your browser. On the left is a panel with
   files in it: the **Explorer**. It may show a `README.md` and not much
   else. That is correct.
4. **Make a folder.** Right-click in the empty space of the Explorer →
   **New Folder** → type `dsap` → Enter. All lowercase. Everything you
   make in this course goes in here.
5. **Open a terminal.** Top menu → Terminal → New Terminal. A dark
   panel appears at the bottom with a blinking cursor. This is where you
   run programs. Type the following and press Enter:
   ```
   cd dsap
   ```
   The line now ends with `dsap`. That means the terminal is *standing
   in* your folder. Programs run from wherever the terminal stands.

☐ **Checkpoint 1 passed:** `dsap` is in the Explorer, and the terminal
line ends with `dsap`.

If this took you the whole time, that is fine. Everything below is on
the course site; do it before 28 September and you have lost nothing.

---

## Checkpoint 2 — Make one thing run (about 15 min)

You pass when a program you typed prints a line.

1. Right-click the `dsap` folder → **New File** → name it `hello.py`.
   The `.py` matters: it tells VS Code and Python what this file is.
2. Type this **exactly**, including the quotes:
   ```python
   print("hello from my workspace")
   ```
3. **Save.** Cmd-S on a Mac, Ctrl-S on Windows. Look at the file's tab
   at the top of the editor. A **white dot** means unsaved. A dot
   means Python cannot see your latest text — it reads the *disk*, not
   the screen. Save until the dot is gone.
4. In the terminal:
   ```
   python hello.py
   ```
   It prints `hello from my workspace`.
5. Change the message to anything you like. Save. Run again. Confirm it
   changed. Now do it once more but **do not save** before running.
   The old message prints. That is the dot lesson, and it costs people
   hours every year. You have now paid for it in one minute.

☐ **Checkpoint 2 passed:** you ran `hello.py` twice with two different
messages.

---

## Checkpoint 3 — Break it on purpose, and read what it says (about 20 min)

You pass when you can point at a line in an error message and say what
it is telling you. This is the most important thing you will do today.

**3a — an error before the program even starts.**

1. In `hello.py`, delete the **closing** quote mark, so the line reads
   `print("hello from my workspace)`. Save. Run.
2. Python refuses. Read the message from the **bottom up**. The last
   line names the kind of problem: `SyntaxError`. Above it, Python shows
   the line and points at where it gave up.
3. Write on your worksheet: *which line number did it name?*
4. Put the quote back. Save. Run. It works again.

**3b — a program that starts, then fails.**

Now a program that reads a data file. First, make the data.

1. New file in `dsap`: `ledger.csv`. Type these four lines exactly:
   ```
   ticker,shares,price
   AAPL,10,190.50
   NESN,4,102.30
   VOO,2,512.00
   ```
   Save. This is a tiny portfolio: three holdings, with the number of
   shares and the price of each. It is the data this whole course is
   built on, and you just made it by hand.
2. New file: `ledger.py`. Type:
   ```python
   print("DSAP ledger, version 0")
   line = open("ledger.csv").readline()
   print("first line of the ledger:", line.strip())
   print("done")
   ```
   Save. Run: `python ledger.py`. Three lines print. Write down the
   second one.
3. **Before you do the next step, write on your worksheet what you
   think will happen.** Then: go one folder up and run it from there.
   ```
   cd ..
   python dsap/ledger.py
   ```
4. Read the error from the bottom up. The last line is
   `FileNotFoundError` and it names the file it could not find.
   Look at what printed *before* the error: the first line of the
   program ran fine. The program did not fail because the code is wrong.
   It failed because **it was standing in the wrong place** — the
   terminal was in `files`, and `ledger.csv` is in `files/dsap`.
5. Was your prediction right? Either answer is fine. Write one sentence:
   why did the first `print` work and the second line not?
6. Go back: `cd dsap`. Run `python ledger.py`. Works.

☐ **Checkpoint 3 passed:** you have seen two different errors, and you
can say in one sentence what each one was about.

> **The rule to take home:** a program that runs is not a program that
> is right, and a program that fails is not always wrong. This one was
> correct both times. Only where it stood changed.

---

## Checkpoint 4 — Ask an assistant, properly (about 10 min)

Any free chatbot will do. Open one in a second browser tab. If you do
not have an account, make one now — you use it all semester.

1. Copy the **whole** error text from checkpoint 3b — every line, from
   `Traceback` to the end.
2. Paste it, and add one line above it:
   *"I am a beginner. Explain this error in plain words. What should I
   check first?"*
3. Read the answer. Does it tell you to check **where you ran the
   program from**, or does it tell you to change the code?
4. Write one sentence on your worksheet: did the assistant understand
   that the code was fine?

The assistant never saw your folders. It saw exactly what you pasted,
nothing more. When its answer is good, it is because you gave it the
whole error. When its answer is wrong, it is usually because it is
guessing about something you did not paste.

> **When you ask an assistant for code, the six words:**
> **Frame · Ask · Run · Read · Judge · Keep.**
> Say what should go in and come out, and one fact you can check by hand
> (Frame). Ask. Run it on real data. Read the lines that do the work.
> Judge it against the fact you chose. Then commit (Keep).
> A mnemonic, not a procedure — use it when you are stuck on how to ask.

☐ **Checkpoint 4 passed:** you pasted a full error and got a useful
answer.

---

## Checkpoint 5 — Save proof (if there is time; otherwise do it in the bridge)

Git is a save button that remembers every version. You will use it at
the end of every workshop. Today you only set it up and press it once.

1. Left sidebar → the **Source Control** icon (three connected dots).
2. Click **Initialize Repository**. If it asks which folder, choose
   `dsap`.
3. In the terminal, tell git who you are. Two lines, with **your**
   name and UNIL email:
   ```
   git config --global user.name "Your Name"
   git config --global user.email "your.name@unil.ch"
   ```
4. Back in Source Control: in the message box type `session 1: first
   run`. Click **Commit**. If it asks whether to stage all changes,
   say yes.
5. The list of changed files is now empty. That is what "saved" looks
   like in git.

☐ **Checkpoint 5 passed:** Source Control shows no changes, and your
message is in the history.

---

## Self-check — write your answers, then unfold

- S1. What did `ledger.py` print on its second line?
- S2. Which error came from the missing quote, and which from running
  in the wrong folder? Give the two error names.
- S3. True or false: when you ran `hello.py` without saving, the file
  on disk already had your new text.

<details><summary>Answers (only after writing yours)</summary>

- S1: `first line of the ledger: ticker,shares,price`
- S2: missing quote → `SyntaxError`; wrong folder → `FileNotFoundError`
- S3: False. The editor had it; the disk did not. The dot on the tab
  told you so.

</details>

---

## The bridge — before 28 September

There is no class on 21 September. Two weeks is long enough to forget
where the terminal is. Two short visits keep your hands warm, and each
one proves your workspace still works.

**Visit 1 (this week, 20 min).** Open Nuvolos → VSCode. In `dsap`,
make `notes.py`. Make it print two lines: one about anything, one that
prints the number of holdings in the ledger — which you can count by
looking at `ledger.csv`. Run it. If you did checkpoint 5, commit it with
the message `bridge: notes`. If you did not, do checkpoint 5 now; it is
above.

**Visit 2 (next week, 20 min).** Do the first two pages of
[futurecoder.io](https://futurecoder.io) in your browser — nothing to
install. Then go back to `notes.py`, add a third line, run, commit.

If either visit fails somewhere, that is useful. Write down exactly
where it stopped and what the screen said, and bring it on 28 September.
You will not be the only one.

---

## Stretch (optional, for the curious)

In the terminal, `pwd` prints where you are standing and `ls` lists
what is there. Try both in `dsap` and in `files`. Then predict, before
running: from inside `dsap`, what does `python ../dsap/hello.py` do,
and why does it work when `python dsap/ledger.py` from `files` did not?
