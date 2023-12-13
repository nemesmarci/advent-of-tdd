from typing import Iterable


class Maze:
    def __init__(self, data: Iterable[str]) -> None:
        self.area: dict[tuple[int, int]] = {}
        self.start: tuple[int, int] = 0, 0
