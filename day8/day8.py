from typing import Sequence


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
        return ''
