from pathlib import Path
from typing import List
import time
from functools import reduce


def read_lines_from_file(file_path: Path) -> List[str]:
    with open(file_path) as file:
        return file.read().splitlines()


def task01(input_lst: List[str], step_x=3, step_y=1) -> int:
    x_max = len(input_lst[0])
    x = 0
    counter = 0
    for row in input_lst[::step_y]:
        if row[x] == "#":
            counter += 1
        x = (x + step_x) % x_max
    return counter


def task02(input_lst: List[str]) -> int:
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return reduce(lambda x, y: x * y, map(lambda x: task01(input_lst, x[0], x[1]), slopes))


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
