from typing import Iterable


class Lagoon:
    def __init__(self, data: Iterable[str]) -> None:
        self.directions: list[str] = []
        self.lengths: list[int] = []
        for line in data:
            direction, length = line.strip().split()[:2]
            self.directions.append(direction)
            self.lengths.append(int(length))

    def perimeter(self) -> int:
        return sum(self.lengths)

    def area(self) -> int:
        return 0
