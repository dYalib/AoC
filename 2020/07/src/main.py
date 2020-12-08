from pathlib import Path
from typing import List, Dict, Set
import time


def read_whole_file(file_path: Path) -> str:
    with open(file_path) as file:
        return file.read()


def read_lines_from_file(file_path: Path) -> List[str]:
    with open(file_path) as file:
        return file.read().splitlines()


def parse_input(file_path: Path) -> Dict:
    """
    Return a bag_contains lookup in form of
    <bag color>: {(<bag_color>),<for x times>), (<bag_color>),<for x times>),...}
    In other words a lookup for bag contain bags for x time.
    """
    bags = {}
    with open(file_path) as file:
        for line in file:
            bag, contains = \
                line.replace("\n", "").replace("bags", "").replace("bag", "").replace(".", "").split("contain")
            if contains.strip() == "no other":
                contains = None
            else:
                contains = set(map(lambda x: (x.strip()[2:], int(x.strip()[:1])), contains.split(",")))
            bags.update({bag.strip(): contains})

    print(bags)
    return bags


def parse_input2(file_path: Path) -> Dict:
    """
    Return a 'bag is part of' lookup in form of:
    <bag color>: {('<bag color', '<for x times>'), ('<bag color', '<for x times>'), ...}
    In other words a lookup for bag is part of bags for x times
    It's the reverse of parse_input1
    """

    bag_is_part_of = {}
    with open(file_path) as file:
        for line in file:
            bag, contains = \
                line.replace("\n", "").replace("bags", "").replace("bag", "").replace(".", "").split("contain")
            if contains.strip() == "no other":
                contains = []
            else:
                contains = set(map(lambda x: (x.strip()[2:], x.strip()[:1]), contains.split(",")))
                for x in contains:
                    if x[0] in bag_is_part_of:
                        part_of = bag_is_part_of[x[0]]
                        part_of.add((bag.strip(), int(x[1])))
                        bag_is_part_of[x[0]] = part_of
                    else:
                        bag_is_part_of.update({x[0]: {(bag.strip(), int(x[1]))}})

        return bag_is_part_of


def bag_is_part_of(bag_is_part_of_lookup: Dict, bag: str) -> Set[str]:
    bag_colors = set()
    if not bag in bag_is_part_of_lookup:
        return {bag}
    else:
        for b in bag_is_part_of_lookup[bag]:
            bag_colors.add(b[0])
            bag_colors = bag_colors | bag_is_part_of(bag_is_part_of_lookup, b[0])
        return bag_colors


def count_nested_bags(bag_contains_lookup: Dict, bag: str) -> int:
    sum = 0
    if bag_contains_lookup[bag] is None:
        return 0
    else:
        for b in bag_contains_lookup[bag]:
            sum += b[1] + b[1] * count_nested_bags(bag_contains_lookup, b[0])
        return sum


def task01(bag_is_part_of_lookup: dict) -> int:
    part_of = bag_is_part_of(bag_is_part_of_lookup, "shiny gold")
    print(part_of)
    return len(part_of)


def task02(bag_is_part_of_lookup: dict) -> int:
    return count_nested_bags(bag_is_part_of_lookup, "shiny gold")


def main():
    start = time.time()
    bag_is_part_of_lookup = parse_input2(Path("./input.txt"))
    # result_task1 = task01(input_str)
    result_task1 = task01(bag_is_part_of_lookup)
    print(f"Time task1: {time.time() - start}")
    print(f"Result for task1: {result_task1}")
    print("----------------------------------")

    start = time.time()
    bag_contains = parse_input(Path("./input.txt"))
    result_task2 = task02(bag_contains)
    print(f"Time task2: {(time.time() - start)}")
    print(f"Result for task2: {result_task2}")
    print("----------------------------------")


if __name__ == '__main__':
    main()
