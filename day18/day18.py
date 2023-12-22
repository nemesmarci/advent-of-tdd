from typing import Iterable
from shapely import Polygon


class Lagoon:
    def __init__(self, data: Iterable[str], swap: bool) -> None:
        self.directions: list[str] = []
        self.lengths: list[int] = []
        for line in data:
            direction, length, colour = line.strip().split()
            if swap:
                direction = 'RDLU'[int(colour[-2])]
                length = int(colour[2:-2], 16)
            self.directions.append(direction)
            self.lengths.append(int(length))

    def perimeter(self) -> int:
        return sum(self.lengths)

    def area(self) -> int:
        corners = []
        y, x = 0, 0
        for direction, length in zip(self.directions, self.lengths):
            match direction:
                case 'U':
                    y -= length
                case 'D':
                    y += length
                case 'L':
                    x -= length
                case 'R':
                    x += length
            corners.append((y, x))
        return int(Polygon(corners).area) + self.perimeter() // 2 + 1


if __name__ == '__main__':
    with open('input.txt') as data:
        lagoon = Lagoon(data, False)
        print(lagoon.area())
        data.seek(0)
        lagoon = Lagoon(data, True)
        print(lagoon.area())
