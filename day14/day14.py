from typing import Iterable


class Rocks:
    def __init__(self, data: Iterable[str]) -> None:
        self.area: list[list[str]] = [list(line.strip()) for line in data]

    @staticmethod
    def move_blocks(line: str) -> str:
        return ''
