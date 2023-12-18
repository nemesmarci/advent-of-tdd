from typing import Iterable, Optional


class Mirrors:
    def __init__(self, data: Iterable[str]) -> None:
        lines = '\n'.join(data)
        blocks = ''.join(lines).split('\n\n')
        self.patterns: list[list[str]] = [[line for line in block.split('\n') if line] for block in blocks]

    @staticmethod
    def find_vertical_mirror(pattern: list[str]) -> Optional[int]:
        for col in range(1, len(pattern[0])):
            left = ([pattern[y][x] for y in range(len(pattern))] for x in range(col - 1, 0 - 1, -1))
            right = ([pattern[y][x] for y in range(len(pattern))] for x in range(col, len(pattern[0])))
            if left and right and all(l == r for l, r in zip(left, right)):
                return col

    @staticmethod
    def find_horizontal_mirror(pattern: list[str]) -> Optional[int]:
        for row in range(1, len(pattern)):
            up = (pattern[y] for y in range(row - 1, 0 - 1, -1))
            down = (pattern[y] for y in range(row, len(pattern)))
            if up and down and all(u == d for u, d in zip(up, down)):
                return row

    @staticmethod
    def find_mirror(pattern: list[str]) -> tuple[Optional[int], Optional[int]]:
        return Mirrors.find_vertical_mirror(pattern), Mirrors.find_horizontal_mirror(pattern)

    @staticmethod
    def value(pattern: list[str]) -> int:
        return 0
