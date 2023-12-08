import unittest
from collections import defaultdict
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
    'two_pairs': [('KK677', 28), ('KTJJT', 220)],
    'three_of_a_kind': [('T55J5', 684), ('QQQJA', 483)]
}

JOKER_BUCKETS = {
    'one_pair': [('32T3K', 765)],
    'two_pairs': [('KK677', 28)],
    'four_of_a_kind': [('T5505', 684), ('KT00T', 220), ('QQQ0A', 483)]
}

MAPPINGS = [
    ('23456', 'high_card'),
    ('789T7', 'one_pair'),
    ('JJQKK', 'two_pairs'),
    ('AAA23', 'three_of_a_kind'),
    ('55A55', 'four_of_a_kind'),
    ('KKKKK', 'five_of_a_kind')
]

JOKER_MAPPINGS = [
    ('23456', 'high_card'),
    ('2345J', 'one_pair'),
    ('234JJ', 'three_of_a_kind'),
    ('23JJJ', 'four_of_a_kind'),
    ('2JJJJ', 'five_of_a_kind'),
    ('JJJJJ', 'five_of_a_kind'),
    ('22345', 'one_pair'),
    ('2234J', 'three_of_a_kind'),
    ('223JJ', 'four_of_a_kind'),
    ('22JJJ', 'five_of_a_kind'),
    ('22334', 'two_pairs'),
    ('2233J', 'full_house'),
    ('22234', 'three_of_a_kind'),
    ('2223J', 'four_of_a_kind'),
    ('222JJ', 'five_of_a_kind'),
    ('22223', 'four_of_a_kind'),
    ('2222J', 'five_of_a_kind'),
    ('22222', 'five_of_a_kind')
]

class TestCards(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cards = CamelCards(TEST_DATA)

    def testParse(self):
        hands = [line.split()[0] for line in TEST_DATA]
        bets = [int(line.split()[1]) for line in TEST_DATA]
        self.assertListEqual(self.cards.hands, hands)
        self.assertListEqual(self.cards.bets, bets)

    def testBucket(self):
        for hand, bucket in MAPPINGS:
            self.assertEqual(self.cards.bucket(hand), bucket)

    def testBuckets(self):
        buckets = defaultdict(list)
        for hand, bet in map(str.split, TEST_DATA):
            buckets[self.cards.bucket(hand)] \
                .append((hand, int(bet)))
        self.assertDictEqual(buckets, BUCKETS)

    def testPart1(self):
        self.assertEqual(self.cards.part_one(), 6440)

    def testJokerBucket(self):
        for hand, bucket in JOKER_MAPPINGS:
            hand = hand.replace('J', '0')
            self.assertEqual(self.cards.bucket(hand), bucket)

    def testJokerBuckets(self):
        buckets = defaultdict(list)
        for hand, bet in map(str.split, TEST_DATA):
            hand = hand.replace('J', '0')
            buckets[self.cards.bucket(hand)].append((hand, int(bet)))
        self.assertDictEqual(buckets, JOKER_BUCKETS)

    def testPart2(self):
        self.assertEqual(self.cards.part_two(), 5905)


if __name__ == '__main__':
    unittest.main()
