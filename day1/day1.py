import os
import sys
import string

from typing import Iterable

SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(SRC)

from utils import check_type  # noqa: E402


class Calibrator():
    digits: dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    @staticmethod
    def get_digit(char: str) -> str:
        check_type(char, [str])
        if not char or char == '0' or char in string.whitespace \
                or len(char) > 1:
            raise ValueError(f'Unexpected value: `{char}`')
        try:
            return str(int(char))
        except ValueError:
            return None

    @staticmethod
    def calibration_value(line: str) -> int:
        check_type(line, [str])
        digits = [d for c in line if (d := Calibrator.get_digit(c))]
        if len(digits) < 1:
            raise ValueError(f'No digits found in `{line}`')
        return int(digits[0] + digits[-1])

    @staticmethod
    def calibration_value2(line: str) -> int:
        return Calibrator.calibration_value(Calibrator.replace_last(
            Calibrator.replace_first(line)))

    @staticmethod
    def replace_first(line: str) -> str:
        check_type(line, [str])
        min_index = next((i for i, c in enumerate(line)
                          if Calibrator.get_digit(c)), len(line))
        first = None
        for num in Calibrator.digits:
            if 0 <= (index := line.find(num)) < min_index:
                first = num
                min_index = index
        return line.replace(first, Calibrator.digits[first], 1) if first \
            else line

    @staticmethod
    def replace_last(line: str) -> str:
        check_type(line, [str])
        max_index = len(line) - 1 - next((i for i, c in enumerate(line[::-1])
                                          if Calibrator.get_digit(c)),
                                         len(line))
        last = None
        for num in Calibrator.digits:
            if (index := line.rfind(num)) > max_index:
                last = num
                max_index = index
        return Calibrator.digits[last].join(line.rsplit(last, 1)) if last \
            else line

    def __init__(self, data: Iterable[str]) -> None:
        self.data = data

    def part_one(self) -> int:
        return sum(self.calibration_value(line.strip()) for line in self.data)

    def part_two(self) -> int:
        return sum(self.calibration_value2(line.strip()) for line in self.data)


def main():
    if len(sys.argv) < 2:
        sys.exit('ERROR: no input file provided')
    input_file = sys.argv[1]
    if not(os.path.isfile(input_file)):
        sys.exit(f'ERROR: {input_file} is not a regular file')
    with open(input_file) as data:
        calibrator = Calibrator(data.readlines())
    print(calibrator.part_one())
    print(calibrator.part_two())


if __name__ == '__main__':
    main()
