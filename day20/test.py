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

CONJUNCTION_INPUTS = [
    {'c': False}
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

    def testInputs(self):
        self.machine.add_inputs()
        for c, inputs in zip(CONJUNCTIONS, CONJUNCTION_INPUTS):
            self.assertDictEqual(self.machine.modules[c].inputs, inputs)


if __name__ == '__main__':
    unittest.main()
