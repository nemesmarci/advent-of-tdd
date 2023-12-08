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

    @staticmethod
    def bucket(hand: str) -> str:
        match (cards := Counter(hand)).most_common(1)[0][1]:
            case 1:
                return 'high_card'
            case 2:
                pairs = len([p for p in cards.values() if p == 2])
                return 'one_pair' if pairs == 1 else 'two_pairs'
            case 3:
                return 'full_house' if 2 in cards.values() \
                    else 'three_of_a_kind'
            case 4:
                return 'four_of_a_kind'
            case 5:
                return 'five_of_a_kind'

    def buckets(self) -> dict[str, list[tuple[str, int]]]:
        buckets = defaultdict(list)
        for hand, bet in zip(self.hands, self.bets):
            buckets[self.bucket(hand)].append((hand, bet))
        return buckets

    @staticmethod
    def key(item: tuple[str, int]) -> str:
        return item[0].translate(str.maketrans('TJQKA', 'ABCDE'))

    def part_one(self) -> int:
        buckets = self.buckets()
        winnings = 0
        for rank, (hand, bet) in enumerate(chain(
                sorted(buckets['high_card'], key=self.key),
                sorted(buckets['one_pair'], key=self.key),
                sorted(buckets['two_pairs'], key=self.key),
                sorted(buckets['three_of_a_kind'], key=self.key),
                sorted(buckets['full_house'], key=self.key),
                sorted(buckets['four_of_a_kind'], key=self.key),
                sorted(buckets['five_of_a_kind'], key=self.key))):
            winnings += (rank + 1) * bet
        return winnings

    @staticmethod
    def joker_bucket(hand: str) -> str:
        cards = Counter(hand)
        jokers = cards.pop('J', 0)
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

    def joker_buckets(self) -> dict[str, list[tuple[str, int]]]:
        buckets = defaultdict(list)
        for hand, bet in zip(self.hands, self.bets):
            buckets[self.joker_bucket(hand)].append((hand, bet))
        return buckets

    @staticmethod
    def joker_key(item: tuple[str, int]) -> str:
        return item[0].translate(str.maketrans('TJQKA', 'A0CDE'))

    def part_two(self) -> int:
        buckets = self.joker_buckets()
        winnings = 0
        for rank, (hand, bet) in enumerate(chain(
                sorted(buckets['high_card'], key=self.joker_key),
                sorted(buckets['one_pair'], key=self.joker_key),
                sorted(buckets['two_pairs'], key=self.joker_key),
                sorted(buckets['three_of_a_kind'], key=self.joker_key),
                sorted(buckets['full_house'], key=self.joker_key),
                sorted(buckets['four_of_a_kind'], key=self.joker_key),
                sorted(buckets['five_of_a_kind'], key=self.joker_key))):
            winnings += (rank + 1) * bet
        return winnings
