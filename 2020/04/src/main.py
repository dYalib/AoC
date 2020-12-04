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


def check_passport_keys(passport: Dict, keys: Set) -> bool:
    return keys.issubset(set(passport.keys()))


def check_passport(passport: Dict, keys: Set) -> bool:
    if check_passport_keys(passport, keys) and \
            1920 <= int(passport.get("byr")) <= 2002 and \
            2010 <= int(passport.get("iyr")) <= 2020 and \
            2020 <= int(passport.get("eyr")) <= 2030 and \
            ((passport.get("hgt")[-2:] == "cm" and \
              150 <= int(passport.get("hgt")[:-2]) <= 193) or \
             (passport.get("hgt")[-2:] == "in" and \
              59 <= int(passport.get("hgt")[:-2]) <= 76)) and \
            passport.get("hcl")[:1] == "#" and \
            bool(re.search(r"^[0-9a-f]{6}$", passport.get("hcl")[1:])) and \
            passport.get("ecl") in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"} and \
            bool(re.search(r"^[0-9]{9}$", passport.get("pid"))):
        return True
    return False


def task01(input_str: str, passport_check_function) -> int:
    required_passport_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    passports = re.split("\n\n", input_str)
    # print(passports)
    return sum(
        map(lambda x: passport_check_function(
            key_colon_value_string_without_quotes_to_dict(key_val_str=x, delimiter="[\n, ]"), required_passport_fields),
            passports))


def task02(input_str: str) -> int:
    return task01(input_str, check_passport)


def main():
    input_str = read_whole_file(Path("./input.txt"))
    start = time.time()
    result_task1 = task01(input_str, check_passport_keys)
    print(f"Time task1: {time.time() - start}")
    print(f"Result for task1: {result_task1}")
    print("----------------------------------")

    start = time.time()
    result_task2 = task02(input_str)
    print(f"Time task2: {time.time() - start}")
    print(f"Result for task2: {result_task2}")
    print("----------------------------------")


if __name__ == '__main__':
    main()
