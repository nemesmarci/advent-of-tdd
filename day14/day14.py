from typing import Iterable
from collections import Counter


class Rocks:
    def __init__(self, data: Iterable[str]) -> None:
        self.area: list[list[str]] = [list(line.strip()) for line in data]
        self.y = len(self.area)
        self.x = len(self.area[0])

    @staticmethod
    def move_blocks(line: str, direction: str) -> str:
        blocks = line.split('#')
        new_blocks = []
        for block in blocks:
            items = Counter(block)
            if direction in ('up', 'left'):
                new_blocks.append('O' * items['O'] + '.' * items['.'])
            else:
                new_blocks.append('.' * items['.'] + 'O' * items['O'])
        return '#'.join(new_blocks)

    def move_cols(self, direction: str) -> None:
        for x in range(self.x):
            col = ''.join(self.area[y][x] for y in range(self.y))
            new_col = self.move_blocks(col, direction)
            for y in range(self.y):
                self.area[y][x] = new_col[y]

    def move_rows(self, direction: str) -> None:
        for y in range(self.y):
            new_row = self.move_blocks(''.join(self.area[y]), direction)
            for x in range(self.x):
                self.area[y][x] = new_row[x]

    def weight(self) -> int:
        w = 0
        for x in range(self.x):
            col = [self.area[y][x] for y in range(self.y)]
            for y in range(self.y, 0, -1):
                if col[self.y - y] == 'O':
                    w += y
        return w

    def cycle(self) -> None:
        self.move_cols('up')
        self.move_rows('left')
        self.move_cols('down')
        self.move_rows('right')

    def run_cycle(self) -> int:
        weights = dict()
        seen = dict()
        for i in range(1, 1000000000 + 1):
            self.cycle()
            weights[i] = self.weight()
            state = tuple(tuple(row) for row in self.area)
            if state in seen:
                offset = seen[state]
                period = i - offset
                return weights[offset + (1000000000 - offset) % period]
            seen[state] = i


if __name__ == '__main__':
    with open('input.txt') as data:
        start = data.readlines()
    rocks = Rocks(start)
    rocks.move_cols('up')
    print(rocks.weight())
    rocks = Rocks(start)
    print(rocks.run_cycle())
