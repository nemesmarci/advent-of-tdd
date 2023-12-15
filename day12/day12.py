from typing import Iterable
from collections import defaultdict


class Springs:
    def __init__(self, data: Iterable[str]) -> None:
        self.rows: list[str] = []
        self.descriptions: list[list[int]] = []
        for line in data:
            t, d = line.strip().split()
            self.rows.append(t)
            self.descriptions.append(list(map(int, d.split(','))))

    @staticmethod
    def possible_solutions(row: str, description: list[int]) -> int:
        """https://www.sciencedirect.com/science/article/pii/S0166218X14000080#s000025"""
        sol = defaultdict(lambda: -1)

        def can_place_block(i, j):
            for m in range(i, i - description[j - 1], -1):
                if row[m - 1] == '.':
                    return False
            if (j > 1) and row[i - description[j - 1] - 1] == '#':
                return False
            return True

        def solve(i, j):
            if i < 0 or j < 0:
                return 0
            elif i == j == 0:
                return 1
            if sol[(i, j)] != -1:
                return sol[(i, j)]
            else:
                sol[(i, j)] = 0
                if solve(i - 1, j) > 0 and row[i - 1] != '#':
                    sol[(i, j)] = sol[(i, j)] + solve(i - 1, j)
                if solve(i - description[j - 1] - (j > 1), j - 1) > 0 and can_place_block(i, j):
                    sol[(i, j)] = sol[(i, j)] + solve(i - description[j - 1] - (j > 1), j - 1)
            return sol[(i, j)]

        return solve(len(row), len(description))

    def part_one(self) -> int:
        return sum(self.possible_solutions(row, description)
                   for row, description in zip(self.rows, self.descriptions))

    def part_two(self) -> int:
        return 0


if __name__ == '__main__':
    with open('input.txt') as data:
        springs = Springs(data)
    print(springs.part_one())
