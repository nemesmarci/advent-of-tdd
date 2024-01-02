import unittest
from day25 import Components

TEST_DATA = [
    "jqt: rhn xhk nvd",
    "rsh: frs pzl lsr",
    "xhk: hfx",
    "cmg: qnr nvd lhk bvb",
    "rhn: xhk bvb hfx",
    "bvb: xhk hfx",
    "pzl: lsr hfx nvd",
    "qnr: nvd",
    "ntq: jqt hfx bvb xhk",
    "nvd: lhk",
    "lsr: lhk",
    "rzs: qnr cmg lsr rsh",
    "frs: qnr lhk lsr",
]


class TestComponents(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.components = Components(TEST_DATA)

    def testParse(self):
        self.assertEqual(self.components.graph.number_of_nodes(), 15)
        self.assertEqual(self.components.graph.number_of_edges(), 33)


if __name__ == '__main__':
    unittest.main()
