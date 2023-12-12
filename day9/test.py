import unittest
from day9 import Oasis

TEST_DATA = [
    "0 3 6 9 12 15",
    "1 3 6 10 15 21",
    "10 13 16 21 30 45"
]

SEQUENCES = [
    [0, 3, 6, 9, 12, 15],
    [1, 3, 6, 10, 15, 21],
    [10, 13, 16, 21, 30, 45]
]

NEW_SEQUENCES = [
    [
        [3, 3, 3, 3, 3],
        [0, 0, 0, 0]
    ],
    [
        [2, 3, 4, 5, 6],
        [1, 1, 1, 1],
        [0, 0, 0]
    ],
    [
        [3, 3, 5, 9, 15],
        [0, 2, 4, 6],
        [2, 2, 2],
        [0, 0]
    ]
]

PREDICTIONS = [18, 28, 68]


class TestOasis(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.oasis = Oasis(TEST_DATA)

    def testParse(self):
        self.assertListEqual(SEQUENCES, self.oasis.sequences)

    def testNewSequence(self):
        for sequence, new_sequences in zip(SEQUENCES, NEW_SEQUENCES):
            for new_sequence in new_sequences:
                sequence = self.oasis.new_sequence(sequence)
                self.assertSequenceEqual(new_sequence, sequence)

    def testPrediction(self):
        for sequence, prediction in zip(SEQUENCES, PREDICTIONS):
            self.assertEqual(sum(self.oasis.predict(sequence)), prediction)

    def testPart1(self):
        self.assertEqual(self.oasis.part_one(), 114)


if __name__ == '__main__':
    unittest.main()
