import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))

x = 225
y = 225
z = 1
r = 255
g = 255
b = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((255, 255, 255))
    pygame.draw.circle(win, (r, g, b), (x, y), 50)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= 2
    elif keys[pygame.K_s]:
        y += 2
    elif keys[pygame.K_a]:
        x -= 2
    elif keys[pygame.K_d]:
        x += 2
    elif x > 225:
        x -= 2
    elif x < 225:
        x += 2
    elif y > 225:
        y -= 2
    elif y < 225:
        y += 2
    if x > 375:
        g = 0
        x -= 1
    elif x < 75:
        g = 0
        x += 1
    elif y > 375:
        g = 0
        y -= 1
    elif y < 75:
        g = 0
        y += 1
    else:
        g = 255


    pygame.display.update()
    pygame.time.delay(8)