import pygame as pg
from constants import *

pg.init()
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
clock = pg.time.Clock()

class Firkant():
    GRAV = 0.3
    def __init__(self, x:int, y:int) -> None:
        self.rect = pg.Rect(0, 0, 30, 30)
        self.rect.center = (x, y)

        self.vy = 0            

    def update(self):
        self.vy += Firkant.GRAV
        self.rect.y += self.vy

        if self.rect.top > VINDU_HOYDE:
            self.rect.bottom = 0
            self.vy = 0

    def draw(self, vindu):
        pg.draw.rect(vindu, BLUE, self.rect)

running = True
rektangler =[]
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos #posisjon for klikket
            rekt = Firkant(x,y)
            rektangler.append(rekt)

    vindu.fill((250,23,130))
    for rekt in rektangler:
        rekt.update()
        rekt.draw(vindu)

    pg.display.flip()
    clock.tick(FPS)

pg.quit()


