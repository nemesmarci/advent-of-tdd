from typing import Tuple, Iterable


class ScratchCards:
    @staticmethod
    def parse(line: str) -> Tuple[int, set, set]:
        card, winning, numbers = line.replace('|', ':').split(':')
        return (int(card.split()[1]),
                set(map(int, winning.split())),
                set(map(int, numbers.split())))

    @staticmethod
    def part_one(data: Iterable[str]) -> int:
        return 0
