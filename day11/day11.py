from typing import Iterable


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

    def part_one(self) -> int:
        return 0
