from typing import Iterable


class Sorter:
    def __init__(self, data: Iterable[str]) -> None:
        self.workflows: dict[str, list[str]] = {}
        self.parts: list[dict[str, int]] = []
