from util import exists
import re

CONFIG = {"red": 12, "blue": 14, "green": 13}


class Game:
    def __init__(self, id, sets) -> None:
        self.id = id
        self.sets = sets

    def is_valid(self):
        for play in self.sets:
            if "red" in play.keys():
                if play["red"] > CONFIG["red"]:
                    return False
            if "blue" in play.keys():
                if play["blue"] > CONFIG["blue"]:
                    return False
            if "green" in play.keys():
                if play["green"] > CONFIG["green"]:
                    return False
        return True

    def power(self):
        max_r = 0
        max_b = 0
        max_g = 0
        for play in self.sets:
            if "red" in play.keys():
                max_r = max(max_r, play["red"])
            if "blue" in play.keys():
                max_b = max(max_b, play["blue"])
            if "green" in play.keys():
                max_g = max(max_g, play["green"])

        print(f"max_r: {max_r} max_b: {max_b} max_g: {max_g}")
        return max_r * max_b * max_g


def parse(file_path):
    exists(file_path)
    games = []
    with open(file_path) as f:
        for line in f.readlines():
            game_id, sets = line.strip().split(":")
            # print(sets)
            sets = sets.strip().replace(" ", "").split(";")
            # print(sets)
            plays = []
            for set in sets:
                set = set.split(",")
                play = {}
                for cubes in set:
                    i = 0
                    num_cubes = ""
                    while cubes[i].isdigit():
                        num_cubes += cubes[i]
                        i += 1
                    color = cubes[i:]
                    play[color] = int(num_cubes)
                plays.append(play)
            # print(game_id.split(" ")[-1])
            games.append(Game(int(game_id.split(" ")[-1]), plays))
    return games


def part1(games):
    ids = []
    for game in games:
        if game.is_valid():
            ids.append(game.id)
    # print(ids)
    return sum(ids)


def part2(games):
    powers = []
    for game in games:
        powers.append(game.power())
    return sum(powers)


if __name__ == "__main__":
    # print(part1(parse("sample.txt")))
    print(part2(parse("data.txt")))
