from typing import Iterable


class Image:
    def __init__(self, data: Iterable[str]) -> None:
        self.area: dict[tuple[int, int], str] = {}
        self.galaxies: set[tuple[int, int]] = set()
        self.max_y: int = 0
        self.max_x: int = 0
