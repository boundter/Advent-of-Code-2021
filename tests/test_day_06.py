import typing

import more_itertools
import pytest

import aoc.day_06


@pytest.fixture
def initial() -> typing.Tuple[int, typing.List[int]]:
    return 7, [0, 1, 1, 2, 1, 0, 0, 0, 0]


def test_LampfishPopulation_population(initial):
    doubling_time, population = initial
    lampfishes = aoc.day_06.LampfishPopulation(
        day=0, doubling_time=doubling_time, population=population
    )
    next(lampfishes)
    next(lampfishes)
    assert lampfishes.population == [1, 1, 2, 1, 0, 0, 0, 0, 0]
    next(lampfishes)
    assert lampfishes.population == [1, 2, 1, 0, 0, 0, 1, 0, 1]
    next(lampfishes)
    assert lampfishes.population == [2, 1, 0, 0, 0, 1, 1, 1, 1]
    next(lampfishes)
    assert lampfishes.population == [1, 0, 0, 0, 1, 1, 3, 1, 2]
    next(lampfishes)
    assert lampfishes.population == [0, 0, 0, 1, 1, 3, 2, 2, 1]


def test_LampfishPopulation_count_small(initial):
    doubling_time, population = initial
    lampfishes = aoc.day_06.LampfishPopulation(
        day=0, doubling_time=doubling_time, population=population
    )
    assert more_itertools.nth(lampfishes, 18) == 26
    assert more_itertools.nth(lampfishes, 80 - 18 - 1) == 5934


def test_LampfishPopulation_count(initial):
    doubling_time, population = initial
    lampfishes = aoc.day_06.LampfishPopulation(
        day=0, doubling_time=doubling_time, population=population
    )
    assert more_itertools.nth(lampfishes, 256) == 26984457539
