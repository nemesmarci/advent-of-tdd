from typing import Iterable


class Walk:
    def __init__(self, data: Iterable[str]) -> None:
        self.area: dict[tuple[int, int], str] = {}
        for y, line in enumerate(map(str.strip, data)):
            for x, c in enumerate(line):
                if c != '#':
                    self.area[(y, x)] = c
        self.y: int = y
        self.x: int = x
