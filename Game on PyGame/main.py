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

level = Levels()
if level.load_menu(W, H) == "Yes":
    level1 = Levels()
    level1.load(W, H, 1)
else:
    pygame.quit()
