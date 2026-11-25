# loop-003-stretch - Grids & Loops (Stretch)

**Time limit: 60 minutes** (stretch assessment: finishing up to 15 minutes over is acceptable. Note how long you took.)

## Learning Outcomes Assessed

- Generalising a border rule to every ring of a grid
- Distance-based rules (`abs()`) and trimming output correctly
- Paths defined by an invariant (`row + col` on a diagonal)
- Spiral walks with four shrinking boundaries and thin leftovers
- Two runners in opposite directions, with modulo on negative indexes
- Bash scripts with loops and exit codes, undoing in Git

---

## Assessment Structure

The following assessment has two sections:

- Coding Assessment (Questions are below)
- Long Questions (Questions are below) - `answers.txt`

You can answer them in any order.

**Suggested time split (60 min):** Q1 7 min · Q2 8 min · Q3 9 min · Q4 15 min · Q5 9 min · Long questions 20 min (10 min each). Total: about 68 min.

---

## Your Goal

Read the instructions below for each coding question, then complete each function in `loops.py` while making sure that:

- The code is valid Python
- Each function behaves according to the instructions
- All unit tests pass

Read the instructions below for each long-format question, then add your answer under each relevant comment in `answers.txt` while making sure that:

- You DO NOT remove the comments
- You read each question carefully before answering

**Rules for this assessment:** Every question must be solved with explicit loops. Do not use list comprehensions, `sorted()`, `.sort()`, `zip()` or `itertools`. Do not import anything. `min()`, `max()` and `abs()` are allowed.

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
python3 -m pytest tests/test_loops.py::test_spiral_walk_every_cell_once
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
loop-003-stretch/
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

### Question 1 - `print_rings(width: int, height: int) -> None`

*Skill: RULE, generalised. The halo is ring 0. Now describe every ring at once.*

A landscaper in Pretoria plants concentric flower beds in a rectangular garden. The outermost outline of cells is ring `0`. The outline just inside it is ring `1`, and so on towards the centre. Print the garden with every cell showing **its ring number**.

`width` and `height` are between 1 and 19, so every ring number is a single digit.

```
Input:  width=5, height=4
Output:
0 0 0 0 0
0 1 1 1 0
0 1 1 1 0
0 0 0 0 0
```

```
Input:  width=7, height=7
Output:
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 1 2 2 2 1 0
0 1 2 3 2 1 0
0 1 2 2 2 1 0
0 1 1 1 1 1 0
0 0 0 0 0 0 0
```

> For any cell, how far is it from the top edge? The bottom edge? The left edge? The right edge? Which of those four distances is its ring number?

---

### Question 2 - `print_hollow_diamond(radius: int) -> None`

*Skill: RULE with distance. Some shapes are easier to describe by distance from the centre than by edges.*

Print a hollow diamond inside a square grid of size `2 * radius + 1`. The centre cell is `(radius, radius)`. A cell is `#` if it is **exactly** `radius` steps from the centre, counting only up/down and left/right moves. Every other cell is a space.

Because the right-hand side of most rows is empty, each printed line must **end at its last `#`**. There must be no trailing spaces.

```
Input:  2
Output:
    #
  #   #
#       #
  #   #
    #
```

```
Input:  0
Output:
#
```

> "Steps from the centre, moving only up/down/left/right" is `abs(row - radius) + abs(col - radius)`. Check it on paper for `radius=2` before coding.

---

### Question 3 - `diagonal_walk(size: int) -> list` - Debug This

*Skill: PATH by invariant. On a diagonal, `row + col` is the same for every cell (remember the triangle slope hint).*

An image scanner reads a `size x size` grid **one diagonal at a time**. First it reads all cells where `row + col == 0`, then all cells where `row + col == 1`, then `== 2`, and so on until the bottom-right corner. Within each diagonal it reads the cell with the **smaller row first**. Return the cells in scanning order.

```
Input:  size=3
Output: [(0, 0),
         (0, 1), (1, 0),
         (0, 2), (1, 1), (2, 0),
         (1, 2), (2, 1),
         (2, 2)]
```

```
Input:  size=1
Output: [(0, 0)]
```

The function below has **four bugs**. One crashes whenever a cell is added. Three never crash but give the wrong path: one skips a whole diagonal, one skips a cell on every diagonal, and one lets cells from outside the grid in. Find and fix all of them.

```python
def diagonal_walk(size):
    cells = []
    for d in range(2 * size - 2):
        for row in range(d):
            col = d - row
            if col < size or row < size:
                cells.append(row, col)
    return cells
```

---

### Question 4 - `spiral_walk(width: int, height: int) -> list`

*Skill: PATH with shrinking boundaries. A spiral is a halo walk, then the next ring's halo walk, then the next.*

A robot vacuum cleans a rectangular room in a clockwise spiral. It starts at `(0, 0)` and goes right along the top, down the right side, left along the bottom, and up the left side. It then turns inward and repeats on the next ring, until **every cell has been visited exactly once**. Return the cells in the order visited.

```
Input:  width=4, height=3
Output: [(0, 0), (0, 1), (0, 2), (0, 3),
         (1, 3), (2, 3),
         (2, 2), (2, 1), (2, 0),
         (1, 0),
         (1, 1), (1, 2)]
```

```
Input:  width=3, height=3
Output: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0), (1, 1)]
```

```
Input:  width=1, height=3
Output: [(0, 0), (1, 0), (2, 0)]
```

> Keep four boundaries, `top`, `bottom`, `left` and `right`, and move them inward after each leg. The hardest cases are the thin leftovers in the middle, such as a single row or a single column. Test `width=4, height=3` and `width=3, height=4` by drawing them.

---

### Question 5 - `print_two_runners(width: int, height: int, steps_a: int, steps_b: int) -> None` - Debug This

**Parameters:**

- `width: int`, `height: int` - size of the track (both at least 2)
- `steps_a: int` - how many moves runner **A** has made. A starts on `(0, 0)` and runs **clockwise**.
- `steps_b: int` - how many moves runner **B** has made. B also starts on `(0, 0)` but runs **counter-clockwise**.
- **returns** `None` - prints the track

Print the outline with `o`, runner A's cell as `A`, runner B's cell as `B`, and `X` if both runners are on the **same** cell. Inside cells are spaces. The helper `clockwise_walk` is provided in `loops.py` and is **correct**, so do not change it.

```
Input:  width=5, height=3, steps_a=2, steps_b=3
Output:
o o A o o
o       o
o B o o o
```

```
Input:  width=5, height=3, steps_a=6, steps_b=6
Output:
o o o o o
o       o
o o o o X
```

```
Input:  width=5, height=3, steps_a=25, steps_b=13
Output:
o A o o o
B       o
o o o o o
```

There are **three bugs**. Two of them come from the **same** missing idea and only crash on some inputs. The third never crashes, but it means one of the symbols can **never** be printed.

```python
def print_two_runners(width, height, steps_a, steps_b):
    path = clockwise_walk(width, height)
    a = path[steps_a]
    b = path[-steps_b]
    for row in range(height):
        cells = []
        for col in range(width):
            if (row, col) == a:
                cells.append("A")
            elif (row, col) == b:
                cells.append("B")
            elif (row, col) == a and (row, col) == b:
                cells.append("X")
            elif row == 0 or row == height - 1 or col == 0 or col == width - 1:
                cells.append("o")
            else:
                cells.append(" ")
        print(" ".join(cells))
```

> Why does `path[-steps_b]` give the right cell for small values of `steps_b`? What happens when B has run more than one lap?

---

## Long-Format Questions

Please answer these in the `answers.txt` file (**DO NOT REMOVE THE COMMENTS AND DO NOT CHANGE THE FORMAT**)

---

### Comprehension Question 1 - Bash: Scripts, Loops & Exit Codes (10 Points)

You have all three loop assessments in one folder:

```
loop-assessments/
├── loop-001-foundations/
├── loop-002-core/
└── loop-003-stretch/
```

You want **one command** that runs the tests of all three assessments, one after another. You write this script and save it as `run_all.sh` inside `loop-assessments/`:

```bash
#!/bin/bash
for folder in loop-00*/; do
    echo "=== $folder ==="
    (cd "$folder" && python3 -m pytest tests/test_loops.py -q)
done
```

a) Explain what **every** line of the script does, including `#!/bin/bash`, `loop-00*/`, `$folder` and the `do ... done` block. (4 points)

b) You type `./run_all.sh` and get `Permission denied`. Explain why, the exact command that fixes it, and what that command changes about the file. (2 points)

c) The `cd` is wrapped in round brackets `( ... )` and joined to pytest with `&&`. Explain what each of those does, and what would go wrong on the **second** pass of the loop if the brackets were removed. (2 points)

d) After a command runs, `echo $?` prints a number. What is that number, what does `0` mean, and how could a script use it to stop at the first failing assessment? (2 points)

---

### Comprehension Question 2 - Git: Undoing Things Safely (10 Points)

You are working on `spiral_walk`. Each scenario below needs a different way of undoing. For each one, give the exact command, explain what it does, and say whether it can **permanently destroy work**.

1. You have changed `loops.py` but not staged it. You want to throw away **only** those changes and get back the last committed version
2. You ran `git add answers.txt` by mistake and want to **unstage** it, but keep your edits
3. You made a commit with a typo in the message and have **not** pushed it yet. You want to fix the message
4. A commit that is **already pushed** to the shared remote broke the tests. You want to undo its changes without rewriting history
5. You want to see what changed in the last 3 commits, one line each

a) Commands and explanations for the five scenarios. (5 points)

b) Explain the difference between `git revert` and `git reset --hard`. Why is `reset --hard` dangerous on a branch other people have pulled? (3 points)

c) What makes a commit message good? Give one good and one bad example for a commit that fixes the thin-row bug in `spiral_walk`. (2 points)
