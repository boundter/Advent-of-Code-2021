import itertools
import importlib.resources
import typing


def pairwise(iterable):
    # backported from itertools
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def depth_measurement(measurements: typing.List[int]) -> int:
    increases = 0
    for previous, current in pairwise(measurements):
        increases += int(current > previous)
    return increases


def read_file(filename: str) -> typing.List[int]:
    data = importlib.resources.read_text("aoc.resources", filename).splitlines()
    return map(int, data)


def main():
    measurements = read_file("day_01.txt")
    print(depth_measurement(measurements))


if __name__ == "__main__":
    main()
