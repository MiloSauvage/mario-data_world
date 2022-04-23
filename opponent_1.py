import pygame


class Opponent_1:
    def __init__(self, image, pos_x, pos_y, player, tile_all, game):
        self.sheet = image
        self.player = player
        self.all_tile = tile_all
        self.game = game

        self.rect = self.sheet.get_rect()
        self.rect.width = 50
        self.rect.height = 50
        self.rect.x = pos_x
        self.rect.y = pos_y

        self.animation_list = []
        self.animation_step = [2, 5]
        self.action = 0
        self.cooldown = 200
        self.last_update = pygame.time.get_ticks()
        self.frame = 0
        self.step_counter = 0

        self.direction = pygame.math.Vector2()
        self.direction. y = 0
        self.direction.x = 1
        self.speed = 1
        self.gravity = 0.12

        self.death = 0

        self.attack_hitbox_right = pygame.Surface((5, 20))
        self.attack_hitbox_right.set_colorkey((0, 0, 0))
        self.attack_hitbox_right_rect = self.attack_hitbox_right.get_rect()

        self.attack_hitbox_left = pygame.Surface((5, 20))
        self.attack_hitbox_left.set_colorkey((0, 0, 0))
        self.attack_hitbox_left_rect = self.attack_hitbox_left.get_rect()


        for animation in self.animation_step:
            temp_animation_list = []
            for _ in range(animation):
                temp_animation_list.append(self.get_image(50, 50, self.step_counter, 1, (0, 0, 0)))
                self.step_counter += 1
            self.animation_list.append(temp_animation_list)

        #print(self.animation_list)

    def get_image(self, width, height, frame, scale, colour):
        image = pygame.Surface((width, height))
        image.blit(self.sheet, (0, 0), (0, (frame * height), width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)

        return image

    def update(self):
        self.attack_hitbox_right_rect.x = self.rect.x + 50
        self.attack_hitbox_right_rect.y = self.rect.y + 5
        self.attack_hitbox_left_rect.x = self.rect.x - 5
        self.attack_hitbox_left_rect.y = self.rect.y + 5

        self.check_direction()
        self.collide()
        self.move()

        self.horizontal_collision()
        #self.apply_gravity()
        #self.vertical_collision()

        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.cooldown:
            self.frame += 1
            self.last_update = current_time
        if self.frame >= len(self.animation_list[self.action]):
            self.frame = 0

    def horizontal_collision(self):
        #print(self.direction.x, self.direction.y)
        for tile in self.all_tile:
            if tile[1].colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = tile[1].right

                if self.direction.x > 0:
                    self.rect.right = tile[1].left

    def vertical_collision(self):
        for tile in self.all_tile:
            if tile[1].colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = tile[1].top
                    self.direction.y = 0


    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def move(self):
        self.rect.x += self.direction.x * self.speed

    def collide(self):
        self.step_death()
        if self.player.rect.colliderect(self.rect) and self.death == 0:
            self.player.health -= 0.05
        if self.player.attack_hitbox_right_rect.colliderect(self.rect) and self.player.attack:
            self.action = 1
        elif self.player.attack_hitbox_left_rect.colliderect(self.rect) and self.player.attack:
            self.action = 1
            if self.frame >= self.animation_step[self.action] - 1:
                self.death = 1

    def step_death(self):
        if self.action == 1:
            if self.frame >= self.animation_step[self.action] - 1:
                self.death = 1
                self.direction.x = 0

    def check_direction(self):
        for tile in self.all_tile:
            if tile[1].colliderect(self.attack_hitbox_right_rect):
                self.direction.x = -1
            if tile[1].colliderect(self.attack_hitbox_left_rect):
                self.direction.x = 1





