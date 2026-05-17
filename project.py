import pygame as pg
import sys

pg.init()
W = 1000
H = 1000
backgroundY = 0
backgroundY2 = H
menu_surface = pg.Surface((W, H))
game_surface = pg.Surface((W, H))
level_surface = pg.Surface((W, H))

MENU = "MENU"
GAME = "GAME"
LEVEL = "LEVEL"
state = MENU

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
        self.health = 20

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
            self.cooldown = 20


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

class MenuButton(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('start.png')
        self.image = pg.transform.scale(self.image, (550, 250))
        self.rect = self.image.get_rect()
        self.rect.left = W / 2 - 275
        self.rect.top = H / 2 - 125


class LevelButtons(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('start.png')
        self.image = pg.transform.scale(self.image, (550, 250))
        self.rect = self.image.get_rect()
        self.rect.left = W / 2 - 285
        self.rect.top = H / 2 - 125


def draw_menu():
    menu_surface.blit(background_image3, (0, 0))
    menu_sprites.draw(menu_surface)
    menu_sprites.update()

def draw_level():
    level_surface.blit(background_image3, (0, 0))
    level_sprites.draw(level_surface)
    level_sprites.update()

def draw_game():
    global backgroundY, backgroundY2

    game_surface.blit(background_image, (0, backgroundY))
    game_surface.blit(background_image2, (0, backgroundY2))

    all_sprites.draw(game_surface)
    enemy_sprites.draw(game_surface)
    arrow_sprites.draw(game_surface)
    enemy_arrow.draw(game_surface)

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

all_sprites = pg.sprite.Group()
start_button = MenuButton()
menu_sprites = pg.sprite.Group()
menu_sprites.add(start_button)
levelsbutton = LevelButtons()
level_sprites = pg.sprite.Group()
level_sprites.add(levelsbutton)
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

background_image3 = pg.image.load('spacebg.jpg')
background_image3 = pg.transform.scale(background_image3, (W, H))



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

        if event.type == pg.MOUSEBUTTONUP:

            if state == MENU:
                mouse_pos = event.pos

                if start_button.rect.collidepoint(mouse_pos):
                    state = LEVEL

            elif state == LEVEL:
                mouse_pos = event.pos

                if levelsbutton.rect.collidepoint(mouse_pos):
                    state = GAME

        elif state == GAME and event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
            if event.key == pg.K_r:
                state = MENU
    if state == MENU:
        win.blit(menu_surface, (0, 0))
        draw_menu()

    elif state == LEVEL:
        win.blit(level_surface, (0, 0))
        draw_level()

    elif state == GAME:
        win.blit(game_surface, (0, 0))
        draw_game()





    pg.display.update()
    clock.tick(fps)