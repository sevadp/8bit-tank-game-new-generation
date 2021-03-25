import pygame

from project import config

config_object = getattr(config, "MainConfig")


class Tile(pygame.sprite.Sprite):
    def __init__(self, game, tile_type, pos_x, pos_y):
        self.game = game
        super().__init__(game.tiles_group, game.all_sprites)
        self.image = config_object.tile_images[tile_type]
        self.type = tile_type
        self.rect = self.image.get_rect().move(
            config_object.tile_width * pos_x, config_object.tile_height * pos_y)
