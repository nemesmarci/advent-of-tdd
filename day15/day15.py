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
        return 0


if __name__ == '__main__':
    with open('input.txt') as data:
        boxes = Boxes(data.readline())
        print(boxes.part_one())
