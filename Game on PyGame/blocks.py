from pygame import *

class Platforms(sprite.Sprite):
    def __init__(self, x, y, W, H, color):
        sprite.Sprite.__init__(self)
        self.image = Surface((W, H))
        self.image.fill(color)
        self.rect = Rect(x, y, W, H)
        