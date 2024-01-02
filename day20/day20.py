import re
from typing import Iterable, Any
from collections import deque
from dataclasses import dataclass
from itertools import count
from math import lcm


@dataclass
class Value:
    value: int


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
        low, high = Value(0), Value(0)
        for _ in range(1000):
            queue = deque([('broadcaster', False, 'button')])
            while queue:
                module, input_signal, source_module = queue.popleft()
                (high if input_signal else low).value += 1
                if module in self.modules:
                    for output, output_signal in self.modules[module].signals(input_signal, source_module):
                        queue.append((output, output_signal, module))
        return low.value * high.value

    def part_two(self) -> int:
        inputs = {ii: None for i in self.modules['rx'].inputs for ii in self.modules[i].inputs}
        for i in count(1):
            queue = deque([('broadcaster', False, 'button')])
            while queue:
                module, input_signal, source_module = queue.popleft()
                if module in inputs and not input_signal:
                    inputs[module] = i
                if all(inputs.values()):
                    return lcm(*(inputs.values()))
                if module in self.modules:
                    for output, output_signal in self.modules[module].signals(input_signal, source_module):
                        queue.append((output, output_signal, module))


if __name__ == "__main__":
    with open('input.txt') as data:
        machine = Machine(data)
        data.seek(0)
        machine2 = Machine(data)
    machine.add_inputs()
    print(machine.part_one())
    machine2.modules['rx'] = Conjunction([])
    machine2.add_inputs()
    print(machine2.part_two())
