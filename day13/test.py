import unittest
from day13 import Mirrors


TEST_DATA = [
    '#.##..##.',
    '..#.##.#.',
    '##......#',
    '##......#',
    '..#.##.#.',
    '..##..##.',
    '#.#.##.#.',
    '',
    '#...##..#',
    '#....#..#',
    '..##..###',
    '#####.##.',
    '#####.##.',
    '..##..###',
    '#....#..#'
]

PATTERNS = [
    ['#.##..##.',
     '..#.##.#.',
     '##......#',
     '##......#',
     '..#.##.#.',
     '..##..##.',
     '#.#.##.#.'],
    ['#...##..#',
     '#....#..#',
     '..##..###',
     '#####.##.',
     '#####.##.',
     '..##..###',
     '#....#..#']
]


class TestMirrors(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mirrors = Mirrors(TEST_DATA)

    def testParse(self):
        self.assertListEqual(self.mirrors.patterns, PATTERNS)


if __name__ == '__main__':
    unittest.main()
