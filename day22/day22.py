from typing import Iterable


class Brick:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.x1, self.y1, self.z1 = x1, y1, z1
        self.x2, self.y2, self.z2 = x2, y2, z2
        self.supporting: set[Brick] = set()
        self.supported_by: set[Brick] = set()


class Bricks:
    def __init__(self, data: Iterable[str]) -> None:
        self.bricks: list[Brick] = []
