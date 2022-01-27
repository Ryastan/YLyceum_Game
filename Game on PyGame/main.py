import pygame
from pygame import *
from levels import Levels

W, H = 1500, 1000 #Ширина и высота окна
clock = pygame.time.Clock()
FPS = 60 #ФПС игры

#1500 / 25 = 60
#1000 / 20 = 50 Стандарт размеров блоков

level = Levels()
level.load_menu(W, H)