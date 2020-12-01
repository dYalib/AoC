from pathlib import Path
from typing import List, Set
import time


def read_lines_from_file(file_path: Path) -> List[str]:
    with open(file_path) as file:
        return file.read().splitlines()


def convert_str_to_int_set(lst: List[str]) -> Set[int]:
    return set(map(lambda x: int(x), lst))


def task01(input_lst: Set[int]) -> int:
    for x in input_lst:
        y = 2020 - x
        if y in input_lst:
            return x * y
    raise RuntimeError("No solution for 2020 = x + y found")


def task02_bad_solution(input_lst: Set[int]) -> int:
    for x in input_lst:
        for y in input_lst:
            for z in input_lst:
                if x + y + z == 2020:
                    # print(x, y, z)
                    return x * y * z
    raise RuntimeError("No solution for 2020 = x + y + z found")


def task02(input_lst: Set[int]) -> int:
    for x in input_lst:
        yz = 2020 - x
        for y in input_lst:
            z_lst = list(filter(lambda z: y + z == yz, input_lst))
            if z_lst:
                # print(x, y, z_lst[0])
                return x * y * z_lst[0]

    raise RuntimeError("No solution for 2020 = x + y + z found")


def task02_list_comprehension(input_lst: List[int]) -> int:
    return [(x * y * z) for x in input_lst for y in input_lst for z in input_lst if 2020 == x + y + z][0]


def main():
    input_lst = convert_str_to_int_set(read_lines_from_file(Path("./input.txt")))
    result_task1 = task01(input_lst)
    print(f"Result for task1: {result_task1}")
    print("----------------------------------")

    start = time.time()
    result_task2 = task02(input_lst)
    print(f"Time task2: {time.time() - start}")
    print(f"Result for task2: {result_task2}")
    print("----------------------------------")

    start = time.time()
    result_task2_bad = task02_bad_solution(input_lst)
    print(f"Time task2_bad_solution: {time.time() - start}")
    print(f"Result for task2_bad_solution: {result_task2}")
    print("----------------------------------")

    start = time.time()
    result_list_comprehension = task02_list_comprehension(input_lst)
    print(f"Time task2_list_comprehension: {time.time() - start}")
    print(f"Result for task2_list_comprehension: {result_list_comprehension}")



if __name__ == '__main__':
    main()
