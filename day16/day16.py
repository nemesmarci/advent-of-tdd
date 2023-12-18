from typing import Iterable
from heapq import heappush, heappop


class Grid:
    rules = {'R': {'|': 'UD', '\\': 'D', '/': 'U', '.': 'R', '-': 'R'},
             'L': {'|': 'UD', '\\': 'U', '/': 'D', '.': 'L', '-': 'L'},
             'D': {'-': 'LR', '\\': 'R', '/': 'L', '.': 'D', '|': 'D'},
             'U': {'-': 'LR', '\\': 'L', '/': 'R', '.': 'U', '|': 'U'}}

    def __init__(self, data: Iterable[str]):
        self.area: dict[tuple[int, int], str] = {}
        for y, line in enumerate(data):
            for x, c, in enumerate(line.strip()):
                self.area[(y, x)] = c
        self.x: int = y
        self.y: int = x

    def energized(self, heap):
        seen = set()
        while heap:
            current = heappop(heap)
            if current in seen:
                continue
            seen.add(current)
            (y, x), cur_d = current
            match cur_d:
                case 'R':
                    next_tile = y, x + 1
                case 'L':
                    next_tile = y, x - 1
                case 'D':
                    next_tile = y + 1, x
                case _:
                    next_tile = y - 1, x
            if next_tile in self.area:
                for tile in ((next_tile, d) for d in self.rules[cur_d][self.area[next_tile]]):
                    heappush(heap, tile)
        return len({x[0] for x in seen})

    def part_one(self) -> int:
        starting_tile = (0, 0)
        match self.area[starting_tile]:
            case '/':
                starting_direction = 'U'
            case '|' | '\\':
                starting_direction = 'D'
            case _:
                starting_direction = 'R'

        return self.energized([(starting_tile, starting_direction)])

    def part_two(self) -> int:
        ranges = {'R': (range(self.y + 1), [0]),
                  'L': (range(self.y + 1), [self.x]),
                  'D': ([0], range(self.x + 1)),
                  'U': ([self.y], range(self.x + 1))}
        return max(self.energized([((y, x), d) for d in self.rules[direction][self.area[(y, x)]]])
                   for direction in self.rules
                   for y in ranges[direction][0]
                   for x in ranges[direction][1])


if __name__ == '__main__':
    with open('input.txt') as data:
        grid = Grid(data)
        print(grid.part_one())
        print(grid.part_two())
