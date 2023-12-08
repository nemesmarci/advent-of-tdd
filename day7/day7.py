from typing import Iterable
from collections import defaultdict, Counter
from itertools import chain


class CamelCards:
    def __init__(self, data: Iterable[str]) -> None:
        self.hands = []
        self.bets = []
        for line in data:
            hand, bet = line.split()
            self.hands.append(hand)
            self.bets.append(int(bet))

    def part_one(self) -> int:
        return self.winnings(joker=False)

    @staticmethod
    def bucket(hand: str) -> str:
        cards = Counter(hand)
        jokers = cards.pop('0', 0)
        if not cards:
            return 'five_of_a_kind'
        match cards.most_common(1)[0][1]:
            case 1:
                return ('high_card', 'one_pair', 'three_of_a_kind',
                        'four_of_a_kind', 'five_of_a_kind')[jokers]
            case 2:
                pairs = len([p for p in cards.values() if p == 2])
                return ('one_pair', 'three_of_a_kind', 'four_of_a_kind',
                        'five_of_a_kind')[jokers] if pairs == 1 \
                    else ('two_pairs', 'full_house')[jokers]
            case 3:
                return 'full_house' if 2 in cards.values() \
                    else ('three_of_a_kind', 'four_of_a_kind',
                          'five_of_a_kind')[jokers]
            case 4:
                return ('four_of_a_kind', 'five_of_a_kind')[jokers]
            case 5:
                return 'five_of_a_kind'

    def part_two(self) -> int:
        return self.winnings(joker=True)

    @staticmethod
    def key_fun(item: tuple[str, int]):
        return item[0].translate(str.maketrans('TJQKA', 'ABCDE'))

    def winnings(self, joker: bool) -> int:
        buckets = defaultdict(list)
        for hand, bet in zip(self.hands, self.bets):
            if joker:
                hand = hand.replace('J', '0')
            buckets[self.bucket(hand)].append((hand, bet))
        winnings = 0
        for rank, (hand, bet) in enumerate(chain(
                sorted(buckets['high_card'], key=self.key_fun),
                sorted(buckets['one_pair'], key=self.key_fun),
                sorted(buckets['two_pairs'], key=self.key_fun),
                sorted(buckets['three_of_a_kind'], key=self.key_fun),
                sorted(buckets['full_house'], key=self.key_fun),
                sorted(buckets['four_of_a_kind'], key=self.key_fun),
                sorted(buckets['five_of_a_kind'], key=self.key_fun))):
            winnings += (rank + 1) * bet
        return winnings


if __name__ == '__main__':
    with open('input.txt') as data:
        cards = CamelCards(data.readlines())
    print(cards.part_one())
    print(cards.part_two())
