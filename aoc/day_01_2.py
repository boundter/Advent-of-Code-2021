import importlib.resources
import itertools
import typing


def threewise(iterable):
    # backported from itertools
    a, b, c = itertools.tee(iterable, 3)
    next(b, None)
    next(c, None)
    next(c, None)
    return zip(a, b, c)


def depth_measurement(measurements: typing.Iterable[int]) -> int:
    increases = 0
    previous_sum = None
    for before, previous, current in threewise(measurements):
        current_sum = before + previous + current
        if previous_sum is not None:
            increases += int(current_sum > previous_sum)
        previous_sum = current_sum
    return increases


def read_file(filename: str) -> typing.List[int]:
    data = importlib.resources.read_text("aoc.resources", filename).splitlines()
    return map(int, data)


def main():
    measurements = read_file("day_01.txt")
    print(depth_measurement(measurements))


if __name__ == "__main__":
    main()
