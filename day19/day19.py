import re
from typing import Iterable


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
        return 0


if __name__ == '__main__':
    with open('input.txt') as data:
        sorter = Sorter(data)
        print(sorter.part_one())
