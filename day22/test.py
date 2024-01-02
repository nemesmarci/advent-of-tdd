import unittest
from day22 import Brick, Bricks


TEST_DATA = [
    '1,0,1~1,2,1',
    '0,0,2~2,0,2',
    '0,2,3~2,2,3',
    '0,0,4~0,2,4',
    '2,0,5~2,2,5',
    '0,1,6~2,1,6',
    '1,1,8~1,1,9'
]


FALLING_BRICKS = [
    Brick(0, 1, 0, 1, 1, 2, 1),
    Brick(1, 0, 0, 2, 2, 0, 2),
    Brick(2, 0, 2, 3, 2, 2, 3),
    Brick(3, 0, 0, 4, 0, 2, 4),
    Brick(4, 2, 0, 5, 2, 2, 5),
    Brick(5, 0, 1, 6, 2, 1, 6),
    Brick(6, 1, 1, 8, 1, 1, 9)
]

SUPPORTING = [
    {1, 2},
    {3, 4},
    {3, 4},
    {5},
    {5},
    {6},
    set()
]

SUPPORTED_BY = [
    set(),
    {0},
    {0},
    {1, 2},
    {1, 2},
    {3, 4},
    {5},
]


class TestBricks(unittest.TestCase):
    def testParse(self):
        bricks = Bricks(TEST_DATA)
        self.assertListEqual(bricks.bricks, FALLING_BRICKS)

    def testFall(self):
        bricks = Bricks(TEST_DATA)
        bricks.fall()
        for brick, supporting, supported_by in zip(bricks.bricks, SUPPORTING, SUPPORTED_BY):
            self.assertSetEqual({s.id for s in brick.supporting}, supporting)
            self.assertSetEqual({s.id for s in brick.supported_by}, supported_by)

    def testPart1(self):
        bricks = Bricks(TEST_DATA)
        bricks.fall()
        self.assertEqual(bricks.part_one(), 5)


if __name__ == '__main__':
    unittest.main()
