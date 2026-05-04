import random
import pygame as pg

pg.init()
W = 500
H = 500
backgroundX = 0
backgroundX2 = W


win = pg.display.set_mode((W, H))

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('ing.png')
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.health = 10
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
        self.image = pg.image.load('enemy.png')
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.health = 100
    def update(self):
        self.move()
    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.rect.top -= 3
        if keys[pg.K_DOWN]:
            self.rect.top += 3
        if keys[pg.K_LEFT]:
            self.rect.left -= 3
        if keys[pg.K_RIGHT]:
            self.rect.left += 3

all_sprites = pg.sprite.Group()
player = Player()
all_sprites.add(player)

enemy_sprites = pg.sprite.Group()
enemy = Enemy()
enemy_sprites.add(enemy)



background_image = pg.image.load('background.png')
background_image = pg.transform.scale(background_image, (W, H))

background_image2 = pg.image.load('background.png')
background_image2 = pg.transform.scale(background_image2, (W, H))

fps = 60
clock = pg.time.Clock()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    win.blit(background_image, (backgroundX, 0))
    win.blit(background_image2, (backgroundX2, 0))
    all_sprites.draw(win)
    enemy_sprites.draw(win)
    all_sprites.update()
    enemy_sprites.update()

    hits = pg.sprite.spritecollide(player, enemy_sprites, False)
    if len(hits) > 0:
        hits[0].health -= 1
        hits[0].rect.left = random.randint(0, W - hits[0].rect.width)
        hits[0].rect.top = random.randint(0, H - hits[0].rect.height)
        if hits[0].health <= 0:
            enemy_sprites.remove(hits[0])

    backgroundX -= 2
    backgroundX2 -= 2
    if backgroundX2 == 0:
        backgroundX = W
    if backgroundX == 0:
        backgroundX2 = W
    pg.display.update()
    clock.tick(fps)