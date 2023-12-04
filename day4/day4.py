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
        points = 0
        for line in data:
            _, winning, numbers = ScratchCards.parse(line)
            points += int(2 ** (len(winning & numbers) - 1))
        return points


if __name__ == '__main__':
    with open('input.txt') as data:
        print(ScratchCards.part_one(data))
