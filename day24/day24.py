from typing import Iterable


class Storm:
    def __init__(self, data: Iterable[str]) -> None:
        self.hails: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
        for line in map(str.strip, data):
            pos, vel = line.split(' @ ')
            self.hails.append((tuple(map(int, pos.split(', '))), tuple(map(int, vel.split(', ')))))
