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


class TestParser(unittest.TestCase):
    def test_parser(self):
        engine = Engine(TEST_INPUT)
        for y in range(len(TEST_INPUT)):
            for x in range(len(TEST_INPUT[0])):
                self.assertEqual(engine.schematic[(y, x)], TEST_INPUT[y][x])


if __name__ == '__main__':
    unittest.main()
