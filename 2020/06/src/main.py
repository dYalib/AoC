from pathlib import Path
from typing import List, Dict, Set
import time
import re
from functools import reduce


def read_whole_file(file_path: Path) -> str:
    with open(file_path) as file:
        return file.read()


def read_lines_from_file(file_path: Path) -> List[str]:
    with open(file_path) as file:
        return file.read().splitlines()


def split_groups(input_str: str) -> List[str]:
    return re.split("\n\n", input_str)


def task01(input_lst: list) -> int:
    # remember [*'lala'] unpack a string to ['l','a','l','a']
    # this works also with a set {*'lala'} -> {'l','a'}
    return sum(map(lambda x: len({*x.replace("\n", "")}), input_lst))


def task02(input_lst: list):
    return sum((map(lambda x: len(reduce(lambda y, z: {*y}.intersection({*z}), re.split("\n", x))), input_lst)))


def main():
    input_str = read_whole_file(Path("./input.txt"))
    start = time.time()
    result_task1 = task01(split_groups(input_str))
    print(f"Time task1: {time.time() - start}")
    print(f"Result for task1: {result_task1}")
    print("----------------------------------")

    start = time.time()
    result_task2 = task02(split_groups(input_str))
    print(f"Time task2: {time.time() - start}")
    print(f"Result for task2: {result_task2}")
    print("----------------------------------")


if __name__ == '__main__':
    main()
