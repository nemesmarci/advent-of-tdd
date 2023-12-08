import unittest
from day7 import CamelCards

TEST_DATA = [
    '32T3K 765',
    'T55J5 684',
    'KK677 28',
    'KTJJT 220',
    'QQQJA 483'
]

BUCKETS = {
    'one_pair': [('32T3K', 765)],
    'two_pair': [('KK677', 28), ('KTJJT', 220)],
    'three_of_a_kind': [('T55J5', 684), ('QQQJA', 483)]
}


class TestCards(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards = CamelCards(TEST_DATA)

    def testParse(self):
        hands = [line.split()[0] for line in TEST_DATA]
        bets = [int(line.split()[1]) for line in TEST_DATA]
        self.assertListEqual(self.cards.hands, hands)
        self.assertListEqual(self.cards.bets, bets)

    def testBuckets(self):
        self.assertDictEqual(self.cards.buckets(), BUCKETS)


if __name__ == '__main__':
    unittest.main()
