import unittest
from day14 import Rocks

TEST_DATA = [
    'O....#....',
    'O.OO#....#',
    '.....##...',
    'OO.#O....O',
    '.O.....O#.',
    'O.#..O.#.#',
    '..O..#O..O',
    '.......O..',
    '#....###..',
    '#OO..#....'
]

AREA = [
    ['O', '.', '.', '.', '.', '#', '.', '.', '.', '.'],
    ['O', '.', 'O', 'O', '#', '.', '.', '.', '.', '#'],
    ['.', '.', '.', '.', '.', '#', '#', '.', '.', '.'],
    ['O', 'O', '.', '#', 'O', '.', '.', '.', '.', 'O'],
    ['.', 'O', '.', '.', '.', '.', '.', 'O', '#', '.'],
    ['O', '.', '#', '.', '.', 'O', '.', '#', '.', '#'],
    ['.', '.', 'O', '.', '.', '#', 'O', '.', '.', 'O'],
    ['.', '.', '.', '.', '.', '.', '.', 'O', '.', '.'],
    ['#', '.', '.', '.', '.', '#', '#', '#', '.', '.'],
    ['#', 'O', 'O', '.', '.', '#', '.', '.', '.', '.']
]

MOVED_COLS = [
    'OOOO....##',
    'OOO.......',
    'O....#OO..',
    'O..#......',
    '.#O.......',
    '#.#O..#.##',
    '..#O....#.',
    'O....#O.#.',
    '....#.....',
    '.#O..#O...'
]


class TestRocks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rocks = Rocks(TEST_DATA)

    def testParse(self):
        self.assertListEqual(self.rocks.area, AREA)

    def testMoveBlocks(self):
        for x in range(len(AREA[0])):
            col = [AREA[y][x] for y in range(len(AREA))]
            self.assertEqual(self.rocks.move_blocks(''.join(col)), MOVED_COLS[x])


if __name__ == '__main__':
    unittest.main()
