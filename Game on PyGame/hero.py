from pygame import *

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR =  "#888888"


class Hero(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.x_speed = 0   #скорость перемещения
        self.startX = x # Начальная позиция Х
        self.startY = y
        self.image = Surface((WIDTH,HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.y_speed = 0 # скорость вертикального перемещения
        self.ground = False
        self.jump_power = 10
        self.gravity = 0.30

    def update(self,  left, right, up, platforms):

        if up:
            if self.ground:
                self.y_speed = -self.jump_power

        if left:
            self.x_speed = -MOVE_SPEED # Лево = x- n

        if right:
            self.x_speed = MOVE_SPEED # Право = x + n

        if not(left or right):
            self.x_speed = 0

        if not self.ground:
            self.y_speed += self.gravity
        
        self.ground = False  

        self.rect.y += self.y_speed
        self.collision_check(0, self.y_speed, platforms)

        self.rect.x += self.x_speed
        self.collision_check(self.x_speed, 0, platforms)

        self.rect.y += self.y_speed
    
    def collision_check(self, x_speed, y_speed, platforms):
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