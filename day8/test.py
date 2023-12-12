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

TEST_DATA2 = [
    "LLR",
    "",
    "AAA = (BBB, BBB)",
    "BBB = (AAA, ZZZ)",
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

TEST_DATA3 = [
    "LR",
    "",
    "11A = (11B, XXX)",
    "11B = (XXX, 11Z)",
    "11Z = (11B, XXX)",
    "22A = (22B, XXX)",
    "22B = (22C, 22C)",
    "22C = (22Z, 22Z)",
    "22Z = (22B, 22B)",
    "XXX = (XXX, XXX)"
]


class TestMap(unittest.TestCase):
    def testParse(self):
        m = Map(TEST_DATA1)
        self.assertEqual(m.instructions, TEST_DATA1[0])
        self.assertDictEqual(m.nodes, MAP1)

    def testStep(self):
        m = Map(TEST_DATA1)
        self.assertEqual(m.step('AAA', 'R'), 'CCC')
        self.assertEqual(m.step('CCC', 'L'), 'ZZZ')

    def testTraverse(self):
        m = Map(TEST_DATA1)
        self.assertEqual(m.traverse('AAA', lambda x: x == 'ZZZ'), 2)
        m = Map(TEST_DATA2)
        self.assertEqual(m.traverse('AAA', lambda x: x == 'ZZZ'), 6)

    def testStartNodes(self):
        m = Map(TEST_DATA3)
        self.assertListEqual(m.start_nodes(), ['11A', '22A'])

    def testPart2(self):
        m = Map(TEST_DATA3)
        self.assertEqual(m.part_two(), 6)


if __name__ == '__main__':
    unittest.main()
