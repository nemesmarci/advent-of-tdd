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
            rules.extend(self.missing_ranges(rules))
            rules.sort(key=lambda x: x[0].start)
            self.map_ranges.append(rules)

    def location(self, target: int) -> int:
        for rules in self.map_ranges:
            for source, dest in rules:
                if target in source:
                    target = dest[target - source.start]
                    break
        return target

    def part_one(self) -> int:
        return min(map(self.location, self.seeds))

    @staticmethod
    def missing_ranges(rules: list[tuple[range, range]]) -> list[tuple[range, range]]:
        missing_ranges = []
        prev_stop = 0
        for src_range in (rule[0] for rule in sorted(rules, key=lambda x: x[0].start)):
            if prev_stop != src_range.start:
                missing_ranges.append((range(prev_stop, src_range.start),
                                       range(prev_stop, src_range.start)))
            prev_stop = src_range.stop
        return missing_ranges

    def target_ranges(self) -> list[range]:
        return [range(start, start + length)
                for start, length in zip(self.seeds[0::2], self.seeds[1::2])]

    @staticmethod
    def transform_ranges(original_ranges: list[range],
                         rules: list[tuple[range, range]]) -> list[range]:
        new_ranges = []
        for source_range in original_ranges:
            if source_range.start >= rules[-1][0].stop:
                new_ranges.append(source_range)
                continue
            first = next(i for i, rule in enumerate(rules)
                         if source_range.start in rule[0])
            for i in range(first, len(rules)):
                new_start = (rules[i][1].start +
                             max(source_range.start, rules[i][0].start) -
                             rules[i][0].start)
                if source_range.stop in rules[i][0]:
                    new_ranges.append(range(new_start,
                                            rules[i][1].start +
                                            source_range.stop -
                                            rules[i][0].start))
                    break
                else:
                    new_ranges.append(range(new_start, rules[i][1].stop))
        return [r for r in new_ranges if r]

    def part_two(self) -> int:
        return 0
