# Session 1 workshop — the ledger, by hand

*Ungraded. You leave today having typed two short programs, predicted
what they print, and been wrong at least once on purpose.*

The next session is in two weeks (no class on 21 September). Today we
make sure everything works, and we do by hand what the lecture did on
the screen.

If you get stuck, raise your hand and say which **part** you are on.

---

## Part 1 — Open the editor

1. Open the enrolment link — https://app.eu1.nuvolos.cloud/enroll/class/OqWYtk7RxbA — and sign in with the email you use for Moodle.
   **Do this before Monday if you can.** It takes two minutes, and it is
   the one step that cannot be hurried in a room of 250 people.
2. Click the app called **VSCode**. Wait — the first start takes up to a
   minute. Do not click it again.
3. You now see the editor. Three areas matter today. **Left:** the list
   of files, called the Explorer. **Middle:** where you type.
   **Bottom:** where results appear after you run something.

✅ **Part 1 done** when you see the editor with the file list on the left.

---

## Part 2 — A folder, a file, a run

A **file** is text with a name, saved on the computer. A **folder** is
a list of files. A program is a file.

1. In the file list, right-click on the empty space → **New Folder**.
   Name it `dsap` — small letters, no spaces. Press Enter.
2. Right-click on `dsap` → **New File**. Name it `hello.py`. Press Enter.
   The ending `.py` tells the computer: *this file is a Python program.*
3. The file opens in the middle, empty. Type this exactly, including the
   quotation marks:

```python
print("hello")
```

4. **Save**: Cmd+S (Mac) or Ctrl+S (Windows). Look at the tab above the
   editor: before saving it shows a **white dot**, after saving the dot
   is gone. The dot means *"what you see is not yet saved."* The program
   you run is always the saved one.
5. Find the **▷ (play) button** at the top right. Click it. A panel
   opens at the bottom and after a moment shows:

```
hello
```

**You have written and run a program.**

6. Replace `hello` with your first name, keeping the quotation marks.
   **Do not save.** Click ▷. The old text appears — the dot is still on
   the tab. Save, run again: now your name. This is the most common
   mistake of the year; you have now made it on purpose.

✅ **Part 2 done** when `hello.py` prints your name.

---

## Part 3 — The ledger, by hand

In the lecture you voted on what this program prints. Now type it. Do
not copy and paste: typing is the point of this course, and the lecture
told you why.

1. New file in `dsap`: `ledger.py`. Type these ten lines (the blank
   lines too — they do nothing, they are for your eyes):

```python
ticker = "AAPL"
shares = 10
price = 190.50

value = shares * price
print("value at", price, "is", value)

price = 200.00
print("price is now", price)
print("value is still", value)
```

2. **Before you run it**, write on paper what the last line prints.
3. Save. Run. Compare with your paper:

```
value at 190.5 is 1905.0
price is now 200.0
value is still 1905.0
```

If you wrote `2000.0`: you read the program as Excel. `value = shares *
price` does not mean *"value is always shares times price"*. It means
*"work it out now, and call the answer `value`"*. Then it is done. The
price changed afterwards; `value` did not look back.

4. Now move one line. Cut `price = 200.00` and paste it **above**
   `value = shares * price`. Delete the two `print` lines that no longer
   make sense, so the file reads:

```python
ticker = "AAPL"
shares = 10
price = 190.50
price = 200.00

value = shares * price
print("value at", price, "is", value)
```

Save, run:

```
value at 200.0 is 2000.0
```

Two versions. Both run without any error. Only one of them is your
portfolio. **Nothing on the computer checks which** — that is what the
lecture called *runs and lies*, and it is what you are here to learn to
see.

5. Add two lines at the very end: `shares = shares + 5`, then
   `print(shares)`. Predict, run. Read the first one from right to
   left: *take what `shares` is, add five, put it back under the name
   `shares`.* It is an instruction, not an equation.

✅ **Part 3 done** when you have seen `1905.0` and `2000.0` from the same
ten lines, and predicted the last one correctly.

---

## Part 4 — Calling things

Look at what you have typed so far. Every line that *does* something
has the same shape:

```python
print("value at", price, "is", value)
```

A **name**, then **parentheses**, and inside them what you hand over,
separated by commas. That is a **call**. `print` is not a magic word;
it is a piece of code somebody else wrote, and the parentheses are how
you run it with your own values. Everything in Python that does work
looks like this. Libraries, which the lecture called the reason Python
won, are shelves of things to call.

There are two kinds. `print` **does** something — text appears. Others
**give something back**, and that is where today's problem hides.

1. New file in `dsap`: `portfolio.py`. Type:

```python
aapl = 10 * 190.50
nesn = 4 * 102.30
voo = 2 * 512.00

total = aapl + nesn + voo
print("total:", total)

share = nesn / total * 100
print("NESN share, in percent:", share)
```

Save, run:

```
total: 3338.2
NESN share, in percent: 12.258103169372717
```

That last number is correct and unreadable. Python has `round` for
this: hand it a number and how many decimals you want, and it gives
back the rounded number.

2. Leave one blank line, then add two lines at the end:

```python
round(share, 2)
print("rounded:", share)
```

Predict. Save, run:

```
total: 3338.2
NESN share, in percent: 12.258103169372717
rounded: 12.258103169372717
```

**Nothing changed.** No error, either. `round` did its job and handed
back `12.26` — and nobody took it. A value that comes back from a call
is not kept anywhere unless you give it a name. The line did work and
threw the result away.

3. Fix the line so the answer is kept:

```python
share = round(share, 2)
print("rounded:", share)
```

```
rounded: 12.26
```

Same `=` as before: *call `round`, take what comes back, put it under
the name `share`.* This is the second thing today that ran perfectly and
lied. Code written by a chatbot does this one all the time.

✅ **Part 4 done** when `rounded: 12.26` appears, and you can say why the
earlier version printed the long number.

---

## Part 5 — Break it, three ways

The lecture said code fails in three ways. You have already met the
worst one — it runs and lies — twice. Now the other two, on purpose,
because you will see them every week and they are the harmless ones.

1. **It won't start.** In `hello.py`, delete the second quotation mark.
   Save, run. Red text. Do not read it all; read only the **last line**:

```
SyntaxError: unterminated string literal (detected at line 1)
```

Python could not understand line 1, so it did not run anything at all.
Put the quotation mark back.

2. **It crashes.** In `portfolio.py`, change the last line to
   `print("rounded:", shar)` — one letter missing. Save, run:

```
total: 3338.2
NESN share, in percent: 12.258103169372717
Traceback (most recent call last):
  File "/files/dsap/portfolio.py", line 12, in <module>
    print("rounded:", shar)
                      ^^^^
NameError: name 'shar' is not defined. Did you mean: 'share'?
```

Two lines printed **before** it stopped: the program ran top to bottom
until line 12, then hit a name it had never seen. The last line says
what went wrong and even guesses the fix. Fix it.

Every error you ever see will look like this: some lines, then a last
line that says what is wrong. **Read the last line first.** Always.

✅ **Part 5 done** when you have seen both messages and both files run
again.

---

## Before 28 September

Come back once, on any day, for ten minutes: open Nuvolos, open VSCode,
open `portfolio.py`, change a number, save, run. If it works, you are
ready for session 2. If it does not, write down what the screen said
and bring it.

---

## If you finished early

- In `portfolio.py`, add a fourth position — `msft = 3 * 410.00` — and
  put it into `total`. What happens to the NESN share? Predict first.
- In a new file, `print(0.1 + 0.2)`. You saw this on a slide; now it is
  your computer saying it.
- New file `me.py`: print three lines — your name, your programme, and
  one number you calculated, for example the days until the end of the
  semester.
