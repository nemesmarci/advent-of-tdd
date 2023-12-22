from typing import Iterable


class Sorter:
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
