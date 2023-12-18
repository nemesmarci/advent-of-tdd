import unittest
from day16 import Grid


TEST_DATA = [
    '.|...\\....',
    '|.-.\\.....',
    '.....|-...',
    '........|.',
    '..........',
    '.........\\',
    '..../.\\\\..',
    '.-.-/..|..',
    '.|....-|.\\',
    '..//.|....'
]

ROW_1 = {
    (0, 0): '.', (0, 1): '|', (0, 2): '.', (0, 3): '.', (0, 4): '.',
    (0, 5): '\\', (0, 6): '.', (0, 7): '.', (0, 8): '.', (0, 9): '.'
}


class TestGrid(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.grid = Grid(TEST_DATA)

    def testParse(self):
        for t in ROW_1:
            self.assertEqual(self.grid.area[t], ROW_1[t])
            self.assertEqual(self.grid.y, 9)
            self.assertEqual(self.grid.x, 9)


if __name__ == '__main__':
    unittest.main()
