import networkx
from typing import Iterable


class Components:
    def __init__(self, data: Iterable[str]) -> None:
        self.graph: networkx.Graph = networkx.Graph()
