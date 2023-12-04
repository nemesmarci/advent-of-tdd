import unittest
from day4 import ScratchCards


TEST_DATA = [
    'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'
]

PARSED = {
    1: ({41, 48, 83, 86, 17}, {83, 86, 6, 31, 17, 9, 48, 53}),
    2: ({13, 32, 20, 16, 61}, {61, 30, 68, 82, 17, 32, 24, 19}),
    3: ({1, 21, 53, 59, 44}, {69, 82, 63, 72, 16, 21, 14, 1}),
    4: ({41, 92, 73, 84, 69}, {59, 84, 76, 51, 58, 5, 54, 83}),
    5: ({87, 83, 26, 28, 32}, {88, 30, 70, 12, 93, 22, 82, 36}),
    6: ({31, 18, 13, 56, 72}, {74, 77, 10, 23, 35, 67, 36, 11})
}


class TestScratchCards(unittest.TestCase):
    def test_parse(self):
        for line, expected in zip(TEST_DATA, PARSED):
            card, winning, numbers = ScratchCards.parse(line)
            self.assertEqual(card, expected)
            self.assertEqual(winning, PARSED[expected][0])
            self.assertEqual(numbers, PARSED[expected][1])


if __name__ == '__main__':
    unittest.main()
