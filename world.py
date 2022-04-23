import pygame


class World:
    def __init__(self, game):
        self.game = game

        self.cloud_tile = pygame.image.load("cloud_tile.png")
        self.rock_tile = pygame.image.load("rock_tile.png")
        self.support_tile = pygame.image.load("support_tile.png")
        self.dirt_tile = pygame.image.load("dirt_tile.png")
        self.grass_tile = pygame.image.load("grass_tile.png")
        self.spike_tile = pygame.image.load("spike_tile.png")
        self.spike_ceiling_tile = pygame.image.load("spike_ceiling_tile.png")

        self.tile_size = 50

        self.wold_data = [
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 6, 5, 5, 5],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 4, 4, 4, 4, 4, 4],
            [0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 7, 7, 4, 4],
            [5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [7, 7, 7, 4, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 4, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [5, 5, 5, 5, 5, 0, 0, 0, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [4, 4, 4, 4, 4, 6, 6, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            [4, 4, 4, 4, 4, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        ]

        self.tile_all = []
        self.tile_list = []
        self.tile_list_damage = []
        self.tile_list_support = []

        row_count = 0
        for row in self.wold_data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = self.cloud_tile
                    img = pygame.transform.scale(img, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = row_count * self.tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                    self.tile_all.append(tile)
                if tile == 2:
                    img = self.rock_tile
                    img = pygame.transform.scale(img, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = row_count * self.tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                    self.tile_all.append(tile)
                if tile == 3:
                    img = self.support_tile
                    img = pygame.transform.scale(img, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = row_count * self.tile_size
                    img_rect.height = (img_rect.height / 2) - 8
                    tile = (img, img_rect)
                    self.tile_list_support.append(tile)
                    self.tile_all.append(tile)
                if tile == 4:
                    img = self.dirt_tile
                    img = pygame.transform.scale(img, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = row_count * self.tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                    self.tile_all.append(tile)
                if tile == 5:
                    img = self.grass_tile
                    img = pygame.transform.scale(img, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = row_count * self.tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                    self.tile_all.append(tile)
                if tile == 6:
                    img = self.spike_tile
                    img = pygame.transform.scale(img, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = row_count * self.tile_size
                    tile = (img, img_rect)
                    self.tile_list_damage.append(tile)
                    self.tile_all.append(tile)
                if tile == 7:
                    img = self.spike_ceiling_tile
                    img = pygame.transform.scale(img, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = row_count * self.tile_size
                    tile = (img, img_rect)
                    self.tile_list_damage.append(tile)
                    self.tile_all.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            self.game.screen.blit(tile[0], tile[1])
        for tile in self.tile_list_damage:
            self.game.screen.blit(tile[0], tile[1])

        for tile in self.tile_list_support:
            self.game.screen.blit(tile[0], tile[1])

        #admin command
            pygame.draw.rect(self.game.screen, (0, 0, 0), tile[1], 2)
