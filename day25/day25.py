import networkx
from typing import Iterable


class Components:
    def __init__(self, data: Iterable[str]) -> None:
        self.graph: networkx.Graph = networkx.Graph()
        for line in data:
            component, others = line.split(': ')
            for other in others.split():
                self.graph.add_edge(component, other)
