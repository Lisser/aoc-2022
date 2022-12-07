from __future__ import annotations
import sys
from typing import Optional, Iterator


class Directory:

    def __init__(self, name: str, parent: Optional[Directory] = None) -> None:
        self.name = name
        if parent is None:
            self.parent = self
        else:
            self.parent = parent
        self.subfolders = []
        self.files = []

    def add_subfolder(self, subfolder: Directory) -> None:
        self.subfolders.append(subfolder)

    def add_file(self, file: File) -> None:
        self.files.append(file)

    @property
    def size(self) -> int:
        return sum([f.size for f in self.files + self.subfolders])

    def __repr__(self):
        return f"Directory(\"{self.name}\")"

    def print_tree(self, indent: int = 0) -> None:
        print(" " * indent + f"- {self.name} (dir)")
        for d in self.subfolders:
            d.print_tree(indent=indent + 2)
        for f in self.files:
            print(" " * (indent + 1) + f"- {f.name}")

    def find_subfolders(self, predicate: callable) -> Iterator[Directory]:
        for d in self.subfolders:
            if predicate(d):
                yield d
            yield from d.find_subfolders(predicate)


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


def main(input_: str) -> None:
    lines = input_.splitlines()

    root = Directory("/")
    current_dir = root

    for line in lines[1:]:
        if line.startswith("$ cd "):
            arg = line[5:]
            if arg == "..":
                current_dir = current_dir.parent
            else:
                subfolder = Directory(arg, current_dir)
                current_dir.add_subfolder(subfolder)
                current_dir = subfolder
        elif line == "$ ls":
            ...
        elif line.startswith("dir "):
            ...
        else:
            size, filename = line.split()
            file = File(filename, int(size))
            current_dir.add_file(file)

    subfolders_lt_100000 = list(root.find_subfolders(lambda d: d.size <= 100000))

    disk_space = 70000000
    required_space = 30000000
    free_space = disk_space - root.size
    needed_space = required_space - free_space
    print("Used space:", root.size)
    print("Free space:", free_space)
    print("Needed space:", needed_space)

    all_subfolders = list(root.find_subfolders(lambda d: True))
    sorted_subfolders = sorted(all_subfolders, key=lambda d: d.size)
    for d in sorted_subfolders:
        if d.size >= needed_space:
            print(d, d.size)
            break


def test_main():
    input_ = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
    main(input_)


if __name__ == "__main__":

    # # read the input from stdin
    stdin = sys.stdin.read()
    main(stdin)

    # test_main()
