import unittest
from day3 import Engine

TEST_INPUT = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..'
]

TEST_PARTS = {
    (0, 0): 467, (0, 5): 114,
    (2, 2): 35, (2, 6): 633,
    (4, 0): 617,
    (5, 7): 58,
    (6, 2): 592,
    (7, 6): 755,
    (9, 1): 664, (9, 5): 598
}


class TestParser(unittest.TestCase):
    def setUp(self):
        self.engine = Engine(TEST_INPUT)

    def test_parse_schematics(self):
        for y in range(len(TEST_INPUT)):
            for x in range(len(TEST_INPUT[0])):
                self.assertEqual(self.engine.schematic[(y, x)],
                                 TEST_INPUT[y][x])

    def test_parse_parts(self):
        self.assertDictEqual(self.engine.parts, TEST_PARTS)


if __name__ == '__main__':
    unittest.main()
