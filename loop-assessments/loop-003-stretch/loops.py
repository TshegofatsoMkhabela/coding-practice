"""loop-003-stretch - Grids & Loops (Stretch)

Complete each function below. Do not rename functions or change their parameters.
Do not import anything.
Run the tests with:  python3 -m pytest tests/test_loops.py -v

Output rules for printing functions:
    one line per row, exactly ONE space between cells, NO trailing spaces.
"""


# ---------------------------------------------------------------------------
# Question 1 - RULE, generalised
# ---------------------------------------------------------------------------
def print_rings(width: int, height: int) -> None:
    """Print every cell's ring number (outer outline = 0).

    print_rings(5, 4)
    0 0 0 0 0
    0 1 1 1 0
    0 1 1 1 0
    0 0 0 0 0
    """
    pass


# ---------------------------------------------------------------------------
# Question 2 - RULE with distance
# ---------------------------------------------------------------------------
def print_hollow_diamond(radius: int) -> None:
    """Print a hollow diamond in a (2*radius + 1) square grid.
    Each line ends at its last '#'.

    print_hollow_diamond(2)
        #
      #   #
    #       #
      #   #
        #
    """
    pass


# ---------------------------------------------------------------------------
# Question 3 - Debug This (four bugs)
# ---------------------------------------------------------------------------
def diagonal_walk(size: int) -> list:
    cells = []
    for d in range(2 * size - 2):
        for row in range(d):
            col = d - row
            if col < size or row < size:
                cells.append(row, col)
    return cells


# ---------------------------------------------------------------------------
# Question 4 - PATH with shrinking boundaries
# ---------------------------------------------------------------------------
def spiral_walk(width: int, height: int) -> list:
    """RETURN every cell once, in a clockwise spiral from (0, 0) inward.

    spiral_walk(4, 3) -> [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3),
                          (2, 2), (2, 1), (2, 0), (1, 0), (1, 1), (1, 2)]
    """
    pass


# ---------------------------------------------------------------------------
# Question 5 - Debug This (three bugs)
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


def print_two_runners(width: int, height: int, steps_a: int, steps_b: int) -> None:
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
