from pathlib import Path
from typing import List


def read_lines_from_file(file_path: Path) -> List[str]:
    with open(file_path) as file:
        return file.read().splitlines()


def convert_str_to_int_list(lst: List[str]) -> List[int]:
    return list(map(lambda x: int(x), lst))


def task01(input_lst: List[int]):
    for x in input_lst:
        y = 2020 - x
        if y in input_lst:
            return x * y


def main():
    input_lst = convert_str_to_int_list(read_lines_from_file(Path("./input.txt")))
    result_task1 = task01(input_lst)
    print(f"Result for task1: {result_task1}")


if __name__ == '__main__':
    main()
