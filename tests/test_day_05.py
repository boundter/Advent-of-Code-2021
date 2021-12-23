import typing

import pytest

import aoc.day_05


@pytest.fixture
def lines() -> typing.List[typing.List[aoc.day_05.Point]]:
    return [
        [aoc.day_05.Point(0, 9), aoc.day_05.Point(5, 9)],
        [aoc.day_05.Point(8, 0), aoc.day_05.Point(0, 8)],
        [aoc.day_05.Point(9, 4), aoc.day_05.Point(3, 4)],
        [aoc.day_05.Point(2, 2), aoc.day_05.Point(2, 1)],
        [aoc.day_05.Point(7, 0), aoc.day_05.Point(7, 4)],
        [aoc.day_05.Point(6, 4), aoc.day_05.Point(2, 0)],
        [aoc.day_05.Point(0, 9), aoc.day_05.Point(2, 9)],
        [aoc.day_05.Point(3, 4), aoc.day_05.Point(1, 4)],
        [aoc.day_05.Point(0, 0), aoc.day_05.Point(8, 8)],
        [aoc.day_05.Point(5, 5), aoc.day_05.Point(8, 2)],
    ]


def test_find_overlap_part_1(lines):
    lines = filter(lambda l: l[0].x == l[1].x or l[0].y == l[1].y, lines)
    assert aoc.day_05.find_overlap(lines) == 5


def test_find_overlap_part_2(lines):
    assert aoc.day_05.find_overlap(lines) == 12
