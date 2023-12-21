from typing import Iterable


class Blocks:
    def __init__(self, data: Iterable[str]):
        self.area: dict[tuple[int, int], str] = {}
        self.y: int = 0
        self.x: int = 0
