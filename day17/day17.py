from typing import Iterable
from heapq import heappush, heappop
from math import inf


class Blocks:
    def __init__(self, data: Iterable[str]) -> None:
        self.area: dict[tuple[int, int], int] = {}
        for y, line in enumerate(data):
            for x, c in enumerate(line.strip()):
                self.area[(y, x)] = int(c)
        self.y: int = y
        self.x: int = x

    @staticmethod
    def possible_steps(y: int, x: int, direction: str, straight: int,
                       min_straight: int, max_straight: int) -> set[tuple[int, int, str, int]]:
        possible = set()
        if straight < 3:
            match direction:
                case 'E':
                    possible.add((y, x + 1, direction, straight + 1))
                case 'W':
                    possible.add((y, x - 1, direction, straight + 1))
                case 'S':
                    possible.add((y + 1, x, direction, straight + 1))
                case 'N':
                    possible.add((y - 1, x, direction, straight + 1))
        if direction in 'EW':
            possible.add((y - 1, x, 'N', 1))
            possible.add((y + 1, x, 'S', 1))
        else:
            possible.add((y, x - 1, 'W', 1))
            possible.add((y, x + 1, 'E', 1))
        return possible

    def shortest_path(self, min_straight, max_straight) -> int:
        distances = dict()
        distances[(0, 1, 'E', 1)] = self.area[(0, 1)]
        distances[(1, 0, 'S', 1)] = self.area[(1, 0)]
        heap = []
        heappush(heap, (self.area[0, 1], 0, 1, 'E', 1))
        heappush(heap, (self.area[1, 0], 1, 0, 'S', 1))
        while heap:
            distance, y, x, direction, straight = heappop(heap)
            if (y, x) == (self.y, self.x):
                return distance
            for next_y, next_x, next_dir, next_straight in self.possible_steps(y, x, direction, straight,
                                                                               min_straight, max_straight):
                if (next_y, next_x) not in self.area:
                    continue
                next_d = distance + self.area[(next_y, next_x)]
                if distances.get((next_y, next_x, next_dir, next_straight), inf) > next_d:
                    distances[(next_y, next_x, next_dir, next_straight)] = next_d
                    heappush(heap, (next_d, next_y, next_x, next_dir, next_straight))


if __name__ == '__main__':
    with open('input.txt') as data:
        blocks = Blocks(data)
    print(blocks.shortest_path(0, 3))
