from typing import Iterable


class Storm:
    def __init__(self, data: Iterable[str]) -> None:
        self.hails: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
        for line in map(str.strip, data):
            pos, vel = line.split(' @ ')
            self.hails.append((tuple(map(int, pos.split(', '))), tuple(map(int, vel.split(', ')))))

    def part_one(self, low: int, high: int) -> int:
        intersections = 0
        for i, ((x1, y1, _), (u1, v1, _)) in enumerate(self.hails):
            for ((x2, y2, _), (u2, v2, _)) in self.hails[i+1:]:
                try:
                    m1, m2 = v1 / u1, v2 / u2
                    b1, b2 = y1 - m1 * x1, y2 - m2 * x2
                    y = (b1 * m2 - b2 * m1) / (m2 - m1)
                    x = (y - b2) / m2
                    if (low <= x <= high and low <= y <= high and
                            (u1 < 0 and x < x1 or u1 > 0 and x > x1) and
                            (u2 < 0 and x < x2 or u2 > 0 and x > x2) and
                            (v1 < 0 and y < y1 or v1 > 0 and y > y1) and
                            (v2 < 0 and y < y2 or v2 > 0 and y > y2)):
                        intersections += 1
                except ZeroDivisionError:
                    pass
        return intersections


if __name__ == '__main__':
    with open('input.txt') as data:
        storm = Storm(data)
    print(storm.part_one(200000000000000, 400000000000000))
