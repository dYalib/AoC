from pathlib import Path
from typing import List, Dict, Set, Tuple
import time


def read_whole_file(file_path: Path) -> str:
    with open(file_path) as file:
        return file.read()


def read_lines_from_file(file_path: Path) -> List[str]:
    with open(file_path) as file:
        return file.read().splitlines()


def parse_input(file_path: Path) -> List[Tuple[str, int]]:
    prog = []
    with open(file_path) as file:
        for line in file:
            cmd, param = line.replace("+", "").split(" ")
            param = int(param)
            prog.append((cmd, param))

    return prog


def run_prog(prog: List[Tuple[str, int]]) -> (bool, int):
    counter = 0
    exec_lines = set()
    line_nr = 0
    while line_nr < len(prog):
        cmd = prog[line_nr]
        if line_nr in exec_lines:
            return False, counter
        elif cmd[0] == "nop":
            exec_lines.add(line_nr)
            line_nr += 1
        elif cmd[0] == "acc":
            counter += cmd[1]
            exec_lines.add(line_nr)
            line_nr += 1
        elif cmd[0] == "jmp":
            exec_lines.add(line_nr)
            line_nr += cmd[1]
    return True, counter


def task01(prog: List[Tuple[str, int]]) -> int:
    return run_prog(prog)[1]


def task02(prog: List[Tuple[str, int]]) -> int:
    # a quick and dirty solution...
    for line_nr in range(0, len(prog)):
        if prog[line_nr][0] == "jmp":
            prog[line_nr] = ("nop", prog[line_nr][1])
            terminated, counter = run_prog(prog)
            if terminated:
                return counter
            prog[line_nr] = ("jmp", prog[line_nr][1])
        elif prog[line_nr][0] == "nop":
            prog[line_nr] = ("jmp", prog[line_nr][1])
            terminated, counter = run_prog(prog)
            if terminated:
                return counter
            prog[line_nr] = ("nop", prog[line_nr][1])
    return 0


def main():
    start = time.time()
    prog = parse_input(Path("./input.txt"))
    # result_task1 = task01(input_str)
    result_task1 = task01(prog)
    print(f"Time task1: {time.time() - start}")
    print(f"Result for task1: {result_task1}")
    print("----------------------------------")

    start = time.time()
    result_task2 = task02(prog)
    print(f"Time task2: {(time.time() - start)}")
    print(f"Result for task2: {result_task2}")
    print("----------------------------------")


if __name__ == '__main__':
    main()
