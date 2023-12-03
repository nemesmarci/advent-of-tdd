import re
from collections import defaultdict
from typing import Iterable


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
