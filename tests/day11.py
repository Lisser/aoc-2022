from pathlib import Path

from aoc.day11.solution import parse_chunk, parse_chunks, Operator
from tests.conftest import SolutionTest


class TestDay11(SolutionTest):
    day = Path(__file__).stem

    def test_parse_chunks(self):
        monkeys = parse_chunks(self.sample_input)
        assert len(monkeys) == 4
        assert monkeys[0].id == 0
        assert monkeys[0].items == [79, 98]
        assert monkeys[0].operation.operator == Operator.MULTIPLY
        assert monkeys[0].operation.operand == 19
        assert monkeys[0].test_divisor == 23
        assert monkeys[0].truth_result_monkey == 2
        assert monkeys[0].false_result_monkey == 3

    def test_solution_a_sample(self):
        res = self.solution_a.solve(self.sample_input)
        print("\n")
        print(res)
        assert res == 10605

    def test_solution_a_puzzle_input(self):
        res = self.solution_a.solve(self.puzzle_input)
        print("\n")
        print(res)
        assert res == 72884

    def test_solution_b_sample(self):
        res = self.solution_b.solve(self.sample_input)
        print("\n")
        print(res)

    def test_solution_b_puzzle_input(self):
        res = self.solution_b.solve(self.puzzle_input)
        print("\n")
        print(res)
