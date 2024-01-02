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
    Brick(1, 0, 1, 1, 2, 1),
    Brick(0, 0, 2, 2, 0, 2),
    Brick(0, 2, 3, 2, 2, 3),
    Brick(0, 0, 4, 0, 2, 4),
    Brick(2, 0, 5, 2, 2, 5),
    Brick(0, 1, 6, 2, 1, 6),
    Brick(1, 1, 8, 1, 1, 9)
]


class TestBricks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bricks = Bricks(TEST_DATA)

    def testParse(self):
        self.assertListEqual(self.bricks.bricks, FALLING_BRICKS)


if __name__ == '__main__':
    unittest.main()
