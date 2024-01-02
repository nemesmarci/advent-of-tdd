import unittest
from day20 import Machine

TEST_DATA = [
    "broadcaster -> a, b, c",
    "%a -> b",
    "%b -> c",
    "%c -> inv",
    "&inv -> a"
]

BROADCASTER_OUTPUTS = ['a', 'b', 'c']

FLIPFLOPS = ['a', 'b', 'c']

FLIPFLOP_OUTPUTS = [
    ['b'],
    ['c'],
    ['inv']
]

CONJUNCTIONS = ['inv']

CONJUNCTION_OUTPUTS = [
    ['a']
]


class TestMachine(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.machine = Machine(TEST_DATA)

    def testParse(self):
        broadcaster = self.machine.modules['broadcaster']
        self.assertListEqual(broadcaster.outputs, BROADCASTER_OUTPUTS)
        for f, outputs in zip(FLIPFLOPS, FLIPFLOP_OUTPUTS):
            flipflop = self.machine.modules[f]
            self.assertEqual(flipflop.state, False)
            self.assertListEqual(flipflop.outputs, outputs)
        for c, outputs in zip(CONJUNCTIONS, CONJUNCTION_OUTPUTS):
            conjunction = self.machine.modules[c]
            self.assertListEqual(conjunction.outputs, outputs)


if __name__ == '__main__':
    unittest.main()
