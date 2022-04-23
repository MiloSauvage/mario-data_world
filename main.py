import pygame
from game import Game

#settings
screen_width = 1000
screen_height = 800


if __name__ == '__main__':
    pygame.init()
    game = Game(screen_width, screen_height)
    game.run()

