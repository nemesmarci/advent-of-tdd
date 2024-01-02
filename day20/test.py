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

TEST_DATA2 = [
    "broadcaster -> a",
    "%a -> inv, con",
    "&inv -> b",
    "%b -> con",
    "&con -> output"
]

BROADCASTER_OUTPUTS2 = ['a']

FLIPFLOPS2 = ['a', 'b']

FLIPFLOP_OUTPUTS2 = [
    ['inv', 'con'],
    ['con']
]

CONJUNCTIONS2 = ['inv', 'con']

CONJUNCTION_OUTPUTS2 = [
    ['b'],
    ['output']
]

CONJUNCTION_INPUTS2 = [
    {'a': False},
    {'a': False, 'b': False}
]


class TestMachine(unittest.TestCase):
    def testParse(self):
        for (test_data, broadcaster_outputs, flipflops, flipflop_outputs,
             conjunctions, conjunction_outputs, conjunction_inputs) in \
                [[TEST_DATA, BROADCASTER_OUTPUTS, FLIPFLOPS, FLIPFLOP_OUTPUTS,
                  CONJUNCTIONS, CONJUNCTION_OUTPUTS, CONJUNCTION_INPUTS],
                 [TEST_DATA2, BROADCASTER_OUTPUTS2, FLIPFLOPS2, FLIPFLOP_OUTPUTS2,
                  CONJUNCTIONS2, CONJUNCTION_OUTPUTS2, CONJUNCTION_INPUTS2]]:
            machine = Machine(test_data)
            broadcaster = machine.modules['broadcaster']
            self.assertListEqual(broadcaster.outputs, broadcaster_outputs)
            for f, outputs in zip(flipflops, flipflop_outputs):
                flipflop = machine.modules[f]
                self.assertEqual(flipflop.state, False)
                self.assertListEqual(flipflop.outputs, outputs)
            for c, outputs in zip(conjunctions, conjunction_outputs):
                conjunction = machine.modules[c]
                self.assertListEqual(conjunction.outputs, outputs)

    def testInputs(self):
        for test_data, conjunctions, conjunction_inputs in \
                [[TEST_DATA, CONJUNCTIONS, CONJUNCTION_INPUTS],
                 [TEST_DATA2, CONJUNCTIONS2, CONJUNCTION_INPUTS2]]:
            machine = Machine(test_data)
            machine.add_inputs()
            for c, inputs in zip(conjunctions, conjunction_inputs):
                self.assertDictEqual(machine.modules[c].inputs, inputs)

    def testSignals(self):
        for (test_data, broadcaster_outputs, flipflops, flipflop_outputs,
             conjunctions, conjunction_outputs, conjunction_inputs) in \
                [[TEST_DATA, BROADCASTER_OUTPUTS, FLIPFLOPS, FLIPFLOP_OUTPUTS,
                  CONJUNCTIONS, CONJUNCTION_OUTPUTS, CONJUNCTION_INPUTS],
                 [TEST_DATA2, BROADCASTER_OUTPUTS2, FLIPFLOPS2, FLIPFLOP_OUTPUTS2,
                  CONJUNCTIONS2, CONJUNCTION_OUTPUTS2, CONJUNCTION_INPUTS2]]:
            machine = Machine(test_data)
            machine.add_inputs()
            for test_signal in [False, True]:
                self.assertListEqual(machine.modules['broadcaster'].signals(test_signal, 'button'),
                                     [(o, test_signal) for o in broadcaster_outputs])

            for f, outputs in zip(flipflops, flipflop_outputs):
                flipflop = machine.modules[f]
                self.assertEqual(flipflop.state, False)
                self.assertListEqual(flipflop.signals(True, 'button'), [])
                self.assertListEqual(flipflop.signals(False, 'button'), [(o, True) for o in outputs])
                self.assertEqual(flipflop.state, True)
                self.assertListEqual(flipflop.signals(True, 'button'), [])
                self.assertListEqual(flipflop.signals(False, 'button'), [(o, False) for o in outputs])
                self.assertEqual(flipflop.state, False)

            for c, inputs, outputs in zip(conjunctions, conjunction_inputs, conjunction_outputs):
                conjunction = machine.modules[c]
                for i in list(inputs)[:-1]:
                    self.assertListEqual(conjunction.signals(True, i), [(o, True) for o in outputs])
                self.assertListEqual(conjunction.signals(True, list(inputs)[-1]), [(o, False) for o in outputs])


if __name__ == '__main__':
    unittest.main()
