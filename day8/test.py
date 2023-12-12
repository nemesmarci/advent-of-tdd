import unittest
from day8 import Map

TEST_DATA1 = [
    "RL",
    "",
    "AAA = (BBB, CCC)",
    "BBB = (DDD, EEE)",
    "CCC = (ZZZ, GGG)",
    "DDD = (DDD, DDD)",
    "EEE = (EEE, EEE)",
    "GGG = (GGG, GGG)",
    "ZZZ = (ZZZ, ZZZ)"
]

MAP1 = {
    "AAA": ("BBB", "CCC"),
    "BBB": ("DDD", "EEE"),
    "CCC": ("ZZZ", "GGG"),
    "DDD": ("DDD", "DDD"),
    "EEE": ("EEE", "EEE"),
    "GGG": ("GGG", "GGG"),
    "ZZZ": ("ZZZ", "ZZZ")
}


class TestMap(unittest.TestCase):
    def testParse(self):
        m = Map(TEST_DATA1)
        self.assertEqual(m.instructions, TEST_DATA1[0])
        self.assertDictEqual(m.nodes, MAP1)


if __name__ == '__main__':
    unittest.main()
