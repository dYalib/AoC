from pathlib import Path
from typing import List, Set, Tuple
from functools import reduce
from operator import mul
import time


def read_lines_from_file(file_path: Path) -> List[str]:
    with open(file_path) as file:
        return file.read().splitlines()


def reduce_three_directions(a, b) -> Tuple[int, int]:
    direction, value = b.split()
    match direction:
        case "forward":
            return a[0] + int(value), a[1]
        case "down":
            return a[0], a[1] + int(value)
        case "up":
            return a[0], a[1] - int(value)


def reduce_with_aim(a, b) -> Tuple[int, int, int]:
    direction, value = b.split()
    match direction:
        case "forward":
            return a[0] + int(value), a[1] + a[2] * int(value), a[2]
        case "down":
            return a[0], a[1], a[2] + int(value)
        case "up":
            return a[0], a[1], a[2] - int(value)


def task01(input_lst: List[str]) -> int:
    x = reduce(reduce_three_directions, input_lst, [0, 0])
    return x[0] * x[1]


def task02(input_lst: List[str]) -> int:
    x = reduce(reduce_with_aim, input_lst, [0, 0, 0])
    return x[0] * x[1]


def main():
    input_lst = read_lines_from_file(Path("./input.txt"))
    start = time.time()
    # print(input_lst)
    result_task1 = task01(input_lst)
    print(f"Time task1: {time.time() - start}")
    print(f"Result for task1: {result_task1}")
    print("----------------------------------")

    start = time.time()
    result_task2 = task02(input_lst)
    print(f"Time task2: {(time.time() - start)}")
    print(f"Result for task2: {result_task2}")
    print("----------------------------------")


if __name__ == '__main__':
    main()
