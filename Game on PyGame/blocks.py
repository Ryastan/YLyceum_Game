from pygame import *
import os
import sys
import pygame

def load_image(name, colorkey=None):
    fullname = os.path.join("sprites/images/Blocks",name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

class Platforms(sprite.Sprite):
    def __init__(self, x, y, W, H, color):
        sprite.Sprite.__init__(self)
        self.image = load_image("block_grass.png")
        self.image = pygame.transform.scale(self.image, (W, H))
        self.rect = Rect(x, y, W, H)
        