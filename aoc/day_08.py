"""
--- Day 8: Seven Segment Search ---

You barely reach the safety of the cave when the whale smashes into the cave mouth, collapsing it. Sensors indicate another exit to this cave at a much greater depth, so you have no choice but to press on.

As your submarine slowly makes its way through the cave system, you notice that the four-digit seven-segment displays in your submarine are malfunctioning; they must have been damaged during the escape. You'll be in a lot of trouble without them, so you'd better figure out what's wrong.

Each digit of a seven-segment display is rendered by turning on or off any of seven segments named a through g:

  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

So, to render a 1, only segments c and f would be turned on; the rest would be off. To render a 7, only segments a, c, and f would be turned on.

The problem is that the signals which control the segments have been mixed up on each display. The submarine is still trying to display numbers by producing output on signal wires a through g, but those wires are connected to segments randomly. Worse, the wire/segment connections are mixed up separately for each four-digit display! (All of the digits within a display use the same connections, though.)

So, you might know that only signal wires b and g are turned on, but that doesn't mean segments b and g are turned on: the only digit that uses two segments is 1, so it must mean segments c and f are meant to be on. With just that information, you still can't tell which wire (b/g) goes to which segment (c/f). For that, you'll need to collect more information.

For each display, you watch the changing signals for a while, make a note of all ten unique signal patterns you see, and then write down a single four digit output value (your puzzle input). Using the signal patterns, you should be able to work out which pattern corresponds to which digit.

For example, here is what you might see in a single entry in your notes:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf

(The entry is wrapped here to two lines so it fits; in your notes, it will all be on a single line.)

Each entry consists of ten unique signal patterns, a | delimiter, and finally the four digit output value. Within an entry, the same wire/segment connections are used (but you don't know what the connections actually are). The unique signal patterns correspond to the ten different ways the submarine tries to render a digit using the current wire/segment connections. Because 7 is the only digit that uses three segments, dab in the above example means that to render a 7, signal lines d, a, and b are on. Because 4 is the only digit that uses four segments, eafb means that to render a 4, signal lines e, a, f, and b are on.

Using this information, you should be able to work out which combination of signal wires corresponds to each of the ten digits. Then, you can decode the four digit output value. Unfortunately, in the above example, all of the digits in the output value (cdfeb fcadb cdfeb cdbaf) use five segments and are more difficult to deduce.

For now, focus on the easy digits. Consider this larger example:

be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
fgae cfgab fg bagce

Because the digits 1, 4, 7, and 8 each use a unique number of segments, you should be able to tell which combinations of signals correspond to those digits. Counting only digits in the output values (the part after | on each line), in the above example, there are 26 instances of digits that use a unique number of segments (highlighted above).

In the output values, how many times do digits 1, 4, 7, or 8 appear?

Your puzzle answer was 493.

--- Part Two ---

Through a little deduction, you should now be able to determine the remaining digits. Consider again the first example above:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf

After some careful analysis, the mapping between signal wires and segments only make sense in the following configuration:

 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc

So, the unique signal patterns would correspond to the following digits:

    acedgfb: 8
    cdfbe: 5
    gcdfa: 2
    fbcad: 3
    dab: 7
    cefabd: 9
    cdfgeb: 6
    eafb: 4
    cagedb: 0
    ab: 1

Then, the four digits of the output value can be decoded:

    cdfeb: 5
    fcadb: 3
    cdfeb: 5
    cdbaf: 3

Therefore, the output value for this entry is 5353.

Following this same process for each entry in the second, larger example above, the output value of each entry can be determined:

    fdgacbe cefdb cefbgd gcbe: 8394
    fcgedb cgb dgebacf gc: 9781
    cg cg fdcagb cbg: 1197
    efabcd cedba gadfec cb: 9361
    gecf egdcabf bgf bfgea: 4873
    gebdcfa ecba ca fadegcb: 8418
    cefg dcbef fcge gbcadfe: 4548
    ed bcgafe cdgba cbgef: 1625
    gbdfcae bgc cg cgb: 8717
    fgae cfgab fg bagce: 4315

Adding all of the output values in this larger example produces 61229.

For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get if you add up all of the output values?

Your puzzle answer was 1010460.
"""
from fnmatch import translate
import typing
import itertools
import functools
from collections import defaultdict
import more_itertools

import aoc.util

NUMBERS = {
    0: set(["a", "b", "c", "e", "f", "g"]),
    1: set(["c", "f"]),
    2: set(["a", "c", "d", "e", "g"]),
    3: set(["a", "c", "d", "f", "g"]),
    4: set(["b", "c", "d", "f"]),
    5: set(["a", "b", "d", "f", "g"]),
    6: set(["a", "b", "d", "e", "f", "g"]),
    7: set(["a", "c", "f"]),
    8: set(["a", "b", "c", "d", "e", "f", "g"]),
    9: set(["a", "b", "c", "d", "f", "g"]),
}


def count_simple_digits(output_vals: typing.Iterable[str]) -> int:
    return sum([int(len(val) in set([2, 3, 4, 7])) for val in output_vals])


def _lookup_clue_by_length(
    clue: typing.Iterable[str],
) -> typing.Dict[int, typing.Tuple[typing.Set[str]]]:
    clue_by_length = defaultdict(lambda: ())
    for c in clue:
        clue_by_length[len(c)] = clue_by_length[len(c)] + (set(c),)
    return clue_by_length


def _union_of_translation(
    translation: typing.Dict[str, typing.Set[str]]
) -> typing.Set[str]:
    return functools.reduce(
        lambda union, key: union.union(translation[key]), translation, set()
    )


def _union_of(clues: typing.Tuple[typing.Set[str]]) -> typing.Set[str]:
    return functools.reduce(set.intersection, clues)


def _create_translation(clue_by_length: typing.Dict[int, str]) -> typing.Dict[str, str]:
    # As a shorthand use n for intersection and \ for without
    translation = {}
    # {a} = 7 \ 1
    translation["a"] = clue_by_length[3][0].difference(clue_by_length[2][0])
    # {b} = (4 \ 1) n (9 n 6 n 0) (all with length 6)
    translation["b"] = (
        clue_by_length[4][0]
        .difference(clue_by_length[2][0])
        .intersection(_union_of(clue_by_length[6]))
    )
    # {d} = (4 \ 1) \ {b}
    translation["d"] = (
        clue_by_length[4][0]
        .difference(clue_by_length[2][0])
        .difference(_union_of_translation(translation))
    )
    # {g} = (2 n 3 n 5) \ {a ,d}
    translation["g"] = _union_of(clue_by_length[5]).difference(
        _union_of_translation(translation)
    )
    # {f} = (9 n 6 n 0) \ {a, b, g}
    translation["f"] = _union_of(clue_by_length[6]).difference(
        _union_of_translation(translation)
    )
    # {c} = 1 \ {f}
    translation["c"] = clue_by_length[2][0].difference(
        _union_of_translation(translation)
    )
    # {e} = 8 \ {a, b, c, d, f, g}
    translation["e"] = clue_by_length[7][0].difference(
        _union_of_translation(translation)
    )
    return {key: value.pop() for key, value in translation.items()}


def _translate_representation(
    translation: typing.Dict[str, str], representation: str
) -> str:
    return "".join(sorted([translation[s] for s in representation]))


def _translate_numbers(translation: typing.Dict[str, str]) -> typing.Dict[str, str]:
    return {
        _translate_representation(translation, "".join(value)): str(key)
        for key, value in NUMBERS.items()
    }


def _lookup_number(translation: typing.Dict[str, str], representation: str) -> str:
    return translation["".join(sorted(list(representation)))]


def translate_output(clue: typing.Iterable[str], output: typing.Iterable[str]) -> int:
    clue_by_length = _lookup_clue_by_length(clue)
    translation = _create_translation(clue_by_length)
    translated_representation = _translate_numbers(translation)
    num_string = "".join(
        map(lambda s: _lookup_number(translated_representation, s), output)
    )
    return int(num_string)


def main():
    inp = aoc.util.read_file("day_08.txt").splitlines()
    digits_in, digits_out = zip(*map(lambda x: x.split(" | "), inp))
    digits_in = list(digits_in)
    digits_out = list(digits_out)
    print("=== Part 1 ===")
    print(
        count_simple_digits(
            itertools.chain.from_iterable(map(lambda x: x.split(" "), digits_out))
        )
    )
    print("=== Part 2 ===")
    result = sum(
        itertools.starmap(
            lambda inp, outp: translate_output(inp.split(" "), outp.split(" ")),
            zip(digits_in, digits_out),
        )
    )
    print(result)


if __name__ == "__main__":
    main()
