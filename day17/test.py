import unittest
from day17 import Blocks


TEST_DATA = [
    '2413432311323',
    '3215453535623',
    '3255245654254',
    '3446585845452',
    '4546657867536',
    '1438598798454',
    '4457876987766',
    '3637877979653',
    '4654967986887',
    '4564679986453',
    '1224686865563',
    '2546548887735',
    '4322674655533'
]

STEPS = [
    (0, 0, 'N', 1, {(-1, 0, 'N', 2), (0, -1, 'W', 1), (0, 1, 'E', 1)}),
    (0, 0, 'E', 1, {(0, 1, 'E', 2), (-1, 0, 'N', 1), (1, 0, 'S', 1)}),
    (0, 0, 'S', 1, {(1, 0, 'S', 2), (0, 1, 'E', 1), (0, -1, 'W', 1)}),
    (0, 0, 'W', 1, {(0, -1, 'W', 2), (-1, 0, 'N', 1), (1, 0, 'S', 1)}),
    (0, 0, 'N', 3, {(0, -1, 'W', 1), (0, 1, 'E', 1)}),
    (0, 0, 'E', 3, {(-1, 0, 'N', 1), (1, 0, 'S', 1)}),
    (0, 0, 'S', 3, {(0, 1, 'E', 1), (0, -1, 'W', 1)}),
    (0, 0, 'W', 3, {(-1, 0, 'N', 1), (1, 0, 'S', 1)}),
]


TEST_DATA_2 = [
    '111111111111',
    '999999999991',
    '999999999991',
    '999999999991',
    '999999999991'
]


class TestBlocks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.blocks = Blocks(TEST_DATA)

    def testParse(self):
        for y, line in enumerate(TEST_DATA):
            for x, c in enumerate(line.strip()):
                self.assertEqual(self.blocks.area[(y, x)], int(c))
        self.assertEqual(self.blocks.y, len(TEST_DATA) - 1)
        self.assertEqual(self.blocks.x, len(TEST_DATA[0]) - 1)

    def testPath(self):
        self.assertEqual(self.blocks.shortest_path(0, 3), 102)
        self.assertEqual(self.blocks.shortest_path(4, 10), 94)
        self.assertEqual(Blocks(TEST_DATA_2).shortest_path(4, 10), 71)

    def testPossibleSteps(self):
        for y, x, direction, straight, expected in STEPS:
            self.assertSetEqual(self.blocks.possible_steps(y, x, direction, straight, 0, 3), expected)


if __name__ == '__main__':
    unittest.main()
