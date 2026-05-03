import pygame as pg

pg.init()
W = 1000
H = 1000
backgroundY = 0
backgroundY2 = H

win = pg.display.set_mode((W, H))

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('ship.png')
        self.image = pg.transform.scale(self.image, (150, 100))
        self.rect = self.image.get_rect()
        self.rect.left = W / 2 - 75
        self.rect.top = H - 200


    def update(self):
        self.move()
    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.top -= 3
        if keys[pg.K_s]:
            self.rect.top += 3
        if keys[pg.K_a]:
            self.rect.left -= 3
        if keys[pg.K_d]:
            self.rect.left += 3

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('enemyship2.png')
        self.image = pg.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.left = W / 2 - 75
        self.rect.top = H - 900
        self.x = 3

    def update(self):
        self.move()
    def move(self):
        self.rect.left += self.x
        if self.rect.left > 600:
            self.x = -3
        elif self.rect.left < 200:
            self.x = 3


all_sprites = pg.sprite.Group()
player = Player()
all_sprites.add(player)

enemy_sprites = pg.sprite.Group()
enemy = Enemy()
enemy_sprites.add(enemy)

background_image = pg.image.load('space.jpg')
background_image = pg.transform.scale(background_image, (W, H))

background_image2 = pg.image.load('space.jpg')
background_image2 = pg.transform.scale(background_image2, (W, H))

fps = 60
clock = pg.time.Clock()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    win.blit(background_image, (0, backgroundY))
    win.blit(background_image2, (0, backgroundY2))

    all_sprites.draw(win)
    enemy_sprites.draw(win)

    all_sprites.update()
    enemy_sprites.update()

    backgroundY -= 2
    backgroundY2 -= 2
    if backgroundY2 == 0:
        backgroundY = H
    if backgroundY == 0:
        backgroundY2 = H
    pg.display.update()
    clock.tick(fps)