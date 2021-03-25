import sys
import pygame
import time

from project.objects.object_game import Game
from project import config

config_object = getattr(config, "MainConfig")


def terminate():
    pygame.quit()
    sys.exit()


def main(level_id):

    game = Game(level_id)
    screen = pygame.display.set_mode(game.get_size())
    pygame.display.set_caption("Tank Game")
    clock = pygame.time.Clock()

    game.start_game()

    while game.running:
        game.process_events()
        if not game.is_frozen and not game.is_ended:
            game.update_groups()
            screen.fill((0, 0, 0))
            game.draw_groups(screen)
            pygame.display.flip()

        clock.tick(config_object.fps)

    if game.is_ended:
        time.sleep(1)
        pygame.quit()


pygame.init()

if __name__ == "__main__":
    main(int(input("Choose level in range[1, 3]: ")))
