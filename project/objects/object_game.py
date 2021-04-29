import pygame

from project import config
from project.utils import load_level, generate_level, generate_filename
from project.objects.object_hpbar import HpBar
from project.objects.object_bullet import Bullet

config_object = getattr(config, "MainConfig")


class Game(object):
    game_object = None

    def __new__(cls, *args, **kwargs):
        # Singleton style
        if cls.game_object is None:
            cls.game_object = super(Game, cls).__new__(cls)
        return cls.game_object

    def __init__(self, level_id):
        self.all_sprites = pygame.sprite.Group()
        self.tiles_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.hp_bars = pygame.sprite.Group()

        self.level_init = load_level(generate_filename(level_id))
        self.size = len(self.level_init[0]) * config_object.tile_width, len(self.level_init) * config_object.tile_height

        self.tick = 0
        self.is_ended = False
        self.is_frozen = False
        self.running = False

        # Планирование будущих объектов.
        self.hp_1 = None
        self.hp_2 = None
        self.player = None
        self.player_2 = None

    def start_game(self):
        self.player, self.player_2 = generate_level(self, self.level_init)

        self.player.set_hpbar(HpBar(self, 1))
        self.player_2.set_hpbar(HpBar(self, 2))

        self.running = True

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.is_frozen = not self.is_frozen

            if not self.is_frozen and self.running:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    self.player.position = "Left"
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.player.position = "Right"
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.player.position = "Up"
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    self.player.position = "Down"

                if event.type == pygame.KEYUP and event.key == pygame.K_LEFT and self.player.position == "Left":
                    self.player.position = "Stop"
                if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT and self.player.position == "Right":
                    self.player.position = "Stop"
                if event.type == pygame.KEYUP and event.key == pygame.K_UP and self.player.position == "Up":
                    self.player.position = "Stop"
                if event.type == pygame.KEYUP and event.key == pygame.K_DOWN and self.player.position == "Down":
                    self.player.position = "Stop"

                if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    self.player_2.position = "Left"
                if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    self.player_2.position = "Right"
                if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                    self.player_2.position = "Up"
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    self.player_2.position = "Down"

                if event.type == pygame.KEYUP and event.key == pygame.K_a and self.player_2.position == "Left":
                    self.player_2.position = "Stop"
                if event.type == pygame.KEYUP and event.key == pygame.K_d and self.player_2.position == "Right":
                    self.player_2.position = "Stop"
                if event.type == pygame.KEYUP and event.key == pygame.K_w and self.player_2.position == "Up":
                    self.player_2.position = "Stop"
                if event.type == pygame.KEYUP and event.key == pygame.K_s and self.player_2.position == "Down":
                    self.player_2.position = "Stop"

                if event.type == pygame.MOUSEBUTTONDOWN:
                    Bullet(self, self.player)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    Bullet(self, self.player_2)

    def update_groups(self):
        self.player_group.update()
        self.bullet_group.update()

    def draw_groups(self, screen):
        self.tiles_group.draw(screen)
        self.player_group.draw(screen)
        self.bullet_group.draw(screen)
        self.hp_bars.draw(screen)

    def get_size(self):
        return self.size
