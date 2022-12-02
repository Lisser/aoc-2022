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


class ResultScore(IntEnum):
    LOSS = 0
    DRAW = 3
    WIN = 6


CHOICE_MAP = {
    "A": ROCK,     # Rock
    "B": PAPER,     # Paper
    "C": SCISSORS,     # Scissors
    "X": ROCK,     # Rock
    "Y": PAPER,     # Paper
    "Z": SCISSORS,     # Scissors
}


def calc_result(opponent: Choice, user: Choice) -> ResultScore:
    if opponent.name == user.name:
        return ResultScore.DRAW
    elif opponent.beats == user.name:
        return ResultScore.LOSS
    else:
        return ResultScore.WIN


def calc_score(line: str) -> int:
    opponent, user = line.split(' ')

    opponent_choice = CHOICE_MAP[opponent]
    user_choice = CHOICE_MAP[user]

    result = calc_result(opponent_choice, user_choice)

    return result.value + user_choice.value


def day2_a(input_: str) -> None:
    scores = list(map(calc_score, input_.splitlines()))
    print(sum(scores))


if __name__ == "__main__":
    # read the input from stdin
    stdin = sys.stdin.read()
    day2_a(stdin)
