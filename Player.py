from Common import *

class PlayerObject(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('ing.png')
        self.image = pg.transform.scale(self.image, (150, 100))
        self.rect = self.image.get_rect()

    def move_by_keys(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.top -= 3
        if keys[pg.K_s]:
            self.rect.top += 3
        if keys[pg.K_a]:
            self.rect.left -= 3
        if keys[pg.K_d]:
            self.rect.left += 3

    def update(self):
        self.move_by_keys()