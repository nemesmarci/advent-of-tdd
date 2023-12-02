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
    def possible_set(set_):
        return all(n <= CubeGame.limits[color] for color, n in set_.items())
