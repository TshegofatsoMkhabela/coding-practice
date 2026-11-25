import loops


def no_trailing_spaces(text):
    return all(line == line.rstrip() for line in text.splitlines())


# ---------------- Question 1: print_coordinates ----------------
def test_print_coordinates_3_by_2(capsys):
    loops.print_coordinates(3, 2)
    assert capsys.readouterr().out == "(0,0) (0,1) (0,2)\n(1,0) (1,1) (1,2)\n"


def test_print_coordinates_one_column(capsys):
    loops.print_coordinates(1, 3)
    assert capsys.readouterr().out == "(0,0)\n(1,0)\n(2,0)\n"


def test_print_coordinates_one_row(capsys):
    loops.print_coordinates(4, 1)
    assert capsys.readouterr().out == "(0,0) (0,1) (0,2) (0,3)\n"


def test_print_coordinates_empty(capsys):
    loops.print_coordinates(0, 3)
    loops.print_coordinates(3, 0)
    loops.print_coordinates(-1, 2)
    assert capsys.readouterr().out == ""


# ---------------- Question 2: checkerboard ----------------
def test_checkerboard_4_by_3(capsys):
    loops.checkerboard(4, 3)
    assert capsys.readouterr().out == "# . # .\n. # . #\n# . # .\n"


def test_checkerboard_single(capsys):
    loops.checkerboard(1, 1)
    assert capsys.readouterr().out == "#\n"


def test_checkerboard_one_column(capsys):
    loops.checkerboard(1, 4)
    assert capsys.readouterr().out == "#\n.\n#\n.\n"


def test_checkerboard_no_trailing_spaces(capsys):
    loops.checkerboard(7, 5)
    out = capsys.readouterr().out
    assert len(out.splitlines()) == 5
    assert no_trailing_spaces(out)


# ---------------- Question 3: print_frame ----------------
def test_print_frame_5_by_4(capsys):
    loops.print_frame(5, 4)
    assert capsys.readouterr().out == (
        "# # # # #\n"
        "# . . . #\n"
        "# . . . #\n"
        "# # # # #\n"
    )


def test_print_frame_square(capsys):
    loops.print_frame(3, 3)
    assert capsys.readouterr().out == "# # #\n# . #\n# # #\n"


def test_print_frame_one_row(capsys):
    loops.print_frame(3, 1)
    assert capsys.readouterr().out == "# # #\n"


def test_print_frame_single_cell(capsys):
    loops.print_frame(1, 1)
    assert capsys.readouterr().out == "#\n"


def test_print_frame_no_trailing_spaces(capsys):
    loops.print_frame(6, 5)
    out = capsys.readouterr().out
    assert len(out.splitlines()) == 5
    assert no_trailing_spaces(out)


# ---------------- Question 4: snake_walk ----------------
def test_snake_walk_3_by_3():
    assert loops.snake_walk(3, 3) == [
        (0, 0), (0, 1), (0, 2),
        (1, 2), (1, 1), (1, 0),
        (2, 0), (2, 1), (2, 2),
    ]


def test_snake_walk_one_column():
    assert loops.snake_walk(1, 3) == [(0, 0), (1, 0), (2, 0)]


def test_snake_walk_one_row():
    assert loops.snake_walk(2, 1) == [(0, 0), (0, 1)]


def test_snake_walk_4_by_2():
    assert loops.snake_walk(4, 2) == [
        (0, 0), (0, 1), (0, 2), (0, 3),
        (1, 3), (1, 2), (1, 1), (1, 0),
    ]


def test_snake_walk_every_cell_once():
    path = loops.snake_walk(5, 4)
    assert len(path) == 20
    assert len(set(path)) == 20


# ---------------- Question 5: triangle_cells ----------------
def test_triangle_cells_height_3():
    assert loops.triangle_cells(3) == [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2)]


def test_triangle_cells_height_1():
    assert loops.triangle_cells(1) == [(0, 0)]


def test_triangle_cells_height_0():
    assert loops.triangle_cells(0) == []


def test_triangle_cells_rule_holds():
    for row, col in loops.triangle_cells(6):
        assert 0 <= col <= row < 6
