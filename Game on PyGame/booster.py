from pygame import *


class double_jump(sprite.Sprite):
    def __init__(self, color):
        sprite.Sprite.__init__(self)
        self.image = Surface((10, 10))
        self.image.fill(color)
        self.rect = Rect(50, 60, 10, 10)
