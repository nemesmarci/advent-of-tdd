from typing import Iterable


class Garden:
    def __init__(self, data: Iterable[str]) -> None:
        self.area: dict[tuple[int, int], str] = {}
        self.start: tuple[int, int] = (0, 0)
        self.y: int = 0
        self.x: int = 0
