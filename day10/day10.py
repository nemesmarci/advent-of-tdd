from typing import Iterable


class Maze:
    def __init__(self, data: Iterable[str]) -> None:
        self.area: dict[tuple[int, int], str] = {}
        for y, line in enumerate(map(str.strip, data)):
            for x, c in enumerate(line):
                if c == 'S':
                    self.start: tuple[int, int] = y, x
                self.area[(y, x)] = c

    def next_in_loop(self, node: tuple[int, int], direction: str) -> tuple[tuple[int, int], str]:
        return (0, 0), 'N'

    def loop(self) -> set[tuple[int, int]]:
        return set()
