from typing import Iterable


class Grid:
    def __init__(self, data: Iterable[str]):
        self.area: dict[tuple[int, int], str] = {}
        self.x: int = 0
        self.y: int = 0
