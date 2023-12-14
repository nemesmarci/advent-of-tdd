import unittest
from collections import defaultdict
from day11 import Image

IMAGE = [
    '...#......',
    '.......#..',
    '#.........',
    '..........',
    '......#...',
    '.#........',
    '.........#',
    '..........',
    '.......#..',
    '#...#.....'
]

GALAXIES = {(0, 3), (1, 7), (2, 0), (4, 6), (5, 1), (6, 9), (8, 7), (9, 0), (9, 4)}


class TestGalaxy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.image = Image(IMAGE)

    def testParse(self):
        self.assertEqual(self.image.max_y, 10)
        self.assertEqual(self.image.max_x, 10)
        self.assertSetEqual(self.image.galaxies, GALAXIES)
        for y in range(len(IMAGE)):
            for x in range(len(IMAGE[y])):
                self.assertEqual(IMAGE[y][x], self.image.area[(y, x)])

    def testEmptyRow(self):
        self.assertSetEqual(self.image.empty_rows(), {3, 7})

    def testEmptyCol(self):
        self.assertSetEqual(self.image.empty_cols(), {2, 5, 8})

    def testPart1(self):
        self.assertEqual(self.image.part_one(), 374)

    def testPart2(self):
        self.assertEqual(self.image.solve(10 - 1), 1030)
        self.assertEqual(self.image.solve(100 - 1), 8410)


if __name__ == '__main__':
    unittest.main()
