import random

import pygame
import config
import math
import utilities

from player import Player
from game_state import GameState


class Menu:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game

    def set_up(self):
        self.menu_image = pygame.image.load("../imgs/menu.png")
        self.menu_image = pygame.transform.scale(self.menu_image, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

    def update(self):
        self.screen.fill(config.BLACK)
        rect = pygame.Rect(1, 1, 2, 2)
        self.screen.blit(self.menu_image, rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GameState.ENDED
                elif event.key in [pygame.K_RETURN, pygame.K_SPACE]:
                    self.game.set_up()
                    self.game.game_state = GameState.RUNNING
