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
LOCATIONS = [82, 43, 86, 35]

MISSING_RANGES = [
    [(range(0, 50), range(0, 50))],
    [],
    [],
    [(range(0, 18), range(0, 18))],
    [(range(0, 45), range(0, 45))],
    [],
    [(range(0, 56), range(0, 56))]
]


class TestAlmanac(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('test.txt') as data:
            cls.almanac = Almanac(data)

    def testParse(self):
        self.assertListEqual(self.almanac.seeds, SEEDS)
        self.assertListEqual(self.almanac.map_ranges, MAP_RANGES)

    def testLocation(self):
        for seed, location in zip(self.almanac.seeds, LOCATIONS):
            self.assertEqual(self.almanac.location(seed), location)

    def testPart1(self):
        self.assertEqual(self.almanac.part_one(), 35)

    def testAddMissingRanges(self):
        for rules, expected in zip(self.almanac.map_ranges, MISSING_RANGES):
            self.assertListEqual(self.almanac.missing_ranges(rules), expected)

    def testTargetRanges(self):
        self.assertEqual(self.almanac.target_ranges(),
                         [range(SEEDS[0], SEEDS[0] + SEEDS[1]),
                          range(SEEDS[2], SEEDS[2] + SEEDS[3])])


if __name__ == '__main__':
    unittest.main()
