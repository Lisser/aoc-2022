import sys
from typing import List, Iterable, Sized, TypeVar, Sequence

T = TypeVar('T')      # Declare type variable


def chunks(list_: Sequence[T], chunk_size: int) -> Iterable[T]:
    """Yield successive chunk_size-sized chunks from list_."""
    for i in range(0, len(list_), chunk_size):
        yield list_[i:i + chunk_size]


class Stack:
    """Represents a stack of items."""

    def __init__(self, id_: int, items: List[str]):
        self.id = id_
        self.items = items

    def __repr__(self):
        return f'Stack({self.id}, {self.items})'


class Operation:
    """Represents an operation consisting of a quantity of items, from a source stack, to a destination stack."""

    def __init__(self, quantity: int, source: Stack, destination: Stack):
        self.quantity = quantity
        self.source = source
        self.destination = destination


def main(input_: str) -> None:
    lines = input_.splitlines()

    # create stacks
    amount_stacks = int((len(lines[0]) + 1) / 4)
    stacks = {i: Stack(i, []) for i in range(1, amount_stacks + 1)}

    print(stacks)

    mark_hit = False
    for line in lines:

        if line == "":
            continue

        line_is_marker = line.startswith(" 1")
        if line_is_marker:
            mark_hit = True
            continue

        if not mark_hit:
            # fill stacks
            chunks_ = chunks(line + " ", 4)
            for i, chunk in enumerate(chunks_):
                item = chunk[1]
                if item != " ":
                    stacks[i + 1].items.insert(0, item)

        else:
            # process operation
            _, amount, _, source, _, dest = line.split(" ")

            # take items from source
            source_stack = stacks[int(source)]
            source_items = source_stack.items[-int(amount):]
            source_stack.items = source_stack.items[:-int(amount)]

            # put items in dest
            dest_stack = stacks[int(dest)]
            dest_stack.items.extend(source_items)

    tops = [stack.items[-1] for stack in stacks.values()]
    print("".join(tops))


def test_main():
    input_ = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
    main(input_)


if __name__ == "__main__":

    # # read the input from stdin
    stdin = sys.stdin.read()
    main(stdin)

    # test_main()
