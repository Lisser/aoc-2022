import sys
from enum import IntEnum


class Choice:

    def __init__(self, name: str, beats: str, value: int):
        self.name = name
        self.beats = beats
        self.value = value


ROCK = Choice('rock', 'scissors', 1)
PAPER = Choice('paper', 'rock', 2)
SCISSORS = Choice('scissors', 'paper', 3)


class Result(IntEnum):
    LOSS = 0
    DRAW = 3
    WIN = 6


DESIRED_RESULTS = {
    "X": Result.LOSS,
    "Y": Result.DRAW,
    "Z": Result.WIN,
}


CHOICE_MAP = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
}


def calc_choice(opponent: Choice, desired_result: Result) -> Choice:
    choices = [ROCK, PAPER, SCISSORS]

    if desired_result == Result.DRAW:
        return opponent

    if desired_result == Result.LOSS:
        return next(filter(lambda c: c.name == opponent.beats, choices))

    return next(filter(lambda c: c.beats == opponent.name, choices))


def calc_score(line: str) -> int:
    first, second = line.split(' ')

    opponent_choice = CHOICE_MAP[first]
    desired_result = DESIRED_RESULTS[second]

    choice = calc_choice(opponent_choice, desired_result)

    return choice.value + desired_result.value


def day2_b(input_: str) -> None:
    scores = list(map(calc_score, input_.splitlines()))
    print(sum(scores))


if __name__ == "__main__":
    # read the input from stdin
    stdin = sys.stdin.read()
    day2_b(stdin)
