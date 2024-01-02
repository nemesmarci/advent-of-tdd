import unittest
from day21 import Garden

TEST_DATA = [
    "...........",
    ".....###.#.",
    ".###.##..#.",
    "..#.#...#..",
    "....#.#....",
    ".##..S####.",
    ".##..#...#.",
    ".......##..",
    ".##.#.####.",
    ".##..##.##.",
    "..........."
]


class TestGarden(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.garden = Garden(TEST_DATA)

    def testParse(self):
        self.assertEqual(self.garden.y, 10)
        self.assertEqual(self.garden.x, 10)
        self.assertEqual(self.garden.start, (5, 5))


if __name__ == '__main__':
    unittest.main()
