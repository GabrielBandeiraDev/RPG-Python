import pygame
import config
from game_state import GameState

from game import Game
from menu import Menu

# iniciar pygame
pygame.init()

# iniciar display
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

pygame.display.set_caption("Rpg-Python")

clock = pygame.time.Clock()
# x = 50
# y = 50
# width = 50
# height = 50
# speed = 1000

game = Game(screen)

menu = Menu(screen, game)
game.set_up()
menu.set_up()

while game.game_state != GameState.ENDED:
    clock.tick(60)

    if game.game_state == GameState.NONE:
        menu.update()

    if game.game_state == GameState.RUNNING:
        game.update()

    pygame.display.flip()
