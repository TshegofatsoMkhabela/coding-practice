# loop-002-core - Grids & Loops (Core)

**Time limit: 60 minutes**

## Learning Outcomes Assessed

- Finding the middle and the slope of a shape, and writing it as a rule
- Rows of different lengths, with a hollow outline
- Walking an outline in a given direction with exact `range()` boundaries
- Modulo (`%`) and floor division (`//`) for wrap-around and laps
- Overlaying markers on a printed grid (order of checks matters)
- Python list aliasing and `break` vs `return`, Git branches

---

## Assessment Structure

The following assessment has two sections:

- Coding Assessment (Questions are below)
- Long Questions (Questions are below) - `answers.txt`

You can answer them in any order.

**Suggested time split (60 min):** Q1 6 min · Q2 8 min · Q3 9 min · Q4 8 min · Q5 9 min · Long questions 20 min (10 min each).

---

## Your Goal

Read the instructions below for each coding question, then complete each function in `loops.py` while making sure that:

- The code is valid Python
- Each function behaves according to the instructions
- All unit tests pass

Read the instructions below for each long-format question, then add your answer under each relevant comment in `answers.txt` while making sure that:

- You DO NOT remove the comments
- You read each question carefully before answering

**Rules for this assessment:** Every question must be solved with explicit loops. Do not use list comprehensions, `itertools`, or `*` to build rows. You may use `" ".join()` once per row.

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
python3 -m pytest tests/test_loops.py::test_runner_report_huge_steps_is_fast
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
loop-002-core/
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

### Question 1 - `print_plus(size: int) -> None`

*Skill: RULE. Find the middle of a grid and describe a shape using it.*

The Red Cross in Durban needs a plus sign for a banner. Print a `size x size` grid where cells on the **middle row** or the **middle column** are `#`, and every other cell is `.`. `size` is always an **odd** number of 1 or more.

```
Input:  5
Output:
. . # . .
. . # . .
# # # # #
. . # . .
. . # . .
```

```
Input:  1
Output:
#
```

> For `size=5` the middle index is 2. Write a rule for the middle index that works for **any** odd size.

---

### Question 2 - `hollow_inverted_triangle(height: int) -> None`

*Skill: ROW LENGTHS + RULE. Rows get shorter, and the outline follows a slope.*

Print a hollow right-angled triangle that is **upside down**. Row 0 is the longest and the last row has a single cell.

- Row `r` has `height - r` cells (columns `0 .. height - 1 - r`)
- A cell is `#` if it is on the outline: the **top row**, the **left column**, or the **slope** (the last cell of each row)
- Every other cell is a space `" "`
- If `height` is 0 or negative, print nothing

```
Input:  5
Output:
# # # # #
#     #
#   #
# #
#
```

```
Input:  2
Output:
# #
#
```

> Index `height=5` on paper. On the slope, what do `row + col` always add up to?

---

### Question 3 - `counter_clockwise_walk(width: int, height: int) -> list` - Debug This

*Skill: PATH. Walk an outline in a new direction, using `range()` stop values that are exactly right.*

A security guard patrols the outer edge of a parking lot, going **counter-clockwise** from the top-left corner `(0, 0)`. They walk **down** the left side, **right** along the bottom, **up** the right side, and **left** along the top until the cell just before `(0, 0)`. Return the outline cells in the order they are visited. **No cell may appear twice.** `width` and `height` are always **at least 2**.

```
Input:  width=4, height=3
Output: [(0, 0), (1, 0), (2, 0),
         (2, 1), (2, 2), (2, 3),
         (1, 3), (0, 3),
         (0, 2), (0, 1)]
```

```
Input:  width=2, height=2
Output: [(0, 0), (1, 0), (1, 1), (0, 1)]
```

The function below has **four bugs**. One crashes on every call. One crashes only on lots wide enough for the top leg to run. Two never crash but give the wrong path. Find and fix all of them.

```python
def counter_clockwise_walk(width, height):
    path = []
    for row in range(height):
        path.append((row, 0))
    for col in range(1, width):
        path.append((height - 1, col))
    for row in range(height - 2, 0, -1):
        path.append((row, width))
    for col in range(width - 2, 0, -1):
        path.append[(0, col)]
    return pth
```

---

### Question 4 - `runner_report(width: int, height: int, steps: int) -> tuple`

*Skill: MODULO. Map any number of steps onto a path that repeats.*

A runner trains around the outline of a `width x height` field. They start on `(0, 0)` and run **clockwise**: along the top row to the right, down the right side, left along the bottom, and up the left side. One move takes them to the next outline cell. After a full lap they are back on `(0, 0)`.

Return a tuple `(row, col, laps)` where `(row, col)` is the cell the runner is on after `steps` moves, and `laps` is the number of **complete** laps they have finished. `width` and `height` are always **at least 2**. `steps` is 0 or more.

The helper `clockwise_walk(width, height)` is **provided** in `loops.py` and is correct. It returns the outline cells in running order, starting with `(0, 0)`. Use it. Do not rewrite it. This question tests **modulo**, not walking.

```
Input:  width=4, height=3, steps=5
Output: (2, 3, 0)

Input:  width=4, height=3, steps=10
Output: (0, 0, 1)

Input:  width=4, height=3, steps=23
Output: (0, 3, 2)

Input:  width=6, height=4, steps=9
Output: (3, 4, 0)
```

> `steps` can be as large as `1_000_000_000_000`. Your function must still answer instantly, so you **cannot** move the runner one step at a time. How long is the path? What do `%` and `//` tell you?

---

### Question 5 - `print_track(width: int, height: int, runner: tuple) -> None` - Debug This

**Parameters:**

- `width: int`, `height: int` - size of the track (both at least 2)
- `runner: tuple` - the runner's position as `(row, col)`. It is always a cell **on the outline**.
- **returns** `None` - prints the track

The track is printed with `o` for every outline cell, `@` for the runner's cell, and a space `" "` for cells inside the track.

```
Input:  width=6, height=4, runner=(3, 4)
Output:
o o o o o o
o         o
o         o
o o o o @ o
```

```
Input:  width=3, height=3, runner=(1, 0)
Output:
o o o
@   o
o o o
```

The code below runs without crashing on every input. There are **three bugs**. One of them **hides** another: you will not be able to see the second bug until you fix the first. Find the hiding bug first.

```python
def print_track(width, height, runner):
    c, r = runner
    for row in range(height):
        cells = []
        for col in range(width):
            if row == 0 or row == height or col == 0 or col == width - 1:
                cells.append("o")
            elif row == r and col == c:
                cells.append("@")
            else:
                cells.append(" ")
        print(" ".join(cells))
```

---

## Long-Format Questions

Please answer these in the `answers.txt` file (**DO NOT REMOVE THE COMMENTS AND DO NOT CHANGE THE FORMAT**)

---

### Comprehension Question 1 - Python Fundamentals: Building Grids Safely (10 Points)

A student wants a 3 x 3 grid of `.` so they can place a runner on it:

```python
grid = [["."] * 3] * 3
grid[0][0] = "@"
for row in grid:
    print(" ".join(row))
```

a) Predict **exactly** what is printed. Then explain **why** it happens. Your answer must use the words *reference* (or *alias*) and *list*. (4 points)

b) Write a version that builds the same 3 x 3 grid using **two loops**. Explain why your version does not have the problem from (a). (3 points)

c) The student searches the grid for the `@` with a nested loop. Explain the difference between using `break` and using `return` to stop once the `@` is found, if the search is inside a function. Which one stops **both** loops, and why? (3 points)

---

### Comprehension Question 2 - Git: Branches & Merging (10 Points)

You want to try a new idea for `runner_report` without risking the version on `main` that already passes its tests.

1. Create a new branch called `runner-modulo` and switch to it in **one** command
2. List all local branches and show which one you are on
3. After committing your new idea on `runner-modulo`, switch back to `main`
4. Bring the commits from `runner-modulo` into `main`
5. Delete the `runner-modulo` branch now that it has been merged

a) For each task, give the exact command and explain what it does. (5 points)

b) What is a **merge conflict**? Describe a realistic way one could happen in this assessment's `loops.py`, and the steps you would take to resolve it. (3 points)

c) Why is working on a branch safer than experimenting directly on `main`? (2 points)
