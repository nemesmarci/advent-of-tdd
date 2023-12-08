import unittest
from day6 import BoatRace

TEST_DATA = ['Time:      7  15   30',
             'Distance:  9  40  200']
TIMES = [7, 15, 30]
RECORDS = [9, 40, 200]

WINS = [2 * [False] + 4 * [True] + 2 * [False],
        4 * [False] + 8 * [True] + 4 * [False],
        11 * [False] + 9 * [True] + 11 * [False]
]

class TestBoatRace(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.race = BoatRace(TEST_DATA)

    def testParse(self):
        self.assertListEqual(self.race.times, TIMES)
        self.assertListEqual(self.race.records, RECORDS)

    def testWin(self):
        for time, record, wins in zip(TIMES, RECORDS, WINS):
            for time_taken in range(0, time + 1):
                self.assertEqual(self.race.win(time_taken, time, record),
                                 wins[time_taken])

    def testWins(self):
        for time, record, wins in zip(TIMES, RECORDS, WINS):
            self.assertEqual(self.race.wins(time, record),
                             len(list(filter(bool, WINS))))


if __name__ == '__main__':
    unittest.main()
