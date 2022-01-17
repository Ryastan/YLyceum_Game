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
        self.rect = Rect(x, y, WIDTH, HEIGHT) # прямоугольный объект
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

        if not(left or right): # стоим, когда нет указаний идти
            self.x_speed = 0

        if not self.ground:
            self.y_speed += self.gravity
        
        self.ground = False; # Мы не знаем, когда мы на земле((   

        self.rect.y += self.y_speed
        self.collision_check(0, self.y_speed, platforms)

        self.rect.x += self.x_speed
        self.collision_check(self.x_speed, 0, platforms)

        self.rect.y += self.y_speed
    
    def collision_check(self, x_speed, y_speed, platforms):
        for platform in platforms:
            if sprite.collide_rect(self, platform): # если есть пересечение платформы с игроком

                if x_speed > 0:                      # если движется вправо
                    self.rect.right = platform.rect.left # то не движется вправо

                if x_speed < 0:                      # если движется влево
                    self.rect.left = platform.rect.right # то не движется влево

                if y_speed > 0:                      # если падает вниз
                    self.rect.bottom = platform.rect.top # то не падает вниз
                    self.ground = True          # и становится на что-то твердое
                    self.y_speed = 0                 # и энергия падения пропадает

                if y_speed < 0:                      # если движется вверх
                    self.rect.top = platform.rect.bottom # то не движется вверх
                    self.y_speed = 0                 # и энергия прыжка пропадает