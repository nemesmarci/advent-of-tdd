from typing import Iterable, Sequence


class Oasis:
    def __init__(self, data: Iterable[str]) -> None:
        self.sequences = [[int(x) for x in line.strip().split()]
                          for line in data]

    @staticmethod
    def new_sequence(sequence: Sequence[int]) -> Sequence[int]:
        return [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]

    @staticmethod
    def predict(sequence: Sequence[int]) -> int:
        prediciton = 0
        while not all(x == 0 for x in sequence):
            prediciton += sequence[-1]
            sequence = Oasis.new_sequence(sequence)
        return prediciton

    def part_one(self) -> int:
        return 0
