import pygame
import scripts.config as config
import math
from scripts.game_state import GameState
import scripts.utilities as utilities


class Battle:
    def __init__(self, screen, monster, player):
        self.screen = screen
        self.monster = monster
        self.player = player

    def load(self):
        pass

    def render(self):
        self.screen.fill(config.WHITE)

        rect = pygame.Rect(1, 1, 2, 2)
        self.screen.blit(self.monster.image, rect)

        self.screen.blit(self.player.image, (320, 40))

        font = pygame.font.SysFont(None, 24)
        img = font.render("Vida: " + str(self.monster.health),
                          True, config.BLACK)
        self.screen.blit(img, (20, 120))

        img = font.render(f"Ataque: " + str(self.monster.attack), True, config.BLACK)
        self.screen.blit(img, (20, 140))

        img = font.render("Use ENTER para atacar!", True, config.BLACK)
        self.screen.blit(img, (20, 220))
        pass

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GameState.ENDED
                if event.key == pygame.K_RETURN:
                    self.monster.health = self.monster.health - 1  # Esse -1 é o ataque do player
