from typing import Iterable


class Oasis:
    def __init__(self, data: Iterable[str]) -> None:
        self.sequences = [[int(x) for x in line.strip().split()]
                          for line in data]
