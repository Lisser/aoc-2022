from pathlib import Path
from typing import Protocol

from aoc.solution import Solution


class SolutionModule(Protocol):
    def SolutionA(self) -> Solution:
        ...

    def SolutionB(self) -> Solution:
        ...


class SolutionTest:

    day: str

    @property
    def module(self) -> SolutionModule:
        return __import__(f"aoc.{self.day}.solution", fromlist=["SolutionA", "SolutionB"])

    @property
    def sample_input(self):
        input_file = Path(__file__).parent / "samples" / f"{self.day}.txt"
        return input_file.read_text()

    @property
    def puzzle_input(self):
        input_file = Path(__file__).parent / "inputs" / f"{self.day}.txt"
        return input_file.read_text()

    @property
    def solution_a(self):
        return self.module.SolutionA()

    @property
    def solution_b(self):
        return self.module.SolutionA()
