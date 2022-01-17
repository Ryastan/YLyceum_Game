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
        self.gravity = 0.35

    def update(self,  left, right, up):
        if up and self.ground:
            self.y_speed = -self.jump_power
        if left:
            self.x_speed = -MOVE_SPEED # Лево = x- n
        elif right:
            self.x_speed = MOVE_SPEED # Право = x + n
        elif not(left or right): # стоим, когда нет указаний идти
            self.x_speed = 0
        self.rect.x += self.x_speed # переносим свои положение на xvel 

        if not self.ground:
            self.y_speed += self.gravity

        self.ground = False; # Мы не знаем, когда мы на земле((   
        self.rect.y += self.y_speed

    def draw(self, screen): # Выводим себя на экран
        screen.blit(self.image, (self.rect.x,self.rect.y))