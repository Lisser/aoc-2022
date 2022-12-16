from __future__ import annotations
from abc import ABC
from collections import defaultdict
from functools import cached_property
from typing import List, Set, Iterator, Tuple, Dict


class Point:

    def __init__(self, x: int, y: int, height: int):
        self.x = x
        self.y = y
        self.height = height

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, height={self.height})"

    def __eq__(self, other: Point):
        """Equality based on position"""
        return self.x == other.x and self.y == other.y

    # implement >
    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __cmp__(self, other: Point):
        if self == other:
            return self
        if self.x + self.y == other.x + other.y:
            # not equal, but inverse x and y. smaller x is higher
            return self.x - other.x
        return self.x + self.y - (other.x + other.y)

    def __hash__(self):
        return hash((self.x, self.y))


class Edge:

    def __init__(self, a: Point, b: Point):
        self.start = a
        self.end = b

    def __eq__(self, other: Edge):
        return hash(self) == hash(other)

    def __repr__(self):
        return f"({self.start.x},{self.start.y}) -> ({self.end.x},{self.end.y})"

    def __hash__(self):
        return hash(str(self))


class Map:

    def __init__(self, input_: str):
        self.start = None
        self.target = None

        lines = []
        for y, input_line in enumerate(input_.splitlines()):
            line = []
            for x, char in enumerate(input_line):
                p = Point(x, y, Map.height(char))
                if char == "S":
                    self.start = p
                elif char == "E":
                    self.target = p
                line.append(p)
            lines.append(line)
        self.lines = lines

    @staticmethod
    def height(char: str) -> int:
        if char == "S":
            return 0
        elif char == "E":
            return 25
        return ord(char) - ord('a')

    def __getitem__(self, item: int) -> List[Point]:
        return self.lines[item]

    @cached_property
    def x_size(self) -> int:
        return len(self[0])

    @cached_property
    def y_size(self) -> int:
        return len(self.lines)

    def neighbours(self) -> Iterator[Tuple[Point, Point]]:
        for line in self.lines:
            for point in line:
                yield from self.neighbours_of(point)

    def neighbours_of(self, point: Point) -> Iterator[Tuple[Point, Point]]:
        if point.x > 0:
            yield point, self[point.y][point.x - 1]  # left
        if point.x < self.x_size - 1:
            yield point, self[point.y][point.x + 1]  # right
        if point.y > 0:
            yield point, self[point.y - 1][point.x]  # up
        if point.y < self.y_size - 1:
            yield point, self[point.y + 1][point.x]  # down

    @cached_property
    def edges(self) -> Set[Edge]:
        return {Edge(a, b) for a, b in self.neighbours() if b.height <= a.height or a.height + 1 == b.height}

    @cached_property
    def edges_per_point(self) -> Dict[Point, Set[Edge]]:
        edges_per_point = defaultdict(set)
        for edge in self.edges:
            edges_per_point[edge.start].add(edge)
        return edges_per_point

    def print_path(self, path: Tuple[Point, ...]):
        grid = []
        for _ in range(self.y_size):
            grid.append(["."] * self.x_size)

        for point in path:
            grid[point.y][point.x] = "#"

        grid[self.start.y][self.start.x] = "S"
        grid[self.target.y][self.target.x] = "E"

        print("=== ... ===")
        for line in grid:
            for char in line:
                print(char, end="")
            print("\n", end="")

class Day12(ABC):

    def solve(self, input_: str) -> int:
        ...


class SolutionA(Day12):

    def __init__(self):
        self.map = None

        self.path = tuple()
        self.visited = set()
        self.shortest_paths: Dict[Point, tuple[Point, ...]] = dict()

    def visit(self, point: Point):
        for edge in self.map.edges_per_point[point]:
            # from_ = point
            target_ = edge.end

            current_path_to_target = self.shortest_paths[point] + (target_,)
            previous_path_to_target = self.shortest_paths.get(target_, None)

            if previous_path_to_target is None or len(current_path_to_target) < len(previous_path_to_target):
                self.shortest_paths[target_] = current_path_to_target
                self.visit(target_)

    def solve(self, input_: str) -> int:
        self.map = Map(input_)
        self.shortest_paths[self.map.start] = tuple()
        self.visit(self.map.start)

        # longest_shortest_path = list(sorted(self.shortest_paths.values(), key=len))[-1]
        target_path = self.shortest_paths[self.map.target]
        self.map.print_path(target_path)
        return len(target_path)


class SolutionB(Day12):

    def solve(self, input_: str) -> int:
        ...
