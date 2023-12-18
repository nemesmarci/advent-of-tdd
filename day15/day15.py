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
        return 0
