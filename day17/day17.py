from typing import Iterable


class Blocks:
    def __init__(self, data: Iterable[str]) -> None:
        self.area: dict[tuple[int, int], int] = {}
        for y, line in enumerate(data):
            for x, c in enumerate(line.strip()):
                self.area[(y, x)] = int(c)
        self.y: int = y
        self.x: int = x

    def possible_steps(self, y: int, x: int, direction: str, straight: int) -> set[tuple[int, int, str, int]]:
        return set()

    def shortest_path(self) -> int:
        return 0
