import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))

x = 450
y = 50
i = 50
s = 50
z = 1
m = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if x > 450:
        z = -1
    elif x < 50:
        z = 1
    x = x + z
    y = y - z



    if s > 450:
        m = -1
    elif s < 50:
        m = 1
    s = s + m
    i = i + m

    win.fill((255, 255, 255))
    pygame.draw.circle(win, (0, 255, 255), (x, y), 50)
    pygame.draw.circle(win, (0, 255, 255), (i, s), 50)
    pygame.display.update()

    pygame.time.delay(10)