from pathlib import Path
from typing import List, Dict, Set, Tuple
import time


def parse_input(file_path: Path) -> List[int]:
    with open(file_path) as file:
        return list(map(lambda x: int(x), file.read().split("\n")))


def is_valid_number(preamble: set, nr: int, ):
    for x in preamble:
        preamble_without_x = preamble.copy()
        preamble_without_x.remove(x)
        for y in preamble:
            if x + y == nr:
                return True
    return False


def task01(input_lst: List[int]) -> int:
    # not efficient, but it works :-D
    preamble_len = 25
    for x in range(preamble_len, len(input_lst)):
        if not is_valid_number(set(input_lst[x - preamble_len:preamble_len + x]), input_lst[x]):
            return input_lst[x]


def task02(input_lst: List[int]) -> int:
    # not efficient, but it works :-D
    for subset_len in range(2, len(input_lst)):
        for x in range(subset_len, len(input_lst)):
            subset=set(input_lst[x - subset_len: subset_len])
            if sum(subset) == 14360655:
                return min(subset) + max(subset)


def main():
    start = time.time()
    input_lst = parse_input(Path("./input.txt"))
    print(input_lst)
    # result_task1 = task01(input_str)
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
