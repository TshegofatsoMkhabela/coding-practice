# CONTEXT BRIDGE - Loop Assessments (WeThinkCode_-style, 1 hour each)

Paste this whole file into any AI assistant (or Claude Code) to continue this work with full context.

---

## 0. Instructions for the AI receiving this file

1. **Do NOT give answers or solutions** to any question in this file, unless the learner explicitly asks for one specific question after attempting it. The learner asked for questions only. When helping, give hints, ask guiding questions, or point to the concept, never the finished code.
2. Keep the exact structure described in section 3 for any new assessment you create.
3. Keep the difficulty ladder: Foundations -> Core (matches the reference assessment) -> Stretch (slightly harder). Do not skip to advanced topics. Fundamentals must be rock-solid first.
4. Every coding question must have pytest tests. Tests must pass against a correct solution and fail against the starter code. Keep any reference solution private and do not show it to the learner.

---

## 1. Who the learner is and what they asked for

- The learner is starting the WeThinkCode_ (WTC) full-time programme in Johannesburg, South Africa. They want to build **first-principles Python problem-solving skills**: all the fundamental constructs and patterns needed to understand coding problems and solve them quickly.
- The theme is **LOOPS**, through grids, shapes and walks.
- Three assessments: one covering all fundamentals, one at the difficulty of the reference problem, and one slightly harder.
- **Don't give answers for any of them. Just the questions.**
- The **coding questions** are the **Halo Patterns** type (square / rectangle / triangle outlines, walks, runners). The FizzBuzz reference is **only** a template for the structure/format of an assessment.
- The **long (written) questions** focus on **Bash/Linux**, **Python fundamentals** (`break`, `continue`, aliasing, loop cost) and **Git**.
- Calibration: the **fun-000 assessment is the benchmark for 60 minutes**. Foundations may be at or under it. Core must **match** it. Stretch may run **up to about 15 minutes over**, with the extra coming from harder thinking per question, not more volume. Each assessment has **two** written questions (10 points each, Q = 20). The three areas rotate so each appears twice: A1 Linux + Python, A2 Python + Git, A3 Bash + Git.
- Gate before the stretch: finish Assessment 1 in ~45 min and Assessment 2 in ~60 min. If not, practise similar questions before attempting Assessment 3.

---

## 2. Theme material - "Halo Patterns" workshop

A "halo" is the outline of a shape with an empty middle. For every shape we answer the same three questions:

1. `halo`   - which cells are on the outline?          (a RULE)
2. `walk`   - in what order do we visit the outline?   (a PATH)
3. `runner` - where is a runner after n steps?         (PATH + MODULO + GRID)

The workshop builds these across a square (I do), a rectangle (you do), and a
right-angled triangle (you do), using the planning routine:
DRAW -> INDEX -> RULE -> TEST -> CODE. Output rule: one line per row, exactly
one space between cells, no trailing spaces.

---

## 3. Reference structure (WTC `fun-000-syntax-v2.2`)

Two sections: a coding assessment (five functions, easiest to hardest; some
from scratch, some "Debug This") and long-format questions in `answers.txt`
(do not remove the comments). Scoring: coding 50% (P/T), long-format 50%
(C/Q), pass mark 60%.

---

## 4. Skill map: what the Halo workshop builds

| Skill | What it trains |
|---|---|
| **INDEX** | 0-based coordinates; row = down, col = across |
| **RULE** | turning a picture into a true/false rule on `row`, `col` and the size |
| **PRINT** | nested loops, exact formatting (one space, no trailing spaces) |
| **ROW LENGTHS** | the inner loop's range depends on the outer loop variable |
| **PATH** | ordered traversal with `range(start, stop, step)`, exact stop values, no duplicates, thin shapes (1 x n) |
| **MODULO** | wrap-around with `%`, laps with `//`, mapping step count to a path index, overlaying a marker |
| **PLAN** | solving on paper before coding |

---

## 5. The three assessments in this folder

| # | Folder | Level | Coding questions (skill) | Written areas |
|---|--------|-------|--------------------------|---------------|
| 1 | `loop-001-foundations` | All fundamentals | `print_coordinates` (INDEX) · `checkerboard` (RULE) · `print_frame` debug, 4 bugs (RULE + PRINT) · `snake_walk` (PATH) · `triangle_cells` debug, 3 bugs root-cause + cover-up (ROW LENGTHS) | Linux navigation · nested loops + `break`/`continue` |
| 2 | `loop-002-core` | Same as fun-000 | `print_plus` (RULE, middle) · `hollow_inverted_triangle` (ROW LENGTHS + RULE) · `counter_clockwise_walk` debug, 4 bugs (PATH) · `runner_report` huge steps (MODULO) · `print_track` debug, 3 bugs one hides another (PRINT + overlay) | list aliasing, break vs return · Git branches & merging |
| 3 | `loop-003-stretch` | Slightly harder | `print_rings` (RULE generalised) · `print_hollow_diamond` (distance rule, rstrip) · `diagonal_walk` debug, 4 bugs (PATH by invariant) · `spiral_walk` (shrinking boundaries) · `print_two_runners` debug, 3 bugs (MODULO, negative index, check order) | Bash script with a for loop, chmod, subshell, `$?` · undoing in Git |

Test counts: 22 / 26 / 23. Every test was checked against a private correct
solution (all pass) and against the starter code (almost all fail). Solutions
are deliberately **not** included.

Ideas for further assessments: an equilateral pyramid (centred rows), a
triangle runner (rows of different lengths + modulo), multiple rings walked in
sequence, a "fill the halo" flood count, a zig-zag diagonal walk, and text-art
letters built from rules. A retired written question to reuse: "How much work
does a loop do?" (counting comparisons in a nested duplicate check, set vs list
lookup).
