import random
import sqlite3
import pygame as pg

pg.init()
W = 500
H = 500

win = pg.display.set_mode((W, H))

okno = pg.Surface((W, 100))
okno2 = pg.Surface((W, 200))


font = pg.font.Font(None, 26)
text = font.render('Hello', False, (0, 0, 0))

con = sqlite3.connect('score.sqlite')
cur = con.cursor()

def create_database():
    que_create = '''
    CREATE TABLE IF NOT EXISTS score(
        id INTEGER PRIMARY KEY, 
        name TEXT, 
        score INTEGER
    )
'''
    cur.execute(que_create)
    con.commit()

create_database()

def insert_data(name, score):
    que_insert = '''
        INSERT INTO score (name, score) VALUES
        ('{}', {})
    '''

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('ing.png')
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

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
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(0, okno2.get_rect().width - self.rect.width)
        self.rect.top = random.randint(0, okno2.get_rect().height - self.rect.height)



player = Player()
enemy = Enemy()
all_sprites = pg.sprite.Group()
all_sprites.add(player)

enemy_sprites = pg.sprite.Group()
enemy_sprites.add(enemy)

currentsurface = 1

name = input('Введите имя')
score = 0

fps = 60
clock = pg.time.Clock()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            insert_data(name, score)
            exit()



    win.fill((255, 255, 255))
    okno.fill((255, 0, 255))
    okno2.fill((0, 255, 255))

    hits = pg.sprite.spritecollide(player, enemy_sprites, False)
    if len(hits) > 0:
        score += 1
        hits[0].rect.left = random.randint(0, okno2.get_rect().width - hits[0].rect.width)
        hits[0].rect.top = random.randint(0, okno2.get_rect().height - hits[0].rect.height)



    all_sprites.update()
    enemy_sprites.draw(okno2)
    enemy_sprites.update()
    okno.blit(text, (200, 0))

    if currentsurface == 1:
        if player.rect.bottom >= okno.get_rect().height:
            currentsurface = 2
            player.rect.top = 2

    if currentsurface == 2:
        if player.rect.top <= 0:
            currentsurface = 1
            player.rect.bottom = okno.get_rect().height - 2

    if currentsurface == 1:
        all_sprites.draw(okno)
    elif currentsurface == 2:
        all_sprites.draw(okno2)


    win.blit(okno, (0, 0))
    win.blit(okno2, (0, 100))


    pg.display.update()
    clock.tick(fps)
