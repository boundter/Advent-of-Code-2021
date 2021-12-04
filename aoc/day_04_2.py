"""
 On the other hand, it might be wise to try a different strategy: let the giant
 squid win.

 You aren't sure how many bingo boards a giant squid could play at once, so
 rather than waste time counting its arms, the safe thing to do is to figure out
 which board will win last and choose that one. That way, no matter which boards
 it picks, it will win for sure.

 In the above example, the second board is the last to win, which happens after
 13 is eventually called and its middle column is completely marked. If you were
 to keep playing until this point, the second board would have a sum of unmarked
 numbers equal to 148 for a final score of 148 * 13 = 1924.

 Figure out which board will win last. Once it wins, what would its final score
 be?
"""
import itertools
import typing

import aoc.day_04_1


def partition(pred, iterable):
    "Use a predicate to partition entries into false entries and true entries"
    # partition(is_odd, range(10)) --> 0 2 4 6 8   and  1 3 5 7 9
    t1, t2 = itertools.tee(iterable)
    return itertools.filterfalse(pred, t1), filter(pred, t2)


def find_losing_board(
    numbers: typing.List[int], boards: typing.List[aoc.day_04_1.BingoBoard]
):
    last_boards = None
    numbers = iter(numbers)
    while len(boards) != 0:
        n = next(numbers)
        [board.tip(n) for board in boards]
        last_boards = boards
        boards, _ = partition(lambda board: board.bingo(), boards)
        boards = list(boards)

    untipped = last_boards[0].untipped()
    return n * sum(untipped)


def main():
    inp = aoc.util.read_file("day_04.txt").split("\n\n")
    numbers = [int(i) for i in inp[0].split(",")]
    split_boards = [b.splitlines() for b in inp[1:]]
    int_boards = [[[int(i) for i in l.split()] for l in b] for b in split_boards]
    boards = [aoc.day_04_1.BingoBoard(board) for board in int_boards]
    print(find_losing_board(numbers, boards))


if __name__ == "__main__":
    main()
