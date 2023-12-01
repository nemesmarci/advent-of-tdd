import sys
import string
import tempfile
import unittest
from unittest.mock import patch
from io import StringIO

from day1 import Calibrator, main as day1_main

TEST_INPUT_1 = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
TEST_INPUT_2 = ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four',
                '4nineeightseven2', 'zoneight234', '7pqrstsixteen']
NONZERO_DIGITS = [d for d in string.digits if d != '0']


class Day1_Part1(unittest.TestCase):
    def setUp(self):
        self.calibrator = Calibrator(TEST_INPUT_1)

    def test_part1(self):
        self.assertEqual(self.calibrator.part_one(), 142)


class Day1_Part2(unittest.TestCase):
    def setUp(self):
        self.calibrator = Calibrator(TEST_INPUT_2)

    def test_part_2(self):
        self.assertEqual(self.calibrator.part_two(), 281)


class Test_get_digit(unittest.TestCase):
    def setUp(self):
        self.get_digit = Calibrator.get_digit

    def test_invalid_type(self):
        for value in (None, int(), list(), tuple(), dict(), set(), object()):
            self.assertRaises(TypeError, self.get_digit, value)

    def test_invalid_argument(self):
        for value in ("", "0", "aa", "a1", "1a", "11", ' '):
            self.assertRaises(ValueError, self.get_digit, value)

    def test_valid_inputs(self):
        for c in NONZERO_DIGITS:
            self.assertEqual(self.get_digit(c), c)
        for c in string.ascii_letters:
            self.assertEqual(self.get_digit(c), None)


class Test_calibration_value(unittest.TestCase):
    def setUp(self):
        self.calibration_value = Calibrator.calibration_value

    def test_invalid_type(self):
        for value in (None, int(), list(), tuple(), dict(), set()), object():
            self.assertRaises(TypeError, self.calibration_value, value)

    def test_invalid_argument(self):
        for value in ('abc', 'aoneb', '0', '0a', '01', '101', '1 1', ' ',
                      'onetwo', 'oneight'):
            self.assertRaises(ValueError, self.calibration_value, value)

    def test_single_digit(self):
        for d in NONZERO_DIGITS:
            self.assertEqual(self.calibration_value(d), int(d + d))

    def test_numeric_digits(self):
        test_data = {
            '11': 11, '46': 46, 'a28': 28, '2a3': 23, '23b': 23, '2abc3': 23,
            '596': 56, 'a19b': 19, '3a83': 33, '9a4b6': 96, 'a5b3c2': 52,
            '1234': 14, '123456789': 19
        }
        for line, value in test_data.items():
            self.assertEqual(self.calibration_value(line), value)


class Test_calibration_value2(unittest.TestCase):
    def setUp(self):
        self.calibration_value = Calibrator.calibration_value2

    def test_invalid_type(self):
        for value in (None, int(), list(), tuple(), dict(), set()), object():
            self.assertRaises(TypeError, self.calibration_value, value)

    def test_invalid_argument(self):
        for value in ('abc', '0', '0a', '01', '101', '1 1', ' '):
            self.assertRaises(ValueError, self.calibration_value, value)

    def test_single_digit(self):
        for d in NONZERO_DIGITS:
            self.assertEqual(self.calibration_value(d), int(d * 2))
        for digit, value in Calibrator.digits.items():
            self.assertEqual(self.calibration_value(digit), int(value * 2))

    def test_numeric_digits(self):
        test_data = {
            '11': 11, '46': 46, 'a28': 28, '2a3': 23, '23b': 23, '2abc3': 23,
            '596': 56, 'a19b': 19, '3a83': 33, '9a4b6': 96, 'a5b3c2': 52,
            '1234': 14, '123456789': 19
        }
        for line, value in test_data.items():
            self.assertEqual(self.calibration_value(line), value)

    def test_mixed_digits(self):
        test_data = {
            '1one': 11, 'four6': 46, 'a2eight': 28, 'twoa3': 23,
            'twothreeb': 23, 'twoabcthree': 23, '5nine6': 56, 'aonenineb': 19,
            'threea8three': 33, 'nineafourb6': 96, 'a5bthreectwo': 52,
            'one2three4': 14, '12three45six789': 19
        }
        for line, value in test_data.items():
            self.assertEqual(self.calibration_value(line), value)

    def test_overlaps(self):
        test_data = {
            'oneight': 11, 'zerone': 11, 'twone': 22, 'threeight': 33,
            'onethreeight': 18, '1fiveight': 18, '1fiveight2': 12,
            'eightwo': 88, 'eighthree': 88, 'oneightwo': 12
        }
        for line, value in test_data.items():
            self.assertEqual(self.calibration_value(line), value)


class Test_replace_first(unittest.TestCase):
    def setUp(self):
        self.replace_first = Calibrator.replace_first

    def test_invalid_type(self):
        for value in (None, int(), list(), tuple(), dict(), set(), object()):
            self.assertRaises(TypeError, self.replace_first, value)

    def test_invalid_argument(self):
        for value in (' ', 'a ', ' a', 'a a'):
            self.assertRaises(ValueError, self.replace_first, value)

    def test_no_replace(self):
        for value in ('abc', '123', '1a2', '1two3', '12three'):
            self.assertEqual(self.replace_first(value), value)

    def test_replace(self):
        test_data = {
            'one2': '12', 'onetwo': '1two', 'onetwo3': '1two3',
            'one2three': '12three'
        }
        for line, value in test_data.items():
            self.assertEqual(self.replace_first(line), value)

    def test_overlaps(self):
        test_data = {
            'oneight': '1ight', 'zerone': 'zer1', 'twone': '2ne',
            'threeight': '3ight', 'onethreeight': '1threeight',
            '1fiveight': '1fiveight', '1fiveight2': '1fiveight2',
            'eightwo': '8wo', 'eighthree': '8hree', 'oneightwo': '1ightwo'
        }
        for line, value in test_data.items():
            self.assertEqual(self.replace_first(line), value)


class Test_replace_last(unittest.TestCase):
    def setUp(self):
        self.replace_last = Calibrator.replace_last

    def test_invalid_type(self):
        for value in (None, int(), list(), tuple(), dict(), set(), object()):
            self.assertRaises(TypeError, self.replace_last, value)

    def test_invalid_argument(self):
        for value in (' ', 'a ', ' a', 'a a'):
            self.assertRaises(ValueError, self.replace_last, value)

    def test_no_replace(self):
        for value in ('abc', '123', '1a2', '1two3', 'one23'):
            self.assertEqual(self.replace_last(value), value)

    def test_replace(self):
        test_data = {
            'one2': 'one2', 'onetwo': 'one2', 'onetwo3': 'onetwo3',
            'one2three': 'one23'
        }
        for line, value in test_data.items():
            self.assertEqual(self.replace_last(line), value)

    def test_overlaps(self):
        test_data = {
            'oneight': 'on8', 'zerone': 'zer1', 'twone': 'tw1',
            'threeight': 'thre8', 'onethreeight': 'onethre8',
            '1fiveight': '1fiv8', '1fiveight2': '1fiveight2',
            'eightwo': 'eigh2', 'eighthree': 'eigh3', 'oneightwo': 'oneigh2'
        }
        for line, value in test_data.items():
            self.assertEqual(self.replace_last(line), value)


class TestMain(unittest.TestCase):
    def test_no_input(self):
        sys.argv = [__file__]
        with self.assertRaises(SystemExit) as cm:
            day1_main()
        self.assertEqual(str(cm.exception), 'ERROR: no input file provided')

    def test_no_such_file(self):
        filename = '/no_such_file'
        sys.argv = [__file__, filename]
        with self.assertRaises(SystemExit) as cm:
            day1_main()
        self.assertEqual(str(cm.exception),
                         f'ERROR: {filename} is not a regular file')

    @patch('sys.stdout', new_callable=StringIO)
    def test_input_file(self, stdout):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as input_file:
            for line in TEST_INPUT_1:
                input_file.write(f'{line}\n')
            input_file.close()
            sys.argv = [__file__, input_file.name]
            day1_main()
            self.assertEqual(stdout.getvalue(), '142\n142\n')


if __name__ == '__main__':
    unittest.main()
