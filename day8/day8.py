from typing import Sequence


class Map:
    def __init__(self, lines: Sequence[str]) -> None:
        self.instructions: str = ''
        self.nodes: dict[str, tuple[str, str]] = {}
