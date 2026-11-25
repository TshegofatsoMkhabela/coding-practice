# loop-001-foundations - Grids & Loops (Foundations)

**Time limit: 60 minutes**

## Learning Outcomes Assessed

- Nested `for` loops over rows and columns
- Indexing a grid with 0-based `(row, col)` coordinates
- Turning a picture into a rule about `row` and `col`
- Printing grids with exact formatting (one space between cells, no trailing spaces)
- Controlling direction with `range(start, stop, step)`
- Rows of different lengths (triangles)
- Linux navigation, Python nested loops with `break`/`continue`

---

## Assessment Structure

The following assessment has two sections:

- Coding Assessment (Questions are below)
- Long Questions (Questions are below) - `answers.txt`

You can answer them in any order.

**Suggested time split (60 min):** Q1 5 min · Q2 6 min · Q3 9 min · Q4 9 min · Q5 11 min · Long questions 20 min (10 min each).

---

## Your Goal

Read the instructions below for each coding question, then complete each function in `loops.py` while making sure that:

- The code is valid Python
- Each function behaves according to the instructions
- All unit tests pass

Read the instructions below for each long-format question, then add your answer under each relevant comment in `answers.txt` while making sure that:

- You DO NOT remove the comments
- You read each question carefully before answering

**Rules for this assessment:** Every question must be solved with explicit loops. Do not use list comprehensions, and do not build rows with `*` (for example `"# " * n`). You may use `" ".join()` once per row.

**Planning routine (use it before every function):**

```
DRAW  -> sketch a small example on paper
INDEX -> write (row, col) on every cell
RULE  -> one sentence: "a cell is ... when ..."
TEST  -> read the matching test in tests/test_loops.py, run it, watch it fail
CODE  -> translate the rule into Python, run until green
```

**Output rules for every printing function:** one line per row, exactly ONE space between cells, NO trailing spaces.

---

## How to Run Your Tests

To run all your tests:

```
python3 -m pytest tests/test_loops.py
```

To run a specific test:

```
python3 -m pytest tests/test_loops.py::test_snake_walk_3_by_3
```

For more detail in the stack trace:

```
python3 -m pytest tests/test_loops.py -v --tb=long
```

---

## Scoring & Weighting

| Component | Weight |
|---|---|
| Coding Section (unit tests) | **50%** |
| Long-format Questions (answers.txt) | **50%** |

### Coding Section

Your coding score is the number of tests you pass.

Let:

- T = total number of coding tests
- P = number of tests you pass

```
Coding Score = (P / T) × 50%
```

### Long-format Section

Your long-format score is based on the quality and correctness of your written answers.

Let:

- Q = total marks available across all long-format questions (20)
- C = marks earned

```
Long-format Score = (C / Q) × 50%
```

### Final Score & Pass Mark

```
Final Score = Coding Score + Long-format Score
```

To pass, your Final Score must be **60% or higher**.

---

## Project Structure

```
loop-001-foundations/
├── loops.py              # <-- This is where you write your code
├── answers.txt           # <-- This is where you write your long-format answers
├── tests/
│   └── test_loops.py     # <-- These tests check your code
└── README.md             # <-- Assessment instructions (this file)
```

---

## Coding Assessment

This assessment has five Python functions about grids, shapes and walks, ordered from easiest to hardest. For some questions you will write the logic from scratch. For others, broken code has been provided. Your job is to find and fix everything that is wrong with it.

All grids use **0-based** `(row, col)` coordinates. `(0, 0)` is the top-left cell. `row` grows downwards and `col` grows to the right.

---

### Question 1 - `print_coordinates(width: int, height: int) -> None`

*Skill: INDEX. Every grid problem starts by knowing exactly which `(row, col)` each cell is.*

A township school is building a seating chart for exams. Write a function that prints the coordinate of every seat in a `width x height` grid, row by row.

- Each cell is written as `(row,col)` with **no space inside the brackets**
- Cells in the same row are separated by exactly one space
- If `width` or `height` is 0 or negative, print nothing

```
Input:  width=3, height=2
Output:
(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
```

```
Input:  width=1, height=3
Output:
(0,0)
(1,0)
(2,0)
```

> Notice which number changes along a row and which changes down a column.

---

### Question 2 - `checkerboard(width: int, height: int) -> None`

*Skill: RULE. Turn a picture into a one-sentence rule about `row` and `col`.*

A tiler in Soweto lays black and white tiles in a checkerboard pattern. The top-left tile is always black. Print the floor, using `#` for black and `.` for white.

```
Input:  width=4, height=3
Output:
# . # .
. # . #
# . # .
```

```
Input:  width=1, height=1
Output:
#
```

> Index the 4 x 3 example on paper first. What do `row` and `col` have in common on every `#` cell?

---

### Question 3 - `print_frame(width: int, height: int) -> None` - Debug This

*Skill: RULE + PRINT. Write the border rule correctly and get the formatting exactly right.*

A picture framer prints a preview of a frame. Cells on the outline are `#` and cells inside are `.`.

```
Input:  width=5, height=4
Output:
# # # # #
# . . . #
# . . . #
# # # # #
```

```
Input:  width=3, height=1
Output:
# # #
```

The function below has **four bugs**. None of them crash. All four produce output that looks almost right. Find and fix all of them.

```python
def print_frame(width, height):
    for row in range(1, height):
        line = ""
        for col in range(width):
            if row == 0 or row == height or col == 0 or col == width - 1:
                line = line + "#" + " "
            else:
                line = line + "."
        print(line)
```

> Run the broken version and compare its output to the expected output **character by character**. Spaces count.

---

### Question 4 - `snake_walk(width: int, height: int) -> list`

*Skill: PATH. Visit cells in a specific order by controlling the direction of `range()`.*

A farmer ploughs a field row by row. They go left-to-right along row 0, then **right-to-left** along row 1, then left-to-right along row 2, and so on, like a snake. Return the list of `(row, col)` cells **in the order they are ploughed**.

```
Input:  width=3, height=3
Output: [(0, 0), (0, 1), (0, 2),
         (1, 2), (1, 1), (1, 0),
         (2, 0), (2, 1), (2, 2)]
```

```
Input:  width=1, height=3
Output: [(0, 0), (1, 0), (2, 0)]
```

```
Input:  width=2, height=1
Output: [(0, 0), (0, 1)]
```

> Do not build a row and then call `.reverse()` or `reversed()`. Use `range()` with a step instead.

---

### Question 5 - `triangle_cells(height: int) -> list` - Debug This

*Skill: ROW LENGTHS. In a right-angled triangle, row `r` has `r + 1` cells (columns `0 .. r`).*

**Parameters:**

- `height: int` - number of rows in the triangle (0 or more)
- **returns** `list` - every cell of the triangle as `(row, col)` tuples, row by row, left to right

```
Input:  height=3
Output: [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2)]

Input:  height=1
Output: [(0, 0)]

Input:  height=0
Output: []
```

The code below runs without crashing on every input. Here is the odd part: it always returns the **right number** of cells, which is why the original developer thought it worked. There are **three bugs**. One is the root cause. Another was added later as a "fix" that covered up the root cause instead of solving it. Find the root cause first.

```python
def triangle_cells(height):
    cells = []
    for row in range(height + 1):
        for col in range(row):
            cells.append((col, row))
    return cells
```

> Draw the triangle for `height=3`, write `(row, col)` in every cell, then trace the broken loop and write down what it really produces.

---

## Long-Format Questions

Please answer these in the `answers.txt` file (**DO NOT REMOVE THE COMMENTS AND DO NOT CHANGE THE FORMAT**)

---

### Comprehension Question 1 - Linux: Navigating & Organising Files (10 Points)

You are on a Linux laptop at the WeThinkCode_ campus. Your home folder is `/home/you`. You want to set up a folder for practising the Halo Patterns workshop. Complete these tasks **in order**, starting from your home folder:

1. Show the full path of the folder you are currently in
2. Create the folder `practice/halo` inside your home folder **in one command**, even though `practice` does not exist yet
3. Move into `practice/halo`
4. Create an empty file called `square.py`
5. Make a copy of `square.py` called `rectangle.py`
6. Rename `rectangle.py` to `rect.py`
7. List the folder's contents in a way that shows each file's size and permissions, **including hidden files**
8. Return to your home folder using the shortest command you know

Describe **exactly how you would complete each task**: what command you would use, what it does, and why you chose it. Also explain the difference between an **absolute** path and a **relative** path, using one example of each from this scenario. Finally, explain what `.` and `..` mean.

---

### Comprehension Question 2 - Python Fundamentals: Nested Loops & `break` (10 Points)

A student wrote this code while practising for the Halo workshop:

```python
for row in range(3):
    for col in range(4):
        if col > row:
            break
        print(row, col)
```

a) Write down **exactly** what is printed, line by line. Then explain what shape of cells this produces and where you have seen that shape before. Do not run the code. Trace it by hand. (4 points)

b) When `break` runs, which loop does it stop: the inner loop, the outer loop, or both? How can you tell from the output in (a)? (2 points)

c) If `break` were replaced with `continue`, what would be printed instead? Explain why the output changes the way it does. (4 points)
