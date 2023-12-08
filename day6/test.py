import unittest
from day6 import BoatRace

TEST_DATA = ['Time:      7  15   30',
             'Distance:  9  40  200']
TIMES = [7, 15, 30]
RECORDS = [9, 40, 200]


class TestBoatRace(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.race = BoatRace(TEST_DATA)

    def testParse(self):
        self.assertListEqual(self.race.times, TIMES)
        self.assertListEqual(self.race.records, RECORDS)


if __name__ == '__main__':
    unittest.main()
