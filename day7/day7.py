from typing import Iterable


class CamelCards:
    def __init__(self, data: Iterable[str]) -> None:
        self.hands = []
        self.bets = []
        for line in data:
            hand, bet = line.split()
            self.hands.append(hand)
            self.bets.append(int(bet))

    def buckets(self) -> dict[str, list[tuple[str, int]]]:
        return {}
