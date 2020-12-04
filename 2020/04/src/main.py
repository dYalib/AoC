from pathlib import Path
from typing import List, Dict, Set
import time
import re


def read_whole_file(file_path: Path) -> str:
    with open(file_path) as file:
        return file.read()


def key_colon_value_string_without_quotes_to_dict(key_val_str: str, delimiter: str) -> Dict:
    # dict comprehension
    try:
        return {x.split(":")[0]: x.split(":")[1] for x in re.split(delimiter, key_val_str)}
    except IndexError as e:
        print(f"Can not convert \"{key_val_str}\" to dict.")


def check_passport_keys(passport: Dict, keys: Set) -> int:
    return keys.issubset(set(passport.keys()))


def task01(input_lst: str) -> int:
    required_passport_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    passports = re.split("\n\n", input_lst)
    # print(passports)
    return sum(
        map(lambda x: check_passport_keys(
            key_colon_value_string_without_quotes_to_dict(key_val_str=x, delimiter="[\n, ]"), required_passport_fields),
            passports))


def task02(input_lst: List[str]) -> int:
    pass


def main():
    input_str = read_whole_file(Path("./input.txt"))
    start = time.time()
    result_task1 = task01(input_str)
    print(f"Time task1: {time.time() - start}")
    print(f"Result for task1: {result_task1}")
    print("----------------------------------")


# start = time.time()
# result_task2 = task02(input_lst)
# print(f"Time task2: {time.time() - start}")
# print(f"Result for task2: {result_task2}")
# print("----------------------------------")


if __name__ == '__main__':
    main()
