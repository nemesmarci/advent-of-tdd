class BoatRace:
    def __init__(self, data) -> None:
        times, records = map(str.split, data)
        self.times = [int(t) for t in times[1:]]
        self.records = [int(r) for r in records[1:]]
