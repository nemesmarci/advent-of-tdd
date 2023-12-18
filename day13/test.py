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
        self.assertEqual(self.mirrors.find_vertical_mirror(PATTERNS[0]), 5)
        self.assertEqual(self.mirrors.find_horizontal_mirror(PATTERNS[1]), 4)
        for pattern, mirrors in zip(PATTERNS, MIRRORS):
            self.assertTupleEqual(self.mirrors.find_mirror(pattern), mirrors)

    def testValue(self):
        self.assertEqual(self.mirrors.value(PATTERNS[0]), 5)
        self.assertEqual(self.mirrors.value(PATTERNS[1]), 400)

    def testPart1(self):
        self.assertEqual(self.mirrors.part_one(), 405)


if __name__ == '__main__':
    unittest.main()
