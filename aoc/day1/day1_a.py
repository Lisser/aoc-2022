import sys


def day1_a(input_: str) -> None:
    sums = [sum(map(int, section.splitlines())) for section in input_.split('\n\n')]
    print(max(sums))


if __name__ == "__main__":
    # read the input from stdin
    stdin = sys.stdin.read()
    day1_a(stdin)
