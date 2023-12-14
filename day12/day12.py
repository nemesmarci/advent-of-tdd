from typing import Iterable


class Springs:
    def __init__(self, data: Iterable[str]) -> None:
        self.rows: list[str] = []
        self.descriptions: list[list[int]] = []
