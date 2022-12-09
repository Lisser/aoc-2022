import sys
from typing import List, Set, cast


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


class Forest:
    def __init__(self, input_: str):
        tree_lines = []
        for y, line in enumerate(input_.splitlines()):
            tree_line = []
            for x, height in enumerate(map(int, line)):
                tree = Tree(x, y, height)
                tree_line.append(tree)
            tree_lines.append(tree_line)

        self._tree_lines_horizontal_left_right = tree_lines
        self._tree_lines_vertical_top_bottom = cast(List[List[Tree]], list(zip(*tree_lines)))
        self._tree_lines_horizontal_right_left = [line[::-1] for line in tree_lines]
        self._tree_lines_vertical_bottom_top = [line[::-1] for line in self._tree_lines_vertical_top_bottom]

        self._visible_trees = set()

        self._visible_trees |= get_visible_trees(self._tree_lines_horizontal_left_right)
        self._visible_trees |= get_visible_trees(self._tree_lines_vertical_top_bottom)
        self._visible_trees |= get_visible_trees(self._tree_lines_horizontal_right_left)
        self._visible_trees |= get_visible_trees(self._tree_lines_vertical_bottom_top)

    @property
    def visible_trees(self):
        return self._visible_trees

    @staticmethod
    def get_scenic_score_per_line(tree: Tree, line: List[Tree]) -> int:
        score = 0
        # scan until we hit a tree with height >= tree.height
        x = 0
        while True:
            if x >= len(line):
                break
            other_tree = line[x]
            score += 1
            if other_tree.height >= tree.height:
                break
            x += 1
        return score

    def get_scenic_score(self, tree: Tree) -> int:
        line_left = self._tree_lines_horizontal_left_right[tree.y][tree.x-1::-1]
        line_above = self._tree_lines_vertical_top_bottom[tree.x][tree.y-1::-1]
        line_right = self._tree_lines_horizontal_left_right[tree.y][tree.x + 1:]
        line_below = self._tree_lines_vertical_top_bottom[tree.x][tree.y + 1:]

        scores = [
            self.get_scenic_score_per_line(tree, line) for line in (line_above, line_left, line_below, line_right)
        ]

        # return product of scores
        return scores[0] * scores[1] * scores[2] * scores[3]


def main(input_: str) -> None:

    forest = Forest(input_)
    # print(forest.visible_trees)

    visible_trees = [tree for tree in forest.visible_trees]
    scores = [forest.get_scenic_score(tree) for tree in visible_trees]
    print(max(scores))


def test_main():
    input_ = """30373
25512
65332
33549
35390"""
    main(input_)


def test_get_scenic_score_per_line_1():
    input_ = """30373
25512
65332
33549
35390"""
    forest = Forest(input_)
    tree_ = Tree(2, 3, 5)
    print(forest.get_scenic_score(tree_))
    assert forest.get_scenic_score(tree_) == 8


def test_get_scenic_score_per_line_2():
    input_ = """30373
25512
65332
33549
35390"""
    forest = Forest(input_)
    tree_ = Tree(2, 1, 5)
    print(forest.get_scenic_score(tree_))
    assert forest.get_scenic_score(tree_) == 4


if __name__ == "__main__":

    # # read the input from stdin
    stdin = sys.stdin.read()
    main(stdin)

    # test_main()
    # test_get_scenic_score_per_line_1()
    # test_get_scenic_score_per_line_2()

