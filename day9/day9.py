from typing import Iterable, Sequence


class Oasis:
    def __init__(self, data: Iterable[str]) -> None:
        self.sequences = [[int(x) for x in line.strip().split()]
                          for line in data]

    @staticmethod
    def new_sequence(sequence: Sequence[int]) -> Sequence[int]:
        return [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]

    @staticmethod
    def predict(sequence: Sequence[int]) -> Sequence[int]:
        predictions = []
        while not all(x == 0 for x in sequence):
            predictions.append(sequence[-1])
            sequence = Oasis.new_sequence(sequence)
        return predictions

    def part_one(self) -> int:
        return sum(sum(self.predict(sequence)) for sequence in self.sequences)


if __name__ == '__main__':
    with open('input.txt') as data:
        oasis = Oasis(data)
    print(oasis.part_one())
