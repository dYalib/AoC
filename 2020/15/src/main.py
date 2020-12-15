from pathlib import Path
from typing import List, Dict, Set, Tuple
import time
from tqdm import tqdm
import itertools


def parse_input(file_path: Path) -> List[int]:
    with open(file_path) as file:
        lst = file.readline().replace("\n", "").split(",")
        return list(map(lambda x: int(x), lst))


def add_to_memory(memory: Dict[int, List[int]], val: int, turn: int) -> None:
    if val in memory:
        memory[val] = memory[val][-1:] + [turn]
    else:
        memory.update({val: [turn]})


def task01(lst: List[int], turns=2020) -> int:
    memory = dict(zip(lst, map(lambda x: [x], range(1, len(lst) + 1))))
    last_spoken = lst[-1]
    first_time_spoken = True
    last_spoken = None
    # memory = {}
    # print(memory)
    for t in tqdm(range(len(lst), turns)):
        if first_time_spoken:
            # spoke 0
            last_spoken = 0
        else:
            last_spoken = memory[last_spoken][-1] - memory[last_spoken][-2]
        first_time_spoken = last_spoken not in memory
        add_to_memory(memory, last_spoken, t + 1)

    return (last_spoken)


def task02(lst: List[int]) -> int:
    return task01(lst, 30000000)


def main():
    input_lst = parse_input(Path("./input.txt"))
    start = time.time()
    result_task1 = task01(input_lst)
    print(f"Time task1: {time.time() - start}")
    print(f"Result for task1: {result_task1}")
    print("----------------------------------")

    #input_lst = parse_input(Path("./input_tst.txt"))
    start = time.time()
    result_task2 = task02(input_lst)
    print(f"Time task2: {(time.time() - start)}")
    print(f"Result for task2: {result_task2}")
    print("----------------------------------")


if __name__ == '__main__':
    main()
