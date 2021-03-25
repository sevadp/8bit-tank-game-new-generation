import pygame

from project import config

config_object = getattr(config, "MainConfig")


class Player(pygame.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y):
        self.game = game
        super().__init__(game.player_group, game.all_sprites)
        self.image = config_object.walkUp
        self.type = "player"
        self.position = "Stop"
        self.hp = 4
        self.hp_bar = None

        self.rect = self.image.get_rect().move(
            config_object.tile_width * pos_x + 15, config_object.tile_height * pos_y + 5)

    def set_hpbar(self, hp_bar):
        self.hp_bar = hp_bar

    def hit(self):
        self.hp -= 1
        self.hp_bar.update()

    def is_alive(self):
        return self.hp >= 1

    def update(self):

        if self.position == "Down":
            self.image = config_object.walkDown
            self.move(0, config_object.step)
        if self.position == "Up":
            self.image = config_object.walkUp
            self.move(0, -config_object.step)
        if self.position == "Right":
            self.image = config_object.walkRight
            self.move(config_object.step, 0)
        if self.position == "Left":
            self.image = config_object.walkLeft
            self.move(-config_object.step, 0)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        tiles = pygame.sprite.spritecollide(self, self.game.tiles_group, False)
        for obj in tiles:
            if obj.type == "stone" or obj.type == "brick":
                self.rect.x -= dx
                self.rect.y -= dy
                break

        players = pygame.sprite.spritecollide(self, self.game.player_group, False)
        for obj in players:
            if obj is not self:
                self.rect.x -= dx
                self.rect.y -= dy
                break
