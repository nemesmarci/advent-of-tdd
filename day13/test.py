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

MIRRORS = [(5, None), (None, 4)]


class TestMirrors(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mirrors = Mirrors(TEST_DATA)

    def testParse(self):
        self.assertListEqual(self.mirrors.patterns, PATTERNS)

    def testFindMirror(self):
        for pattern, mirrors in zip(PATTERNS, MIRRORS):
            self.assertTupleEqual(self.mirrors.find_mirror(pattern), mirrors)


if __name__ == '__main__':
    unittest.main()
