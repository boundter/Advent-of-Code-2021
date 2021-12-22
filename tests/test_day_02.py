import typing

import pytest

import aoc.day_02


@pytest.fixture
def commands() -> typing.List[str]:
    return ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


def test_get_position_part_1(commands):
    result = aoc.day_02.get_final_position(aoc.day_02.Position(0, 0, 0), commands)
    assert result == aoc.day_02.Position(15, 10, 0)
    assert result.inner_product() == 150


def test_get_position(commands):
    result = aoc.day_02.get_final_position(aoc.day_02.PositionAim(0, 0, 0), commands)
    assert result == aoc.day_02.PositionAim(15, 60, 10)
    assert result.inner_product() == 900
