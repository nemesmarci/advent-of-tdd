from typing import Iterable
from heapq import heappush, heappop
from collections import defaultdict


class Walk:
    def __init__(self, data: Iterable[str]) -> None:
        self.area: dict[tuple[int, int], str] = {}
        for y, line in enumerate(map(str.strip, data)):
            for x, c in enumerate(line):
                if c != '#':
                    self.area[(y, x)] = c
        self.y: int = y
        self.x: int = x

    def neighbours(self, y, x):
        return [n for n in ((y - 1, x), (y, x - 1), (y, x + 1), (y + 1, x)) if n in self.area]

    def part_one(self) -> int:
        start = (0, 1)
        end = (self.y, self.x - 1)
        distances = {}
        max_hike = 0
        heap = [(0, start, {start})]
        while heap:
            cur_d, (y, x), visited = heappop(heap)
            if (y, x) in distances and distances[(y, x)] <= cur_d:
                continue
            distances[(y, x)] = cur_d
            if (y, x) == end and len(visited) - 1 > max_hike:
                max_hike = len(visited) - 1
                continue
            if (slope := self.area[(y, x)]) in '^<>v':
                down = ((y - 1, x), (y, x - 1), (y, x + 1), (y + 1, x))['^<>v'.index(slope)]
                if down not in visited:
                    visited.add(down)
                    heappush(heap, (cur_d - 1, down, visited))
            else:
                for n in (n for n in self.neighbours(y, x) if n not in visited):
                    heappush(heap, (cur_d - 1, n, visited | {n}))
        return max_hike

    def paths(self, nodes):
        graph = defaultdict(dict)
        for node in nodes:
            for neighbour in (n for n in self.neighbours(*node)):
                visited = {node}
                cur = neighbour
                while cur not in nodes:
                    visited.add(cur)
                    cur = next(n for n in self.neighbours(*cur) if n not in visited)
                graph[node][cur] = len(visited)
                graph[cur][node] = len(visited)
        return graph

    def part_two(self) -> int:
        start = (0, 1)
        end = (self.y, self.x - 1)
        nodes = [start] + [n for n in self.area if len(self.neighbours(*n)) > 2] + [end]
        graph = self.paths(nodes)
        max_hike = 0
        heap = [(0, start, {start})]
        while heap:
            cur_d, (y, x), visited = heappop(heap)
            if (y, x) == end and -cur_d > max_hike:
                max_hike = -cur_d
                continue
            for n in (n for n in graph[(y, x)] if n not in visited):
                heappush(heap, (cur_d - graph[(y, x)][n], n, visited | {n}))
        return max_hike


if __name__ == "__main__":
    with open('input.txt') as data:
        walk = Walk(data)
    print(walk.part_one())
    print(walk.part_two())
