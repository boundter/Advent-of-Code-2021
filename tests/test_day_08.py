import pytest

import aoc.day_08


def data():
    inp = {
        "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb": (
            "fdgacbe cefdb cefbgd gcbe",
            8394,
        ),
        "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec": (
            "fcgedb cgb dgebacf gc",
            9781,
        ),
        "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef": (
            "cg cg fdcagb cbg",
            1197,
        ),
        "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega": (
            "efabcd cedba gadfec cb",
            9361,
        ),
        "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga": (
            "gecf egdcabf bgf bfgea",
            4873,
        ),
        "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf": (
            "gebdcfa ecba ca fadegcb",
            8418,
        ),
        "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf": (
            "cefg dcbef fcge gbcadfe",
            4548,
        ),
        "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd": (
            "ed bcgafe cdgba cbgef",
            1625,
        ),
        "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg": (
            "gbdfcae bgc cg cgb",
            8717,
        ),
        "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc": (
            "fgae cfgab fg bagce",
            4315,
        ),
    }
    return {
        tuple(key.split(" ")): (value[0].split(" "), value[1])
        for key, value in inp.items()
    }


def test_count_simple_digits():
    total_sum = sum(
        [aoc.day_08.count_simple_digits(output[0]) for _, output in data().items()]
    )
    assert total_sum == 26


@pytest.mark.parametrize(
    "clue, output, solution",
    [(clue, output, solution) for clue, (output, solution) in data().items()],
)
def test_translate_numbers(clue, output, solution):
    assert aoc.day_08.translate_output(clue=clue, output=output) == solution
