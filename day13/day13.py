from typing import Iterable, Optional


class Mirrors:
    def __init__(self, data: Iterable[str]) -> None:
        lines = '\n'.join(data)
        blocks = ''.join(lines).split('\n\n')
        self.patterns: list[list[str]] = [[line for line in block.split('\n') if line] for block in blocks]

    @staticmethod
    def find_vertical_mirror(pattern: list[str]) -> Optional[int]:
        return None

    @staticmethod
    def find_horizontal_mirror(pattern: list[str]) -> Optional[int]:
        return None

    @staticmethod
    def find_mirror(pattern: list[str]) -> tuple[Optional[int], Optional[int]]:
        return Mirrors.find_vertical_mirror(pattern), Mirrors.find_horizontal_mirror(pattern)
