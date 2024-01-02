from typing import Iterable
from heapq import heappush, heappop
from numpy.polynomial.polynomial import Polynomial


class Garden:
    def __init__(self, data: Iterable[str]) -> None:
        self.area: set[tuple[int, int]] = set()
        y, x = 0, 0
        for y, line in enumerate(data):
            for x, c in enumerate(line.strip()):
                if c == 'S':
                    self.start: tuple[int, int] = y, x
                if c != '#':
                    self.area.add((y, x))
        self.y: int = y
        self.x: int = x

    @staticmethod
    def around(y, x):
        return (y - 1, x), (y, x - 1), (y, x + 1), (y + 1, x)

    def reachable(self, steps, infinite, even) -> int:
        visited = set()
        heap = [(0, self.start, (0, 0))]
        while heap:
            current_steps, current_plot, map_tile = heappop(heap)
            if current_steps > steps or (current_plot, map_tile) in visited:
                continue
            if current_steps % 2 != even:
                visited.add((current_plot, map_tile))
            for neighbour in self.around(*current_plot):
                (y, x), (map_y, map_x) = neighbour, map_tile
                if infinite:
                    if y == -1:
                        y = self.y
                        map_y -= 1
                    elif y == self.y + 1:
                        y = 0
                        map_y += 1
                    elif x == -1:
                        x = self.x
                        map_x -= 1
                    elif x == self.x + 1:
                        x = 0
                        map_x += 1
                if (y, x) in self.area:
                    heappush(heap, (current_steps + 1, (y, x), (map_y, map_x)))
        return len(visited)

    def part_two(self):
        sequence = []
        for i in range(3):
            sequence.append(self.reachable(i * (self.y + 1) + self.start[0], True, i % 2))
        return int(Polynomial.fit([0, 1, 2], sequence, 2)(26501365 // (self.y + 1)))


if __name__ == '__main__':
    with open('input.txt') as data:
        garden = Garden(data)
    print(garden.reachable(64, False, True))
    print(garden.part_two())
