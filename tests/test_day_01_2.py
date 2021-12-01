import aoc.day_01_2


def test_depth_measurement():
    measurements = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert aoc.day_01_2.depth_measurement(measurements) == 5
