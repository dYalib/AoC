from pathlib import Path
from typing import List, Dict, Set, Tuple
import time
from sympy.ntheory.modular import crt


def parse_input(file_path: Path) -> Tuple[int, Set[int]]:
    with open(file_path) as file:
        timestamp = int(file.readline())
        bus_ids = set(file.readline().replace("x", "").replace("\n", "").split(","))
        bus_ids.remove("")
        bus_ids = set(map(lambda x: int(x), bus_ids))
        print(timestamp, bus_ids)

        return timestamp, bus_ids


def parse_input2(file_path: Path) -> List[str]:
    with open(file_path) as file:
        file.readline()
        bus_ids = list(file.readline().replace("\n", "").split(","))
        #print(bus_ids)

        return bus_ids


def next_bus_times(timestamp: int, bus_id: int) -> int:
    return ((timestamp // bus_id) + 1) * bus_id


def task01(input_tuple: Tuple[int, Set[int]]) -> int:
    timestamp = input_tuple[0]
    bus_ids = input_tuple[1]
    next_bus = min(map(lambda x: (x, next_bus_times(timestamp, x)), bus_ids), key=lambda x: x[1])
    print(next_bus)
    return next_bus[0] * (next_bus[1] - timestamp)


def valid_departure(timestamp: int, bus: Tuple[int, int]) -> bool:
    return (timestamp + bus[1]) % bus[0] == 0


def earliest_timestamp(timestamp: int, bus_lst: List[Tuple[int, int]]) -> bool:
    for bus in bus_lst:
        if not valid_departure(timestamp, bus):
            return False
    return True


def task02_bruteforce(input_lst: List[str]) -> int:
    """
    Need incredible much time. not a suitable solution...
    Better way : https://de.wikipedia.org/wiki/Chinesischer_Restsatz
    """
    lst = list(zip(input_lst, range(len(input_lst))))
    lst = list(filter(lambda x: x[0] != "x", lst))
    lst = list(map(lambda x: (int(x[0]), x[1]), lst))

    step = lst[0][0]
    lst.pop(0)

    # t = step
    t = 100000000000304
    while True:
        if earliest_timestamp(t, lst):
            return t
        t += 823


def task02b(input_lst: List[str]):
    """Use the CRT implementation from SymPy https://docs.sympy.org/latest/modules/ntheory.html """
    lst = list(zip(input_lst, range(len(input_lst))))
    lst = list(filter(lambda x: x[0] != "x", lst))
    lst = list(map(lambda x: (int(x[0]), x[1]), lst))
    m = []
    v = []
    for e in lst:
        m.append(e[0])
        v.append((e[0] - e[1]) % e[0])
    # print(m, v)
    return crt(m, v)[0]


def main():
    input_lst = parse_input(Path("./input.txt"))
    start = time.time()
    print(next_bus_times(939, 59))
    result_task1 = task01(input_lst)
    print(f"Time task1: {time.time() - start}")
    print(f"Result for task1: {result_task1}")
    print("----------------------------------")

    input_lst = parse_input2(Path("./input.txt"))
    start = time.time()
    result_task2 = task02b(input_lst)
    print(f"Time task2: {(time.time() - start)}")
    print(f"Result for task2: {result_task2}")
    print("----------------------------------")


if __name__ == '__main__':
    main()
