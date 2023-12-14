from typing import Iterable
from heapq import heappush, heappop


class Maze:
    def __init__(self, data: Iterable[str]) -> None:
        self.area: dict[tuple[int, int], str] = {}
        for y, line in enumerate(map(str.strip, data)):
            for x, c in enumerate(line):
                if c == 'S':
                    self.start: tuple[int, int] = y, x
                self.area[(y, x)] = c
        self.max_y = y * 3 + 3
        self.max_x = x * 3 + 3
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

    def zoom(self) -> set[tuple[int, int]]:
        zoomed_in = set()
        loop = self.loop()
        for y, x in loop:
            c = self.area[(y, x)]
            zoomed_in.add((3 * y + 1, 3 * x + 1))
            if c in '|LJ':
                zoomed_in.add((3 * y, 3 * x + 1))
            if c in '|7F':
                zoomed_in.add((3 * y + 2, 3 * x + 1))
            if c in '-J7':
                zoomed_in.add((3 * y + 1, 3 * x))
            if c in '-LF':
                zoomed_in.add((3 * y + 1, 3 * x + 2))
        return zoomed_in

    @staticmethod
    def get_neighbours(current):
        return ((current[0] - 1, current[1]),
                (current[0], current[1] - 1),
                (current[0], current[1] + 1),
                (current[0] + 1, current[1]))

    def enclosed(self, tile, loop):
        seen = set()
        heap = []
        heappush(heap, tile)
        while heap:
            cur_node = heappop(heap)
            if cur_node in seen:
                continue
            seen.add(cur_node)
            neighbours = self.get_neighbours(cur_node)
            for n in neighbours:
                if not 0 <= n[0] < self.max_y or not 0 <= n[1] < self.max_x:
                    return False
                if n not in seen and n not in loop:
                    heappush(heap, n)
        return True

    def fill(self, start, loop):
        seen = set()
        heap = []
        heappush(heap, start)
        while heap:
            cur_node = heappop(heap)
            if cur_node in seen:
                continue
            seen.add(cur_node)
            neighbours = self.get_neighbours(cur_node)
            for n in neighbours:
                if n not in seen and 0 <= n[0] < self.max_y and 0 <= n[1] < self.max_x and n not in loop:
                    heappush(heap, n)
        return seen

    def enclosed_tiles(self) -> set[tuple[int, int]]:
        enclosed_tiles = set()
        enclosed_zoom = set()
        free_zoom = set()
        loop = self.loop()
        zoomed_in = self.zoom()
        for tile in filter(lambda x: x not in loop, self.area):
            zoom = tile[0] * 3, tile[1] * 3
            if zoom in enclosed_zoom:
                enclosed_tiles.add(tile)
            elif zoom in free_zoom:
                continue
            elif self.enclosed(zoom, zoomed_in):
                enclosed_tiles.add(tile)
                enclosed_zoom |= self.fill(zoom, zoomed_in)
            else:
                free_zoom |= self.fill(zoom, zoomed_in)
        return enclosed_tiles

    def part_two(self) -> int:
        return 0


if __name__ == '__main__':
    with open('input.txt') as data:
        maze = Maze(data)
        print(maze.part_one())
