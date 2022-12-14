from pathlib import Path

from tests.conftest import SolutionTest


class TestDay10(SolutionTest):
    day = Path(__file__).stem

    def test_solution_a_sample(self):
        res = self.solution_a.solve(self.sample_input)
        print("\n")
        print(res)
        assert res == 13140

    def test_solution_a_puzzle_input(self):
        res = self.solution_a.solve(self.puzzle_input)
        print("\n")
        print(res)
        assert res == 14520

    def test_solution_b_sample(self):
        res = self.solution_b.solve(self.sample_input)
        print(res)

    def test_solution_b_puzzle_input(self):
        res = self.solution_b.solve(self.puzzle_input)
        print(res)
