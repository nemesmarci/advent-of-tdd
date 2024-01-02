from typing import Iterable


class Walk:
    def __init__(self, data: Iterable[str]) -> None:
        self.area: dict[tuple[int, int], str] = {}
        self.y: int = 0
        self.x: int = 0
