import sys
from typing import Set


class Compartiment(Set[str]):
    ...


class RuckSack(Set[str]):

    @property
    def compartments(self) -> tuple[Compartiment, Compartiment]:
        half = int(len(self) / 2)
        return Compartiment(self[:half]), Compartiment(self[half:])


class Group:
    def __init__(self, rucksacks: tuple[RuckSack, ...]) -> None:
        self.rucksacks = rucksacks

    def __str__(self):
        return f"Group({self.rucksacks})"

    @property
    def badge(self):
        badges = set.intersection(*self.rucksacks)
        return next(iter(badges))


def to_priority(item: str) -> int:
    """Converts a char to a score. lower case chars are worth 1 point through 26 points, upper case chars are worth 27 points through 52 points."""
    if item.islower():
        return ord(item) - ord('a') + 1
    return ord(item) - ord('A') + 27


def day3_b(input_: str) -> None:
    lines = input_.splitlines()

    groups = []
    group_size = 3
    for i in range(0, len(lines), group_size):
        rucksacks = tuple(RuckSack(line) for line in lines[i:i + group_size])
        groups.append(Group(rucksacks))

    badges = [group.badge for group in groups]
    priorities = [to_priority(badge) for badge in badges]
    print(sum(priorities))


def test_day3_b():
    input_ = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
    day3_b(input_)


if __name__ == "__main__":
    # read the input from stdin
    stdin = sys.stdin.read()
    day3_b(stdin)

    # test_day3_b()

