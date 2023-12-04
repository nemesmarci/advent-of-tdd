from collections import Counter
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

    @staticmethod
    def part_two(data: Iterable[str]) -> int:
        cards = Counter()
        for line in data:
            card, winning, numbers = ScratchCards.parse(line)
            cards[card] += 1
            for new_card in range(card + 1, card + 1 + len(winning & numbers)):
                cards[new_card] += cards[card]
        return sum(cards.values())


if __name__ == '__main__':
    with open('input.txt') as data:
        print(ScratchCards.part_one(data))
        data.seek(0)
        print(ScratchCards.part_two(data))
