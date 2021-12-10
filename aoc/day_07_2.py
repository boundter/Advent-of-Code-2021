"""
 The crabs don't seem interested in your proposed solution. Perhaps you
 misunderstand crab engineering?

 As it turns out, crab submarine engines don't burn fuel at a constant rate.
 Instead, each change of 1 step in horizontal position costs 1 more unit of fuel
 than the last: the first step costs 1, the second step costs 2, the third step
 costs 3, and so on.

 As each crab moves, moving further becomes more expensive. This changes the
 best horizontal position to align them all on; in the example above, this
 becomes 5:

    Move from 16 to 5: 66 fuel
    Move from 1 to 5: 10 fuel
    Move from 2 to 5: 6 fuel
    Move from 0 to 5: 15 fuel
    Move from 4 to 5: 1 fuel
    Move from 2 to 5: 6 fuel
    Move from 7 to 5: 3 fuel
    Move from 1 to 5: 10 fuel
    Move from 2 to 5: 6 fuel
    Move from 14 to 5: 45 fuel

 This costs a total of 168 fuel. This is the new cheapest possible outcome; the
 old alignment position (2) now costs 206 fuel instead.

 Determine the horizontal position that the crabs can align to using the least
 fuel possible so they can make you an escape route! How much fuel must they
 spend to align to that position?

Your puzzle answer was 99788435.
"""

from collections import Counter
import typing

import aoc.util


def get_fuel_consumption(pos: typing.Iterable[int]) -> typing.Tuple[int, int]:
    sum_squared = sum([p ** 2 for p in pos])
    sum_double = sum([2 * p for p in pos])

    def calc_fuel(
        left_sum: int, right_sum: int, n_left: int, n_right: int, target: int
    ):
        return 0.5 * (
            sum_squared
            - target * sum_double
            + len(pos) * target ** 2
            + right_sum
            - left_sum
            + (n_left - n_right) * target
        )

    position_counts = Counter(pos)
    positions = sorted(position_counts.keys())
    left_sum = 0
    right_sum = sum([abs(p - positions[0]) * position_counts[p] for p in positions])
    n_left = 0
    n_right = sum([position_counts[p] for p in positions])
    previous_result = (
        positions[0],
        calc_fuel(left_sum, right_sum, n_left, n_right, positions[0]),
    )
    for target in range(positions[0] + 1, positions[-1] + 1):
        left_sum = sum(
            [
                abs(p - positions[0]) * position_counts[p]
                for p in positions
                if p < target
            ]
        )
        right_sum = sum(
            [
                abs(p - positions[0]) * position_counts[p]
                for p in positions
                if p > target
            ]
        )
        n_left = sum([position_counts[p] for p in positions if p < target])
        n_right = sum([position_counts[p] for p in positions if p > target])
        fuel = calc_fuel(left_sum, right_sum, n_left, n_right, target)
        if previous_result[1] < fuel:
            return previous_result
        previous_result = (target, fuel)
    return None


def main():
    inp = aoc.util.read_file("day_07.txt").split(",")
    positions = [int(i) for i in inp]
    res = get_fuel_consumption(positions)
    print(res)


if __name__ == "__main__":
    main()
