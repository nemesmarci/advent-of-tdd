import unittest
from day23 import Walk


TEST_DATA = [
    '#.#####################',
    '#.......#########...###',
    '#######.#########.#.###',
    '###.....#.>.>.###.#.###',
    '###v#####.#v#.###.#.###',
    '###.>...#.#.#.....#...#',
    '###v###.#.#.#########.#',
    '###...#.#.#.......#...#',
    '#####.#.#.#######.#.###',
    '#.....#.#.#.......#...#',
    '#.#####.#.#.#########v#',
    '#.#...#...#...###...>.#',
    '#.#.#v#######v###.###v#',
    '#...#.>.#...>.>.#.###.#',
    '#####v#.#.###v#.#.###.#',
    '#.....#...#...#.#.#...#',
    '#.#########.###.#.#.###',
    '#...###...#...#...#.###',
    '###.###.#.###v#####v###',
    '#...#...#.#.>.>.#.>.###',
    '#.###.###.#.###.#.#v###',
    '#.....###...###...#...#',
    '#####################.#'
]


class TestWalk(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.walk = Walk(TEST_DATA)

    def testParse(self):
        self.assertEqual(self.walk.y, 22)
        self.assertEqual(self.walk.x, 22)

    def testPart1(self):
        self.assertEqual(self.walk.part_one(), 94)

    def testPart2(self):
        self.assertEqual(self.walk.part_two(), 154)


if __name__ == '__main__':
    unittest.main()
