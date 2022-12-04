from __future__ import annotations

import sys


# Assignment is a class representing a range of numbers between 1 and 9
class Assignment:

    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def contains(self, other: Assignment):
        return self.start <= other.start and self.end >= other.end

    def overlaps(self, other: Assignment):
        return set(range(self.start, self.end + 1)).intersection(set(range(other.start, other.end + 1)))


def to_assignment(part: str) -> Assignment:
    left, right = part.split("-")
    return Assignment(int(left), int(right))


def main(input_: str) -> None:
    total = 0
    for line in input_.splitlines():
        first_, second_ = line.split(",")
        first = to_assignment(first_)
        second = to_assignment(second_)
        if first.overlaps(second):
            total += 1

    print(total)


def test_main():
    input_ = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
    main(input_)


if __name__ == "__main__":

    # # read the input from stdin
    stdin = sys.stdin.read()
    main(stdin)

    # test_main()
