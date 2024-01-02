from __future__ import annotations
from typing import Iterable
from collections import defaultdict


class Brick:
    def __init__(self, id_: int, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int) -> None:
        self.id = id_
        self.x1, self.y1, self.z1 = x1, y1, z1
        self.x2, self.y2, self.z2 = x2, y2, z2
        self.supporting: set[Brick] = set()
        self.supported_by: set[Brick] = set()

    def __eq__(self, other: Brick) -> bool:
        return self.x1 == other.x1 and self.y1 == other.y1 and self.z1 == other.z1 and \
            self.x2 == other.x2 and self.y2 == other.y2 and self.z2 == other.z2

    def __hash__(self):
        return self.id


class Bricks:
    def __init__(self, data: Iterable[str]) -> None:
        self.bricks: list[Brick] = []
        for i, line in enumerate(data):
            c1, c2 = line.strip().split('~')
            x1, y1, z1 = map(int, c1.split(','))
            x2, y2, z2 = map(int, c2.split(','))
            self.bricks.append(Brick(i, x1, y1, z1, x2, y2, z2))

    def fall(self) -> None:
        tops = defaultdict(set)
        for brick in sorted(self.bricks, key=lambda x: x.z1):
            assert brick.z1 <= brick.z2 and brick.y1 <= brick.y2 and brick.x1 <= brick.x2
            while brick.z1 > 1 and not any(any(other.y1 <= y <= other.y2 for y in range(brick.y1, brick.y2 + 1)) and
                                     any(other.x1 <= x <= other.x2 for x in range(brick.x1, brick.x2 + 1))
                                     for other in tops[brick.z1 - 1]):
                brick.z1 -= 1
                brick.z2 -= 1
            tops[brick.z2].add(brick)
            for support in (other for other in tops[brick.z1 - 1]
                      if any(other.y1 <= y <= other.y2 for y in range(brick.y1, brick.y2 + 1)) and
                         any(other.x1 <= x <= other.x2 for x in range(brick.x1, brick.x2 + 1))):
                support.supporting.add(brick)
                brick.supported_by.add(support)
