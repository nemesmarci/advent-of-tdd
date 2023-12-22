import re
from typing import Iterable
from collections import deque
from math import prod


class Sorter:
    rule_regex = re.compile(r'(\w+)([<>]?)(\d*):?(\w*)')

    def __init__(self, data: Iterable[str]) -> None:
        self.workflows: dict[str, list[str]] = {}
        self.parts: list[dict[str, int]] = []
        raw_workflows, raw_parts = ''.join(data).split('\n\n')
        for workflow in raw_workflows.split('\n'):
            name, steps = workflow.replace('}', '').split('{')
            self.workflows[name] = steps.split(',')
        x, m, a, s = 'x', 'm', 'a', 's'
        for part in raw_parts[:-1].split('\n'):
            self.parts.append(eval(part.replace('=', ':')))

    def part_one(self) -> int:
        xmas = 0
        for part in self.parts:
            step = 'in'
            while True:
                if step == 'A':
                    xmas += sum(part.values())
                    break
                elif step == 'R':
                    break
                for rule in self.workflows[step]:
                    match self.rule_regex.match(rule).groups():
                        case field, '<' | '>' as op, value, step:
                            if eval(f'part[field] {op} int(value)'):
                                break
                        case step, *_:
                            pass
        return xmas

    def part_two(self) -> int:
        queue = deque([('in', [])])
        accepted = []
        while queue:
            step, conditions = queue.popleft()
            if step == 'A':
                accepted.append(conditions)
                continue
            if step == 'R':
                continue
            for i, rule in enumerate(self.workflows[step]):
                if failed := self.workflows[step][:i]:
                    for f in failed:
                        match self.rule_regex.match(f).groups():
                            case field, '<', value, _:
                                value = int(value)
                                conditions.append(f'{field}>{value - 1}')
                            case field, '>', value, _:
                                value = int(value)
                                conditions.append(f'{field}<{value + 1}')
                match self.rule_regex.match(rule).groups():
                    case field, ('<' | '>') as op, value, str(next_step):
                        queue.append((next_step, conditions + [f'{field}{op}{value}']))
                    case next_step, *_:
                        queue.append((next_step, conditions))

        xmas = 0
        for rules in accepted:
            bounds = {b: range(1, 4001) for b in 'xmas'}
            for rule in rules:
                match self.rule_regex.match(rule).groups():
                    case field, '<', value, _:
                        bounds[field] = range(bounds[field].start, min(int(value), bounds[field].stop))
                    case field, '>', value, _:
                        bounds[field] = range(max(int(value) + 1, bounds[field].start), bounds[field].stop)
            xmas += prod(len(b) for b in bounds.values())
        return xmas


if __name__ == '__main__':
    with open('input.txt') as data:
        sorter = Sorter(data)
        print(sorter.part_one())
        print(sorter.part_two())
