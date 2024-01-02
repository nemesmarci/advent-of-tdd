from typing import Iterable


class Garden:
    def __init__(self, data: Iterable[str]) -> None:
        self.area: set[tuple[int, int]] = set()
        y, x = 0, 0
        for y, line in enumerate(data):
            for x, c in enumerate(line.strip()):
                if c == 'S':
                    self.start: tuple[int, int] = y, x
                if c != '#':
                    self.area.add((y, x))
        self.y: int = y
        self.x: int = x
