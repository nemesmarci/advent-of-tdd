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
        possible = set()
        if straight < 3:
            match direction:
                case 'E':
                    possible.add((y, x + 1, direction, straight + 1))
                case 'W':
                    possible.add((y, x - 1, direction, straight + 1))
                case 'S':
                    possible.add((y + 1, x, direction, straight + 1))
                case 'N':
                    possible.add((y - 1, x, direction, straight + 1))
        if direction in 'EW':
            possible.add((y - 1, x, 'N', 1))
            possible.add((y + 1, x, 'S', 1))
        else:
            possible.add((y, x - 1, 'W', 1))
            possible.add((y, x + 1, 'E', 1))
        return possible

    def shortest_path(self) -> int:
        return 0
