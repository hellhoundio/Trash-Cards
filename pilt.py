import pygame as pg

pg.init()
ekraan = pg.display.set_mode((900,600))
ekraan.fill((200,150,150))

korgus = ekraan.get_height()
laius = ekraan.get_width()

tegelase_dimensioonid = (500,500)
lehtede_dimensioonid = (900,600)

menuu_algne = pg.image.load("pildid/menuu_algne copy.JPG")
menuu_algne = pg.transform.scale(menuu_algne,lehtede_dimensioonid)
menuu_alustame_mangu = pg.image.load("pildid/menuu_alustame_mangu copy.JPG")
menuu_alustame_mangu = pg.transform.scale(menuu_alustame_mangu,lehtede_dimensioonid)
menuu_kuidas_mang = pg.image.load("pildid/menuu_kuidas_mang copy.JPG")
menuu_kuidas_mang = pg.transform.scale(menuu_kuidas_mang,lehtede_dimensioonid)
menuu_aitab_kah = pg.image.load("pildid/menuu_aitab_kah copy.JPG")
menuu_aitab_kah = pg.transform.scale(menuu_aitab_kah,lehtede_dimensioonid)
menuu_kreditid = pg.image.load("pildid/menuu_kreditid copy.JPG")
menuu_kreditid = pg.transform.scale(menuu_kreditid,lehtede_dimensioonid)