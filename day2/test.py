import unittest

from day2 import CubeGame, Day2

TEST_INPUT = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
]

PARSED = [
    CubeGame(id_=1, sets=[
        dict(blue=3, red=4),
        dict(red=1, green=2, blue=6),
        dict(green=2)
    ]),
    CubeGame(id_=2, sets=[
        dict(blue=1, green=2),
        dict(green=3, blue=4, red=1),
        dict(green=1, blue=1)
    ]),
    CubeGame(id_=3, sets=[
        dict(green=8, blue=6, red=20),
        dict(blue=5, red=4, green=13),
        dict(green=5, red=1)
    ]),
    CubeGame(id_=4, sets=[
        dict(green=1, red=3, blue=6),
        dict(green=3, red=6),
        dict(green=3, blue=15, red=14)
    ]),
    CubeGame(id_=5, sets=[
        dict(red=6, blue=1, green=3),
        dict(blue=2, red=1, green=2)
    ])
]


class TestParser(unittest.TestCase):
    def test_parse_lines(self):
        for input_, parsed in zip(TEST_INPUT, PARSED):
            cube = CubeGame.parse(input_)
            self.assertEqual(cube.id, parsed.id)
            self.assertListEqual(cube.sets, parsed.sets)


class TestLimits(unittest.TestCase):
    def test_limits(self):
        self.assertEqual(CubeGame.limits['red'], 12)
        self.assertEqual(CubeGame.limits['green'], 13)
        self.assertEqual(CubeGame.limits['blue'], 14)


class TestPossibleSet(unittest.TestCase):
    def setUp(self):
        self.possible = CubeGame.possible_set

    def testValid(self):
        for set_ in (
            dict(red=1),
            dict(red=12),
            dict(green=2),
            dict(green=13),
            dict(blue=3),
            dict(blue=14),
            dict(red=4, green=5),
            dict(red=6, blue=7),
            dict(green=8, blue=9),
            dict(red=10, green=11, blue=12)
        ):
            self.assertTrue(self.possible(set_), msg=set_)

    def testInvalid(self):
        for set_ in (
            dict(red=13),
            dict(green=14),
            dict(blue=15),
            dict(red=1, green=14),
            dict(red=2, blue=15),
            dict(red=13, green=3),
            dict(red=13, blue=4),
            dict(green=5, blue=15),
            dict(green=14, blue=5),
            dict(red=6, green=14, blue=7),
            dict(red=8, green=9, blue=15),
            dict(red=9, green=14, blue=15),
            dict(red=13, green=10, blue=11),
            dict(red=13, green=14, blue=12),
            dict(red=13, green=13, blue=15),
            dict(red=13, green=14, blue=15)
        ):
            self.assertFalse(self.possible(set_), msg=set_)


class TestPossibleGame(unittest.TestCase):
    def testValid(self):
        for game_id in (1, 2, 5):
            self.assertTrue(PARSED[game_id - 1].possible_game())

    def testInvalid(self):
        for game_id in (3, 4):
            self.assertFalse(PARSED[game_id - 1].possible_game())


class TestPart1(unittest.TestCase):
    def setUp(self):
        self.day2 = Day2(TEST_INPUT)

    def test_part1(self):
        self.assertEqual(self.day2.part_one(), 8)


if __name__ == '__main__':
    unittest.main()
