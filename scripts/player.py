import pygame
import config


class Player:
    def __init__(self, x_position, y_position):
        print("Jogador Criado")
        self.position = [x_position, y_position]
        self.image = pygame.image.load("../imgs/player.png")
        self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        self.rect = pygame.Rect(self.position[0] * config.SCALE, self.position[1] * config.SCALE, config.SCALE, config.SCALE)
        self.sprite = self.image

    def update(self):
        print("Jogador atualizado")

    def update_position(self, new_position):
        self.position[0] = new_position[0]
        self.position[1] = new_position[1]

    def render(self, screen, camera):
        self.rect = pygame.Rect(self.position[0] * config.SCALE - camera[0] * config.SCALE,
                                self.position[1] * config.SCALE - camera[1] * config.SCALE,
                                config.SCALE, config.SCALE)
        screen.blit(self.image, self.rect)
