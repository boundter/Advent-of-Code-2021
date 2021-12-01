import importlib.resources
import itertools


def read_file(filename: str) -> str:
    data = importlib.resources.read_text("aoc.resources", filename)
    return data


def pairwise(iterable):
    # backported from itertools
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def threewise(iterable):
    # adapted from pairwise
    a, b, c = itertools.tee(iterable, 3)
    next(b, None)
    next(c, None)
    next(c, None)
    return zip(a, b, c)
