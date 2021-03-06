from pygame import *
import pygame
import os
import sys

MOVE_SPEED = 7
WIDTH = 150
HEIGHT = 150
COLOR =  "#888888"
def load_image(name, colorkey=None):
    fullname = os.path.join("sprites\images\Hero",name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Hero(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.time = 15 * 60
        self.condition = 0
        self.prev_cond = 0
        self.anim_time = 0
        self.live = 1
        self.x_speed = 0   #скорость перемещения
        self.startX = x # Начальная позиция Х
        self.startY = y
        self.image = load_image("Main_hero.png")
        self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
        self.rect = Rect(x, y, WIDTH-100, HEIGHT - 40)
        self.y_speed = 0 # скорость вертикального перемещения
        self.ground = False
        self.jump_power = 6
        self.gravity = 0.30
        self.shift_used = 0
        self.extra_jump = 0
        self.ground_time = 0
        self.picked_up = False
        self.walking = False
        self.shift_sound = False

    def update(self,  left, right, up, shift, platforms, crystals, enemies, exit):
        if self.time < 1 and self.condition != 6:
            self.condition = 5
            self.live = 0
            self.anim_time = 0
            self.time = 110
        if up and self.live == 1:
            if self.check_ground(platforms):
                self.y_speed = -self.jump_power
            if self.extra_jump > 0:
                self.y_speed = -self.jump_power
                self.extra_jump = 0


        if left and self.live == 1:
            if self.condition != 3:
                self.anim_time = 0
            if self.anim_time > 11:
                self.anim_time = 0
            self.condition = 3
            self.x_speed = MOVE_SPEED # Право = x + n
            self.image = load_image("Walking\Moving Forward_0" + str(self.anim_time) + ".png")
            self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
            self.image = pygame.transform.flip(self.image, True, False)
            self.x_speed = -MOVE_SPEED # Лево = x- n
            self.prev_cond = 3
            self.walking = True

        if right and self.live == 1:
            if self.condition != 1:
                self.anim_time = 0
            if self.anim_time > 11:
                self.anim_time = 0
            self.condition = 1
            self.prev_cond = 1
            self.x_speed = MOVE_SPEED # Право = x + n
            self.image = load_image("Walking\Moving Forward_0" + str(self.anim_time) + ".png")
            self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
            self.walking = True


        if not(left or right) and self.live == 1:
            if self.x_speed > 0:
                self.x_speed -= 1
            if self.x_speed < 0:
                self.x_speed += 1

            if self.condition == 1 or self.condition == 2:
                self.condition = 2
                if self.anim_time > 11:
                    self.anim_time = 0

                self.image = load_image("Walking\Moving Forward_0" + str(self.anim_time) + ".png")
                self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
            else:
                self.condition = 4
                if self.anim_time > 11:
                    self.anim_time = 0
                self.image = load_image("Walking\Moving Forward_0" + str(self.anim_time) + ".png")
                self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
                self.image = pygame.transform.flip(self.image, True, False)
        if not self.ground:
            self.y_speed += self.gravity

        if shift and self.live == 1 and self.shift_used == 0:
            self.shift_used = 100

        if self.shift_used > 80 and self.prev_cond == 1:
            self.x_speed = 21
            self.shift_sound = True

        if self.shift_used > 80 and self.prev_cond == 3:
            self.x_speed = -21
            self.shift_sound = True

        if self.condition == 5:
            if self.anim_time == 14:
                self.kill()
                self.anim_time = 0
                self.condition = 6
            self.x_speed = 0
            self.image = load_image("Dying\Dying_0" + str(self.anim_time) + ".png")
            if self.prev_cond == 3:
                self.image = pygame.transform.flip(self.image, True, False)
            self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))

        if self.condition == 6:
            self.image = Surface((0, 0))
            self.kill()

        if self.ground_time == 0:
            self.ground = False
        else:
            self.ground_time -= 1

        self.rect.y += self.y_speed
        self.collision_check(0, self.y_speed, platforms, crystals, enemies, exit)

        self.rect.x += self.x_speed
        self.collision_check(self.x_speed, 0, platforms, crystals, enemies, exit)

        self.rect.y += self.y_speed



    
    def collision_check(self, x_speed, y_speed, platforms, crystals, enemies, exit):
        for platform in platforms:
            if sprite.collide_rect(self, platform):

                if x_speed > 0:                
                    self.rect.right = platform.rect.left

                if x_speed < 0:
                    self.rect.left = platform.rect.right 

                if y_speed > 0:
                    self.rect.bottom = platform.rect.top
                    self.ground = True
                    self.y_speed = 0

                if y_speed < 0:
                    self.rect.top = platform.rect.bottom 
                    self.y_speed = 0

        for crystal in crystals:
            if sprite.collide_rect(self, crystal):
                self.time = 15 * 60
                self.extra_jump = 50
                crystal.kill()
                self.picked_up = True

        for enemie in enemies:
            if sprite.collide_rect(self, enemie) and self.live == 1:
                self.condition = 5
                self.live = 0
                self.anim_time = 0
                self.time = 110

        if sprite.collide_rect(self, exit) and self.live == 1:
            self.condition = 7
            self.x_speed = 0
            self.y_speed = 0
            self.live = 0

    def check_ground(self, platforms):
        self.rect.y += 1
        for platform in platforms:
            if sprite.collide_rect(self, platform):
                self.rect.y -= 1
                return True
        self.rect.y -= 1
        return False