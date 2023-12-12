from typing import Iterable, Sequence, Callable
from operator import add, sub


class Oasis:
    def __init__(self, data: Iterable[str]) -> None:
        self.sequences = [[int(x) for x in line.strip().split()]
                          for line in data]

    @staticmethod
    def new_sequence(sequence: Sequence[int]) -> Sequence[int]:
        return [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]

    @staticmethod
    def predict(sequence: Sequence[int], index: int) -> Sequence[int]:
        predictions = []
        while not all(x == 0 for x in sequence):
            predictions.append(sequence[index])
            sequence = Oasis.new_sequence(sequence)
        return predictions

    def part_one(self) -> int:
        return self.solve(add, -1)

    def part_two(self) -> int:
        return self.solve(sub, 0)

    def solve(self, op: Callable[[int, int], int], index: int) -> int:
        values = 0
        for sequence in self.sequences:
            n = 0
            for x in self.predict(sequence, index)[::-1]:
                n = op(x, n)
            values += n
        return values


if __name__ == '__main__':
    with open('input.txt') as data:
        oasis = Oasis(data)
    print(oasis.part_one())
    print(oasis.part_two())
