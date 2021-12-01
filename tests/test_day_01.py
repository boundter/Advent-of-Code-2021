import aoc.day_01


def test_depth_measurement():
    measurements = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert aoc.day_01.depth_measurement(measurements) == 7
