import pygame
pygame.init()
x = int(input('Ширина и высота окна'))
y = int(input('Ширина и высота клетки'))
win = pygame.display.set_mode((x, x))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    color = (255, 255, 255)
    win.fill(color)
    pygame.draw.rect(win, (0, 0, 0), (y, y, y*y))
    pygame.display.update()
    '''pygame.draw.rect(win, (255, 255, 0), (10, 12, 100, 70))
    pygame.draw.circle(win, (0, 255, 255), (60, 150), 45)
    pygame.draw.polygon(win, (0, 0, 0), [(0, 100), (100, 50), (100, 150)], False)
    pygame.draw.line(win, (0, 255, 255), (0,0), (100, 100), 5)
    pygame.draw.lines(win, (0, 0, 0), True, ((200, 200), (300, 150), (300, 250)), 10)
    pygame.display.update()'''


