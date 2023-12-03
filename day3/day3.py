from collections import defaultdict
from typing import Iterable


class Engine:
    def __init__(self, data: Iterable[str]) -> None:
        self.schematic = defaultdict(lambda: '.')
        for y, line in enumerate(map(str.strip, data)):
            for x, c in enumerate(line):
                self.schematic[(y, x)] = line[x]
