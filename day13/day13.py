from typing import Iterable, Optional


class Mirrors:
    def __init__(self, data: Iterable[str]) -> None:
        lines = ''.join(data)
        blocks = ''.join(lines).split('\n\n')
        self.patterns: list[list[str]] = [[line for line in block.split('\n') if line] for block in blocks]


    @staticmethod
    def get_left(col, pattern):
        return ([pattern[y][x] for y in range(len(pattern))] for x in range(col - 1, 0 - 1, -1))

    @staticmethod
    def get_right(col, pattern):
       return ([pattern[y][x] for y in range(len(pattern))] for x in range(col, len(pattern[0])))

    @staticmethod
    def find_vertical_mirror(pattern: list[str]) -> Optional[int]:
        for col in range(1, len(pattern[0])):
            if all(l == r for l, r in zip(Mirrors.get_left(col, pattern), Mirrors.get_right(col, pattern))):
                return col

    @staticmethod
    def get_up(row, pattern):
        return (pattern[y] for y in range(row - 1, 0 - 1, -1))

    @staticmethod
    def get_down(row, pattern):
        return (pattern[y] for y in range(row, len(pattern)))

    @staticmethod
    def find_horizontal_mirror(pattern: list[str]) -> Optional[int]:
        for row in range(1, len(pattern)):
            if all(u == d for u, d in zip(Mirrors.get_up(row, pattern), Mirrors.get_down(row, pattern))):
                return row

    @staticmethod
    def find_mirror(pattern: list[str]) -> tuple[Optional[int], Optional[int]]:
        return Mirrors.find_vertical_mirror(pattern), Mirrors.find_horizontal_mirror(pattern)

    @staticmethod
    def value(pattern: list[str]) -> int:
        vertical_mirror, horizontal_mirror = Mirrors.find_mirror(pattern)
        return vertical_mirror if vertical_mirror else 100 * horizontal_mirror

    def part_one(self) -> int:
        return sum(self.value(pattern) for pattern in self.patterns)

    @staticmethod
    def find_smudged_vertical_mirror(pattern: list[str]) -> Optional[int]:
        old_vertical_mirror = Mirrors.find_vertical_mirror(pattern)
        for col in range(1, len(pattern[0])):
            if old_vertical_mirror is None or col != old_vertical_mirror:
                if sum(l[i] != r[i] for l, r in zip(Mirrors.get_left(col, pattern), Mirrors.get_right(col, pattern))
                       for i in range(len(l))) <= 1:
                    return col

    @staticmethod
    def find_smudged_horizontal_mirror(pattern: list[str]) -> Optional[int]:
        old_horizontal_mirror = Mirrors.find_vertical_mirror(pattern)
        for row in range(1, len(pattern)):
            if old_horizontal_mirror is None or row != old_horizontal_mirror:
                if sum(u[i] != d[i] for u, d in zip(Mirrors.get_up(row, pattern), Mirrors.get_down(row, pattern))
                       for i in range(len(u))) <= 1:
                    return row


    @staticmethod
    def find_smudged_mirror(pattern: list[str]) -> tuple[Optional[int], Optional[int]]:
        return Mirrors.find_smudged_vertical_mirror(pattern), Mirrors.find_smudged_horizontal_mirror(pattern)


if __name__ == '__main__':
    with open('input.txt') as data:
        mirrors = Mirrors(''.join(data.readlines()))
        print(mirrors.part_one())
