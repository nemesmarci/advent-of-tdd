from typing import Iterable, Any


class Machine:
    def __init__(self, data: Iterable[str]) -> None:
        self.modules: dict[str, Any] = {}
