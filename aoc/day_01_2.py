import functools
import math
import typing

import aoc.util


def depth_measurement(measurements: typing.Iterable[int]) -> int:
    sums = map(lambda triple: sum(triple), aoc.util.threewise(measurements))
    return functools.reduce(
        lambda counter, current: [counter[0] + int(current > counter[1]), current],
        sums,
        [0, math.inf],
    )[0]


def main():
    measurements = map(int, aoc.util.read_file("day_01.txt").splitlines())
    print(depth_measurement(measurements))


if __name__ == "__main__":
    main()
