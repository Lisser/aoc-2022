from pathlib import Path

import pytest

from aoc.day10.solution import Day10SolutionA, Day10SolutionB

day = Path(__file__).stem

print(day)


@pytest.fixture
def sample_input():
    input_file = Path(__file__).parent / "samples" / f"{day}.txt"
    return input_file.read_text()


@pytest.fixture
def puzzle_input():
    input_file = Path(__file__).parent / "inputs" / f"{day}.txt"
    return input_file.read_text()


@pytest.fixture
def solution_a():
    return Day10SolutionA()


@pytest.fixture
def solution_b():
    return Day10SolutionB()


def test_solution_a_sample(sample_input, solution_a):
    assert solution_a.solve(sample_input) == 13140


def test_solution_a_puzzle_input(puzzle_input, solution_a):
    n = solution_a.solve(puzzle_input)
    print(f"Solution: {n}")
    assert n == 14520


def test_solution_b_sample(sample_input, solution_b):
    res = solution_b.solve(sample_input)
    print(res)


def test_solution_b_puzzle_input(puzzle_input, solution_b):
    res = solution_b.solve(puzzle_input)
    print(res)
