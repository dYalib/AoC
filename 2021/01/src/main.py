from pathlib import Path
from typing import List, Set
from functools import reduce
import time


def read_lines_from_file(file_path: Path) -> List[int]:
    with open(file_path) as file:
        return list(map(lambda x: int(x), file.read().splitlines()))


def task01(input_lst: List[int]) -> int:
    return reduce(lambda a, b: (a[0] + 1, b) if a[1] < b else (a[0], b), input_lst, (0, input_lst[0]))[0]


# better
def task01b(input_lst: List[int]) -> int:
    return len([(y - x) for x, y in zip(input_lst[:-1], input_lst[1:]) if y - x > 0])


def task02(input_lst: List[int]) -> int:
    lst = [input_lst[x] + input_lst[x + 1] + input_lst[x + 2] for x in range(0, len(input_lst) - 2)]
    return task01(lst)


# better
def task02b(input_lst: List[int]) -> int:
    return len([(y - x) for x, y in zip(input_lst[:-3], input_lst[3:]) if y - x > 0])


def main():
    input_lst = read_lines_from_file(Path("./input.txt"))
    start = time.time()
    # print(input_lst)
    result_task1 = task01(input_lst)
    print(f"Time task1: {time.time() - start}")
    print(f"Result for task1: {result_task1}")
    print("----------------------------------")

    start = time.time()
    result_task1 = task01b(input_lst)
    print(f"Time task1: {time.time() - start}")
    print(f"Result for task1: {result_task1}")
    print("----------------------------------")

    start = time.time()
    result_task2 = task02(input_lst)
    print(f"Time task2: {(time.time() - start)}")
    print(f"Result for task2: {result_task2}")
    print("----------------------------------")

    start = time.time()
    result_task1 = task02b(input_lst)
    print(f"Time task1: {time.time() - start}")
    print(f"Result for task1: {result_task1}")
    print("----------------------------------")


if __name__ == '__main__':
    main()
