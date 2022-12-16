from pathlib import Path

from aoc.day12.solution import Map, Point, Edge
from tests.conftest import SolutionTest


class TestDay11(SolutionTest):
    day = Path(__file__).stem

    def test_parse_map(self):
        map_ = Map.parse(self.sample_input)
        assert map_[0][0].height == 0  # S
        assert map_[1][0].height == 1  # a
        assert map_[0][2].height == 2  # b
        assert map_[0][3].height == 17  # q
        assert map_[4][5].height == 7  # g
        assert map_[4][7].height == 9  # i
        assert map_[2][5].height == 27  # E

    def test_points(self):
        assert Point(0, 0, 0) == Point(0, 0, 0)
        assert Point(5, 5, 10) == Point(5, 5, 0)
        assert Point(1, 0, 0) > Point(0, 0, 0)
        assert Point(0, 0, 0) < Point(1, 0, 0)
        assert Point(0, 1, 0) > Point(0, 0, 0)
        assert Point(1, 0, 0) > Point(0, 1, 0)

        assert list(sorted([Point(1, 0, 0), Point(0, 1, 1)])) == [Point(0, 1, 1), Point(1, 0, 0)]

    def test_neighbours(self):
        map_ = Map(self.sample_input)
        start = Point(0, 0, 0)
        assert list(map_.neighbours_of(start)) == [(start, Point(1, 0, 1)), (start, Point(0, 1, 1))]

    def test_edges(self):
        a = Point(0, 0, 0)
        b = Point(1, 0, 0)
        assert Edge(b, a) == Edge(a, b)

    def test_edges_hash(self):
        sample_map = """Sa
aE"""
        self.solution_a.solve(sample_map)

    def test_solution_a_sample(self):
        res = self.solution_a.solve(self.sample_input)
        print("\n")
        print(res)
        assert res == 31

    def test_solution_a_sample2(self):
        sample = "SEzyxwv\napqrstu\nbonmlkj\ncdefghi"
        res = self.solution_a.solve(sample)
        print("\n")
        print(res)
        assert res == 27

    def test_solution_a_puzzle_input(self):
        res = self.solution_a.solve(self.puzzle_input)
        print("\n")
        print(res)
        assert res == 339

    def test_solution_b_sample(self):
        res = self.solution_b.solve(self.sample_input)
        print("\n")
        print(res)

    def test_solution_b_puzzle_input(self):
        res = self.solution_b.solve(self.puzzle_input)
        print("\n")
        print(res)
