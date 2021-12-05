"""
 Unfortunately, considering only horizontal and vertical lines doesn't give you
 the full picture; you need to also consider diagonal lines.

 Because of the limits of the hydrothermal vent mapping system, the lines in
 your list will only ever be horizontal, vertical, or a diagonal line at exactly
 45 degrees. In other words:

    An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
    An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.

 Considering all lines from the above example would now produce the following
 diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....

 You still need to determine the number of points where at least two lines
 overlap. In the above example, this is still anywhere in the diagram with a 2
 or larger - now a total of 12 points.

 Consider all of the lines. At how many points do at least two lines overlap?
"""
import typing
import dataclasses
import math
from collections import defaultdict
import functools

import aoc.util


@dataclasses.dataclass(frozen=True)
class Point:
    x: int
    y: int

    def _get_iterator(self, this: int, other: int) -> typing.Iterable[int]:
        step = int(math.copysign(int(1), other - this))
        return range(this, other + step, step)

    def to(self, other: "Point") -> typing.Iterable["Point"]:
        if self.x != other.x and self.y == other.y:
            return map(lambda x: Point(x, self.y), self._get_iterator(self.x, other.x))
        elif self.y != other.y and self.x == other.x:
            return map(lambda y: Point(self.x, y), self._get_iterator(self.y, other.y))
        return map(
            lambda xy: Point(*xy),
            zip(
                self._get_iterator(self.x, other.x), self._get_iterator(self.y, other.y)
            ),
        )


def count_dictionary(counts: typing.Dict[Point, int], min_count: int = 2) -> int:
    return functools.reduce(
        lambda x, y: x + 1 if y[1] >= min_count else x, counts.items(), 0
    )


def find_overlap(lines: typing.Iterable[typing.List[Point]]) -> int:
    fields = defaultdict(int)
    connected_lines = map(lambda row: row[0].to(row[1]), lines)
    for line in connected_lines:
        for point in line:
            fields[point] += 1
    return count_dictionary(fields, 2)


def main():
    inp = aoc.util.read_file("day_05.txt").splitlines()
    separated_begin_end = map(lambda l: l.split(" -> "), inp)

    def num_to_point(numbers: str) -> Point:
        split = [int(n) for n in numbers.split(",")]
        return Point(*split)

    lines = map(lambda l: [num_to_point(l[0]), num_to_point(l[1])], separated_begin_end)
    print(find_overlap(lines))


if __name__ == "__main__":
    main()
