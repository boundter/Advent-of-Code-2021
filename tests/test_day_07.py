import aoc.day_07


def test_get_fuel_consumption_constant():
    pos = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    assert aoc.day_07.get_fuel_consumption(pos, aoc.day_07.constant_cost) == (2, 37)


def test_get_fuel_consumption_linear():
    pos = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    cost = aoc.day_07.get_linear_cost(pos)
    assert aoc.day_07.get_fuel_consumption(pos, cost) == (5, 168)
