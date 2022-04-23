import pygame


class Player:
    def __init__(self, image, pos_x, pos_y, game, tile_collision, tile_damage, tile_support):
        self.game = game
        self.tile_collision = tile_collision
        self.tile_damage = tile_damage
        self.tile_support = tile_support

        self.sheet = image
        self.rect = self.sheet.get_rect()
        self.rect.width = 50
        self.rect.height = 100
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.velocity = pygame.math.Vector2()
        self.speed = 2
        self.gravity = 0.12
        self.jump_speed = 4.6
        self.health_max = 50
        self.health = self.health_max
        self.on_floor = False

        self.direction = "droite"
        self.attack = False

        self.size = 24
        self.transparent = (0, 0, 0)

        self.animation_list = []
        self.animation_steps = [3, 3, 4, 4, 5]
        self.action = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 300
        self.frame = 0
        self.step_counter = 0

        self.attack_hitbox_right = pygame.Surface((20, 50))
        self.attack_hitbox_right.set_colorkey((0, 0, 0))
        self.attack_hitbox_right_rect = self.attack_hitbox_right.get_rect()

        self.attack_hitbox_left = pygame.Surface((20, 50))
        self.attack_hitbox_left.set_colorkey((0, 0, 0))
        self.attack_hitbox_left_rect = self.attack_hitbox_left.get_rect()

        for animation in self.animation_steps:
            temp_img_list = []
            for _ in range(animation):
                temp_img_list.append(self.get_image(self.step_counter, 24, 24, 4.2, self.transparent))
                self.step_counter += 1
            self.animation_list.append(temp_img_list)

    def get_image(self, frame, width, height, scale, colour):
        image = pygame.Surface((width, height))
        image.blit(self.sheet, (0, 0), (0, (frame * height), width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)

        return image

    def horizontal_collision(self):
        for tile in self.tile_collision:
            if tile[1].colliderect(self.rect):
                if self.velocity.x < 0:
                    self.rect.left = tile[1].right
                if self.velocity.x > 0:
                    self.rect.right = tile[1].left
        for tile in self.tile_damage:
            if tile[1].colliderect(self.rect):
                if self.velocity.x < 0:
                    self.rect.left = tile[1].right
                if self.velocity.x > 0:
                    self.rect.right = tile[1].left

    def vertical_collision(self):
        for tile in self.tile_collision:
            if tile[1].colliderect(self.rect):
                if self.velocity.y > 0:
                    self.rect.bottom = tile[1].top
                    self.velocity.y = 0
                    self.on_floor = True
                if self.velocity.y < 0:
                    self.rect.top = tile[1].bottom
        for tile in self.tile_damage:
            if tile[1].colliderect(self.rect):
                if self.velocity.y > 0:
                    self.rect.bottom = tile[1].top
                    self.velocity.y = 0
                    self.on_floor = True
                    self.health -= 1
                if self.velocity.y < 0:
                    self.rect.top = tile[1].bottom
                    self.health -= 1
        for tile in self.tile_support:
            if tile[1].colliderect(self.rect) and self.velocity.y > 0:
                if self.rect.y < tile[1][1] - 90:
                    self.rect.bottom = tile[1].top
                    self.velocity.y = 0
                    self.on_floor = True

        if self.on_floor and self.velocity.y != 0:
            self.on_floor = False

    def input(self):

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            self.velocity.x = 1
        elif pressed[pygame.K_LEFT]:
            self.velocity.x = -1
        else:
            self.velocity.x = 0

        if pressed[pygame.K_UP] and self.on_floor:
            self.velocity.y = -self.jump_speed

    def update(self):
        self.attack_hitbox_right_rect.x = self.rect.x + 50
        self.attack_hitbox_right_rect.y = self.rect.y + 25
        self.attack_hitbox_left_rect.x = self.rect.x - 20
        self.attack_hitbox_left_rect.y = self.rect.y + 25

        self.input()

        self.move()

        self.horizontal_collision()
        self.apply_gravity()
        self.vertical_collision()

        self.check_attack()

        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = current_time
            if self.frame >= len(self.animation_list[self.action]):
                self.frame = 0

    def move(self):
        self.rect.x += self.velocity.x * self.speed

    def apply_gravity(self):
        self.velocity.y += self.gravity
        self.rect.y += self.velocity.y

    def check_attack(self):
        if self.action == 2 or self.action == 3:

            #print(self.frame, self.animation_steps[self.action] - 1)
            if self.frame >= self.animation_steps[self.action] - 1:
                self.action = 0
                self.frame = 0
                if self.action == 0:
                    self.attack = False
            else:
                self.attack = True
        else:
            self.attack = False

    def set_hitbox(self):
        if self.attack and self.action == 2:
            self.game.screen.blit(self.attack_hitbox_right, (self.rect.x + 50, self.rect.y + 25))
        if self.attack and self.action == 3:
            self.game.screen.blit(self.attack_hitbox_left, (self.rect.x - 20, self.rect.y + 25))

    def health_display(self):
        pygame.draw.rect(self.game.screen, (60, 63, 60), [self.rect.x, self.rect.y - 20, self.health_max, 5])
        pygame.draw.rect(self.game.screen, (111, 206, 46), [self.rect.x, self.rect.y - 20, self.health, 5])










