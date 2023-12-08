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
    'two_pairs': [('KK677', 28), ('KTJJT', 220)],
    'three_of_a_kind': [('T55J5', 684), ('QQQJA', 483)]
}

JOKER_BUCKETS = {
    'one_pair': [('32T3K', 765)],
    'two_pairs': [('KK677', 28)],
    'four_of_a_kind': [('T55J5', 684), ('KTJJT', 220), ('QQQJA', 483)]
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

    def testBucket(self):
        self.assertEqual(self.cards.bucket('23456'), 'high_card')
        self.assertEqual(self.cards.bucket('789T7'), 'one_pair')
        self.assertEqual(self.cards.bucket('JJQKK'), 'two_pairs')
        self.assertEqual(self.cards.bucket('AAA23'), 'three_of_a_kind')
        self.assertEqual(self.cards.bucket('55A55'), 'four_of_a_kind')
        self.assertEqual(self.cards.bucket('KKKKK'), 'five_of_a_kind')

    def testBuckets(self):
        self.assertDictEqual(self.cards.buckets(), BUCKETS)

    def testPart1(self):
        self.assertEqual(self.cards.part_one(), 6440)

    def testJokerBucket(self):
        self.assertEqual(self.cards.joker_bucket('23456'), 'high_card')
        self.assertEqual(self.cards.joker_bucket('2345J'), 'one_pair')
        self.assertEqual(self.cards.joker_bucket('234JJ'), 'three_of_a_kind')
        self.assertEqual(self.cards.joker_bucket('23JJJ'), 'four_of_a_kind')
        self.assertEqual(self.cards.joker_bucket('2JJJJ'), 'five_of_a_kind')
        self.assertEqual(self.cards.joker_bucket('JJJJJ'), 'five_of_a_kind')
        self.assertEqual(self.cards.joker_bucket('22345'), 'one_pair')
        self.assertEqual(self.cards.joker_bucket('2234J'), 'three_of_a_kind')
        self.assertEqual(self.cards.joker_bucket('223JJ'), 'four_of_a_kind')
        self.assertEqual(self.cards.joker_bucket('22JJJ'), 'five_of_a_kind')
        self.assertEqual(self.cards.joker_bucket('22334'), 'two_pairs')
        self.assertEqual(self.cards.joker_bucket('2233J'), 'full_house')
        self.assertEqual(self.cards.joker_bucket('22234'), 'three_of_a_kind')
        self.assertEqual(self.cards.joker_bucket('2223J'), 'four_of_a_kind')
        self.assertEqual(self.cards.joker_bucket('222JJ'), 'five_of_a_kind')
        self.assertEqual(self.cards.joker_bucket('22223'), 'four_of_a_kind')
        self.assertEqual(self.cards.joker_bucket('2222J'), 'five_of_a_kind')
        self.assertEqual(self.cards.joker_bucket('22222'), 'five_of_a_kind')

    def testJokerBuckets(self):
        self.assertDictEqual(self.cards.joker_buckets(), JOKER_BUCKETS)

    def testPart2(self):
        self.assertEqual(self.cards.part_two(), 5905)


if __name__ == '__main__':
    unittest.main()
