import re
from collections import defaultdict
from typing import Iterable, Optional, Tuple


class Engine:
    def __init__(self, data: Iterable[str]) -> None:
        self.schematic = defaultdict(lambda: '.')
        self.parts = dict()
        for y, line in enumerate(map(str.strip, data)):
            parsed_number = False
            for x, c in enumerate(line):
                self.schematic[(y, x)] = line[x]
                if c.isnumeric():
                    if not parsed_number:
                        parsed_number = True
                        self.parts[(y, x)] = int(
                            re.match(r'(\d+).*', line[x:]).group(1)
                        )
                else:
                    parsed_number = False

    def has_symbol(self, part: int, y: int, x: int) -> bool:
        for i in range(y - 1, y + 2):
            for j in range(x - 1, x + len(str(part)) + 1):
                c = self.schematic[(i, j)]
                if c != '.' and not c.isnumeric():
                    return True
        return False

    def near_gear(
            self, part: int, y: int, x: int) -> Optional[Tuple[int, int]]:
        for i in range(y - 1, y + 2):
            for j in range(x - 1, x + len(str(part)) + 1):
                if self.schematic[(i, j)] == '*':
                    return i, j
        return None

    def part_one(self) -> int:
        return (sum(part for coord, part in self.parts.items()
                    if self.has_symbol(part, *coord)))


if __name__ == '__main__':
    with open('input.txt') as data:
        engine = Engine(data)
    print(engine.part_one())
