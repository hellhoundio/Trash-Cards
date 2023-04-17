import pygame as pg
import sys

pg.init()

res = (800,800)
ekraan = pg.display.set_mode(res)

hele_nupp = (200,200,200)
varv_nupp = (200,50,50)
tume_nupp = (50,50,50)

smallfont = pg.font.SysFont('Corbel', 35)
text = smallfont.render('quit', True, varv_nupp)
korgus = ekraan.get_height()
laius = ekraan.get_width()
ekraan.fill((60, 25, 60))


while True:
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            pg.quit()
        if ev.type == pg.MOUSEBUTTONDOWN:
            if laius / 2 <= mouse[0] <= laius / 2 + 140 and korgus / 2 <= mouse[1] <= korgus / 2 + 40:
                ekraan.fill((0,200,50))
                pg.display.update()
    mouse = pg.mouse.get_pos()
    if laius / 2 <= mouse[0] <= laius / 2 + 140 and korgus / 2 <= mouse[1] <= korgus / 2 + 40:
        pg.draw.rect(ekraan, hele_nupp, [laius / 2, korgus / 2, 140, 40])
    else:
        pg.draw.rect(ekraan, tume_nupp, [laius / 2, korgus / 2, 140, 40])
    ekraan.blit(text, (laius / 2 + 50, korgus / 2))
    pg.display.update()

