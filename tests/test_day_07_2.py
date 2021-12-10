import aoc.day_07_2


def test_get_fuel_consumption():
    pos = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    assert aoc.day_07_2.get_fuel_consumption(pos) == (5, 168)
