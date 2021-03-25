import pygame

from project import config

config_object = getattr(config, "MainConfig")


class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, player):
        self.game = game
        self.player = player
        super().__init__(game.all_sprites, game.bullet_group)
        self.image = config_object.bullet_image
        self.move = None
        config_object.song_shoot.play()

        if player.image == config_object.walkDown:
            self.rect = self.image.get_rect().move(
                    player.rect.x + 16, player.rect.y + 50)
            self.move = "Down"
        elif player.image == config_object.walkRight:
            self.rect = self.image.get_rect().move(
                    player.rect.x + 50, player.rect.y + 16)
            self.move = "Right"
        elif player.image == config_object.walkLeft:
            self.rect = self.image.get_rect().move(
                    player.rect.x - 2, player.rect.y + 16)
            self.move = "Left"
        elif player.image == config_object.walkUp:
            self.rect = self.image.get_rect().move(
                    player.rect.x + 16, player.rect.y - 2)
            self.move = "Up"

    def update(self):
        if self.move == "Down":
            self.rect.y += config_object.move_bullet
        elif self.move == "Up":
            self.rect.y -= config_object.move_bullet
        elif self.move == "Right":
            self.rect.x += config_object.move_bullet
        elif self.move == "Left":
            self.rect.x -= config_object.move_bullet

        self.check()

    def check(self):
        tiles_objects = pygame.sprite.spritecollide(self, self.game.tiles_group, False)
        for obj in tiles_objects:
            if obj.type == "stone":
                self.rect.x = 250
                self.rect.y = 250
                self.kill()
                break
            elif obj.type == "brick":
                self.rect.x = 100000
                self.rect.y = 100000
                obj.kill()
                self.kill()
                break

        bullets = pygame.sprite.spritecollide(self, self.game.bullet_group, False)
        for obj in bullets:
            if obj is not self:
                self.kill()
                obj.kill()

        if self.alive():
            players = pygame.sprite.spritecollide(self, self.game.player_group, False)
            for obj in players:
                if obj is not self.player:
                    self.kill()
                    obj.hit()
                    if not obj.is_alive():
                        self.game.is_ended = True
                        self.game.running = False
                        config_object.song_death.play()
