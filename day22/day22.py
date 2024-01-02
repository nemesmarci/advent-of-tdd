from typing import Iterable


class Brick:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.x1, self.y1, self.z1 = x1, y1, z1
        self.x2, self.y2, self.z2 = x2, y2, z2
        self.supporting: set[Brick] = set()
        self.supported_by: set[Brick] = set()

    def __eq__(self, other) -> bool:
        return self.x1 == other.x1 and self.y1 == other.y1 and self.z1 == other.z1 and \
            self.x2 == other.x2 and self.y2 == other.y2 and self.z2 == other.z2


class Bricks:
    def __init__(self, data: Iterable[str]) -> None:
        self.bricks: list[Brick] = []
        for line in data:
            c1, c2 = line.strip().split('~')
            x1, y1, z1 = map(int, c1.split(','))
            x2, y2, z2 = map(int, c2.split(','))
            self.bricks.append(Brick(x1, y1, z1, x2, y2, z2))
