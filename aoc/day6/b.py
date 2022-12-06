import sys

MARKER_SIZE = 14


def main(input_: str) -> None:
    for i in range(0, len(input_) - (MARKER_SIZE - 1)):
        chunk = input_[i:i + MARKER_SIZE]
        if len(set(chunk)) == MARKER_SIZE:
            print(i + MARKER_SIZE)
            return


def test_main():
    main("mjqjpqmgbljsphdztnvjfqwrcgsmlb")
    main("bvwbjplbgvbhsrlpgdmjqwftvncz")
    main("nppdvjthqldpwncqszvftbrmjlhg")
    main("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
    main("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")


if __name__ == "__main__":

    # # read the input from stdin
    stdin = sys.stdin.read()
    main(stdin)

    # test_main()
