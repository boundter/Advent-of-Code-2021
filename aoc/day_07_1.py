"""
 A giant whale has decided your submarine is its next meal, and it's much faster
 than you are. There's nowhere to run!

 Suddenly, a swarm of crabs (each in its own tiny submarine - it's too deep for
 them otherwise) zooms in to rescue you! They seem to be preparing to blast a
 hole in the ocean floor; sensors indicate a massive underground cave system
 just beyond where they're aiming!

 The crab submarines all need to be aligned before they'll have enough power to
 blast a large enough hole for your submarine to get through. However, it
 doesn't look like they'll be aligned before the whale catches you! Maybe you
 can help?

 There's one major catch - crab submarines can only move horizontally.

 You quickly make a list of the horizontal position of each crab (your puzzle
 input). Crab submarines have limited fuel, so you need to find a way to make
 all of their horizontal positions match while requiring them to spend as little
 fuel as possible.

 For example, consider the following horizontal positions:

 16,1,2,0,4,2,7,1,2,14

 This means there's a crab with horizontal position 16, a crab with horizontal
 position 1, and so on.

 Each change of 1 step in horizontal position of a single crab costs 1 fuel. You
 could choose any horizontal position to align them all on, but the one that
 costs the least fuel is horizontal position 2:

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

 This costs a total of 37 fuel. This is the cheapest possible outcome; more
 expensive outcomes include aligning at position 1 (41 fuel), position 3 (39
 fuel), or position 10 (71 fuel).

 Determine the horizontal position that the crabs can align to using the least
 fuel possible. How much fuel must they spend to align to that position?

 Your puzzle answer was 356179.
"""
from collections import Counter
import typing

import aoc.util


def calc_fuel_consumption_brute_force(pos: typing.Iterable[int], target: int) -> int:
    return sum(map(lambda p: abs(p - target), pos))


def get_fuel_consumption(pos: typing.Iterable[int]) -> typing.Tuple[int, int]:
    def calc_fuel(
        left_sum: int, right_sum: int, n_left: int, n_right: int, target: int
    ):
        return right_sum - left_sum + (n_left - n_right) * target

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
    print(calc_fuel_consumption_brute_force(positions, res[0]))


if __name__ == "__main__":
    main()
