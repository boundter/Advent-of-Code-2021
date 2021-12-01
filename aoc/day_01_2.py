"""
Instead, consider sums of a three-measurement sliding window.

 Start by comparing the first and second three-measurement windows. The
 measurements in the first window are marked A (199, 200, 208); their sum is 199
 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is
 618. The sum of measurements in the second window is larger than the sum of the
 first, so this first comparison increased.

 Your goal now is to count the number of times the sum of measurements in this
 sliding window increases from the previous sum. So, compare A with B, then
 compare B with C, then C with D, and so on. Stop when there aren't enough
 measurements left to create a new three-measurement sum.
"""
import numbers
import typing

import aoc.day_01_1
import aoc.util


def depth_measurement(measurements: typing.Iterable[numbers.Number]) -> int:
    sums = map(lambda triple: sum(triple), aoc.util.threewise(measurements))
    return aoc.day_01_1.depth_measurement(sums)


def main():
    measurements = map(int, aoc.util.read_file("day_01.txt").splitlines())
    print(depth_measurement(measurements))


if __name__ == "__main__":
    main()
