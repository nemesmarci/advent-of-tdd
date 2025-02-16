from typing import Sequence, Callable
from itertools import cycle
from math import lcm


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

    def traverse(self, start: str, end: Callable[[str], bool]) -> int:
        instructions = cycle(self.instructions)
        steps = 0
        while not(end(start)):
            steps += 1
            start = self.step(start, next(instructions))
        return steps

    def start_nodes(self) -> list[str]:
        return [node for node in self.nodes if node[-1] == 'A']

    def part_two(self) -> int:
        steps_taken = [self.traverse(node, lambda x: x[-1] == 'Z')
                       for node in self.start_nodes()]
        return lcm(*steps_taken)


if __name__ == '__main__':
    with open('input.txt') as data:
        m = Map(data.readlines())
    print(m.traverse('AAA', lambda x: x == 'ZZZ'))
    print(m.part_two())
