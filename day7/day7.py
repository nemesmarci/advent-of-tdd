from typing import Iterable
from collections import defaultdict, Counter


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

    def part_one(self) -> int:
        return 0
