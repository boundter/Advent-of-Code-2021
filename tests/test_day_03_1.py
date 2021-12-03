import aoc.day_03_1


def test_power_consumption():
    inp = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    assert aoc.day_03_1.power_consumption(inp) == 198
