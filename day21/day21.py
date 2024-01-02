from typing import Iterable
from heapq import heappush, heappop


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

    def reachable(self, steps) -> int:
        visited = set()
        heap = [(0, self.start)]
        while heap:
            current_steps, current_plot = heappop(heap)
            if current_steps > steps or current_plot in visited:
                continue
            for neighbour in filter(lambda n: n in self.area, self.around(*current_plot)):
                heappush(heap, (current_steps + 1, neighbour))
            if current_steps % 2 == 0:
                visited.add(current_plot)
        return len(visited)


if __name__ == '__main__':
    with open('input.txt') as data:
        garden = Garden(data)
    print(garden.reachable(64))
