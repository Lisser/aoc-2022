from __future__ import annotations

import sys
from enum import Enum
from pathlib import Path


class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def adjacent(self, other: Position):
        """Return True if x or y is max 1 apart"""
        return abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1

    def middle(self, other: Position):
        """Return the position between self and other"""
        return Position(round((self.x + other.x) // 2), round((self.y + other.y) // 2))

    def in_grid_line(self, other: Position):
        """Return True if self and other are in a line"""
        return self.x == other.x or self.y == other.y

    def __repr__(self):
        return f"Position({self.x}, {self.y})"

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other: Position):
        return self.x == other.x and self.y == other.y



class Direction(Enum):
    UP = "U"
    RIGHT = "R"
    DOWN = "D"
    LEFT = "L"


class Board:

    def __init__(self):
        self.head = Position(0, 0)
        self.tail = Position(0, 0)
        self.tail_visited = {self.tail}

    def move_head(self, direction: Direction):
        if direction == Direction.UP:
            self.head.y += 1
        elif direction == Direction.RIGHT:
            self.head.x += 1
        elif direction == Direction.DOWN:
            self.head.y -= 1
        elif direction == Direction.LEFT:
            self.head.x -= 1

        # if tail is within distance 1 of head, don't move
        if self.tail.adjacent(self.head):
            return

        # if self.tail is in same line as self.head, move it to middle
        if self.tail.in_grid_line(self.head):
            self.tail = self.head.middle(self.tail)

        # self.head is two spaces apart from self.tail, move diagonal
        else:
            move_x = 1 if self.head.x > self.tail.x else -1
            move_y = 1 if self.head.y > self.tail.y else -1
            self.tail = Position(self.tail.x + move_x, self.tail.y + move_y)

        self.tail_visited.add(self.tail)

    def print(self):
        for y in range(20, -20, -1):
            for x in range(-20, 20):
                if Position(x, y) == self.head:
                    print("H", end="")
                elif Position(x, y) == self.tail:
                    print("T", end="")
                elif Position(x, y) in self.tail_visited:
                    print("#", end="")
                else:
                    print(".", end="")
            print()


def main(input_: str) -> None:
    board = Board()

    for line in input_.splitlines():
        direction, distance = line.split()

        for i in range(int(distance)):
            board.move_head(Direction(direction))

    print(len(board.tail_visited))


def test_main():

    input_ = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
    main(input_)


def test_positions():
    assert Position(0, 0).adjacent(Position(0, 1))
    assert Position(1, 0).adjacent(Position(0, 1))
    assert Position(0, 0).adjacent(Position(1, 1))
    assert Position(0, 0).adjacent(Position(1, 0))

    assert Position(2, 2).in_grid_line(Position(2, 4))
    assert Position(2, 2).in_grid_line(Position(4, 2))
    assert Position(2, 2).in_grid_line(Position(0, 2))
    assert Position(2, 2).in_grid_line(Position(2, 0))

    assert not Position(2, 2).in_grid_line(Position(3, 3))

    assert Position(2, 2).middle(Position(2, 4)) == Position(2, 3)
    assert Position(2, 2).middle(Position(4, 2)) == Position(3, 2)
    assert Position(2, 2).middle(Position(0, 2)) == Position(1, 2)
    assert Position(2, 2).middle(Position(2, 0)) == Position(2, 1)


if __name__ == "__main__":

    # # read the input from stdin
    # stdin = sys.stdin.read()
    # main(stdin)

    # read input
    path = Path(__file__).parent / "input.txt"
    with open(path) as f:
        main(f.read())

    # test_main()
    # test_positions()
