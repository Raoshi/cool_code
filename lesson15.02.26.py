import pygame as pg

WHITE = [255] * 3
GRAY = (100,) * 3
RED = (255, 0, 0)
LIGHTGREEN = (0, 200, 200)


pg.init()
W,H = 600, 600
win = pg.display.set_mode((W, H))

def draw_flag(sc, x, y, size):
    x = (x + .5) * size
    y = (y + .5) * size
    pg.draw.circle(sc, RED, (x, y), (size - 3) // 2, 3)


def draw_empty(sc, x, y, size):
    x = (x + .5) * size
    y = (y + .5) * size
    pg.draw.circle(sc, LIGHTGREEN, (x, y), (size - 3) // 2, 3)


class Board:
    def __init__(self, W, H, size):
        self.W, self.H = W, H
        self.size = size
        self.board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]


    def click(self, mouse_pos):
        x = mouse_pos[0] // self.size
        y = mouse_pos[1] // self.size


    def render(self, win):
        for i in range(int(self.W / self.size)):
            pg.draw.line(win, GRAY, (0, (i + 1) * self.size), (self.W, (i + 1) * self.size))
            pg.draw.line(win, GRAY, ((i + 1) * self.size, 0), ((i + 1) * self.size, self.H))


board = Board(W, H, 120)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            board.click(event.pos)

    mouse_pos = pg.mouse.get_pos()
    print(mouse_pos)
    win.fill(WHITE)
    board.render(win)
    pg.display.update()
