from typing import Iterable


class Springs:
    def __init__(self, data: Iterable[str]) -> None:
        self.rows: list[str] = []
        self.descriptions: list[list[int]] = []
        for line in data:
            t, d = line.strip().split()
            self.rows.append(t)
            self.descriptions.append(list(map(int, d.split(','))))
