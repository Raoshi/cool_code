import pygame as pg

pg.init()
W,H = 600, 600
win = pg.display.set_mode((W, H))

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('ing.png')
        self.image = pg.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()

    def update(self):
        self.move_by_keys()

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

player = Player()
all_sprites = pg.sprite.Group()
all_sprites.add(player)

fps = 60
clock = pg.time.Clock()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    win.fill((255, 255, 255))
    all_sprites.draw(win)
    all_sprites.update()

    pg.display.update()
    clock.tick(fps)



