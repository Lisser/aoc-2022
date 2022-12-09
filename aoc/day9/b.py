from __future__ import annotations

from enum import Enum
from pathlib import Path


class Position:

    def __init__(self, x: int, y: int):
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


class Rope:

    def __init__(self, tail_segments: int = 1):
        self.head = Position(0, 0)
        self.tail_segments = {i: Position(0, 0) for i in range(tail_segments)}
        self.tail_visited = {Position(0, 0)}

    def move_head(self, direction: Direction):
        if direction == Direction.UP:
            self.head.y += 1
        elif direction == Direction.RIGHT:
            self.head.x += 1
        elif direction == Direction.DOWN:
            self.head.y -= 1
        elif direction == Direction.LEFT:
            self.head.x -= 1

        self.move_next_segment(self.head, 0)

    @staticmethod
    def next_position(previous_segment: Position, next_segment: Position) -> Position:
        # if previous_segment is within distance 1 of next_segment, don't move
        if next_segment.adjacent(previous_segment):
            return next_segment

        # if next_segment is in same line as previous_segment, move it to middle
        if next_segment.in_grid_line(previous_segment):
            return previous_segment.middle(next_segment)

        # previous_segment is two spaces apart from next_segment, move diagonal
        move_x = 1 if previous_segment.x > next_segment.x else -1
        move_y = 1 if previous_segment.y > next_segment.y else -1
        return Position(next_segment.x + move_x, next_segment.y + move_y)

    def move_next_segment(self, segment: Position, next_segment_index: int):
        next_segment = self.tail_segments[next_segment_index]

        # calc new position
        next_position = self.next_position(segment, next_segment)

        # not changed
        if next_position == next_segment:
            return

        # update position
        self.tail_segments[next_segment_index] = next_position

        # if tail, add to visited
        if next_segment_index == max(self.tail_segments.keys()):
            self.tail_visited.add(self.tail_segments[next_segment_index])
        else:
            # if not tail, move next segment
            self.move_next_segment(self.tail_segments[next_segment_index], next_segment_index + 1)

    def print(self):
        segment_positions = {}
        for key in reversed(self.tail_segments.keys()):
            segment_positions[self.tail_segments[key]] = key + 1
        for y in range(20, -10, -1):
            for x in range(-20, 20):
                p = Position(x, y)
                if p == self.head:
                    print("H", end="")
                elif p in segment_positions.keys():
                    print(segment_positions[p], end="")
                elif p in self.tail_visited:
                    print("#", end="")
                else:
                    print(".", end="")
            print()


def main(input_: str) -> None:
    rope = Rope(9)

    for line in input_.splitlines():
        direction, distance = line.split()

        for i in range(int(distance)):
            rope.move_head(Direction(direction))

        # rope.print()

    print(len(rope.tail_visited))


def test_main():

    input_ = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
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

    # read input
    path = Path(__file__).parent / "input.txt"
    with open(path) as f:
        main(f.read())

    # test_main()
    # test_positions()
