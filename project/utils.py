from project.objects.object_player import Player
from project.objects.object_tile import Tile
from project import config

config_object = getattr(config, "MainConfig")


def load_level(filename):
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(game, level):
    new_player, new_player_2 = None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile(game, 'empty', x, y)
            elif level[y][x] == '#':
                Tile(game, 'empty', x, y)
                Tile(game, 'stone', x, y)
            elif level[y][x] == '$':
                Tile(game, 'empty', x, y)
                Tile(game, 'brick', x, y)
            elif level[y][x] == '@':
                Tile(game, 'empty', x, y)
                new_player = Player(game, x, y)
            elif level[y][x] == '%':
                Tile(game, 'empty', x, y)
                new_player_2 = Player(game, x, y)
    return new_player, new_player_2


def generate_filename(level_id):
    return config_object.files_dir + "/" + config_object.level_basename + str(level_id) + ".txt"
