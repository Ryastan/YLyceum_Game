from pygame import *


class coal(sprite.Sprite):
    def __init__(self, color):
        sprite.Sprite.__init__(self)
        self.image = Surface((10, 10))
        self.image.fill(color)
        self.rect = Rect(500, 100, 10, 10)
