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


def convert_to_seat_id(input_lst: list) -> Set[int]:
    # remap "B","R" with 1 and "F","L" with 0
    # -> the result looks like a binary representation an can easy convert to a number
    return set(map(lambda x: int(re.sub("[BR]", "1", re.sub("[FL]", "0", x)), 2), input_lst))


def task01(input_lst: list) -> int:
    # simply return the maximum of the set
    return max(convert_to_seat_id(input_lst))


def task02(input_lst: list):
    id_lst= list(convert_to_seat_id(input_lst))
    list_iter = iter(id_lst)
    for x in list_iter:
        try:
            if list_iter.__next__() - x == 2:
                return x + 1
        except StopIteration:
            print("Oh. oh, there is no free seat :-(")


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
