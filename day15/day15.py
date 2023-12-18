class Boxes:
    def __init__(self, data: str) -> None:
        self.strings: list[str] = data.strip().split(',')

    @staticmethod
    def hash(string) -> int:
        value = 0
        for c in string:
            value += ord(c)
            value *= 17
            value %= 256
        return value

    def part_one(self) -> int:
        return sum(self.hash(string) for string in self.strings)

    def part_two(self) -> int:
        boxes = [dict() for _ in range(256)]
        for string in self.strings:
            match string.split('='):
                case label, focal:
                    box = self.hash(label)
                    boxes[box][label] = int(focal)
                case _:
                    label = string.rstrip('-')
                    box = self.hash(label)
                    boxes[box].pop(label, None)
        return sum((i + 1) * (j + 1) * focal
                   for i, box in enumerate(boxes)
                   for j, focal in enumerate(box.values()))


if __name__ == '__main__':
    with open('input.txt') as data:
        boxes = Boxes(data.readline())
        print(boxes.part_one())
        print(boxes.part_two())
