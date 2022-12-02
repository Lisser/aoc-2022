import sys


def day1_b(input_: str) -> None:
    sums = [sum(map(int, section.splitlines())) for section in input_.split('\n\n')]
    top_3 = list(sorted(sums, reverse=True))[0:3]
    print(sum(top_3))


if __name__ == "__main__":
    # read the input from stdin
    stdin = sys.stdin.read()
    day1_b(stdin)
