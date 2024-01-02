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

    def testReachable(self):
        self.assertEqual(self.garden.reachable(6, False), 16)
        self.assertEqual(self.garden.reachable(6, True), 16)
        self.assertEqual(self.garden.reachable(10, True), 50)
        self.assertEqual(self.garden.reachable(50, True), 1594)
        self.assertEqual(self.garden.reachable(100, True), 6536)
        self.assertEqual(self.garden.reachable(500, True), 167004)
        self.assertEqual(self.garden.reachable(1000, True), 668697)


if __name__ == '__main__':
    unittest.main()
