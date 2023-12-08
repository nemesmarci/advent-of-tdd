from typing import Iterable, Callable
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

    @staticmethod
    def get_key(mapped: str) -> Callable[[tuple[str, int]], str]:
        return lambda item: item[0].translate(str.maketrans('TJQKA', mapped))

    @staticmethod
    def prep(hand: str) -> tuple[Counter[str], int]:
        return Counter(hand), 0

    def part_one(self) -> int:
        return self.winnings(self.prep, self.get_key('ABCDE'))

    @staticmethod
    def bucket(hand: str, prep_fun: Callable) -> str:
        cards, jokers = prep_fun(hand)
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

    @staticmethod
    def joker_prep(hand: str) -> tuple[Counter[str], int]:
        cards = Counter(hand)
        jokers = cards.pop('J', 0)
        return cards, jokers

    def part_two(self) -> int:
        return self.winnings(self.joker_prep, self.get_key('A0CDE'))

    def winnings(self, prep_fun: Callable, key_fun: Callable) -> int:
        buckets = defaultdict(list)
        for hand, bet in zip(self.hands, self.bets):
            buckets[self.bucket(hand, prep_fun)].append((hand, bet))
        winnings = 0
        for rank, (hand, bet) in enumerate(chain(
                sorted(buckets['high_card'], key=key_fun),
                sorted(buckets['one_pair'], key=key_fun),
                sorted(buckets['two_pairs'], key=key_fun),
                sorted(buckets['three_of_a_kind'], key=key_fun),
                sorted(buckets['full_house'], key=key_fun),
                sorted(buckets['four_of_a_kind'], key=key_fun),
                sorted(buckets['five_of_a_kind'], key=key_fun))):
            winnings += (rank + 1) * bet
        return winnings


if __name__ == '__main__':
    with open('input.txt') as data:
        cards = CamelCards(data.readlines())
    print(cards.part_one())
    print(cards.part_two())
