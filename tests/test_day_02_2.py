import aoc.day_02_2


def test_get_position():
    commands = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
    result = aoc.day_02_2.get_position(commands)
    assert result == aoc.day_02_2.Position(15, 60, 10)
    assert result.inner_product() == 900
