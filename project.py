import pygame as pg
import math

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
        self.health = 30


    def update(self):
        self.move()
    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.top -= 5
        if keys[pg.K_s]:
            self.rect.top += 5
        if keys[pg.K_a]:
            self.rect.left -= 5
        if keys[pg.K_d]:
            self.rect.left += 5


class EnemyArrow(pg.sprite.Sprite):
    def __init__(self, direction):
        super().__init__()
        self.image = pg.image.load('arrow.png')
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.speed = 3
        self.rect.left = enemy.rect.left + 50
        self.rect.top = enemy.rect.top
        self.direction = direction

    def update(self):
        self.move()

    def move(self):
        self.rect.y += self.speed
        if self.direction == 1:
            self.rect.x -= self.speed // 2
        if self.direction == 2:
            self.rect.x = self.rect.x
        if self.direction == 3:
            self.rect.x += self.speed // 2
        if self.rect.bottom > 1000:
            self.kill()


class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('enemyship2.png')
        self.image = pg.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.left = W / 2 - 75
        self.rect.top = H - 900
        self.x = 3
        self.cooldown = 0
        self.health = 2

    def update(self):
        self.move()
        self.shoot()
    def move(self):
        self.rect.left += self.x
        if self.rect.left > 600:
            self.x = -3
        elif self.rect.left < 200:
            self.x = 3

    def shoot(self):
        if self.cooldown > 0:
            self.cooldown -= 1
        else:
            number = 3
            for i in range(number):
                bullet = EnemyArrow(i + 1)
                enemy_arrow.add(bullet)
            self.cooldown = 90


class Arrow(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('arrow.png')
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.speed = 3
        self.rect.left = player.rect.left + 50
        self.rect.top = player.rect.top

    def update(self):
        self.move()

    def move(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()



all_sprites = pg.sprite.Group()
player = Player()
all_sprites.add(player)


enemy_sprites = pg.sprite.Group()
enemy = Enemy()
enemy_sprites.add(enemy)

arrow_sprites = pg.sprite.Group()
enemy_arrow = pg.sprite.Group()

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

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            arrow = Arrow()
            arrow_sprites.add(arrow)



    win.blit(background_image, (0, backgroundY))
    win.blit(background_image2, (0, backgroundY2))

    all_sprites.draw(win)
    enemy_sprites.draw(win)
    arrow_sprites.draw(win)
    enemy_arrow.draw(win)


    all_sprites.update()
    enemy_sprites.update()
    arrow_sprites.update()
    enemy_arrow.update()

    hits = pg.sprite.spritecollide(player, enemy_arrow, True)
    if len(hits) > 0:
        player.health -= 1
        if player.health <= 0:
            all_sprites.remove(player)

    hits2 = pg.sprite.spritecollide(enemy, arrow_sprites, True)
    if len(hits2) > 0:
        enemy.health -= 1
        if enemy.health <= 0:
            enemy_sprites.remove(enemy)

    backgroundY -= 2
    backgroundY2 -= 2
    if backgroundY2 == 0:
        backgroundY = H
    if backgroundY == 0:
        backgroundY2 = H
    pg.display.update()
    clock.tick(fps)