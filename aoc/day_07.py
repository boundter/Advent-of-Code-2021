"""
--- Day 7: The Treachery of Whales ---

A giant whale has decided your submarine is its next meal, and it's much faster than you are. There's nowhere to run!

Suddenly, a swarm of crabs (each in its own tiny submarine - it's too deep for them otherwise) zooms in to rescue you! They seem to be preparing to blast a hole in the ocean floor; sensors indicate a massive underground cave system just beyond where they're aiming!

The crab submarines all need to be aligned before they'll have enough power to blast a large enough hole for your submarine to get through. However, it doesn't look like they'll be aligned before the whale catches you! Maybe you can help?

There's one major catch - crab submarines can only move horizontally.

You quickly make a list of the horizontal position of each crab (your puzzle input). Crab submarines have limited fuel, so you need to find a way to make all of their horizontal positions match while requiring them to spend as little fuel as possible.

For example, consider the following horizontal positions:

16,1,2,0,4,2,7,1,2,14

This means there's a crab with horizontal position 16, a crab with horizontal position 1, and so on.

Each change of 1 step in horizontal position of a single crab costs 1 fuel. You could choose any horizontal position to align them all on, but the one that costs the least fuel is horizontal position 2:

    Move from 16 to 2: 14 fuel
    Move from 1 to 2: 1 fuel
    Move from 2 to 2: 0 fuel
    Move from 0 to 2: 2 fuel
    Move from 4 to 2: 2 fuel
    Move from 2 to 2: 0 fuel
    Move from 7 to 2: 5 fuel
    Move from 1 to 2: 1 fuel
    Move from 2 to 2: 0 fuel
    Move from 14 to 2: 12 fuel

This costs a total of 37 fuel. This is the cheapest possible outcome; more expensive outcomes include aligning at position 1 (41 fuel), position 3 (39 fuel), or position 10 (71 fuel).

Determine the horizontal position that the crabs can align to using the least fuel possible. How much fuel must they spend to align to that position?

Your puzzle answer was 356179.
--- Part Two ---

The crabs don't seem interested in your proposed solution. Perhaps you misunderstand crab engineering?

As it turns out, crab submarine engines don't burn fuel at a constant rate. Instead, each change of 1 step in horizontal position costs 1 more unit of fuel than the last: the first step costs 1, the second step costs 2, the third step costs 3, and so on.

As each crab moves, moving further becomes more expensive. This changes the best horizontal position to align them all on; in the example above, this becomes 5:

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

This costs a total of 168 fuel. This is the new cheapest possible outcome; the old alignment position (2) now costs 206 fuel instead.

Determine the horizontal position that the crabs can align to using the least fuel possible so they can make you an escape route! How much fuel must they spend to align to that position?

Your puzzle answer was 99788435.
"""
from collections import Counter
import typing

import aoc.util


def constant_cost(
    left_sum: int, right_sum: int, n_left: int, n_right: int, target: int
):
    # This should have a minimum at the median.
    # It can be seen as a simple reformulation of the absolute difference.
    return right_sum - left_sum + (n_left - n_right) * target


def get_linear_cost(
    pos: typing.Iterable[int],
) -> typing.Callable[[int, int, int, int, int], int]:
    # This function returns isa  closure to prevent recalculation of the total sum.
    sum_squared = sum([p ** 2 for p in pos])
    sum_double = sum([2 * p for p in pos])

    def calc_fuel(
        left_sum: int, right_sum: int, n_left: int, n_right: int, target: int
    ):
        # The same principle as a bove but now we also have a constant term as a
        # result of the series ("kleiner Gauss").
        return 0.5 * (
            sum_squared
            - target * sum_double
            + len(pos) * target ** 2
            + right_sum
            - left_sum
            + (n_left - n_right) * target
        )

    return calc_fuel


def get_fuel_consumption(
    pos: typing.Iterable[int],
    calc_fuel: typing.Callable[[int, int, int, int, int], int],
) -> typing.Tuple[int, int]:
    # This function can be optimized a lot.
    # The left and right sums of the target are calculated and then the fuel is
    # calculated using these two. Then the target is incremented and the fuel is
    # calculated again. Thjis is done until the function reaches its minimum.
    # Improvements:
    # 1. Use the median as starting position, as it will be close to the desired
    #    target for most cost functions.
    # 2. Do not fully recalculate the sums but only update them. Then we can use
    #    only one iteration here (+ the creation of the Counter).
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
    print("=== Part 1 ===")
    print(get_fuel_consumption(positions, constant_cost))
    print("=== Part 2 ===")
    cost = get_linear_cost(positions)
    print(get_fuel_consumption(positions, cost))


if __name__ == "__main__":
    main()
