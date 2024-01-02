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
    [1, 2],
    [3, 4],
    [3, 4],
    [5],
    [5],
    [6],
    []
]

SUPPORTED_BY = [
    [],
    [0],
    [0],
    [1, 2],
    [1, 2],
    [3, 4],
    [5],
]


class TestBricks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bricks = Bricks(TEST_DATA)

    def testParse(self):
        self.assertListEqual(self.bricks.bricks, FALLING_BRICKS)

    def testFall(self):
        self.bricks.fall()
        for brick, supporting, supported_by in zip(self.bricks.bricks, SUPPORTING, SUPPORTED_BY):
            self.assertSetEqual(brick.supporting, {self.bricks.bricks[s] for s in supporting})
            self.assertSetEqual(brick.supported_by, {self.bricks.bricks[s] for s in supported_by})


if __name__ == '__main__':
    unittest.main()
