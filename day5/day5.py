from typing import TextIO


class Almanac:
    def __init__(self, data: TextIO) -> None:
        seeds, *maps = ''.join(data.readlines()).split('\n\n')
        self.seeds = [int(seed) for seed in seeds.split(':')[1].split()]
        self.map_ranges = []
        for map_ in maps:
            rules = []
            for line in map_.split('\n')[1:]:
                if line:
                    dest, source, length = map(int, line.split())
                    rules.append((range(source, source + length),
                                  range(dest, dest + length)))
            self.map_ranges.append(rules)

    def location(self, target: int) -> int:
        for rules in self.map_ranges:
            for source, dest in rules:
                if target in source:
                    target = dest[target - source.start]
                    break
        return target

    def part_one(self) -> int:
        return 0
