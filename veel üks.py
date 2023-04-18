import pygame as pg
import sys
import math as m
import time

#tehnilised asjad
pg.init()
ekraan = pg.display.set_mode((900,600))
ekraan.fill((200,150,150))

korgus = ekraan.get_height()
laius = ekraan.get_width()

tegelase_dimensioonid = (500,500)
lehtede_dimensioonid = (900,600)

#mängu asjad

nadal = 1
sober = 1

# värvid
roheline = (202, 202, 170)
sisekollane = (238, 197, 132)
valikollane = (200, 171, 131)
sinine = (85, 134, 140)
lilla = (127, 99, 110)
beez = (231, 207, 205)
lillakas = (159, 154, 164)
hall = (127,127,127)

tehniline_font = pg.font.SysFont('Courier New', 50, True)
tekst_font = pg.font.SysFont('Courier New', 20)

#pildid

#pilt = pg.image.load("giphy.gif")
#pilt = pg.transform.scale(pilt,lehtede_dimensioonid)
menuu_algne = pg.image.load("menuu_algne copy.JPG")
menuu_algne = pg.transform.scale(menuu_algne,lehtede_dimensioonid)
menuu_alustame_mangu = pg.image.load("menuu_alustame_mangu copy.JPG")
menuu_alustame_mangu = pg.transform.scale(menuu_alustame_mangu,lehtede_dimensioonid)
menuu_kuidas_mang = pg.image.load("menuu_kuidas_mang copy.JPG")
menuu_kuidas_mang = pg.transform.scale(menuu_kuidas_mang,lehtede_dimensioonid)
menuu_aitab_kah = pg.image.load("menuu_aitab_kah copy.JPG")
menuu_aitab_kah = pg.transform.scale(menuu_aitab_kah,lehtede_dimensioonid)
menuu_kreditid = pg.image.load("menuu_kreditid copy.JPG")
menuu_kreditid = pg.transform.scale(menuu_kreditid,lehtede_dimensioonid)
kuidas_algne = pg.image.load("kuidas_algne copy.JPG")
kuidas_algne = pg.transform.scale(kuidas_algne,lehtede_dimensioonid)
kuidas_tagasi = pg.image.load("kuidas_tagasi copy.JPG")
kuidas_tagasi = pg.transform.scale(kuidas_tagasi,lehtede_dimensioonid)
alguses_kuidas = pg.image.load("alguses_kuidas copy.jpg")
alguses_kuidas = pg.transform.scale(alguses_kuidas,lehtede_dimensioonid)

layout = pg.image.load("layout_valitud copy.PNG")
layout = pg.transform.scale(layout,lehtede_dimensioonid)
layout_valitud = pg.image.load("layout copy.PNG")
layout_valitud = pg.transform.scale(layout_valitud,lehtede_dimensioonid)
paus_algus = pg.image.load("paus copy.JPG")
paus_algus = pg.transform.scale(paus_algus,lehtede_dimensioonid)
paus_tagasi = pg.image.load("paus_valitud copy.JPG")
paus_tagasi = pg.transform.scale(paus_tagasi,lehtede_dimensioonid)
paus_kuidas = pg.image.load("paus_kuidas copy.JPG")
paus_kuidas = pg.transform.scale(paus_kuidas,lehtede_dimensioonid)
paus_aitab = pg.image.load("paus_aitab copy.JPG")
paus_aitab = pg.transform.scale(paus_aitab,lehtede_dimensioonid)
paus_tanud = pg.image.load("paus_tanud copy.JPG")
paus_tanud = pg.transform.scale(paus_tanud,lehtede_dimensioonid)
mitmes_nadal = pg.image.load("nadal.JPG")
mitmes_nadal = pg.transform.scale(mitmes_nadal,lehtede_dimensioonid)

haircut_angry = pg.image.load("haircut_angry copy.png")
haircut_angry = pg.transform.scale(haircut_angry,tegelase_dimensioonid)
haircut_angry_home = pg.image.load("haircut_angry_home copy.png")
haircut_angry_home = pg.transform.scale(haircut_angry_home,tegelase_dimensioonid)
haircut_curious = pg.image.load("haircut_curious copy.png")
haircut_curious = pg.transform.scale(haircut_curious,tegelase_dimensioonid)
haircut_curious_home = pg.image.load("haircut_curious_home copy.png")
haircut_curious_home = pg.transform.scale(haircut_curious_home,tegelase_dimensioonid)
haircut_happy = pg.image.load("haircut_happy copy.png")
haircut_happy = pg.transform.scale(haircut_happy,tegelase_dimensioonid)
haircut_happy_home = pg.image.load("haircut_happy_home copy.png")
haircut_happy_home = pg.transform.scale(haircut_happy_home,tegelase_dimensioonid)
haircut_mus = pg.image.load("haircut_mus copy.png")
haircut_mus = pg.transform.scale(haircut_mus,tegelase_dimensioonid)
haircut_norm_home = pg.image.load("haircut_norm_home copy.png")
haircut_norm_home = pg.transform.scale(haircut_norm_home,tegelase_dimensioonid)
haircut_sad = pg.image.load("haircut_sad copy.png")
haircut_sad = pg.transform.scale(haircut_sad,tegelase_dimensioonid)
haircut_sad_home = pg.image.load("haircut_sad_home copy.png")
haircut_sad_home = pg.transform.scale(haircut_sad_home,tegelase_dimensioonid)
haircut_scared = pg.image.load("haircut_scared copy.png")
haircut_scared = pg.transform.scale(haircut_scared,tegelase_dimensioonid)
haircut_scared_home = pg.image.load("haircut_scared_home copy.png")
haircut_scared_home = pg.transform.scale(haircut_scared_home,tegelase_dimensioonid)
hoodie_angry = pg.image.load("hoodie_angry copy.png")
hoodie_angry = pg.transform.scale(hoodie_angry,tegelase_dimensioonid)
hoodie_curious = pg.image.load("hoodie_curious copy.png")
hoodie_curious = pg.transform.scale(hoodie_curious,tegelase_dimensioonid)
hoodie_happy = pg.image.load("hoodie_happy copy.png")
hoodie_happy = pg.transform.scale(hoodie_happy,tegelase_dimensioonid)
hoodie_mus = pg.image.load("hoodie_mus copy.png")
hoodie_mus = pg.transform.scale(hoodie_mus,tegelase_dimensioonid)
hoodie_norm = pg.image.load("hoodie_norm copy.png")
hoodie_norm = pg.transform.scale(hoodie_norm,tegelase_dimensioonid)
hoodie_sad = pg.image.load("hoodie_sad copy.png")
hoodie_sad = pg.transform.scale(hoodie_sad,tegelase_dimensioonid)
hoodie_scared = pg.image.load("hoodie_scared copy.png")
hoodie_scared = pg.transform.scale(hoodie_scared,tegelase_dimensioonid)
hoodie_work = pg.image.load("hoodie_work copy.png")
hoodie_work = pg.transform.scale(hoodie_work,tegelase_dimensioonid)
norm_angry = pg.image.load("norm_angry copy.png")
norm_angry = pg.transform.scale(norm_angry,tegelase_dimensioonid)
norm_curious = pg.image.load("norm_curious copy.png")
norm_curious = pg.transform.scale(norm_curious,tegelase_dimensioonid)
norm_happy = pg.image.load("norm_happy copy.png")
norm_happy = pg.transform.scale(norm_happy,tegelase_dimensioonid)
norm_mus = pg.image.load("norm_mus copy.png")
norm_mus = pg.transform.scale(norm_mus,tegelase_dimensioonid)
norm_norm = pg.image.load("norm_norm copy.png")
norm_norm = pg.transform.scale(norm_norm,tegelase_dimensioonid)
norm_sad = pg.image.load("norm_sad copy.png")
norm_sad = pg.transform.scale(norm_sad,tegelase_dimensioonid)
norm_scared = pg.image.load("norm_scared copy.png")
norm_scared = pg.transform.scale(norm_scared,tegelase_dimensioonid)
norm_work = pg.image.load("norm_work copy.png")
norm_work = pg.transform.scale(norm_work,tegelase_dimensioonid)
norm_write = pg.image.load("norm_write copy.png")
norm_write = pg.transform.scale(norm_write,tegelase_dimensioonid)

pop_curious = pg.image.load("pop_curious.png")
pop_curious = pg.transform.scale(pop_curious,tegelase_dimensioonid)
pop_happy = pg.image.load("pop_happy.png")
pop_happy = pg.transform.scale(pop_happy,tegelase_dimensioonid)
pop_norm = pg.image.load("pop_norm.png")
pop_norm = pg.transform.scale(pop_norm,tegelase_dimensioonid)
pop_sad = pg.image.load("pop_sad.png")
pop_sad = pg.transform.scale(pop_sad,tegelase_dimensioonid)

#mäng kui definitsioonid
hetkene_tuju = norm_norm
hetkene_koht = "kool"
otsus = 0
def kuidas():
    kuidas_jookseb = True
    tagasi = 0
    while kuidas_jookseb:
        if tagasi == 0:
            ekraan.blit(kuidas_algne, (0, 0))
            pg.display.update()
        else:
            ekraan.blit(kuidas_tagasi, (0, 0))
            pg.display.update()
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif ev.type == pg.KEYDOWN:
                if ev.key == pg.K_q:
                    pg.quit()
                    sys.exit()
                elif ev.key == pg.K_RETURN:
                    if tagasi == True:
                        kuidas_jookseb = False
                elif tagasi != 0:
                    tagasi = 0
                elif ev.key == pg.K_DOWN:
                    tagasi += 1
                elif ev.key == pg.K_UP:
                    tagasi += 1
def menuu():
    menuu_jookseb = True
    menuu_valik = 0
    kloksas = False
    while menuu_jookseb:
        if menuu_valik == 0 or menuu_valik == -5:
            ekraan.blit(menuu_algne, (0, 0))
        elif menuu_valik == 1 or menuu_valik == -4:
            ekraan.blit(menuu_alustame_mangu, (0, 0))
        elif menuu_valik == 2 or menuu_valik == -3:
            ekraan.blit(menuu_kuidas_mang, (0, 0))
        elif menuu_valik == 3 or menuu_valik == -2:
            ekraan.blit(menuu_aitab_kah, (0, 0))
        elif menuu_valik == 4 or menuu_valik == -1:
            ekraan.blit(menuu_kreditid, (0, 0))
        else:
            menuu_valik = 0
        if kloksas == False:
            kloksa_tekst = tehniline_font.render("vajuta ↑ või ↓", True, (200,200,200))
            ekraan.blit(kloksa_tekst, (200, 500))
        pg.display.update()
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif ev.type == pg.KEYDOWN:
                kloksas = True
                if ev.key == pg.K_q:
                    pg.quit()
                    sys.exit()
                elif ev.key == pg.K_DOWN:
                    menuu_valik += 1
                elif ev.key == pg.K_UP:
                    menuu_valik -= 1
                elif ev.key == pg.K_RETURN:
                    if menuu_valik == 2 or menuu_valik == -3:
                        kuidas()
                    elif menuu_valik == 1 or menuu_valik == -4:
                        menuu_jookseb = False
                    elif menuu_valik == 3 or menuu_valik == -2:
                        pg.quit()
                        sys.exit()
def paus():
    global hetkene_tuju
    global hetkene_koht
    tuju = hetkene_tuju
    koht = hetkene_koht
    paus_jookseb = True
    paus_valik = 0
    while paus_jookseb:
        if paus_valik == 0 or paus_valik == -5:
            ekraan.blit(paus_algus, (0, 0))
        elif paus_valik == 1 or paus_valik == -4:
            ekraan.blit(paus_tagasi, (0, 0))
        elif paus_valik == 2 or paus_valik == -3:
            ekraan.blit(paus_kuidas, (0, 0))
        elif paus_valik == 3 or paus_valik == -2:
            ekraan.blit(paus_aitab, (0, 0))
        elif paus_valik == 4 or paus_valik == -1:
            ekraan.blit(paus_tanud, (0, 0))
        else:
            paus_valik = 0
        pg.display.update()
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif ev.type == pg.KEYDOWN:
                if ev.key == pg.K_q:
                    pg.quit()
                    sys.exit()
                elif ev.key == pg.K_DOWN:
                    paus_valik += 1
                elif ev.key == pg.K_UP:
                    paus_valik -= 1
                elif ev.key == pg.K_RETURN:
                    if paus_valik == 2 or paus_valik == -3:
                        kuidas()
                    elif paus_valik == 1 or paus_valik == -4:
                        ekraan.fill("light gray")
                        ekraan.blit(tuju, (400, 100))
                        ekraan.blit(layout, (0, 0))
                        koha_tekst = tehniline_font.render(koht, True, "black")
                        ekraan.blit(koha_tekst, (610, 10))
                        nadala_tekst = tehniline_font.render(str(nadal), True, "black")
                        ekraan.blit(nadala_tekst, (325, 15))
                        paus_olek = False
                        paus_jookseb = False
                    elif paus_valik == 3 or paus_valik == -2:
                        pg.quit()
                        sys.exit()
def render_multi_line(text, x, y, fsize, varv): #tnx https://stackoverflow.com/users/7467288/justincai
    lines = text.splitlines()
    for i, l in enumerate(lines):
        ekraan.blit(tekst_font.render(l, 0, varv), (x, y + fsize * i))
def jutt(raakimine,tuju,koht):
    global hetkene_tuju
    global hetkene_koht
    hetkene_tuju = tuju
    hetkene_koht = koht

    ekraan.fill("light gray")
    ekraan.blit(tuju, (400, 100))
    ekraan.blit(layout, (0, 0))
    koha_tekst = tehniline_font.render(koht, True, "black")
    ekraan.blit(koha_tekst, (610, 10))
    nadala_tekst = tehniline_font.render(str(nadal), True, "black")
    ekraan.blit(nadala_tekst, (325, 15))

    mitmes_taht = 0
    paus_olek = False
    for x in range(len(raakimine)):
        if mitmes_taht == len(raakimine):
            break
        if paus_olek == True:
            ekraan.fill("light gray")
            ekraan.blit(tuju, (400, 100))
            ekraan.blit(layout_valitud, (0, 0))
            koha_tekst = tehniline_font.render(koht, True, "black")
            ekraan.blit(koha_tekst, (610, 10))
            nadala_tekst = tehniline_font.render(str(nadal), True, "black")
            ekraan.blit(nadala_tekst, (325, 15))
        if paus_olek == False:
            ekraan.fill("light gray")
            ekraan.blit(tuju, (400, 100))
            ekraan.blit(layout, (0, 0))
            koha_tekst = tehniline_font.render(koht, True, "black")
            ekraan.blit(koha_tekst, (610, 10))
            nadala_tekst = tehniline_font.render(str(nadal), True, "black")
            ekraan.blit(nadala_tekst, (325, 15))
        mitmes_taht += 1
        render_multi_line(raakimine[:mitmes_taht], 55, 150, 30, "black")
        time.sleep(0.02)
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif ev.type == pg.KEYDOWN:
                if ev.key == pg.K_q:
                    pg.quit()
                    sys.exit()
                elif ev.key == pg.K_RETURN:
                    if paus_olek == True:
                        paus()
                    render_multi_line(raakimine, 55, 150, 30, "black")
                    mitmes_taht = len(raakimine)
                if ev.key == pg.K_DOWN:
                    if paus_olek == False:
                        paus_olek = True
                    else:
                        paus_olek = False
                if ev.key == pg.K_UP:
                    if paus_olek == False:
                        paus_olek = True
                    else:
                        paus_olek = False
        pg.display.update()
    jutt_jookseb = True
    paus_olek = False
    while jutt_jookseb:
        if paus_olek == True:
            ekraan.fill("light gray")
            ekraan.blit(tuju, (400, 100))
            ekraan.blit(layout_valitud, (0, 0))
            koha_tekst = tehniline_font.render(koht, True, "black")
            ekraan.blit(koha_tekst, (610, 10))
            nadala_tekst = tehniline_font.render(str(nadal), True, "black")
            ekraan.blit(nadala_tekst, (325, 15))
            render_multi_line(raakimine, 55, 150, 30, "black")
        elif paus_olek == False:
            ekraan.fill("light gray")
            ekraan.blit(tuju, (400, 100))
            ekraan.blit(layout, (0, 0))
            koha_tekst = tehniline_font.render(koht, True, "black")
            ekraan.blit(koha_tekst, (610, 10))
            nadala_tekst = tehniline_font.render(str(nadal), True, "black")
            ekraan.blit(nadala_tekst, (325, 15))
            render_multi_line(raakimine, 55, 150, 30, "black")
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif ev.type == pg.KEYDOWN:
                if ev.key == pg.K_q:
                    pg.quit()
                    sys.exit()
                elif ev.key == pg.K_DOWN:
                    if paus_olek == False:
                        paus_olek = True
                    else:
                        paus_olek = False
                elif ev.key == pg.K_UP:
                    if paus_olek == False:
                        paus_olek = True
                    else:
                        paus_olek = False
                elif ev.key == pg.K_RETURN:
                    if paus_olek == True:
                        paus()
                    else:
                        jutt_jookseb = False
        pg.display.update()
def pilt(kusimus, tuju, valikud, koht):
    global hetkene_tuju
    global hetkene_koht
    global otsus
    otsus = 0
    hetkene_tuju = tuju
    hetkene_koht = koht
    jutt(kusimus,hetkene_tuju,hetkene_koht)
    pilt_jookseb = True
    valik = len(valikud)+1
    while pilt_jookseb:
        #taust
        if valik == len(valikud) or valik == len(valikud)*2+2:
            paus_olek = layout_valitud
        else:
            paus_olek = layout

        ekraan.fill("light gray")
        ekraan.blit(tuju, (400, 100))
        ekraan.blit(paus_olek, (0, 0))
        koha_tekst = tehniline_font.render(koht, True, "black")
        ekraan.blit(koha_tekst, (610, 10))
        nadala_tekst = tehniline_font.render(str(nadal), True, "black")
        ekraan.blit(nadala_tekst, (325, 15))
        #tekst
        render_multi_line(kusimus, 55,150,30,"black")
        for x in range(len(valikud)):
            mitmes = x+1
            valitud_valik = "black"
            if valik == len(valikud)-1 or valik == len(valikud)*2+1:
                if mitmes == 1:
                    valitud_valik = hall
                    otsus = 1
            elif valik == len(valikud)-2 or valik == len(valikud)*2:
                if mitmes == 2:
                    valitud_valik = hall
                    otsus = 2
            elif valik == len(valikud)-3 or valik == len(valikud)*2-1:
                if mitmes == 3:
                    valitud_valik = hall
                    otsus = 3
            render_multi_line(str(mitmes)+")"+valikud[x],50,380+x*60,30,valitud_valik)
        pg.display.update()
        #vajutused
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif ev.type == pg.KEYDOWN:
                if ev.key == pg.K_q:
                    pg.quit()
                    sys.exit()
                elif ev.key == pg.K_DOWN:
                    if valik == 0:
                        valik = len(valikud)+1
                    valik -= 1
                elif ev.key == pg.K_UP:
                    if valik == len(valikud)*2+3:
                        valik = len(valikud)+1
                    valik += 1
                elif ev.key == pg.K_RETURN:
                    if valik == len(valikud) or valik == 2*len(valikud):
                        paus()
                    elif otsus != 0:
                        pilt_jookseb = False
def sinu_jutt(raakimine):
    global hetkene_tuju
    global hetkene_tuju
    mitmes_taht = 0
    paus_olek = False
    for x in range(len(raakimine)):
        if mitmes_taht == len(raakimine):
            break
        if paus_olek == True:
            ekraan.fill("light gray")
            ekraan.blit(hetkene_tuju, (400, 100))
            ekraan.blit(layout_valitud, (0, 0))
            koha_tekst = tehniline_font.render(hetkene_koht, True, "black")
            ekraan.blit(koha_tekst, (610, 10))
            nadala_tekst = tehniline_font.render(str(nadal), True, "black")
            ekraan.blit(nadala_tekst, (325, 15))
        if paus_olek == False:
            ekraan.fill("light gray")
            ekraan.blit(hetkene_tuju, (400, 100))
            ekraan.blit(layout, (0, 0))
            koha_tekst = tehniline_font.render(hetkene_koht, True, "black")
            ekraan.blit(koha_tekst, (610, 10))
            nadala_tekst = tehniline_font.render(str(nadal), True, "black")
            ekraan.blit(nadala_tekst, (325, 15))
        mitmes_taht += 1
        render_multi_line(raakimine[:mitmes_taht], 55, 380, 30, "black")
        time.sleep(0.02)
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif ev.type == pg.KEYDOWN:
                if ev.key == pg.K_q:
                    pg.quit()
                    sys.exit()
                elif ev.key == pg.K_RETURN:
                    if paus_olek == True:
                        paus()
                    render_multi_line(raakimine, 55, 380, 30, "black")
                    mitmes_taht = len(raakimine)
                if ev.key == pg.K_DOWN:
                    if paus_olek == False:
                        paus_olek = True
                    else:
                        paus_olek = False
                if ev.key == pg.K_UP:
                    if paus_olek == False:
                        paus_olek = True
                    else:
                        paus_olek = False
        pg.display.update()
    jutt_jookseb = True
    while jutt_jookseb:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif ev.type == pg.KEYDOWN:
                if ev.key == pg.K_q:
                    pg.quit()
                    sys.exit()
                elif ev.key == pg.K_RETURN:
                    jutt_jookseb = False

def mang():
    mangib = True
    nadal = 1
    usaldus = 1
    while mangib:
        m.floor(usaldus)
        #nädal 1
        if nadal == 1:
            uks_nadal = True
            if usaldus == 1:
                while uks_nadal:
                    #\n
                    #5 row
                    #     test test test test test t

                    jutt("ou lükka friikat",pop_norm,"park")
                    sinu_jutt("käi persse minu omad")
                    jutt("ja siis? nagu mind\nhuvitaks",pop_curious,"park")
                    sinu_jutt("no eks sa siis võta\nkui nii väga soovid")
                    jutt("võtangi noh.",pop_norm,"park")
                    jutt("...",pop_curious,"park")
                    sinu_jutt("... mida sa veel tahad?")
                    jutt("kas sa oled juba mõelnud\nsellele pakkumisele?",pop_curious,"park")
                    sinu_jutt("pakkumine? mis ajast\noled sina mulle üldse\nmidagi niisama pakkunud?")
                    jutt("ei lollakas. mitte selles\nmõttes. rohkem nagu\nsee...",pop_norm,"park")
                    jutt("see väljakutse, kui seda\nvõib nii kutsuda.\nsee asi.",pop_norm,"park")
                    sinu_jutt("palun aga värseknda minu\nmälu, sest ma tõepoolest\nei tea millest sa räägid")
                    jutt("noo...",pop_norm,"park")
                    jutt("okei nii. ma vean sinuga\nkihla et sa ei suuda\nveenda seda venda seal\nendaga aineid tarbima.",pop_norm,"park")
                    sinu_jutt("aaaa see asi. ja mis\nsiis? mis mina sellest\nsaan?")
                    jutt("noo kui sa päriselt suudad\nseda teha, mida sa\nmuide absoluutselt ei\nsuuda, siis sa saaksid\nendale kohe päris oma",pop_norm,"park")
                    jutt("mootoratta. see vana romu\nmida sa oled koguaeg\nsilmanud seal minu aias.\nniitideta diil selline.",pop_happy,"park")
                    sinu_jutt("oh sa...")
                    sinu_jutt("see isegi...see isegi\noleks ju midagi. ja\nma pean lihtsalt selle\nvennikese seal ära veenma?")
                    jutt("just. see on ju aus\nkokkulepe? onju?",pop_norm,"park")
                    sinu_jutt("ega ma sellele otseselt\nvastu ole jah.")
                    sinu_jutt("ehk siis, mina pean\nainult panema selle tüübi\nmidagi proovima ja ma\nsaan endale uue sõiduki?")
                    jutt("justament.",pop_norm,"park")
                    sinu_jutt("miks sa sellise väga\nkallutatud ettepanekuga\nüldse lagedale tulid?\nmida sina sellest saad?")

                    jutt("no see on juba pikem jutt.\nma mõni teine kord\npajatan.",pop_norm,"park")
                    pilt("aga kuule... kas sa oled\nsiis nõus sellega?",pop_curious,["jah","ei"],"park")
                    if otsus == 1:
                        sinu_jutt("tead mis. ma võtan vastu\nsinu väljakutse. mulle tuleb\nplus üks mootoratas")
                        sinu_jutt("ja sulle üks ära moositud\nkuid kogenud nooruk.")
                        jutt("imeline. lihtsalt imeline.",pop_happy,"park")
                        jutt("eks ma soovin sulle siis\nkivi kotti, sõna otseses\nmõttes.",pop_happy,"park")
                        sinu_jutt("nagu mul oleks seda\nõnne vaja")
                        jutt("muiugi on. kuidas muidu\nsa eesmärki täidad",pop_happy,"park")
                        jutt("kuid nüüd,\nhüvasti mu kallis sõber\nkohtume veel teisesgi elus",pop_norm,"park")
                        sinu_jutt("kohtumiseni!")
                    elif otsus == 2:
                        sinu_jutt("see...see ei tundu olevat\nväga mõistlik. mängida nii\nteise inimesega.")
                        jutt("misasja?",pop_sad,"park")
                        jutt("no see on pettumust valmistav\naga eks see on sinu otsus\nikkagi.",pop_norm,"park")
                        sinu_jutt("on jah minu otsustada\nja mina otsustan et see\nei ole okei.")
                        jutt("ei ei ega ma ei hakka\npeale ka midagi suruma.\nlihtsalt oli idee.",pop_norm,"park")
                        sinu_jutt("noh ära suru siis. ")
                        jutt("ei surugi. noh siis kihlvedu\njääb katki. ja edasi ei\nsaa mängida seda mängu",pop_norm,"park")
                        jutt("sest siin mängus on vaja\net sa räägiksid selle teise\ntegelasega. aga aitüma mängimast\nja nüüd te siis teate mida teha\nkui tuleb taas valik",pop_norm,"park")
                        mangib = False
                        uks_nadal = False
                        break
                    ekraan.blit(mitmes_nadal, (0, 0))
                    nadala_tekst = tehniline_font.render(str(nadal), True, "white")
                    ekraan.blit(nadala_tekst, (400, 300))
                    pg.display.update()
                    pg.time.wait(3000)
                    jutt(" ",norm_mus,"kool")
                    sinu_jutt("hei!")
                    pilt("..?",norm_scared,["küsi muusika kohta","tutvusta ennast"],"kool")
                    if otsus == 1:
                        sinu_jutt("kuule aga mida sa siin\nkuulad?")
                        jutt("mitte midagi erilist.\nlihtsalt ´vennaskonna' vanu\nlugusid",norm_norm,"kool")
                        sinu_jutt("või kohe nii. kas sul\non ka mõni lemmik laul ka\nnende poolt?")
                        jutt("ma ei ütleks nii. kui just...",norm_norm,"kool")
                        sinu_jutt("kui just?")
                        pilt("mulle väga meeldb nende\nversioon sellest krokodill\nGena laulust",norm_norm,["krokodill gena?","laul meeldib","laul ei meeldi"],"kool")
                        if otsus == 1:
                            sinu_jutt("mis asi on krokodill Gena?")
                            jutt("..",norm_curious,"kool")
                            jutt("kas sa oled kuulnud midagi\npotsatajast?",norm_norm,"kool")
                            sinu_jutt("kus sa nüüd sellega.\nei ole isegi. mis see\nsiis on?")
                            jutt("üks väga armas\nnõukogudeaegne multikas, ma\nsoovitan sull sellega\ntutvuda. tõeliselt nostalgiline",norm_norm,"kool")
                            sinu_jutt("kui sa seda nii\npropageerid siis vast peab jah")
                        if otsus == 2:
                            sinu_jutt("oh vot see on üks\nkorralik laul ikka. ei\nei mulle ka väga meeldib\nsee.")
                            jutt("väga lahe. mulle endale\non ka see laul meeltmööda\nmeenutab mulle lihtsamaid\naegu",norm_happy,"kool")
                            sinu_jutt("kas siis nõukogudeajad\nolid lihtsamad ajad?")
                            jutt("ah ei mitte nii\nrohkem nagu lapsepõlv ja-",norm_norm,"kool")
                            jutt("see on lihtalt\neriline laul mulle.",norm_norm,"kool")
                            usaldus += 0.5
                        if otsus == 3:
                            sinu_jutt("hm. vaat nii lahe kui\nsee multikas ka polnud,\nmulle kunagi kuidagi see\nlaul ei istunud.")
                            sinu_jutt("meenutab neid vanu aegu.\nja kõike mis sellega kaasnes")
                            jutt("mnja. seda see teeb. kuid\nmulle just meenutab see\nlaul selle aja lihtsust.",norm_happy,"kool")
                            jutt("muidugi ma ei ütle, et need\nvanad ajad oled just head\nkuid mälestused sellest\najaperioodist tunduvad kuidagi...",norm_norm,"kool")
                            jutt("...lihtsad.",norm_norm,"kool")
                            sinu_jutt("eks kõik mälestused ole\nsellised. kõige lihtsamad\nversioonid päris tegevustest.")
                            sinu_jutt("vaena aju muud moodi ei\njõuaks neid ju hoiustada")
                    elif otsus == 2:
                        sinu_jutt("nii et...")
                        sinu_jutt("tere!")
                        jutt("tere?",norm_scared,"kool")
                        sinu_jutt("tead mis, ma pole pea\nüldse sinuga rääkinud\nkõikide meie jagatud\nkooliaastate vältel.")
                        sinu_jutt("niisiis täna ma lõhun selle\npikaajalise traditsiooni ja\nütlen sullegi tere")
                        jutt("miks just praegu? miks\njust nüüd?",norm_scared,"kool")
                        sinu_jutt("mis muu päev kui mitte\ntäna? tuli tuju ja \nvõttis kätte")
                    jutt("kuule. nii vägagi kui\nma seda vestlust ei\nnaudiks, ma pean nüüd\ntööd edasi tegema",norm_norm,"kool")
                    sinu_jutt("segan ma sind siis nii väga?")
                    jutt("mitte just seda...",norm_scared,"kool")
                    jutt("kuid harjumatu on et\nsinusugune minuga rääkima\nhakkas",norm_norm,"kool")
                    sinu_jutt("harjumatu...")
                    pilt("...",norm_norm,["reageeri solvunult","lohuta"],"kool")
                    if otsus == 1:
                        sinu_jutt("või kohe minusugused?")
                        jutt("...",norm_scared,"kool")
                        sinu_jutt("minusugused ehk siis?")
                        jutt("sellised, kes julgevad\nastuda igale võõrale ligi\nja alustada nendega vestlust",norm_norm,"kool")
                        sinu_jutt("arusaadav. arusaadav tõepoolest")
                    elif otsus == 2:
                        sinu_jutt("a.. ma vabandan, et\nma olen sulle sellise ilme\njätnud.")
                        jutt("ah ei ega see polegi\nmidagi mida sa saad muuta.\nsee on lihtsalt kuidas sa mulle\npaistad",norm_norm,"kool")
                        sinu_jutt("aga siiski, tahaksin\nseda muuta.")
                        jutt(" ",norm_happy,"kool")
                    #      test test test test test t
                    nadal += 1
                    uks_nadal = False

        elif nadal == 2:
            ekraan.blit(mitmes_nadal, (0, 0))
            nadala_tekst = tehniline_font.render(str(nadal), True, "white")
            ekraan.blit(nadala_tekst, (400, 300))
            pg.display.update()
            pg.time.wait(3000)
            uks_nadal = True
            if usaldus == 1:
                while uks_nadal:
                    pilt("ärka üles",norm_angry,["ei","ei","ei"],"universum")





#mäng
mang_jookseb = True
while mang_jookseb:
    menuu()
    mang()
    break