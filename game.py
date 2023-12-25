import random

import pygame
import config
import math
import utilities

from player import Player, NPC
from game_state import GameState, CurrentGameState
from monsterfactory import MonsterFactory
from game_view.map import Map
from game_view.battle import Battle

# Se for adicionar novo sprites como obstáculos coloque aqui
obstacles = ['J', 'K', 'L', 'Z', 'N', 'B', 'C', 'V', 'R', 'E', 'T', 'U', 'I', 'A', 'S', 'D', 'Q']


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = GameState.NONE
        self.current_game_state = CurrentGameState.MAP
        self.player_has_moved = False
        self.monster_factory = MonsterFactory()
        self.map = Map(screen)
        self.battle = None

    def set_up(self):
        player = Player(1, 1)
        npc = NPC(3, 8, "imgs/npc.png")
        self.player = player
        self.objects.append(player)
        self.objects.append(npc)
        print("configure")
        self.game_state = GameState.RUNNING

        self.map.load("01")

    def update(self):
        if self.current_game_state == CurrentGameState.MAP:
            self.player_has_moved = False
            self.screen.fill(config.BLACK)
            self.handle_events()

            self.map.render(self.screen, self.player, self.objects)

            if self.player_has_moved:
                self.determine_game_events()
        elif self.current_game_state == CurrentGameState.BATTLE:
            self.battle.update()
            self.battle.render()

            if self.battle.monster.health <= 0:
                self.current_game_state = CurrentGameState.MAP

    def determine_game_events(self):
        map_tile = self.map.map_array[self.player.position[1]][self.player.position[0]]
        print(map_tile)

        if map_tile == config.MAP_TILE_ROAD:
            return

        self.determine_pokemon_found(map_tile)

    def determine_pokemon_found(self, map_tile):
        random_number = utilities.generate_random_number(1, 10)

        if random_number <= 2:
            found_monster = self.monster_factory.create_monster(map_tile)
            print("you found a monster!")
            print("Monster Type: " + found_monster.type)
            print("Attack: " + str(found_monster.attack))
            print("Health: " + str(found_monster.health))

            self.battle = Battle(self.screen, found_monster, self.player)
            self.current_game_state = CurrentGameState.BATTLE

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

    def move_unit(self, unit, position_change):
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]

        if new_position[0] < 0 or new_position[0] > (len(self.map.map_array[0]) - 1):
            return

        if new_position[1] < 0 or new_position[1] > (len(self.map.map_array) - 1):
            return

        if self.map.map_array[new_position[1]][new_position[0]] == config.MAP_TILE_WATER:
            return

        self.player_has_moved = True

        unit.update_position(new_position)


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
