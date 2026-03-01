import random

import pygame as pg

pg.init()
W,H = 600, 600
win = pg.display.set_mode((W, H))

def load_image(name):
    img = pg.image.load(name)
    img = img.convert_alpha()
    colorkey = img.get_at((0, 0))
    img.set_colorkey(colorkey)
    return img

class inginirium(pg.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image('ing.png')
        self.image = pg.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(W)
        self.rect.y = random.randrange(H)
    def update(self):
        self.rect = self.rect.move(random.randrange(3) - 1,
                       random.randrange(3) - 1)
all_sprites = pg.sprite.Group()
for i in range(500):
    inginirium(all_sprites)

'''img = pg.image.load('ing.png')
img1 = pg.transform.scale(img, (200, 200))
img2 = pg.transform.scale(img, (700, 700))'''


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    win.fill((255, 0, 255))
    #win.blit(img1, (0, 0))
    #win.blit(img2, (100, 200))
    all_sprites.draw(win)
    all_sprites.update()
    pg.display.update()
