import pygame as pg
import random

GRAY = [70] * 3
BLACK = [0] * 3
WHITE = [255] * 3
GREEN = [0, 255, 0]
RED = [255, 0, 0]
W, H = 500, 500

pg.init()

win = pg.display.set_mode((W, H))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    #win.fill((255, 255, 255))

    for i in range(10):
        pg.draw.circle(win, GRAY, (random.randint(0, W), random.randint(0, H)), 1)

    pressed = pg.mouse.get_pressed()
    if pressed[0]:
        pos = pg.mouse.get_pos()
        pg.draw.circle(win, WHITE, pos, 3)

    if pressed[1]:
        pos = pg.mouse.get_pos()
        pg.draw.circle(win, RED, pos, 3)

    if pressed[2]:
        pos = pg.mouse.get_pos()
        pg.draw.circle(win, GREEN, pos, 3)



    pg.display.update()

    pg.time.delay(20)
