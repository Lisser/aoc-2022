import math
from collections import defaultdict
from enum import Enum
from typing import List, Literal, Union

from aoc.solution import Solution


class Product:
    """Represents a product of a list of numbers."""

    def __init__(self, factors: List[int]):
        self.factors = factors

    @property
    def value(self) -> int:
        return math.prod(self.factors)

    def __repr__(self):
        return str(self.value)


class Operator(Enum):
    ADD = "+"
    MULTIPLY = "*"


class Operation:
    def __init__(self, operator: Operator, operand: Union[int, Literal["old"]]):
        self.operator = operator
        self.operand = operand


class Monkey:
    def __init__(
        self,
        id_: int,
        items: List[Product],
        operation: Operation,
        test_divisor: int,
        truth_result_monkey: int,
        false_result_monkey: int,
    ):
        self.id = id_
        self.items = items
        self.operation = operation
        self.test_divisor = test_divisor
        self.truth_result_monkey = truth_result_monkey
        self.false_result_monkey = false_result_monkey


def parse_chunk(chunk: str) -> Monkey:
    line1, line2, line3, line4, line5, line6 = chunk.splitlines()
    id_ = int(line1[-2])
    items_ = list(map(int, line2.split(": ")[1].split(", ")))
    items_ = [Product([i]) for i in items_]
    *_, operator, operand = line3.split()
    operation = Operation(Operator(operator), int(operand) if operand.isdigit() else operand)
    return Monkey(id_, items_, operation, int(line4.split()[-1]), int(line5.split()[-1]), int(line6.split()[-1]))


def parse_chunks(chunks: str) -> List[Monkey]:
    return list(map(parse_chunk, chunks.split("\n\n")))


class Day11(Solution):
    def __init__(self):
        self.monkeys = {}
        self.inspections = defaultdict(int)

    def solve(self, input_: str) -> int:
        ...

    def process_round(self) -> None:
        for monkey in self.monkeys.values():
            self.process_turn(monkey)

    def process_turn(self, monkey: Monkey) -> None:
        ...

    def print_monkey_items(self):
        print("\n")
        for monkey in self.monkeys.values():
            items_str = ", ".join(map(str, monkey.items))
            print(f"Monkey {monkey.id}: {items_str}")

    def print_monkey_inspections(self):
        for monkey in self.monkeys.values():
            print(f"Monkey {monkey.id} inspected items {self.inspections[monkey.id]} times.")


class SolutionA(Day11):

    def process_turn(self, monkey: Monkey) -> None:
        for item in monkey.items:
            operand = monkey.operation.operand
            if operand == "old":
                operand = item.value
            result = item.value + operand if monkey.operation.operator == Operator.ADD else item.value * operand
            result = math.floor(result / 3)
            throw_to_monkey = monkey.truth_result_monkey if result % monkey.test_divisor == 0 else monkey.false_result_monkey
            self.monkeys[throw_to_monkey].items.append(Product([result]))
            self.inspections[monkey.id] += 1

        monkey.items = []

    def solve(self, input_: str) -> int:
        self.monkeys = {monkey.id: monkey for monkey in parse_chunks(input_)}
        for _ in range(20):
            self.process_round()
        self.print_monkey_inspections()
        *_, top1, top2 = sorted(self.inspections.values())
        return top1 * top2


class SolutionB(Day11):

    def __init__(self):
        super().__init__()
        self.divisor = 0

    def process_turn(self, monkey: Monkey) -> None:
        for item in monkey.items:
            operand = monkey.operation.operand
            if operand == "old":
                operand = item.value
            result = item.value + operand if monkey.operation.operator == Operator.ADD else item.value * operand
            result = result % self.divisor
            throw_to_monkey = monkey.truth_result_monkey if result % monkey.test_divisor == 0 else monkey.false_result_monkey
            self.monkeys[throw_to_monkey].items.append(Product([result]))
            self.inspections[monkey.id] += 1

        monkey.items = []

    def solve(self, input_: str) -> int:
        self.monkeys = {monkey.id: monkey for monkey in parse_chunks(input_)}
        self.divisor = math.lcm(*[monkey.test_divisor for monkey in self.monkeys.values()])

        print_round_at = [1, 20, 1000, 2000, 9000, 10000]
        for i in range(1, 10001):
            self.process_round()
            if i in print_round_at:
                print(f"== After round {i} ==")
                self.print_monkey_inspections()
                print("")

        *_, top1, top2 = sorted(self.inspections.values())
        return top1 * top2
