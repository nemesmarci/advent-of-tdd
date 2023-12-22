from typing import Iterable


class Lagoon:
    def __init__(self, data: Iterable[str]) -> None:
        self.directions: list[str] = []
        self.lengths: list[int] = []
