import unittest
from day18 import Lagoon

TEST_DATA = [
    'R 6 (#70c710)',
    'D 5 (#0dc571)',
    'L 2 (#5713f0)',
    'D 2 (#d2c081)',
    'R 2 (#59c680)',
    'D 2 (#411b91)',
    'L 5 (#8ceee2)',
    'U 2 (#caa173)',
    'L 1 (#1b58a2)',
    'U 2 (#caa171)',
    'R 2 (#7807d2)',
    'U 3 (#a77fa3)',
    'L 2 (#015232)',
    'U 2 (#7a21e3)'
]


class TestLagoon(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lagoon = Lagoon(TEST_DATA)

    def testParse(self):
        self.assertListEqual(self.lagoon.directions, list('RDLDRDLULURULU'))
        self.assertListEqual(self.lagoon.lengths, [6, 5, 2, 2, 2, 2, 5, 2, 1, 2, 2, 3, 2, 2])

    def testPerimeter(self):
        self.assertEqual(self.lagoon.perimeter(), 38)


if __name__ == '__main__':
    unittest.main()
