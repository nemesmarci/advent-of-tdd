import unittest
from day13 import Mirrors


TEST_DATA = [
    '#.##..##.\n',
    '..#.##.#.\n',
    '##......#\n',
    '##......#\n',
    '..#.##.#.\n',
    '..##..##.\n',
    '#.#.##.#.\n',
    '\n',
    '#...##..#\n',
    '#....#..#\n',
    '..##..###\n',
    '#####.##.\n',
    '#####.##.\n',
    '..##..###\n',
    '#....#..#\n'
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
SMUDGED_MIRRORS = [(None, 3), (None, 1)]


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


    def testFindMirrorWithSmudge(self):
        self.assertEqual(self.mirrors.find_smudged_horizontal_mirror(PATTERNS[0]), 3)
        self.assertEqual(self.mirrors.find_smudged_horizontal_mirror(PATTERNS[1]), 1)
        for pattern, mirrors in zip(PATTERNS, SMUDGED_MIRRORS):
            self.assertTupleEqual(self.mirrors.find_smudged_mirror(pattern), mirrors)


if __name__ == '__main__':
    unittest.main()
