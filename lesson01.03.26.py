import random

import pygame as pg
import pygame.transform

pg.init()
W = 500
H = 500

win = pg.display.set_mode((W, H))

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('ing.png')
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.right = W
        self.rect.top = random.randint(0, H - self.rect.height)

    def update(self):
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
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

all_sprites = pg.sprite.Group()
player = Player()
all_sprites.add(player)

enemy_sprites = pg.sprite.Group()
enemy = Enemy()
enemy_sprites.add(enemy)
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

    #if player.rect.right >= enemy.rect.left and player.rect.left <= enemy.rect.right and player.rect.top <= enemy.rect.bottom and player.rect.bottom >= enemy.rect.top:
     #   print('ckrtogkrto')

    hits = pg.sprite.spritecollide(player, enemy_sprites, False)
    if len(hits) > 0:
        print('gtgggg')
        hits[0].rect.left = random.randint(0, W - hits[0].rect.width)
        hits[0].rect.top = random.randint(0, H - hits[0].rect.height)

    enemy_sprites.draw(win)
    enemy_sprites.update()

    


    pg.display.update()
    clock.tick(fps)