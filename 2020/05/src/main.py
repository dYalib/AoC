from pathlib import Path
from typing import List, Dict, Set
import time
import re


def read_whole_file(file_path: Path) -> str:
    with open(file_path) as file:
        return file.read()


def read_lines_from_file(file_path: Path) -> List[str]:
    with open(file_path) as file:
        return file.read().splitlines()


def task01(input_lst: list) -> int:
    # remap "B","R" with 1 and "F","L" with 0
    # -> the result looks like a binary representation an can easy convert to a number
    input_lst_subst = set(map(lambda x: re.sub("[BR]", "1", re.sub("[FL]", "0", x)), input_lst))
    # simply the formula applied...
    return max(map(lambda x: int(x[:-3], 2) * 8 + int(x[7:], 2), input_lst_subst))


def task02(input_lst: list) -> int:
    pass


def main():
    input_lst = read_lines_from_file(Path("./input.txt"))
    start = time.time()
    result_task1 = task01(input_lst)
    print(f"Time task1: {time.time() - start}")
    print(f"Result for task1: {result_task1}")
    print("----------------------------------")

    start = time.time()
    result_task2 = task02(input_lst)
    print(f"Time task2: {time.time() - start}")
    print(f"Result for task2: {result_task2}")
    print("----------------------------------")


if __name__ == '__main__':
    main()
