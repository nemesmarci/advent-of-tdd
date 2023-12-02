from __future__ import annotations


class CubeGame:
    limits = dict(red=12, green=13, blue=14)

    @classmethod
    def parse(cls, line: str) -> CubeGame:
        game_str, sets_str = line.split(': ')
        game_id = int(game_str.split()[1])
        sets = []
        for set_str in sets_str.split('; '):
            dice = {}
            for die in set_str.split(', '):
                n, color = die.split(' ')
                dice[color] = int(n)
            sets.append(dice)
        return(CubeGame(id_=game_id, sets=sets))

    def __init__(self, id_: int,
                 sets: list[dict[str, int]]) -> None:
        self.id = id_
        self.sets = sets

    @staticmethod
    def possible_set(set_: dict) -> bool:
        return all(n <= CubeGame.limits[color] for color, n in set_.items())

    def possible_game(self) -> bool:
        return all(self.possible_set(set_) for set_ in self.sets)

    def min_cubes(self) -> dict:
        min_cubes = dict(red=0, green=0, blue=0)
        for set_ in self.sets:
            for color, n in set_.items():
                if n > min_cubes[color]:
                    min_cubes[color] = n
        return min_cubes


class Day2:
    def __init__(self, data: list) -> None:
        self.games = [CubeGame.parse(line.strip()) for line in data]

    def part_one(self):
        return sum(game.id for game in self.games if game.possible_game())


if __name__ == '__main__':
    with open('input.txt') as data:
        day2 = Day2(data)
        print(day2.part_one())
