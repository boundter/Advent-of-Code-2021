import aoc.day_05_1


def test_find_overlap():
    lines = [
        [aoc.day_05_1.Point(0, 9), aoc.day_05_1.Point(5, 9)],
        [aoc.day_05_1.Point(8, 0), aoc.day_05_1.Point(0, 8)],
        [aoc.day_05_1.Point(9, 4), aoc.day_05_1.Point(3, 4)],
        [aoc.day_05_1.Point(2, 2), aoc.day_05_1.Point(2, 1)],
        [aoc.day_05_1.Point(7, 0), aoc.day_05_1.Point(7, 4)],
        [aoc.day_05_1.Point(6, 4), aoc.day_05_1.Point(2, 0)],
        [aoc.day_05_1.Point(0, 9), aoc.day_05_1.Point(2, 9)],
        [aoc.day_05_1.Point(3, 4), aoc.day_05_1.Point(1, 4)],
        [aoc.day_05_1.Point(0, 0), aoc.day_05_1.Point(8, 8)],
        [aoc.day_05_1.Point(5, 5), aoc.day_05_1.Point(8, 2)],
    ]
    assert aoc.day_05_1.find_overlap(lines) == 5
