import pygame as pg

from Player import PlayerObject
pg.init()
W = 500
H = 500

win = pg.display.set_mode((W, H))
menu_sprites = pg.sprite.Group()

all_sprites = pg.sprite.Group()
player = PlayerObject()

all_sprites.add(player)

fps = 60
clock = pg.time.Clock()

menu_surface = pg.Surface((W, H))
menu_surface.fill((255, 255, 255))

game = False
showmenu = True

background_image = pg.image.load('background.png')
background_image = pg.transform.scale(background_image, (W, H))