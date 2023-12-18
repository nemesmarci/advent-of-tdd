from typing import Iterable
from collections import Counter


class Rocks:
    def __init__(self, data: Iterable[str]) -> None:
        self.area: list[list[str]] = [list(line.strip()) for line in data]

    @staticmethod
    def move_blocks(line: str) -> str:
        blocks = line.split('#')
        new_blocks = []
        for block in blocks:
            items = Counter(block)
            new_blocks.append('O' * items['O'] + '.' * items['.'])
        return '#'.join(new_blocks)
