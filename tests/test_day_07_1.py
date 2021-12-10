import aoc.day_07_1


def test_calc_fuel_consumption_brute_force():
    pos = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    assert aoc.day_07_1.calc_fuel_consumption_brute_force(pos, 2) == 37
    assert aoc.day_07_1.calc_fuel_consumption_brute_force(pos, 1) == 41
    assert aoc.day_07_1.calc_fuel_consumption_brute_force(pos, 3) == 39
    assert aoc.day_07_1.calc_fuel_consumption_brute_force(pos, 10) == 71


def test_get_fuel_consumption():
    pos = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    assert aoc.day_07_1.get_fuel_consumption(pos) == (2, 37)