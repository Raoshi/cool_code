import pygame as pg

class Button(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('i.webp')
        self.rect = self.image.get_rect()
        self.image = pg.transform.scale(self.image, (250, 100))
        self.rect = self.image.get_rect()
