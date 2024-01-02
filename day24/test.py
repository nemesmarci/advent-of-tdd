import unittest
from day24 import Storm

TEST_DATA = [
    '19, 13, 30 @ -2,  1, -2',
    '18, 19, 22 @ -1, -1, -2',
    '20, 25, 34 @ -2, -2, -4',
    '12, 31, 28 @ -1, -2, -1',
    '20, 19, 15 @  1, -5, -3'
]

HAILS = [
    ((19, 13, 30), (-2, 1, -2)),
    ((18, 19, 22), (-1, -1, -2)),
    ((20, 25, 34), (-2, -2, -4)),
    ((12, 31, 28), (-1, -2, -1)),
    ((20, 19, 15), (1, -5, -3))
]


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.storm = Storm(TEST_DATA)

    def testParse(self):
        self.assertListEqual(self.storm.hails, HAILS)


if __name__ == '__main__':
    unittest.main()
