import functools
import typing

import aoc.util


def depth_measurement(measurements: typing.List[int]) -> int:
    return functools.reduce(
        lambda count, pair: count + int(pair[1] > pair[0]),
        aoc.util.pairwise(measurements),
        0,
    )


def main():
    measurements = map(int, aoc.util.read_file("day_01.txt").splitlines())
    print(depth_measurement(measurements))


if __name__ == "__main__":
    main()
