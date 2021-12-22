import typing

import pytest

import aoc.day_03


@pytest.fixture
def inp() -> typing.List[str]:
    return [
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


def test_power_consumption(inp):
    assert aoc.day_03.power_consumption(inp) == 198


def test_life_support_rating(inp):
    assert aoc.day_03.life_support_rating(inp) == 230
