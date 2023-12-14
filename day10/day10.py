from typing import Iterable


class Maze:
    def __init__(self, data: Iterable[str]) -> None:
        self.area: dict[tuple[int, int], str] = {}
        for y, line in enumerate(map(str.strip, data)):
            for x, c in enumerate(line):
                if c == 'S':
                    self.start: tuple[int, int] = y, x
                self.area[(y, x)] = c
        self.area[self.start] = self.start_pipe_shape()

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
        visited = {self.start}
        if self.area[self.start] in '|LJ':
            cur_dir = 'N'
        elif self.area[self.start] in 'F7':
            cur_dir = 'S'
        else:
            cur_dir = 'E'
        cur_node = self.start
        while True:
            cur_node, cur_dir = self.next_in_loop(cur_node, cur_dir)
            if cur_node == self.start:
                return visited
            visited.add(cur_node)

    def start_pipe_shape(self) -> str:
        up = self.start[0] - 1, self.start[1]
        up = up in self.area and self.area[up] in '|7F'
        left = self.start[0], self.start[1] - 1
        left = left in self.area and self.area[left] in '-LF'
        right = self.start[0], self.start[1] + 1
        right = right in self.area and self.area[right] in '-J7'
        down = self.start[0] + 1, self.start[1]
        down = down in self.area and self.area[down] in '|LJ'
        if up and down:
            return '|'
        if up and left:
            return 'J'
        if up and right:
            return 'L'
        if left and right:
            return '-'
        if left and down:
            return '7'
        if down and right:
            return 'F'

    def part_one(self) -> int:
        return len(self.loop()) // 2


if __name__ == '__main__':
    with open('input.txt') as data:
        maze = Maze(data)
        print(maze.part_one())
