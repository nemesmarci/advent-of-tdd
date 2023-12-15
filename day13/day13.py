from typing import Iterable


class Mirrors:
    def __init__(self, data: Iterable[str]) -> None:
        self.patterns: list[list[str]] = []
