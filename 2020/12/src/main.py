from pathlib import Path
from typing import List, Dict, Set, Tuple
import time


class Ferry:
    def __init__(self, waypoint: bool = False):
        # E=0, S=1, W=2, N=3
        self.cur_direction = 0
        self.pos = (0, 0)
        self.waypoint = waypoint
        self.waypoint_pos = (10, -1)

    @staticmethod
    def _direction_str_to_int(direction: str) -> int:
        if direction == "E":
            return 0
        elif direction == "S":
            return 1
        elif direction == "W":
            return 2
        elif direction == "N":
            return 3

    def __move_n(self, units: int) -> None:
        if not self.waypoint:
            self.pos = (self.pos[0], self.pos[1] - units)
        else:
            self.waypoint_pos = (self.waypoint_pos[0], self.waypoint_pos[1] - units)

    def __move_s(self, units: int) -> None:
        if not self.waypoint:
            self.pos = (self.pos[0], self.pos[1] + units)
        else:
            self.waypoint_pos = (self.waypoint_pos[0], self.waypoint_pos[1] + units)

    def __move_e(self, units: int) -> None:
        if not self.waypoint:
            self.pos = (self.pos[0] + units, self.pos[1])
        else:
            self.waypoint_pos = (self.waypoint_pos[0] + units, self.waypoint_pos[1])

    def __move_w(self, units: int) -> None:
        if not self.waypoint:
            self.pos = (self.pos[0] - units, self.pos[1])
        else:
            self.waypoint_pos = (self.waypoint_pos[0] - units, self.waypoint_pos[1])

    def __move_l(self, units: int) -> None:
        if not self.waypoint:
            self.cur_direction = int((self.cur_direction - units / 90) % 4)
        else:
            if units == 90:
                self.waypoint_pos = (self.waypoint_pos[1], -1 * self.waypoint_pos[0])
            elif units == 180:
                self.waypoint_pos = (-1 * self.waypoint_pos[0], -1 * self.waypoint_pos[1])
            elif units == 270:
                self.waypoint_pos = (-1 * self.waypoint_pos[1], self.waypoint_pos[0])

    def __move_r(self, units: int):
        if not self.waypoint:
            self.cur_direction = int((self.cur_direction + units / 90) % 4)
        else:
            if units == 90:
                self.waypoint_pos = (-1 * self.waypoint_pos[1], self.waypoint_pos[0])
            elif units == 180:
                self.waypoint_pos = (-1 * self.waypoint_pos[0], -1 * self.waypoint_pos[1])
            elif units == 270:
                self.waypoint_pos = (self.waypoint_pos[1], -1 * self.waypoint_pos[0])

    def __move_f(self, units: int) -> None:
        if not self.waypoint:
            if self.cur_direction == 0:
                self.__move_e(units)
            elif self.cur_direction == 1:
                self.__move_s(units)
            elif self.cur_direction == 2:
                self.__move_w(units)
            elif self.cur_direction == 3:
                self.__move_n(units)
        else:
            self.pos = (self.pos[0] + self.waypoint_pos[0] * units, self.pos[1] + self.waypoint_pos[1] * units)

    def move(self, action: str, units: int) -> None:
        if action == "N":
            self.__move_n(units)
        if action == "S":
            self.__move_s(units)
        if action == "E":
            self.__move_e(units)
        if action == "W":
            self.__move_w(units)
        if action == "L":
            self.__move_l(units)
        if action == "R":
            self.__move_r(units)
        if action == "F":
            self.__move_f(units)

        # print(
        #    f"move: {action}{units} -> waypoint: {self.waypoint_pos} pos: {self.pos}, direction= {self.cur_direction}")

    def get_manhattan_distance(self) -> int:
        return abs(self.pos[0]) + abs(self.pos[1])


def parse_input(file_path: Path) -> List[Tuple[int, int]]:
    with open(file_path) as file:
        return list(map(lambda x: (x[:1], x[1:]), file.read().split("\n")))


def task01(input_lst: Tuple[int, int]) -> int:
    ferry = Ferry()
    for x in input_lst:
        ferry.move(x[0], int(x[1]))
    return ferry.get_manhattan_distance()


def task02(input_lst: Tuple[int, int]) -> int:
    ferry = Ferry(waypoint=True)
    for x in input_lst:
        ferry.move(x[0], int(x[1]))
    return ferry.get_manhattan_distance()


def main():
    input_lst = parse_input(Path("/home/david/git/AoC/2020/12/src/input.txt"))
    start = time.time()
    # print(input_lst)
    result_task1 = task01(input_lst)
    print(f"Time task1: {time.time() - start}")
    print(f"Result for task1: {result_task1}")
    print("----------------------------------")

    start = time.time()
    result_task2 = task02(input_lst)
    print(f"Time task2: {(time.time() - start)}")
    print(f"Result for task2: {result_task2}")
    print("----------------------------------")


if __name__ == '__main__':
    main()
