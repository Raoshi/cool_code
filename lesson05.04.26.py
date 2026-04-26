from MyButton import *
from Common import *



button = Button()
menu_sprites.add(button)






fps = 60
clock = pg.time.Clock()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        elif event.type == pg.MOUSEBUTTONUP:
            mouse_pos = pg.mouse.get_pos()
            x = mouse_pos[0]
            y = mouse_pos[1]
            if x >= button.rect.left and x <= button.rect.right and y <= button.rect.bottom and y >= button.rect.top:
                print('button is pressed')
                game = True
                showmenu = False

    if not game and showmenu:
        menu_sprites.draw(menu_surface)
        menu_sprites.update()
        win.blit(menu_surface, (0, 0))
    if game:
        win.blit(background_image, (0, 0))
        all_sprites.draw(win)
        all_sprites.update()



    mouse_button = pg.mouse.get_pressed()


    pg.display.update()
    clock.tick(fps)