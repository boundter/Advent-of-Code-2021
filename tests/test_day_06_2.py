import more_itertools

import aoc.day_06_1


def test_LampfishPopulation_count():
    doubling_time = 7
    population = [0, 1, 1, 2, 1, 0, 0, 0, 0]
    lampfishes = aoc.day_06_1.LampfishPopulation(
        day=0, doubling_time=doubling_time, population=population
    )
    assert more_itertools.nth(lampfishes, 256) == 26984457539
