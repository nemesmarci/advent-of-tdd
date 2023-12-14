import unittest
from day12 import Springs

SPRINGS = [
    '#.#.### 1,1,3',
    '.#...#....###. 1,1,3',
    '.#.###.#.###### 1,3,1,6',
    '####.#...#... 4,1,1',
    '#....######..#####. 1,6,5',
    '.###.##....# 3,2,1'
]

ROWS = [
    '#.#.###', '.#...#....###.', '.#.###.#.######', '####.#...#...', '#....######..#####.', '.###.##....#'
]

DESCRIPTIONS = [
    [1, 1, 3], [1, 1, 3], [1, 3, 1, 6], [4, 1, 1], [1, 6, 5], [3, 2, 1]
]

SOLUTIONS = [1, 4, 1, 1, 4, 10]


class TestSprings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.springs = Springs(SPRINGS)

    def testParse(self):
        self.assertListEqual(self.springs.rows, ROWS)
        self.assertListEqual(self.springs.descriptions, DESCRIPTIONS)

    def testPossibleSolutions(self):
        for row, description, solutions in zip(ROWS, DESCRIPTIONS, SOLUTIONS):
            self.assertEqual(self.springs.possible_solutions(row, description),
                             solutions)


if __name__ == '__main__':
    unittest.main()