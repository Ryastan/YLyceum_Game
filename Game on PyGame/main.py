import pygame
from pygame import *
from hero import Hero
from portal import Portal
from levels import Levels
from blocks import Platforms
from booster import double_jump

run_game = True #
W, H = 900, 1000 #Ширина и высота окна
clock = pygame.time.Clock()
FPS = 60 #ФПС игры

# Цвета в RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

left = False
right = False
up = False
hero = Hero(550, 550)#Класс героя
entities = pygame.sprite.Group() # Все объекты
platforms = [] #Все Платформы
entities.add(hero)

level1 = ["-------------------------",
          "-                       -",
          "-     1                 -",
          "-               ------- -",
          "-            --         -",
          "-                       -",
          "--                      -",
          "-                       -",
          "-                   --- -",
          "-                       -",
          "-                       -",
          "-      ---              -",
          "-                       -",
          "-                       -",
          "-                       -",
          "-   -------      -      -",
          "-                       -",
          "-             -----------",
          "-                       -",
          "-------------------------"]

surface = pygame.display.set_mode((W, H))
pygame.display.set_caption('Game')

bg = Surface((W, H))
bg.fill(RED)
x = 0
y = 0
for row in level1:
    for col in row:
        if col == "-":
            platform = Platforms(x, y, W // 25, H // 20, GREEN)
            entities.add(platform)
            platforms.append(platform)
        if col == "1":
            dd = double_jump(BLACK)
            entities.add(dd)
            platforms.append(dd)
        x += W // 25
    y += H // 20
    x = 0

while run_game: #Главный цикл игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                left = True
            elif event.key == K_RIGHT:
                right = True
            elif event.key == K_UP:
                up = True
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                left = False
            elif event.key == K_RIGHT:
                right = False
            elif event.key == K_UP:
                up = False
    surface.blit(bg, (0, 0))



    hero.update(left, right, up, platforms) # передвижение
    entities.draw(surface)

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
