import aoc.day_02_1


def test_get_position():
    commands = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
    result = aoc.day_02_1.get_position(commands)
    assert result == aoc.day_02_1.Position(15, 10)
    assert result.inner_product() == 150
