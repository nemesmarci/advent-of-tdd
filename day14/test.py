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

MOVED_AREA = [
    ['O', 'O', 'O', 'O', '.', '#', '.', 'O', '.', '.'],
    ['O', 'O', '.', '.', '#', '.', '.', '.', '.', '#'],
    ['O', 'O', '.', '.', 'O', '#', '#', '.', '.', 'O'],
    ['O', '.', '.', '#', '.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
    ['.', '.', '#', '.', '.', '.', '.', '#', '.', '#'],
    ['.', '.', 'O', '.', '.', '#', '.', 'O', '.', 'O'],
    ['.', '.', 'O', '.', '.', '.', '.', '.', '.', '.'],
    ['#', '.', '.', '.', '.', '#', '#', '#', '.', '.'],
    ['#', '.', '.', '.', '.', '#', '.', '.', '.', '.']
]


class TestRocks(unittest.TestCase):
    def setUp(self):
        self.rocks = Rocks(TEST_DATA)

    def testParse(self):
        self.assertListEqual(self.rocks.area, AREA)
        self.assertEqual(self.rocks.y, 10)
        self.assertEqual(self.rocks.x, 10)

    def testMoveBlocks(self):
        for x in range(len(AREA[0])):
            col = [AREA[y][x] for y in range(len(AREA))]
            self.assertEqual(self.rocks.move_blocks(''.join(col), 'up'), MOVED_COLS[x])

    def testMoveCols(self):
        self.rocks.move_cols('up')
        self.assertListEqual(self.rocks.area, MOVED_AREA)

    def testWeigh(self):
        self.rocks.move_cols('up')
        self.assertEqual(self.rocks.weight(), 136)

    def testCycle(self):
        self.assertEqual(self.rocks.run_cycle(), 64)


if __name__ == '__main__':
    unittest.main()
