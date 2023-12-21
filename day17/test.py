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


class TestBlocks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.blocks = Blocks(TEST_DATA)

    def testParse(self):
        for y, line in enumerate(TEST_DATA):
            for x, c in enumerate(line.strip()):
                self.assertEqual(self.blocks.area[(y, x)], c)
        self.assertEqual(self.blocks.y, len(TEST_DATA))
        self.assertEqual(self.blocks.x, len(TEST_DATA[0]))


if __name__ == '__main__':
    unittest.main()
