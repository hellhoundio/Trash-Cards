import pygame as pg
import sys
from pildid import *

pg.init()
ekraan = pg.display.set_mode((800,800))
ekraan.fill((200,150,150))

korgus = ekraan.get_height()
laius = ekraan.get_width()

algne_varv = (255, 222, 254)
lopp_varv = (182, 120, 178)
basic_varv = (75,20,75)
font = pg.font.SysFont('Ariel', 50)
vaikefont = pg.font.SysFont('Ariel', 30)
menu_tekst = font.render('Menüü', True, basic_varv)
alusta_tekst = vaikefont.render('Alusta Mänguga', True, basic_varv)
opetus_tekst = vaikefont.render('Õpetus', True, basic_varv)

def vajutas_menu_nuppu():
    ekraan.fill((200, 200, 200))
    pg.display.update()

while True:
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif ev.type == pg.KEYDOWN:
            if ev.key == pg.K_DOWN:
                pg.draw.rect(ekraan, lopp_varv, [laius / 2 - 55, korgus / 2, 140, 40])
                pg.display.update()
            elif ev.key == pg.K_q:
                pg.quit()
                sys.exit()
            else:
                pg.draw.rect(ekraan, algne_varv, [laius / 2-55, korgus / 2, 140, 40])
    ekraan.blit(alusta_tekst, (laius / 2 - 55, korgus / 2 ))
    pg.draw.rect(ekraan, algne_varv, [laius / 2-55, korgus / 2+100, 140, 40])
    ekraan.blit(opetus_tekst, (laius / 2 - 55, korgus / 2 +100))
    ekraan.blit(menu_tekst, (laius / 2 -40, korgus / 2-150))
    pg.display.update()
    hiir = pg.mouse.get_pos()
