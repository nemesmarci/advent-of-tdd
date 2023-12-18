from typing import Iterable


class Grid:
    def __init__(self, data: Iterable[str]):
        self.area: dict[tuple[int, int], str] = {}
        for y, line in enumerate(data):
            for x, c, in enumerate(line.strip()):
                self.area[(y, x)] = c
        self.x: int = y
        self.y: int = x

    def part_one(self) -> int:
        return 0
