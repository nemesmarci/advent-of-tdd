from typing import Iterable


class Storm:
    def __init__(self, data: Iterable[str]) -> None:
        self.hails: list[tuple[tuple[int, int, int], tuple[int, int, int]]] = []
