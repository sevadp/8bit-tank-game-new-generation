import pygame


class MainConfig(object):
    """Production configuration."""
    walkRight = pygame.image.load("assets/64_r.png")
    walkLeft = pygame.image.load("assets/64_l.png")
    walkUp = pygame.image.load("assets/64.png")
    walkDown = pygame.image.load("assets/64_d.png")

    hp0 = pygame.image.load("assets/0.png")
    hp1 = pygame.image.load("assets/1.png")
    hp2 = pygame.image.load("assets/2.png")
    hp3 = pygame.image.load("assets/3.png")
    hp4 = pygame.image.load("assets/4.png")
    hp0_2 = pygame.image.load("assets/00.png")
    hp1_2 = pygame.image.load("assets/01.png")
    hp2_2 = pygame.image.load("assets/02.png")
    hp3_2 = pygame.image.load("assets/03.png")
    hp4_2 = pygame.image.load("assets/04.png")

    tile_images = {"stone": pygame.image.load("assets/cant_lomatsa.png"),
                   "empty": pygame.image.load("assets/listva.png"),
                   "brick": pygame.image.load("assets/brick_comp.png")}

    bullet_image = pygame.image.load("assets/16x16bullet.png")

    song_death = pygame.mixer.Sound('assets/Audio/enemy_destroy.wav')
    song_engine = pygame.mixer.Sound('assets/Audio/tank_engine.wav')
    song_shoot = pygame.mixer.Sound('assets/Audio/regular_shoot.wav')

    step = 3
    move_bullet = 9
    is_stopped = False
    tile_width = tile_height = 64
