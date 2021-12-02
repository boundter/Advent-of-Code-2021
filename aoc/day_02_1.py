"""
Now, you need to figure out how to pilot this thing.

 It seems like the submarine can take a series of commands like forward 1, down
 2, or up 3:

    forward X increases the horizontal position by X units.
    down X increases the depth by X units.
    up X decreases the depth by X units.

 Note that since you're on a submarine, down and up affect your depth, and so
 they have the opposite result of what you might expect.

 The submarine seems to already have a planned course (your puzzle input). You
 should probably figure out where it's going. For example:

forward 5
down 5
forward 8
up 3
down 8
forward 2


 Your horizontal position and depth both start at 0. The steps above would then
 modify them as follows:

    forward 5 adds 5 to your horizontal position, a total of 5.
    down 5 adds 5 to your depth, resulting in a value of 5.
    forward 8 adds 8 to your horizontal position, a total of 13.
    up 3 decreases your depth by 3, resulting in a value of 2.
    down 8 adds 8 to your depth, resulting in a value of 10.
    forward 2 adds 2 to your horizontal position, a total of 15.

 After following these instructions, you would have a horizontal position of 15
 and a depth of 10. (Multiplying these together produces 150.)

 Calculate the horizontal position and depth you would have after following the
 planned course. What do you get if you multiply your final horizontal position
 by your final depth?
"""
import dataclasses
from functools import reduce
import typing

import aoc.util


@dataclasses.dataclass(frozen=True)
class Position:
    x: int
    y: int

    def multiply_scalar(self, scalar: int) -> "Position":
        return Position(self.x * scalar, self.y * scalar)

    def multiply(self, other: "Position") -> "Position":
        return Position(self.x * other.x, self.y * other.y)

    def inner_product(self):
        return self.x * self.y

    def add(self, other: "Position") -> "Position":
        return Position(self.x + other.x, self.y + other.y)


def get_position(commands: typing.Iterable[str]) -> Position:
    directions = {
        "forward": Position(1, 0),
        "down": Position(0, 1),
        "up": Position(0, -1),
    }

    def apply_command(command: str) -> Position:
        split = command.split(" ")
        return directions[split[0]].multiply_scalar(int(split[1]))

    return reduce(lambda x, y: x.add(y), map(apply_command, commands), Position(0, 0))


def main():
    lines = aoc.util.read_file("day_02.txt").splitlines()
    result = get_position(lines)
    print(result, result.inner_product())


if __name__ == "__main__":
    main()
