import re
from typing import Iterable, Any


class Module:
    def __init__(self, outputs) -> None:
        self.outputs: list[str] = outputs


class Broadcaster(Module):
    def __init__(self, outputs) -> None:
        super().__init__(outputs)

    def signals(self, input_signal, _) -> list[tuple[str, bool]]:
        return [(o, input_signal) for o in self.outputs]


class FlipFlop(Module):
    def __init__(self, outputs) -> None:
        super().__init__(outputs)
        self.state: bool = False

    def signals(self, input_signal, _) -> list[tuple[str, bool]]:
        if input_signal:
            return []
        else:
            self.state = not self.state
        return [(o, self.state) for o in self.outputs]


class Conjunction(Module):
    def __init__(self, outputs) -> None:
        super().__init__(outputs)
        self.inputs: dict[str, bool] = {}

    def signals(self, input_signal, source_module) -> list[tuple[str, bool]]:
        self.inputs[source_module] = input_signal
        output_signal = not all(self.inputs.values())
        return [(o, output_signal) for o in self.outputs]


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

    def add_inputs(self) -> None:
        for m, module in self.modules.items():
            if type(module) is Conjunction:
                for o, other in self.modules.items():
                    if m in other.outputs:
                        module.inputs[o] = False

    def part_one(self) -> int:
        return 0
