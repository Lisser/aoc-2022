from abc import ABC

from aoc.day5.a import chunks


class Day10(ABC):

    def __init__(self):
        self.x = 1
        self.cycle = 1

    def process_cycle(self):
        self.cycle += 1

    def process_instruction(self, instruction: str):

        if instruction == "noop":
            self.process_cycle()
            return

        _, arg = instruction.split()
        self.process_cycle()
        self.process_cycle()
        self.x += int(arg)


class Day10SolutionA(Day10):

    def __init__(self):
        super().__init__()
        self.signals = []

    def process_cycle(self):
        if self.cycle % 40 == 20:
            self.signals.append(self.x * self.cycle)
        self.cycle += 1

    def solve(self, input_: str) -> int:
        for line in input_.splitlines():
            self.process_instruction(line)
        return sum(self.signals)


class Day10SolutionB(Day10):

    def __init__(self):
        super().__init__()
        self.output = ""

    def process_cycle(self):
        x_index_cycle = (self.cycle - 1) % 40
        if abs(x_index_cycle - self.x) <= 1:
            self.output += "\u2588"
            # self.output += "#"
        else:
            self.output += " "
        self.cycle += 1

    def solve(self, input_: str) -> str:
        for line in input_.splitlines():
            self.process_instruction(line)
        result = "\n".join(chunks(self.output, 40))
        return f"\n{result}"
