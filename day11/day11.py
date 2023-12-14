from typing import Iterable
from itertools import combinations


class Image:
    def __init__(self, data: Iterable[str]) -> None:
        self.area: dict[tuple[int, int], str] = {}
        self.galaxies: set[tuple[int, int]] = set()
        for y, line in enumerate(data):
            for x, c in enumerate(line.strip()):
                self.area[(y, x)] = c
                if c == '#':
                    self.galaxies.add((y, x))
        self.max_y: int = y + 1
        self.max_x: int = x + 1

    def empty_rows(self) -> set[int]:
        return {y for y in range(self.max_y)
                if all(self.area[(y, x)] == '.' for x in range(self.max_x))}

    def empty_cols(self) -> set[int]:
        return {x for x in range(self.max_x)
                      if all(self.area[(y, x)] == '.' for y in range(self.max_y))}

    def solve(self, offset: int) -> int:
        total_distance = 0
        empty_rows = self.empty_rows()
        empty_cols = self.empty_cols()
        for (y1, x1), (y2, x2) in combinations(self.galaxies, 2):
            if y2 < y1:
                y1, y2 = y2, y1
            if x2 < x1:
                x1, x2 = x2, x1
            total_distance += y2 - y1
            for row in empty_rows:
                if row in range(y1 + 1, y2 + 1):
                    total_distance += offset
            total_distance += x2 - x1
            for col in empty_cols:
                if col in range(x1 + 1, x2 + 1):
                    total_distance += offset
        return total_distance

    def part_one(self) -> int:
        return self.solve(1)

    def part_two(self) -> int:
        return self.solve(1000000 - 1)


if __name__ == '__main__':
    with open('input.txt') as data:
        image = Image(data)
        print(image.part_one())
        print(image.part_two())
