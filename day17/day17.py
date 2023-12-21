from typing import Iterable


class Blocks:
    def __init__(self, data: Iterable[str]):
        self.area: dict[tuple[int, int], int] = {}
        for y, line in enumerate(data):
            for x, c in enumerate(line.strip()):
                self.area[(y, x)] = int(c)
        self.y: int = y
        self.x: int = x
