"""loop-002-core - Grids & Loops (Core)

Complete each function below. Do not rename functions or change their parameters.
Run the tests with:  python3 -m pytest tests/test_loops.py -v

Output rules for printing functions:
    one line per row, exactly ONE space between cells, NO trailing spaces.
"""


# ---------------------------------------------------------------------------
# Question 1 - RULE
# ---------------------------------------------------------------------------
def print_plus(size: int) -> None:
    """Print a plus sign: '#' on the middle row or middle column, '.' elsewhere.
    size is always odd.

    print_plus(5)
    . . # . .
    . . # . .
    # # # # #
    . . # . .
    . . # . .
    """
    pass


# ---------------------------------------------------------------------------
# Question 2 - ROW LENGTHS + RULE
# ---------------------------------------------------------------------------
def hollow_inverted_triangle(height: int) -> None:
    """Print an upside-down hollow right-angled triangle.
    Row r has height - r cells.

    hollow_inverted_triangle(5)
    # # # # #
    #     #
    #   #
    # #
    #
    """
    pass


# ---------------------------------------------------------------------------
# Question 3 - Debug This (four bugs)
# ---------------------------------------------------------------------------
def counter_clockwise_walk(width: int, height: int) -> list:
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


# ---------------------------------------------------------------------------
# Question 4 - MODULO
# ---------------------------------------------------------------------------
def clockwise_walk(width: int, height: int) -> list:
    """PROVIDED - this helper is correct. Do not change it.
    Returns the outline cells clockwise from (0, 0) for width, height >= 2.
    """
    path = []
    for col in range(width):
        path.append((0, col))
    for row in range(1, height):
        path.append((row, width - 1))
    for col in range(width - 2, -1, -1):
        path.append((height - 1, col))
    for row in range(height - 2, 0, -1):
        path.append((row, 0))
    return path


def runner_report(width: int, height: int, steps: int) -> tuple:
    """RETURN (row, col, laps) for a runner going clockwise from (0, 0).
    Use clockwise_walk(). Must work instantly for huge values of steps.

    runner_report(4, 3, 23) -> (0, 3, 2)
    """
    pass


# ---------------------------------------------------------------------------
# Question 5 - Debug This (three bugs, one hides another)
# ---------------------------------------------------------------------------
def print_track(width: int, height: int, runner: tuple) -> None:
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
