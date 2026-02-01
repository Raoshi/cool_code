import pygame
pygame.init()
win = pygame.display.set_mode((1000, 1000))

x = 250
y = 250

class Circle:
    def __init__(self, x, y, color, rad):
        self.x = x
        self.y = y
        self.color = color
        self.rad = rad
    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.rad)
    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        self.ToUp = True
        self.ToDown = True
        if keys[pygame.K_w]:
            self.y -= 1
        elif keys[pygame.K_s]:
            self.y += 1
        elif keys[pygame.K_a]:
            self.x -= 1
        elif keys[pygame.K_d]:
            self.x += 1
        elif keys[pygame.K_SPACE]:
            if self.ToUp:
                self.y -= 1
            elif self.ToDown:
                self.ToDown > 250
                self.y += 1



krug = Circle(250, 250, (255, 255, 0), 20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((255, 255, 255))
    krug.draw()
    krug.move_by_keys()
    krug.jump()
    pygame.display.update()
    pygame.time.delay(4)

