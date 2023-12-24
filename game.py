import pygame
import math
from player import Player, NPC
import config
from game_state import GameState


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = GameState.NONE
        self.map = []
        self.camera = [0, 0]

    def set_up(self):
        player = Player(1, 1)
        npc = NPC(3, 8, "imgs/npc.png")
        self.player = player
        self.objects.append(player)
        self.objects.append(npc)
        print("configure")
        self.game_state = GameState.RUNNING

        self.load_map("01")

    def update(self):
        self.screen.fill(config.BLACK)
        print("atualizando")
        self.handle_events()

        self.render_map(self.screen)

        for game_object in self.objects:
            game_object.update()

        for game_object in self.objects:
            game_object.render(self.screen, self.camera)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.ENDED
                elif event.key == pygame.K_w:
                    self.move_unit(self.player, [0, -1])
                elif event.key == pygame.K_s:
                    self.move_unit(self.player, [0, 1])
                elif event.key == pygame.K_a:
                    self.move_unit(self.player, [-1, 0])
                elif event.key == pygame.K_d:
                    self.move_unit(self.player, [1, 0])

    def load_map(self, file_name):
        with open('maps/' + file_name + ".txt") as map_file:
            for line in map_file:
                tiles = []

                for i in range(0, len(line) - 1, 2):
                    tiles.append(line[i])
                self.map.append(tiles)
        print(self.map)

    def render_map(self, screen):
        self.determine_camera()

        y_pos = 0
        for line in self.map:
            x_pos = 0
            for tile in line:
                image = map_tile_image[tile]
                rect = pygame.Rect(x_pos * config.SCALE, y_pos * config.SCALE - (self.camera[1] * config.SCALE),
                                   config.SCALE, config.SCALE)
                screen.blit(image, rect)
                x_pos = x_pos + 1

            y_pos = y_pos + 1

    def move_unit(self, unit, position_change):
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]

        if 0 <= new_position[0] < len(self.map[0]) and 0 <= new_position[1] < len(self.map):
            if self.map[new_position[1]][new_position[0]] != "U":
                unit.update_position(new_position)

    def determine_camera(self):
        max_y_position = len(self.map) - config.SCREEN_HEIGHT / config.SCALE

        y_position = self.player.position[1] - math.ceil(round(config.SCREEN_HEIGHT / config.SCALE) / 2)

        if 0 <= y_position <= max_y_position:
            self.camera[1] = y_position
        elif y_position < 0:
            self.camera[1] = 0
        else:
            self.camera[1] = max_y_position


map_tile_image = {
    "G": pygame.transform.scale(pygame.image.load("imgs/grass1.png"), (config.SCALE, config.SCALE)),
    "W": pygame.transform.scale(pygame.image.load("imgs/grass2.png"), (config.SCALE, config.SCALE)),
    "J": pygame.transform.scale(pygame.image.load("imgs/grass3.png"), (config.SCALE, config.SCALE)),
    "K": pygame.transform.scale(pygame.image.load("imgs/grass4.png"), (config.SCALE, config.SCALE)),
    "L": pygame.transform.scale(pygame.image.load("imgs/grass5.png"), (config.SCALE, config.SCALE)),
    "Z": pygame.transform.scale(pygame.image.load("imgs/grass6.png"), (config.SCALE, config.SCALE)),
    "X": pygame.transform.scale(pygame.image.load("imgs/grass7.png"), (config.SCALE, config.SCALE)),
    "C": pygame.transform.scale(pygame.image.load("imgs/grass8.png"), (config.SCALE, config.SCALE)),
    "V": pygame.transform.scale(pygame.image.load("imgs/grass9.png"), (config.SCALE, config.SCALE)),
    "B": pygame.transform.scale(pygame.image.load("imgs/grass10.png"), (config.SCALE, config.SCALE)),
    "N": pygame.transform.scale(pygame.image.load("imgs/grass11.png"), (config.SCALE, config.SCALE)),
    "M": pygame.transform.scale(pygame.image.load("imgs/grass12.png"), (config.SCALE, config.SCALE)),
    "Q": pygame.transform.scale(pygame.image.load("imgs/grass27.png"), (config.SCALE, config.SCALE)),
    "R": pygame.transform.scale(pygame.image.load("imgs/grass14.png"), (config.SCALE, config.SCALE)),
    "E": pygame.transform.scale(pygame.image.load("imgs/grass15.png"), (config.SCALE, config.SCALE)),
    "T": pygame.transform.scale(pygame.image.load("imgs/grass16.png"), (config.SCALE, config.SCALE)),
    "Y": pygame.transform.scale(pygame.image.load("imgs/grass18.png"), (config.SCALE, config.SCALE)),
    "U": pygame.transform.scale(pygame.image.load("imgs/grass17.png"), (config.SCALE, config.SCALE)),
    "I": pygame.transform.scale(pygame.image.load("imgs/grass19.png"), (config.SCALE, config.SCALE)),
    "O": pygame.transform.scale(pygame.image.load("imgs/grass22.png"), (config.SCALE, config.SCALE)),
    "P": pygame.transform.scale(pygame.image.load("imgs/grass21.png"), (config.SCALE, config.SCALE)),
    "A": pygame.transform.scale(pygame.image.load("imgs/grass24.png"), (config.SCALE, config.SCALE)),
    "S": pygame.transform.scale(pygame.image.load("imgs/grass25.png"), (config.SCALE, config.SCALE)),
    "D": pygame.transform.scale(pygame.image.load("imgs/grass26.png"), (config.SCALE, config.SCALE))
}
