from pathlib import Path
from typing import List


def read_lines_from_file(file_path: Path) -> List[str]:
    with open(file_path) as file:
        return file.read().splitlines()


def convert_str_to_int_list(lst: List[str]) -> List[int]:
    return list(map(lambda x: int(x), lst))


def task01(input_lst: List[int]) -> int:
    for x in input_lst:
        y = 2020 - x
        if y in input_lst:
            return x * y
    raise RuntimeError("No solution for 2020 = x + y found")


def task02_bad_solution(input_lst: List[int]) -> int:
    for x in input_lst:
        for y in input_lst:
            for z in input_lst:
                if x + y + z == 2020:
                    # print(x, y, z)
                    return x * y * z
    raise RuntimeError("No solution for 2020 = x + y + z found")


def task02(input_lst: List[int]) -> int:
    for x in input_lst:
        yz = 2020 - x
        for y in input_lst:
            z_lst = list(filter(lambda z: y + z == yz, input_lst))
            if z_lst:
                # print(x, y, z_lst[0])
                return x * y * z_lst[0]

    raise RuntimeError("No solution for 2020 = x + y + z found")


def main():
    input_lst = convert_str_to_int_list(read_lines_from_file(Path("./input.txt")))
    result_task1 = task01(input_lst)
    print(f"Result for task1: {result_task1}")
    result_task2 = task02(input_lst)
    print(f"Result for task2: {result_task2}")


if __name__ == '__main__':
    main()
