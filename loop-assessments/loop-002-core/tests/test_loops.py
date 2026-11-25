import time

import loops


def no_trailing_spaces(text):
    return all(line == line.rstrip() for line in text.splitlines())


# ---------------- Question 1: print_plus ----------------
def test_print_plus_5(capsys):
    loops.print_plus(5)
    assert capsys.readouterr().out == (
        ". . # . .\n"
        ". . # . .\n"
        "# # # # #\n"
        ". . # . .\n"
        ". . # . .\n"
    )


def test_print_plus_1(capsys):
    loops.print_plus(1)
    assert capsys.readouterr().out == "#\n"


def test_print_plus_3(capsys):
    loops.print_plus(3)
    assert capsys.readouterr().out == ". # .\n# # #\n. # .\n"


def test_print_plus_7_shape(capsys):
    loops.print_plus(7)
    lines = capsys.readouterr().out.splitlines()
    assert len(lines) == 7
    assert lines[3] == "# # # # # # #"
    assert lines[0] == ". . . # . . ."
    assert no_trailing_spaces("\n".join(lines))


# ---------------- Question 2: hollow_inverted_triangle ----------------
def test_hollow_inverted_triangle_5(capsys):
    loops.hollow_inverted_triangle(5)
    assert capsys.readouterr().out == (
        "# # # # #\n"
        "#     #\n"
        "#   #\n"
        "# #\n"
        "#\n"
    )


def test_hollow_inverted_triangle_2(capsys):
    loops.hollow_inverted_triangle(2)
    assert capsys.readouterr().out == "# #\n#\n"


def test_hollow_inverted_triangle_1(capsys):
    loops.hollow_inverted_triangle(1)
    assert capsys.readouterr().out == "#\n"


def test_hollow_inverted_triangle_0(capsys):
    loops.hollow_inverted_triangle(0)
    assert capsys.readouterr().out == ""


def test_hollow_inverted_triangle_row_lengths(capsys):
    loops.hollow_inverted_triangle(7)
    lines = capsys.readouterr().out.splitlines()
    assert len(lines) == 7
    for r, line in enumerate(lines):
        cells = (len(line) + 1) // 2
        assert cells == 7 - r
    assert no_trailing_spaces("\n".join(lines))


# ---------------- Question 3: counter_clockwise_walk ----------------
def test_counter_clockwise_walk_4_by_3():
    assert loops.counter_clockwise_walk(4, 3) == [
        (0, 0), (1, 0), (2, 0),
        (2, 1), (2, 2), (2, 3),
        (1, 3), (0, 3),
        (0, 2), (0, 1),
    ]


def test_counter_clockwise_walk_2_by_2():
    assert loops.counter_clockwise_walk(2, 2) == [(0, 0), (1, 0), (1, 1), (0, 1)]


def test_counter_clockwise_walk_3_by_2():
    assert loops.counter_clockwise_walk(3, 2) == [
        (0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 1)
    ]


def test_counter_clockwise_walk_2_by_4():
    assert loops.counter_clockwise_walk(2, 4) == [
        (0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (2, 1), (1, 1), (0, 1)
    ]


def test_counter_clockwise_walk_no_duplicates_and_count():
    for w in range(2, 8):
        for h in range(2, 8):
            path = loops.counter_clockwise_walk(w, h)
            assert len(path) == len(set(path)) == 2 * w + 2 * h - 4
            assert path[0] == (0, 0)


# ---------------- Question 4: runner_report ----------------
def test_runner_report_start():
    assert loops.runner_report(4, 3, 0) == (0, 0, 0)


def test_runner_report_mid_lap():
    assert loops.runner_report(4, 3, 5) == (2, 3, 0)


def test_runner_report_exact_lap():
    assert loops.runner_report(4, 3, 10) == (0, 0, 1)


def test_runner_report_several_laps():
    assert loops.runner_report(4, 3, 23) == (0, 3, 2)


def test_runner_report_workshop_example():
    assert loops.runner_report(6, 4, 9) == (3, 4, 0)


def test_runner_report_left_side():
    assert loops.runner_report(4, 3, 9) == (1, 0, 0)


def test_runner_report_huge_steps_is_fast():
    start = time.time()
    result = loops.runner_report(6, 4, 1_000_000_000_000)
    assert time.time() - start < 1.0
    assert result == (0, 0, 62_500_000_000)


# ---------------- Question 5: print_track ----------------
def test_print_track_workshop_example(capsys):
    loops.print_track(6, 4, (3, 4))
    assert capsys.readouterr().out == (
        "o o o o o o\n"
        "o         o\n"
        "o         o\n"
        "o o o o @ o\n"
    )


def test_print_track_left_side(capsys):
    loops.print_track(3, 3, (1, 0))
    assert capsys.readouterr().out == "o o o\n@   o\no o o\n"


def test_print_track_top_row(capsys):
    loops.print_track(4, 3, (0, 2))
    assert capsys.readouterr().out == "o o @ o\no     o\no o o o\n"


def test_print_track_right_side(capsys):
    loops.print_track(3, 4, (2, 2))
    assert capsys.readouterr().out == "o o o\no   o\no   @\no o o\n"


def test_print_track_exactly_one_runner(capsys):
    loops.print_track(7, 5, (4, 1))
    out = capsys.readouterr().out
    assert out.count("@") == 1
    assert out.splitlines()[4] == "o @ o o o o o"
    assert no_trailing_spaces(out)
