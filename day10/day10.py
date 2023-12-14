from typing import Iterable


class Maze:
    def __init__(self, data: Iterable[str]) -> None:
        self.area: dict[tuple[int, int], str] = {}
        for y, line in enumerate(map(str.strip, data)):
            for x, c in enumerate(line):
                if c == 'S':
                    self.start: tuple[int, int] = y, x
                self.area[(y, x)] = c

    def next_in_loop(self, node: tuple[int, int], direction: str) -> tuple[tuple[int, int], str]:
        if direction == 'N':
            next_node = (node[0] - 1, node[1])
            dirs = {'|': 'N', '7': 'W', 'F': 'E'}
        elif direction == 'E':
            next_node = (node[0], node[1] + 1)
            dirs = {'-': 'E', 'J': 'N', '7': 'S'}
        elif direction == 'S':
            next_node = (node[0] + 1, node[1])
            dirs = {'|': 'S', 'L': 'E', 'J': 'W'}
        else:
            next_node = (node[0], node[1] - 1)
            dirs = {'-': 'W', 'L': 'N', 'F': 'S'}
        return next_node, dirs[self.area[next_node]]


    def loop(self) -> set[tuple[int, int]]:
        return set()
