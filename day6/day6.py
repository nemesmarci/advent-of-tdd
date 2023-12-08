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
        return 0
