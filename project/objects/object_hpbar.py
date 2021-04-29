import pygame

from project import config

config_object = getattr(config, "MainConfig")


class HpBar(pygame.sprite.Sprite):
    def __init__(self, game, type_hpbar):
        self.game = game
        super().__init__(game.hp_bars)
        self.type = type_hpbar
        self.image = None
        self.rect = None

        self.set_image()
        self.move_rect()

    def set_image(self):
        if self.type == 1:
            self.image = config_object.hp4
        else:
            self.image = config_object.hp4_2

    def move_rect(self):
        if self.type == 1:
            self.rect = self.image.get_rect().move(0, 0)
        elif self.type == 2:
            self.rect = self.image.get_rect().move(self.game.get_size()[0] - 216, 0)

    def update(self):
        if self.type == 1:
            if self.image == config_object.hp4:
                self.image = config_object.hp3
            elif self.image == config_object.hp3:
                self.image = config_object.hp2
            elif self.image == config_object.hp2:
                self.image = config_object.hp1
            elif self.image == config_object.hp1:
                self.image = config_object.hp0
        elif self.type == 2:
            if self.image == config_object.hp4_2:
                self.image = config_object.hp3_2
            elif self.image == config_object.hp3_2:
                self.image = config_object.hp2_2
            elif self.image == config_object.hp2_2:
                self.image = config_object.hp1_2
            elif self.image == config_object.hp1_2:
                self.image = config_object.hp0_2
