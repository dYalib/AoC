from pathlib import Path
from typing import List, Set
import time
import re


def read_lines_from_file(file_path: Path) -> List[str]:
    with open(file_path) as file:
        return file.read().splitlines()


def task01(input_lst: Set[str]) -> int:
    counter = 0
    for row in input_lst:
        least, most, pattern, empty, passwd = re.split("[- :]", row)
        if int(least) <= passwd.count(pattern) <= int(most):
            # print(least, most, pattern, empty, passwd)
            counter += 1
    return counter


def task02(input_lst: Set[str]) -> int:
    counter = 0
    for row in input_lst:
        match_pos, missmatch_pos, pattern, empty, passwd = re.split("[- :]", row)
        match_pos = int(match_pos) - 1
        missmatch_pos = int(missmatch_pos) - 1
        if (passwd[match_pos] == pattern and passwd[missmatch_pos] != pattern) or \
                (passwd[match_pos] != pattern and passwd[missmatch_pos] == pattern):
            # print(match_pos, missmatch_pos, pattern, empty, passwd)
            counter += 1
    return counter


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
