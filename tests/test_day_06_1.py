import more_itertools
from more_itertools import more

import aoc.day_06_1


def test_LampfishPopulation_population():
    doubling_time = 7
    population = [0, 1, 1, 2, 1, 0, 0, 0, 0]
    lampfishes = aoc.day_06_1.LampfishPopulation(
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


def test_LampfishPopulation_count():
    doubling_time = 7
    population = [0, 1, 1, 2, 1, 0, 0, 0, 0]
    lampfishes = aoc.day_06_1.LampfishPopulation(
        day=0, doubling_time=doubling_time, population=population
    )
    assert more_itertools.nth(lampfishes, 18) == 26
    assert more_itertools.nth(lampfishes, 80 - 18 - 1) == 5934
