"""
--- Day 4: Giant Squid ---

You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7

After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?

Your puzzle answer was 72770.
--- Part Two ---

On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?

Your puzzle answer was 13912.
"""
import copy
from dataclasses import dataclass, field
import typing

import more_itertools

import aoc.util


def transpose(board: typing.List[typing.List[int]]) -> typing.List[typing.List[int]]:
    return map(list, zip(*board))


@dataclass
class BingoBoard:
    """Contains the rows and columns needed to get a bingo."""

    board: typing.List[typing.List[int]]
    tipped: typing.List[int] = field(init=False, default_factory=list)
    rows: typing.List[typing.Set[int]] = field(init=False)
    cols: typing.List[typing.Set[int]] = field(init=False)

    def __post_init__(self):
        self.rows = [set(row) for row in self.board]
        self.cols = [set(col) for col in transpose(self.board)]

    def tip(self, number: int):
        self.tipped.append(number)
        for r in self.rows:
            r.discard(number)
        for c in self.cols:
            c.discard(number)

    def bingo(self) -> bool:
        return any(map(lambda r: len(r) == 0, self.rows)) or any(
            map(lambda c: len(c) == 0, self.cols)
        )

    def untipped(self) -> typing.List[int]:
        # Going over the rows is enough, as the numbers are doubled in rows and
        # cols.
        return [element for row in self.rows for element in row]

    def score(self) -> int:
        return sum(self.untipped()) * self.tipped[-1]


def get_winning_sequence(
    numbers: typing.List[int], boards: typing.List[BingoBoard]
) -> typing.List[BingoBoard]:
    def get_winners(
        num: int, boards: typing.List[BingoBoard]
    ) -> typing.Tuple[typing.Iterator[BingoBoard], typing.Iterator[BingoBoard]]:
        # Returns the winning boards in the first tuple elements and the
        # non-winning boards in the second element.
        for b in boards:
            b.tip(num)
        return more_itertools.partition(lambda b: not b.bingo(), boards)

    sequence = []
    for num in numbers:
        winner, non_winner = get_winners(num, boards)
        sequence += list(winner)
        non_winner = list(non_winner)
        boards = non_winner
        if len(non_winner) == 0:
            break
    return sequence


def find_winning_board(numbers, boards):
    seq = get_winning_sequence(numbers, boards)
    return seq[0].score()


def find_losing_board(numbers, boards):
    seq = get_winning_sequence(numbers, boards)
    return seq[-1].score()


def main():
    inp = aoc.util.read_file("day_04.txt").split("\n\n")
    numbers = [int(i) for i in inp[0].split(",")]
    split_boards = [b.splitlines() for b in inp[1:]]
    int_boards = [[[int(i) for i in l.split()] for l in b] for b in split_boards]
    boards = [BingoBoard(board) for board in int_boards]
    print("=== Part 1 ===")
    print(find_winning_board(numbers, copy.deepcopy(boards)))
    print("=== Part 2 ===")
    print(find_losing_board(numbers, copy.deepcopy(boards)))


if __name__ == "__main__":
    main()
