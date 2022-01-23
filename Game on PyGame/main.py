import pygame
from pygame import *
from hero import Hero
from portal import Portal
from levels import Levels
from blocks import Platforms
from booster import coal

run_game = True #
W, H = 1500, 1000 #Ширина и высота окна
clock = pygame.time.Clock()
FPS = 60 #ФПС игры

# Цвета в RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#1500 / 25 = 60
#1000 / 20 = 50 Стандарт размеров блоков
level = Levels()
if level.load_menu(W, H) == "Yes":
    level1 = Levels()
    if level1.load(W, H, 1) == "Yes":
        level1 = Levels()
        if level1.load(W, H, 2) == "Yes":
            level1 = Levels()
            if level.load(W, H, 3) == "Yes":
                level1 = Levels()
                if level.load(W, H, 4) == "Yes":
                    level1 = Levels()
                    if level.load(W, H, 5) == "Yes":
                        level1 = Levels()
                        if level.load(W, H, 6) == "Yes":
                            pygame.quit()
else:
    pygame.quit()
