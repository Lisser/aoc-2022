import sys
from typing import Set


class Compartiment(Set[str]):
    ...


def to_compartiments(line: str) -> tuple[Compartiment, Compartiment]:
    half = int(len(line) / 2)
    return Compartiment(line[:half]), Compartiment(line[half:])


def to_score(item: str) -> int:
    """Converts a char to a score. lower case chars are worth 1 point through 26 points, upper case chars are worth 27 points through 52 points."""
    if item.islower():
        return ord(item) - ord('a') + 1
    return ord(item) - ord('A') + 27


def day3_a(input_: str) -> None:
    rucksacks = list(map(to_compartiments, input_.splitlines()))
    priorities = []
    for left, right in rucksacks:
        double_items = left & right
        double_items_scores = list(map(to_score, double_items))
        priorities.append(sum(double_items_scores))
    print(priorities)
    print(sum(priorities))


def test_day3_a():
    input_ = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
    day3_a(input_)


if __name__ == "__main__":
    # read the input from stdin
    stdin = sys.stdin.read()
    day3_a(stdin)

    # test_day3_a()

