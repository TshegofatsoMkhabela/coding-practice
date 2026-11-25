# Loop Assessments — WeThinkCode_-style, 1 hour each

First-principles Python problem-solving practice built around **loops**, through
grids, shapes and walks. Three timed assessments on a difficulty ladder, each
matching the structure of the WTC `fun-000-syntax` assessment.

## The three assessments

| # | Folder | Level | Target time |
|---|--------|-------|-------------|
| 1 | [`loop-001-foundations`](loop-001-foundations/) | All fundamentals | ~45 min |
| 2 | [`loop-002-core`](loop-002-core/) | Same level as `fun-000` | ~60 min |
| 3 | [`loop-003-stretch`](loop-003-stretch/) | Slightly harder | up to ~75 min |

Each assessment has:

- **5 coding questions** in `loops.py`, easiest to hardest. Q3 and Q5 are
  "Debug This" (broken code to find and fix).
- **2 long-format questions** in `answers.txt` (10 points each), rotating across
  Bash/Linux, Python fundamentals and Git.
- **pytest** tests in `tests/test_loops.py`.
- Scoring: coding 50%, long-format 50%, pass mark 60%.

## How to work through one

```bash
cd loop-001-foundations
python3 -m pytest tests/test_loops.py
```

Fill in `loops.py` and `answers.txt`. Run the tests until they pass.

## Gate before the stretch

Finish Assessment 1 in about 45 minutes and Assessment 2 in about 60 minutes.
If not, practise similar questions before attempting Assessment 3.

## Context

The full brief, theme material (the "Halo Patterns" workshop) and the skill map
are in [`CONTEXT_BRIDGE.md`](CONTEXT_BRIDGE.md). Reference solutions are
deliberately **not** included — these are practice assessments.
