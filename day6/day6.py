from math import prod

class BoatRace:
    def __init__(self, data) -> None:
        times, records = map(str.split, data)
        self.times = [int(t) for t in times[1:]]
        self.records = [int(r) for r in records[1:]]

    @staticmethod
    def win(time_charging: int, max_time: int, record: int) -> bool:
        return time_charging * (max_time - time_charging) > record

    @staticmethod
    def wins(max_time: int, record: int) -> int:
        num_wins = 0
        for time_charging in range(0, max_time + 1):
            if BoatRace.win(time_charging, max_time, record):
                num_wins += 1
        return num_wins

    def part_one(self) -> int:
        return prod(self.wins(time, record)
                    for time, record in zip(self.times, self.records))

    def part_two(self) -> int:
        return self.wins(int(''.join(map(str, self.times))),
                         int(''.join(map(str, self.records))))


if __name__ == '__main__':
    with open('input.txt') as data:
        race = BoatRace(data)
    print(race.part_one())
    print(race.part_two())
