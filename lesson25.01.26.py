import random

import pygame
pygame.init()
width = 500
heigh = 500
win = pygame.display.set_mode((width, heigh))
FPS = 30
clock = pygame.time.Clock()

class Circle:
    def __init__(self, x, y, color, rad):
        self.x = x
        self.y = y
        self.color = color
        self.rad = rad
        self.move = 1
        self.z = 10
    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.rad)
        self.tuda()
    def tuda(self):
        if self.x < width:
            self.move += 1
        elif self.x > width:
            self.move -= 1
        self.x += self.move




krug = Circle(10, 20, (255, 255, 0), 20)
krugi = []
for i in range(100):
    krugi.append(Circle(i * 10, i * 5, random.choices(range(256), k = 3), 20))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((255, 255, 255))
    for i in range(100):
        krugi[i].draw()
    #krug.draw()
    #krug.tuda()

    pygame.display.update()
    clock.tick(FPS)
