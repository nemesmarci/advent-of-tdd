import unittest

from day2 import CubeGame

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


if __name__ == '__main__':
    unittest.main()
