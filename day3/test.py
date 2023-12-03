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

TEST_HAS_SYMBOL = {
    (0, 0): True, (0, 5): False,
    (2, 2): True, (2, 6): True,
    (4, 0): True,
    (5, 7): False,
    (6, 2): True,
    (7, 6):  True,
    (9, 1):  True, (9, 5): True
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


class TestHasSymbol(unittest.TestCase):
    def test_has_symbol(self):
        engine = Engine(TEST_INPUT)
        has_symbol = {coord: engine.has_symbol(part_no, *coord)
                      for coord, part_no in engine.parts.items()}
        self.assertDictEqual(has_symbol, TEST_HAS_SYMBOL)


if __name__ == '__main__':
    unittest.main()
