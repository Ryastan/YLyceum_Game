import pygame
from pygame import *
from hero import Hero
from portal import Portal
from levels import Levels
from blocks import Platforms

run_game = True #
W, H = 600, 400 #Ширина и высота окна
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
hero = Hero(55, 55)#Класс героя

entities = pygame.sprite.Group() # Все объекты
platforms = [] #Все Платформы
entities.add(hero)

level1 = ["-------------------------",
          "-                       -",
          "-                       -",
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
    x = 0
    y = 0
    for row in level1: # вся строка
        for col in row: # каждый символ
            if col == "-":
                platform = Platforms(x,y, W//25, H//20, GREEN)
                entities.add(platform)
                platforms.append(platform)
            x += W//25 #блоки платформы ставятся на ширине блоков
        y += H//20    #то же самое и с высотой
        x = 0                   #на каждой новой строчке начинаемplatform нуля

    hero.update(left, right, up, platforms) # передвижение
    entities.draw(surface)

    pygame.display.update() 
    clock.tick(FPS)

pygame.quit()
