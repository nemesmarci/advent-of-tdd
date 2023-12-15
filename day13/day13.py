from typing import Iterable


class Mirrors:
    def __init__(self, data: Iterable[str]) -> None:
        lines = '\n'.join(data)
        blocks = ''.join(lines).split('\n\n')
        self.patterns: list[list[str]] = [[line for line in block.split('\n') if line] for block in blocks]
