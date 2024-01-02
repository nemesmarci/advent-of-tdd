import re
from typing import Iterable, Any


class Module:
    def __init__(self, outputs) -> None:
        self.outputs: list[str] = outputs


class Broadcaster(Module):
    def __init__(self, outputs) -> None:
        super().__init__(outputs)


class FlipFlop(Module):
    def __init__(self, outputs) -> None:
        super().__init__(outputs)
        self.state: bool = False


class Conjunction(Module):
    def __init__(self, outputs) -> None:
        super().__init__(outputs)
        self.inputs: dict[str, bool] = {}


class Machine:
    module_regex = re.compile(r'([%&])?(\w+) -> (.+)')

    def __init__(self, data: Iterable[str]) -> None:
        self.modules: dict[str, Any] = {}
        for line in map(str.strip, data):
            match self.module_regex.match(line).groups():
                case _, 'broadcaster' as module, outputs:
                    module_type = Broadcaster
                case '%', module, outputs:
                    module_type = FlipFlop
                case '&', module, outputs:
                    module_type = Conjunction
                case _:
                    raise ValueError(f'Cannot parse module `{line}`')
            self.modules[module] = module_type(outputs.split(', '))
