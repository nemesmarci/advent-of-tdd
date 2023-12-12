from typing import Sequence
from itertools import cycle


class Map:
    def __init__(self, lines: Sequence[str]) -> None:
        self.instructions: str = lines[0].strip()
        self.nodes: dict[str, tuple[str, str]] = {}
        for line in lines[2:]:
            starting, left_right = line.strip().split(' = ')
            left, right = left_right.split(', ')
            left = left.strip('(')
            right = right.strip(')')
            self.nodes[starting] = (left, right)

    def step(self, node: str, instruction: str) -> str:
        return self.nodes[node][instruction == 'R']

    def traverse(self, start: str, end: str) -> int:
        instructions = cycle(self.instructions)
        steps = 0
        while start != end:
            steps += 1
            start = self.step(start, next(instructions))
        return steps

    def start_nodes(self) -> list[str]:
        return [node for node in self.nodes if node[-1] == 'A']

    def part_two(self) -> int:
        return 0


if __name__ == '__main__':
    with open('input.txt') as data:
        m = Map(data.readlines())
    print(m.traverse('AAA', 'ZZZ'))
