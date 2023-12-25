import pygame
import scripts.config as config
import math
import scripts.utilities as utilities


class Map:
    def __init__(self, screen):
        self.screen = screen
        self.map_array = []
        self.camera = [0, 0]
        self.map_tile_image = {
            "G": pygame.transform.scale(pygame.image.load("../imgs/grass1.png"), (config.SCALE, config.SCALE)),
            "W": pygame.transform.scale(pygame.image.load("../imgs/grass2.png"), (config.SCALE, config.SCALE)),
            "J": pygame.transform.scale(pygame.image.load("../imgs/grass3.png"), (config.SCALE, config.SCALE)),
            "K": pygame.transform.scale(pygame.image.load("../imgs/grass4.png"), (config.SCALE, config.SCALE)),
            "L": pygame.transform.scale(pygame.image.load("../imgs/grass5.png"), (config.SCALE, config.SCALE)),
            "Z": pygame.transform.scale(pygame.image.load("../imgs/grass6.png"), (config.SCALE, config.SCALE)),
            "X": pygame.transform.scale(pygame.image.load("../imgs/grass7.png"), (config.SCALE, config.SCALE)),
            "C": pygame.transform.scale(pygame.image.load("../imgs/grass8.png"), (config.SCALE, config.SCALE)),
            "V": pygame.transform.scale(pygame.image.load("../imgs/grass9.png"), (config.SCALE, config.SCALE)),
            "B": pygame.transform.scale(pygame.image.load("../imgs/grass10.png"), (config.SCALE, config.SCALE)),
            "N": pygame.transform.scale(pygame.image.load("../imgs/grass11.png"), (config.SCALE, config.SCALE)),
            "M": pygame.transform.scale(pygame.image.load("../imgs/grass12.png"), (config.SCALE, config.SCALE)),
            "Q": pygame.transform.scale(pygame.image.load("../imgs/grass27.png"), (config.SCALE, config.SCALE)),
            "R": pygame.transform.scale(pygame.image.load("../imgs/grass14.png"), (config.SCALE, config.SCALE)),
            "E": pygame.transform.scale(pygame.image.load("../imgs/grass15.png"), (config.SCALE, config.SCALE)),
            "T": pygame.transform.scale(pygame.image.load("../imgs/grass16.png"), (config.SCALE, config.SCALE)),
            "Y": pygame.transform.scale(pygame.image.load("../imgs/grass18.png"), (config.SCALE, config.SCALE)),
            "U": pygame.transform.scale(pygame.image.load("../imgs/grass17.png"), (config.SCALE, config.SCALE)),
            "I": pygame.transform.scale(pygame.image.load("../imgs/grass19.png"), (config.SCALE, config.SCALE)),
            "O": pygame.transform.scale(pygame.image.load("../imgs/grass22.png"), (config.SCALE, config.SCALE)),
            "P": pygame.transform.scale(pygame.image.load("../imgs/grass21.png"), (config.SCALE, config.SCALE)),
            "A": pygame.transform.scale(pygame.image.load("../imgs/grass24.png"), (config.SCALE, config.SCALE)),
            "S": pygame.transform.scale(pygame.image.load("../imgs/grass25.png"), (config.SCALE, config.SCALE)),
            "D": pygame.transform.scale(pygame.image.load("../imgs/grass26.png"), (config.SCALE, config.SCALE)),
            'w': pygame.transform.scale(pygame.image.load("../imgs/white.png"), (config.SCALE, config.SCALE)),
            'b': pygame.transform.scale(pygame.image.load("../imgs/black.png"), (config.SCALE, config.SCALE)),
            'g': pygame.transform.scale(pygame.image.load("../imgs/green.png"), (config.SCALE, config.SCALE)),
        }

    def load(self, file_name):
        self.map_array = []
        with open('../maps/' + file_name + ".txt") as map_file:
            for line in map_file:
                tiles = []
                for i in range(0, len(line) - 1, 2):
                    tiles.append(line[i])
                self.map_array.append(tiles)
            print(self.map_array)

    def render(self, screen, player, objects):
        self.determine_camera(player)

        y_pos = 0
        for line in self.map_array:
            x_pos = 0
            for tile in line:
                image = self.map_tile_image[tile]
                rect = pygame.Rect(x_pos * config.SCALE - (self.camera[0] * config.SCALE),
                                   y_pos * config.SCALE - (self.camera[1] * config.SCALE),
                                   config.SCALE, config.SCALE)
                screen.blit(image, rect)
                x_pos = x_pos + 1

            y_pos = y_pos + 1

        for object in objects:
            object.render(self.screen, self.camera)

    def determine_camera(self, player):

        # Camera em y
        max_y_position = len(self.map_array) - config.SCREEN_HEIGHT / config.SCALE

        y_position = player.position[1] - math.ceil(round(config.SCREEN_HEIGHT / config.SCALE) / 2)

        if 0 <= y_position <= max_y_position:
            self.camera[1] = y_position
        elif y_position < 0:
            self.camera[1] = 0
        else:
            self.camera[1] = max_y_position

        # Camera em x
        max_x_position = len(self.map_array[0]) - config.SCREEN_WIDTH / config.SCALE

        x_position = player.position[0] - math.ceil(round(config.SCREEN_WIDTH / config.SCALE) / 2)

        if 0 <= x_position <= max_x_position:
            self.camera[0] = x_position
        elif x_position < 0:
            self.camera[0] = 0
        else:
            self.camera[0] = max_x_position
