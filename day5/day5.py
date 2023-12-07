from typing import TextIO


class Almanac:
    def __init__(self, data: TextIO) -> None:
        self.seeds = []
        self.map_ranges = []
