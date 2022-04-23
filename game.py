import pygame

import opponent_1
from world import World
import player


class Game:
    def __init__(self, screen_width, screen_height):

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("World Data")

        self.background = pygame.image.load("bg.jpg")
        self.background = pygame.transform.scale(self.background, (screen_width, screen_height + 130))

        self.world = World(self)
        self.player_image = pygame.image.load("player.png")
        self.player = player.Player(self.player_image, 150, 550, self, self.world.tile_list, self.world.tile_list_damage, self.world.tile_list_support)

        self.opponent_1_image = pygame.image.load("opponent_1.png")
        self.opponent = opponent_1.Opponent_1(self.opponent_1_image, 600, 650, self.player, self.world.tile_all, self)


    def update(self):

        self.opponent.update()
        self.player.update()

    def display(self):

        self.screen.blit(self.background, (0, 0))
        self.world.draw()

        if self.opponent.death == 0:
            self.screen.blit(self.opponent.animation_list[self.opponent.action][self.opponent.frame], (self.opponent.rect.x, self.opponent.rect.y))
        self.screen.blit(self.player.animation_list[self.player.action][self.player.frame], (self.player.rect.x - 21, self.player.rect.y))
        #admin command
        #pygame.draw.rect(self.screen, (0, 0, 0), self.player.rect, 1)
        #pygame.draw.rect(self.screen, (0, 0, 0), self.opponent.rect, 1)
        #pygame.draw.rect(self.screen, (255, 255, 255), self.player.attack_hitbox_right_rect, 1)
        #pygame.draw.rect(self.screen, (255, 255, 255), self.player.attack_hitbox_left_rect, 1)
        #ygame.draw.rect(self.screen, (255, 255, 255), self.opponent.attack_hitbox_right_rect, 1)
        #pygame.draw.rect(self.screen, (255, 255, 255), self.opponent.attack_hitbox_left_rect, 1)

        self.player.health_display()
        self.player.set_hitbox()

        pygame.display.flip()

    def run(self):
        #print(self.world.tile_list)

        running = True

        while running:

            self.update()
            self.display()
            #print(self.player.frame)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c and self.player.action > 0:
                        self.player.action -= 1
                        self.player.frame = 0
                    if event.key == pygame.K_v and self.player.action < len(self.player.animation_list) - 1:
                        self.player.action += 1
                        self.player.frame = 0
                    if event.key == pygame.K_RIGHT and self.player.action < len(self.player.animation_list) - 1:
                        self.player.animation_cooldown = 150
                        self.player.action = 1
                        self.player.frame = 0
                        self.player.direction = "droite"
                    if event.key == pygame.K_LEFT and self.player.action < len(self.player.animation_list) - 1:
                        self.player.animation_cooldown = 150
                        self.player.action = 1
                        self.player.frame = 0
                        self.player.direction = "gauche"
                    if event.key == pygame.K_SPACE and self.player.action < len(self.player.animation_list) - 1 and self.player.direction == "gauche":
                        self.player.animation_cooldown = 200
                        self.player.action = 3
                        self.player.frame = 0
                    if event.key == pygame.K_SPACE and self.player.action < len(self.player.animation_list) - 1 and self.player.direction == "droite":
                        self.player.animation_cooldown = 200
                        self.player.action = 2
                        self.player.frame = 0
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        self.player.animation_cooldown = 300
                        self.player.action = 0
                        self.player.frame = 0
