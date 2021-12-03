import aoc.day_03_2


def test_life_support_rating():
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
    assert aoc.day_03_2.life_support_rating(inp) == 230