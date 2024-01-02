import networkx
from typing import Iterable


class Components:
    def __init__(self, data: Iterable[str]) -> None:
        self.graph: networkx.Graph = networkx.Graph()
        for line in data:
            component, others = line.split(': ')
            for other in others.split():
                self.graph.add_edge(component, other)

    def part_one(self) -> int:
        cuts, (side1, side2) = networkx.algorithms.connectivity.stoerwagner.stoer_wagner(self.graph)
        assert cuts == 3
        return len(side1) * len(side2)


if __name__ == '__main__':
    with open('input.txt') as data:
        components = Components(data)
    print(components.part_one())
