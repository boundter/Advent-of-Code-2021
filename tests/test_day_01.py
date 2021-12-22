import aoc.day_01


def test_depth_measurement_part_1():
    measurements = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert aoc.day_01.depth_measurement(measurements, 2) == 7


def test_depth_measurement_part_2():
    measurements = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert aoc.day_01.depth_measurement(measurements, 3) == 5
