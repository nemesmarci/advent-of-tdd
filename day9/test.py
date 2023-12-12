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


class TestOasis(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.oasis = Oasis(TEST_DATA)

    def testParse(self):
        self.assertListEqual(SEQUENCES, self.oasis.sequences)


if __name__ == '__main__':
    unittest.main()
