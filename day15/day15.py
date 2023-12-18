class Boxes:
    def __init__(self, data: str) -> None:
        self.strings: list[str] = data.strip().split(',')

    @staticmethod
    def hash(string) -> int:
        return 0
