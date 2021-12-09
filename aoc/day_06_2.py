"""
 Suppose the lanternfish live forever and have unlimited food and space. Would
 they take over the entire ocean?

 After 256 days in the example above, there would be a total of 26984457539
 lanternfish!

How many lanternfish would there be after 256 days?

Your puzzle answer was 1640526601595.
"""
from collections import Counter
import more_itertools

import aoc.day_06_1
import aoc.util


def main():
    inp = aoc.util.read_file("day_06.txt").split(",")
    counts = Counter(map(int, inp))
    initial_population = (
        [0] + [counts[key] for key in sorted(counts.keys())] + [0, 0, 0]
    )
    print(initial_population, counts)
    print(counts, initial_population)
    population = aoc.day_06_1.LampfishPopulation(7, initial_population)
    print(more_itertools.nth(population, 256))


if __name__ == "__main__":
    main()
