"""loop-001-foundations - Grids & Loops (Foundations)

Complete each function below. Do not rename functions or change their parameters.
Run the tests with:  python3 -m pytest tests/test_loops.py -v

Output rules for printing functions:
    one line per row, exactly ONE space between cells, NO trailing spaces.
"""


# ---------------------------------------------------------------------------
# Question 1 - INDEX
# ---------------------------------------------------------------------------
def print_coordinates(width: int, height: int) -> None:
    """Print "(row,col)" for every cell, row by row.

    print_coordinates(3, 2)
    (0,0) (0,1) (0,2)
    (1,0) (1,1) (1,2)
    """
    pass


# ---------------------------------------------------------------------------
# Question 2 - RULE
# ---------------------------------------------------------------------------
def checkerboard(width: int, height: int) -> None:
    """Print a checkerboard: '#' and '.', top-left cell is '#'.

    checkerboard(4, 3)
    # . # .
    . # . #
    # . # .
    """
    pass


# ---------------------------------------------------------------------------
# Question 3 - Debug This (four bugs)
# ---------------------------------------------------------------------------
def print_frame(width: int, height: int) -> None:
    for row in range(1, height):
        line = ""
        for col in range(width):
            if row == 0 or row == height or col == 0 or col == width - 1:
                line = line + "#" + " "
            else:
                line = line + "."
        print(line)


# ---------------------------------------------------------------------------
# Question 4 - PATH
# ---------------------------------------------------------------------------
def snake_walk(width: int, height: int) -> list:
    """RETURN the cells in snake order: row 0 left-to-right, row 1 right-to-left, ...

    snake_walk(3, 3) -> [(0, 0), (0, 1), (0, 2), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2)]
    """
    pass


# ---------------------------------------------------------------------------
# Question 5 - Debug This (three bugs, one root cause)
# ---------------------------------------------------------------------------
def triangle_cells(height: int) -> list:
    cells = []
    for row in range(height + 1):
        for col in range(row):
            cells.append((col, row))
    return cells
