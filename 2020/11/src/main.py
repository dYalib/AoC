from pathlib import Path
from typing import List, Tuple
import time
import copy


def parse_input(file_path: Path) -> List[List[str]]:
    grid = []
    with open(file_path) as file:
        for line in file:
            grid.append([*line.replace("\n", "")])
    return grid


def is_occupied(grid, x: int, y: int) -> bool:
    try:
        if x >= 0 and y >= 0 and grid[x][y] == "#":
            return True
    except IndexError:
        pass
    return False


def adjacent_occupied_seats(grid: List[List[str]], seat_pos: Tuple[int, int]) -> int:
    x = seat_pos[0]
    y = seat_pos[1]
    return sum([is_occupied(grid, x + a, y + b) for a in [-1, 0, 1] for b in [-1, 0, 1] if not 0 == a == b])


def first_see_occupied_seats(grid: List[List[str]], seat_pos: Tuple[int, int]) -> int:

    # TODO: Holy moly is this a terrible ugly function... Because the lack of time i can't refactor it yet :-(

    x = seat_pos[0]
    y = seat_pos[1]
    cnd = 0

    for a in range(x + 1, len(grid)):
        if grid[a][y] == "L":
            break
        elif is_occupied(grid, a, y):
            cnd += 1
            break

    for a in range(x - 1, -1, -1):
        if grid[a][y] == "L":
            break
        elif is_occupied(grid, a, y):
            cnd += 1
            break

    for b in range(y + 1, len(grid[x])):
        if grid[x][b] == "L":
            break
        elif is_occupied(grid, x, b):
            cnd += 1
            break

    for b in range(y - 1, -1, -1):
        if grid[x][b] == "L":
            break
        elif is_occupied(grid, x, b):
            cnd += 1
            break
    a = x + 1
    b = y + 1
    try:
        while a <= len(grid) and b <= len(grid[a]):
            if grid[a][b] == "L":
                break
            elif is_occupied(grid, a, b):
                cnd += 1
                break
            a += 1
            b += 1
    except IndexError:
        pass

    a = x + 1
    b = y - 1
    try:
        while a <= len(grid) and b >= 0:
            if grid[a][b] == "L":
                break
            if is_occupied(grid, a, b):
                cnd += 1
                break
            a += 1
            b -= 1
    except IndexError:
        pass

    a = x - 1
    b = y + 1
    try:
        while a >= 0 and b <= len(grid[a]):
            if grid[a][b] == "L":
                break
            if is_occupied(grid, a, b):
                cnd += 1
                break
            a -= 1
            b += 1
    except IndexError:
        pass

    a = x - 1
    b = y - 1
    try:
        while a >= 0 and b >= 0:
            if grid[a][b] == "L":
                break
            if is_occupied(grid, a, b):
                cnd += 1
                break
            a -= 1
            b -= 1
    except IndexError:
        pass

    return cnd


def print_grid(grid: List[List[str]]) -> None:
    for row in grid:
        print("".join(row))


def simulate(grid: List[List[str]]) -> List[List[str]]:
    result_grid = copy.deepcopy(grid)
    while True:
        work_grid = copy.deepcopy(result_grid)
        changed = False
        for x in range(len(work_grid)):
            for y in range(len(work_grid[x])):
                if work_grid[x][y] == "L" and adjacent_occupied_seats(work_grid, (x, y)) == 0:
                    result_grid[x][y] = "#"
                    changed = True
                elif work_grid[x][y] == "#" and adjacent_occupied_seats(work_grid, (x, y)) >= 4:
                    result_grid[x][y] = "L"
                    changed = True
        #print_grid(result_grid)
        #print("-------------------------------------------")
        if not changed:
            break
    return result_grid


def simulate2(grid: List[List[str]]) -> List[List[str]]:
    result_grid = copy.deepcopy(grid)
    while True:
        cur_grid = copy.deepcopy(result_grid)
        changed = False
        for x in range(len(cur_grid)):
            for y in range(len(cur_grid[x])):
                if cur_grid[x][y] == "L" and first_see_occupied_seats(cur_grid, (x, y)) == 0:
                    result_grid[x][y] = "#"
                    changed = True
                elif cur_grid[x][y] == "#" and first_see_occupied_seats(cur_grid, (x, y)) >= 5:
                    result_grid[x][y] = "L"
                    changed = True
        #print_grid(result_grid)
        #print("-------------------------------------------")
        if not changed:
            break
    return result_grid


def task01(grid: List[List[str]]) -> int:
    final_grid = simulate(grid)
    cnt = 0
    for row in final_grid:
        for seat in row:
            if seat == "#":
                cnt += 1
    return cnt


def task02(grid: List[List[str]]) -> int:
    final_grid = simulate2(grid)
    cnt = 0
    for row in final_grid:
        for seat in row:
            if seat == "#":
                cnt += 1
    return cnt


def main():
    grid = parse_input(Path("./input.txt"))
    # print_grid(grid)
    start = time.time()
    result_task1 = task01(grid)
    print(f"Time task1: {time.time() - start}")
    # print(f"Result for task1: {result_task1}")
    print("----------------------------------")

    start = time.time()
    result_task2 = task02(grid)
    print(f"Time task2: {time.time() - start}")
    print(f"Result for task2: {result_task2}")
    print("----------------------------------")


if __name__ == '__main__':
    main()
