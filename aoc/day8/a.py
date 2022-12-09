import sys
from typing import List, Set


class Tree:

    def __init__(self, x: int, y: int, height: int):
        self.x = x
        self.y = y
        self.height = height

    def __repr__(self):
        return f"Tree({self.x}, {self.y}, {self.height})"

    def __hash__(self):
        return hash((self.x, self.y))


def get_visible_trees(tree_lines: List[List[Tree]]) -> Set[Tree]:
    visible_trees = set()

    for tree_line in tree_lines:
        max_line_height = -1
        for tree in tree_line:
            if max_line_height == 9:
                break
            if tree.height > max_line_height:
                visible_trees.add(tree)
                max_line_height = tree.height

    return visible_trees


def main(input_: str) -> None:
    tree_lines = []
    for y, line in enumerate(input_.splitlines()):
        tree_line = []
        for x, height in enumerate(map(int, line)):
            tree = Tree(x, y, height)
            tree_line.append(tree)
        tree_lines.append(tree_line)

    visible_trees = set()

    tree_lines_horizontal_left_right = tree_lines
    tree_lines_vertical_top_to_bottom = list(zip(*tree_lines))
    tree_lines_horiztonal_right_left = [line[::-1] for line in tree_lines]
    tree_lines_vertical_bottom_to_top = [line[::-1] for line in tree_lines_vertical_top_to_bottom]

    visible_trees |= get_visible_trees(tree_lines_horizontal_left_right)
    visible_trees |= get_visible_trees(tree_lines_vertical_top_to_bottom)
    visible_trees |= get_visible_trees(tree_lines_horiztonal_right_left)
    visible_trees |= get_visible_trees(tree_lines_vertical_bottom_to_top)

    print(len(visible_trees))


def test_main():
    input_ = """30373
25512
65332
33549
35390"""
    main(input_)


if __name__ == "__main__":

    # # read the input from stdin
    stdin = sys.stdin.read()
    main(stdin)

    # test_main()
