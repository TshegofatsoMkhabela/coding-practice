import loops


def no_trailing_spaces(text):
    return all(line == line.rstrip() for line in text.splitlines())


# ---------------- Question 1: print_rings ----------------
def test_print_rings_5_by_4(capsys):
    loops.print_rings(5, 4)
    assert capsys.readouterr().out == (
        "0 0 0 0 0\n"
        "0 1 1 1 0\n"
        "0 1 1 1 0\n"
        "0 0 0 0 0\n"
    )


def test_print_rings_7_by_7(capsys):
    loops.print_rings(7, 7)
    assert capsys.readouterr().out == (
        "0 0 0 0 0 0 0\n"
        "0 1 1 1 1 1 0\n"
        "0 1 2 2 2 1 0\n"
        "0 1 2 3 2 1 0\n"
        "0 1 2 2 2 1 0\n"
        "0 1 1 1 1 1 0\n"
        "0 0 0 0 0 0 0\n"
    )


def test_print_rings_single_row(capsys):
    loops.print_rings(4, 1)
    assert capsys.readouterr().out == "0 0 0 0\n"


def test_print_rings_wide(capsys):
    loops.print_rings(8, 5)
    assert capsys.readouterr().out == (
        "0 0 0 0 0 0 0 0\n"
        "0 1 1 1 1 1 1 0\n"
        "0 1 2 2 2 2 1 0\n"
        "0 1 1 1 1 1 1 0\n"
        "0 0 0 0 0 0 0 0\n"
    )


# ---------------- Question 2: print_hollow_diamond ----------------
def test_print_hollow_diamond_2(capsys):
    loops.print_hollow_diamond(2)
    assert capsys.readouterr().out == (
        "    #\n"
        "  #   #\n"
        "#       #\n"
        "  #   #\n"
        "    #\n"
    )


def test_print_hollow_diamond_0(capsys):
    loops.print_hollow_diamond(0)
    assert capsys.readouterr().out == "#\n"


def test_print_hollow_diamond_1(capsys):
    loops.print_hollow_diamond(1)
    assert capsys.readouterr().out == "  #\n#   #\n  #\n"


def test_print_hollow_diamond_shape(capsys):
    loops.print_hollow_diamond(4)
    out = capsys.readouterr().out
    lines = out.splitlines()
    assert len(lines) == 9
    assert out.count("#") == 16
    assert no_trailing_spaces(out)
    assert lines[4] == "#" + " " * 15 + "#"


# ---------------- Question 3: diagonal_walk ----------------
def test_diagonal_walk_3():
    assert loops.diagonal_walk(3) == [
        (0, 0),
        (0, 1), (1, 0),
        (0, 2), (1, 1), (2, 0),
        (1, 2), (2, 1),
        (2, 2),
    ]


def test_diagonal_walk_1():
    assert loops.diagonal_walk(1) == [(0, 0)]


def test_diagonal_walk_2():
    assert loops.diagonal_walk(2) == [(0, 0), (0, 1), (1, 0), (1, 1)]


def test_diagonal_walk_invariant():
    path = loops.diagonal_walk(6)
    assert len(path) == len(set(path)) == 36
    sums = []
    for row, col in path:
        assert 0 <= row < 6 and 0 <= col < 6
        sums.append(row + col)
    assert sums == sorted(sums)


# ---------------- Question 4: spiral_walk ----------------
def test_spiral_walk_4_by_3():
    assert loops.spiral_walk(4, 3) == [
        (0, 0), (0, 1), (0, 2), (0, 3),
        (1, 3), (2, 3),
        (2, 2), (2, 1), (2, 0),
        (1, 0),
        (1, 1), (1, 2),
    ]


def test_spiral_walk_3_by_3():
    assert loops.spiral_walk(3, 3) == [
        (0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0), (1, 1)
    ]


def test_spiral_walk_3_by_4():
    assert loops.spiral_walk(3, 4) == [
        (0, 0), (0, 1), (0, 2),
        (1, 2), (2, 2), (3, 2),
        (3, 1), (3, 0),
        (2, 0), (1, 0),
        (1, 1), (2, 1),
    ]


def test_spiral_walk_one_column():
    assert loops.spiral_walk(1, 3) == [(0, 0), (1, 0), (2, 0)]


def test_spiral_walk_one_row():
    assert loops.spiral_walk(3, 1) == [(0, 0), (0, 1), (0, 2)]


def test_spiral_walk_every_cell_once():
    for w in range(1, 8):
        for h in range(1, 8):
            path = loops.spiral_walk(w, h)
            assert len(path) == len(set(path)) == w * h
            for i in range(1, len(path)):
                (r1, c1), (r2, c2) = path[i - 1], path[i]
                assert abs(r1 - r2) + abs(c1 - c2) == 1


# ---------------- Question 5: print_two_runners ----------------
def test_print_two_runners_basic(capsys):
    loops.print_two_runners(5, 3, 2, 3)
    assert capsys.readouterr().out == "o o A o o\no       o\no B o o o\n"


def test_print_two_runners_collision(capsys):
    loops.print_two_runners(5, 3, 6, 6)
    assert capsys.readouterr().out == "o o o o o\no       o\no o o o X\n"


def test_print_two_runners_many_laps(capsys):
    loops.print_two_runners(5, 3, 25, 13)
    assert capsys.readouterr().out == "o A o o o\nB       o\no o o o o\n"


def test_print_two_runners_both_at_start(capsys):
    loops.print_two_runners(3, 3, 0, 0)
    assert capsys.readouterr().out == "X o o\no   o\no o o\n"


def test_print_two_runners_b_more_than_one_lap(capsys):
    loops.print_two_runners(3, 3, 1, 9)
    assert capsys.readouterr().out == "o A o\nB   o\no o o\n"
