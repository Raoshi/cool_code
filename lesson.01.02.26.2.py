import pygame as pg
import random

W, H = 500, 500
object_to_draw = 'figura'

pg.init()
win = pg.display.set_mode((W, H))

win.fill((255, 255, 255))
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    keys = pg.key.get_pressed()
    cursor = pg.mouse.get_pos()
    if keys[pg.K_w]:
        object_to_draw = 'kvadrat'
    elif keys[pg.K_q]:
        object_to_draw = 'krug'
    elif keys[pg.K_SPACE]:
        win.fill((255, 255, 255))

    if object_to_draw == 'kvadrat':
        pg.draw.rect(win, random.choices(range(256), k=3), (cursor[0], cursor[1], 40, 40))
    elif object_to_draw == 'krug':
        pg.draw.circle(win, random.choices(range(256), k=3), cursor, 20)

    pg.display.update()
