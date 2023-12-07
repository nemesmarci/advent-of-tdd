import unittest
from day5 import Almanac


SEEDS = [79, 14, 55, 13]
MAP_RANGES = [
    [(range(98, 100), range(50, 52)), (range(50, 98), range(52, 100))],
    [(range(15, 52), range(0, 37)), (range(52, 54), range(37, 39)),
     (range(0, 15), range(39, 54))],
    [(range(53, 61), range(49, 57)), (range(11, 53), range(0, 42)),
     (range(0, 7), range(42, 49)), (range(7, 11), range(57, 61))],
    [(range(18, 25), range(88, 95)), (range(25, 95), range(18, 88))],
    [(range(77, 100), range(45, 68)), (range(45, 64), range(81, 100)),
     (range(64, 77), range(68, 81))],
    [(range(69, 70), range(0, 1)), (range(0, 69), range(1, 70))],
    [(range(56, 93), range(60, 97)), (range(93, 97), range(56, 60))]
]


class TestAlmanac(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('test.txt') as data:
            cls.almanac = Almanac(data)

    def testParse(self):
        self.assertListEqual(self.almanac.seeds, SEEDS)
        self.assertListEqual(self.almanac.map_ranges, MAP_RANGES)


if __name__ == '__main__':
    unittest.main()
