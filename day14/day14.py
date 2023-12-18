from typing import Iterable
from collections import Counter


class Rocks:
    def __init__(self, data: Iterable[str]) -> None:
        self.area: list[list[str]] = [list(line.strip()) for line in data]
        self.y = len(self.area)
        self.x = len(self.area[0])

    @staticmethod
    def move_blocks(line: str) -> str:
        blocks = line.split('#')
        new_blocks = []
        for block in blocks:
            items = Counter(block)
            new_blocks.append('O' * items['O'] + '.' * items['.'])
        return '#'.join(new_blocks)

    def move_cols(self) -> None:
        for x in range(self.x):
            col = ''.join(self.area[y][x] for y in range(self.y))
            new_col = self.move_blocks(col)
            for y in range(self.y):
                self.area[y][x] = new_col[y]

    def weight(self) -> int:
        w = 0
        for x in range(self.x):
            col = [self.area[y][x] for y in range(self.y)]
            for y in range(self.y, 0, -1):
                if col[self.y - y] == 'O':
                    w += y
        return w

    def cycle(self) -> int:
        ...


if __name__ == '__main__':
    with open('input.txt') as data:
        start = data.readlines()
    rocks = Rocks(start)
    rocks.move_cols()
    print(rocks.weight())
