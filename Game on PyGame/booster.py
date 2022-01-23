import pygame
from pygame import *
from hero import Hero
from portal import Portal
from blocks import Platforms
from blocks import Platforms1
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join("sprites\images\Blocks",name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

class coal(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = load_image("life_crystal.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = Rect(x, y, 50, 50)


class spike(sprite.Sprite):
    def __init__(self, x, y, floor = 0):
        sprite.Sprite.__init__(self)
        self.image = load_image("metal_spike.png")
        self.image = pygame.transform.scale(self.image, (60, 50))
        self.rect = Rect(x, y, 60, 50)
