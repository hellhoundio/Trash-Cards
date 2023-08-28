import pygame as pg
import sys
import math as m
import time
from pildid import *

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
hall = (127,127,127)
must = (0,0,0)

tehniline_font = pg.font.SysFont('Courier New', 50, True)
tekst_font = pg.font.SysFont('Courier New', 20)
paks_tekst_font = pg.font.SysFont('Courier New', 20,bold=True)

#pildid

#pilt = pg.image.load("giphy.gif")
#pilt = pg.transform.scale(pilt,lehtede_dimensioonid)

#mäng kui definitsioonid
hetkene_tuju = norm_norm
hetkene_koht = "kool"
otsus = 0
paks = False
varu_paks = False
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
def automaatne_jargmine_rida(tekst,x,y,fsuurus,varv,paksus):
    n = 26
    chunks = []
    i = 0
    while i < len(tekst):
        if i + n < len(tekst):
            chunks.append(tekst[i:i + n])
        else:
            chunks.append(tekst[i:len(tekst)])
        i += n
    for i, l in enumerate(chunks):
        if paksus == True:
            ekraan.blit(paks_tekst_font.render(l, False, varv), (x, y + fsuurus * i))
        else:
            ekraan.blit(tekst_font.render(l, False, varv), (x, y + fsuurus * i))
def jutt(raakimine,tuju):
    global hetkene_tuju
    global hetkene_koht
    global paks
    hetkene_tuju = tuju

    ekraan.fill("light gray")
    ekraan.blit(tuju, (400, 100))
    ekraan.blit(layout, (0, 0))
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
        automaatne_jargmine_rida(raakimine[:mitmes_taht], 55, 150, 30, "black",paks)
        time.sleep(0.01)
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
                    automaatne_jargmine_rida(raakimine, 55, 150, 30, "black",paks)
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
            automaatne_jargmine_rida(raakimine, 55, 150, 30, "black",paks)
        elif paus_olek == False:
            ekraan.fill("light gray")
            ekraan.blit(tuju, (400, 100))
            ekraan.blit(layout, (0, 0))
            koha_tekst = tehniline_font.render(koht, True, "black")
            ekraan.blit(koha_tekst, (610, 10))
            nadala_tekst = tehniline_font.render(str(nadal), True, "black")
            ekraan.blit(nadala_tekst, (325, 15))
            automaatne_jargmine_rida(raakimine, 55, 150, 30, "black",paks)
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
def pilt(kusimus, tuju, valikud):
    global hetkene_tuju
    global otsus
    global paks
    otsus = 0
    hetkene_tuju = tuju
    jutt(kusimus,hetkene_tuju)
    pilt_jookseb = True
    valik = len(valikud)+1
    while pilt_jookseb:
        #taust
        paks = False
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
        automaatne_jargmine_rida(kusimus, 55,150,30,"black",paks)
        for x in range(len(valikud)):
            mitmes = x+1
            valitud_valik = "black"
            paks = False
            if valik == len(valikud)-1 or valik == len(valikud)*2+1:
                if mitmes == 1:
                    valitud_valik = hall
                    paks = True
                    otsus = 1
            elif valik == len(valikud)-2 or valik == len(valikud)*2:
                if mitmes == 2:
                    valitud_valik = hall
                    paks = True
                    otsus = 2
            elif valik == len(valikud)-3 or valik == len(valikud)*2-1:
                if mitmes == 3:
                    valitud_valik = hall
                    paks = True
                    otsus = 3
            automaatne_jargmine_rida(str(mitmes)+")"+valikud[x],50,380+x*60,30,must,paks)
            automaatne_jargmine_rida(str(mitmes) + ")" + valikud[x], 50, 380 + x * 60, 30, valitud_valik,varu_paks)
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
            koha_tekst = tehniline_font.render(koht, True, "black")
            ekraan.blit(koha_tekst, (610, 10))
            nadala_tekst = tehniline_font.render(str(nadal), True, "black")
            ekraan.blit(nadala_tekst, (325, 15))
        if paus_olek == False:
            ekraan.fill("light gray")
            ekraan.blit(hetkene_tuju, (400, 100))
            ekraan.blit(layout, (0, 0))
            koha_tekst = tehniline_font.render(koht, True, "black")
            ekraan.blit(koha_tekst, (610, 10))
            nadala_tekst = tehniline_font.render(str(nadal), True, "black")
            ekraan.blit(nadala_tekst, (325, 15))
        mitmes_taht += 1
        automaatne_jargmine_rida(raakimine[:mitmes_taht], 55, 380, 30, "black",paks)
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
                    automaatne_jargmine_rida(raakimine, 55, 380, 30, "black",paks)
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

                    jutt("ou lükka friikat aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",pop_norm)
                    sinu_jutt("käi persse minu omad")
                    jutt("ja siis? nagu mind huvitaks",pop_curious)
                    sinu_jutt("no eks sa siis võta kui nii väga soovid")
                    jutt("võtangi noh.",pop_norm)
                    jutt("...",pop_curious)
                    sinu_jutt("... mida sa veel tahad?")
                    jutt("kas sa oled juba mõelnud sellele pakkumisele?",pop_curious)
                    sinu_jutt("pakkumine? mis ajast oled sina mulle üldse midagi niisama pakkunud?")
                    jutt("ei lollakas. mitte selles mõttes. rohkem nagu see...",pop_norm)
                    jutt("see väljakutse, kui seda võib nii kutsuda. see asi.",pop_norm)
                    sinu_jutt("palun aga värseknda minu\nmälu, sest ma tõepoolest\nei tea millest sa räägid")
                    jutt("noo...",pop_norm)
                    jutt("okei nii. ma vean sinuga\nkihla et sa ei suuda\nveenda seda venda seal\nendaga aineid tarbima.",pop_norm)
                    sinu_jutt("aaaa see asi. ja mis\nsiis? mis mina sellest\nsaan?")
                    jutt("noo kui sa päriselt suudad\nseda teha, mida sa\nmuide absoluutselt ei\nsuuda, siis sa saaksid\nendale kohe päris oma",pop_norm)
                    jutt("mootoratta. see vana romu\nmida sa oled koguaeg\nsilmanud seal minu aias.\nniitideta diil selline.",pop_happy)
                    sinu_jutt("oh sa...")
                    sinu_jutt("see isegi...see isegi\noleks ju midagi. ja\nma pean lihtsalt selle\nvennikese seal ära veenma?")
                    jutt("just. see on ju aus\nkokkulepe? onju?",pop_norm)
                    sinu_jutt("ega ma sellele otseselt\nvastu ole jah.")
                    sinu_jutt("ehk siis, mina pean\nainult panema selle tüübi\nmidagi proovima ja ma\nsaan endale uue sõiduki?")
                    jutt("justament.",pop_norm)
                    sinu_jutt("miks sa sellise väga\nkallutatud ettepanekuga\nüldse lagedale tulid?\nmida sina sellest saad?")

                    jutt("no see on juba pikem jutt.\nma mõni teine kord\npajatan.",pop_norm)
                    pilt("aga kuule... kas sa oled\nsiis nõus sellega?",pop_curious,["jah","ei"])
                    if otsus == 1:
                        sinu_jutt("tead mis. ma võtan vastu\nsinu väljakutse. mulle tuleb\nplus üks mootoratas")
                        sinu_jutt("ja sulle üks ära moositud\nkuid kogenud nooruk.")
                        jutt("imeline. lihtsalt imeline.",pop_happy)
                        jutt("eks ma soovin sulle siis\nkivi kotti, sõna otseses\nmõttes.",pop_happy)
                        sinu_jutt("nagu mul oleks seda\nõnne vaja")
                        jutt("muiugi on. kuidas muidu\nsa eesmärki täidad",pop_happy)
                        jutt("kuid nüüd,\nhüvasti mu kallis sõber\nkohtume veel teisesgi elus",pop_norm)
                        sinu_jutt("kohtumiseni!")
                    elif otsus == 2:
                        sinu_jutt("see...see ei tundu olevat\nväga mõistlik. mängida nii\nteise inimesega.")
                        jutt("misasja?",pop_sad)
                        jutt("no see on pettumust valmistav\naga eks see on sinu otsus\nikkagi.",pop_norm)
                        sinu_jutt("on jah minu otsustada\nja mina otsustan et see\nei ole okei.")
                        jutt("ei ei ega ma ei hakka\npeale ka midagi suruma.\nlihtsalt oli idee.",pop_norm)
                        sinu_jutt("noh ära suru siis. ")
                        jutt("ei surugi. noh siis kihlvedu\njääb katki. ja edasi ei\nsaa mängida seda mängu",pop_norm)
                        jutt("sest siin mängus on vaja\net sa räägiksid selle teise\ntegelasega. aga aitüma mängimast\nja nüüd te siis teate mida teha\nkui tuleb taas valik",pop_norm)
                        mangib = False
                        uks_nadal = False
                        break
                    ekraan.blit(mitmes_nadal, (0, 0))
                    nadala_tekst = tehniline_font.render(str(nadal), True, "white")
                    ekraan.blit(nadala_tekst, (400, 300))
                    pg.display.update()
                    pg.time.wait(3000)
                    jutt(" ",norm_mus)
                    sinu_jutt("hei!")
                    pilt("..?",norm_scared,["küsi muusika kohta","tutvusta ennast"])
                    if otsus == 1:
                        sinu_jutt("kuule aga mida sa siin\nkuulad?")
                        jutt("mitte midagi erilist.\nlihtsalt ´vennaskonna' vanu\nlugusid",norm_norm)
                        sinu_jutt("või kohe nii. kas sul\non ka mõni lemmik laul ka\nnende poolt?")
                        jutt("ma ei ütleks nii. kui just...",norm_norm)
                        sinu_jutt("kui just?")
                        pilt("mulle väga meeldb nende\nversioon sellest krokodill\nGena laulust",norm_norm,["krokodill gena?","laul meeldib","laul ei meeldi"])
                        if otsus == 1:
                            sinu_jutt("mis asi on krokodill Gena?")
                            jutt("..",norm_curious)
                            jutt("kas sa oled kuulnud midagi\npotsatajast?",norm_norm)
                            sinu_jutt("kus sa nüüd sellega.\nei ole isegi. mis see\nsiis on?")
                            jutt("üks väga armas\nnõukogudeaegne multikas, ma\nsoovitan sull sellega\ntutvuda. tõeliselt nostalgiline",norm_norm)
                            sinu_jutt("kui sa seda nii\npropageerid siis vast peab jah")
                        if otsus == 2:
                            sinu_jutt("oh vot see on üks\nkorralik laul ikka. ei\nei mulle ka väga meeldib\nsee.")
                            jutt("väga lahe. mulle endale\non ka see laul meeltmööda\nmeenutab mulle lihtsamaid\naegu",norm_happy)
                            sinu_jutt("kas siis nõukogudeajad\nolid lihtsamad ajad?")
                            jutt("ah ei mitte nii\nrohkem nagu lapsepõlv ja-",norm_norm)
                            jutt("see on lihtalt\neriline laul mulle.",norm_norm)
                            usaldus += 0.5
                        if otsus == 3:
                            sinu_jutt("hm. vaat nii lahe kui\nsee multikas ka polnud,\nmulle kunagi kuidagi see\nlaul ei istunud.")
                            sinu_jutt("meenutab neid vanu aegu.\nja kõike mis sellega kaasnes")
                            jutt("mnja. seda see teeb. kuid\nmulle just meenutab see\nlaul selle aja lihtsust.",norm_happy)
                            jutt("muidugi ma ei ütle, et need\nvanad ajad oled just head\nkuid mälestused sellest\najaperioodist tunduvad kuidagi...",norm_norm)
                            jutt("...lihtsad.",norm_norm)
                            sinu_jutt("eks kõik mälestused ole\nsellised. kõige lihtsamad\nversioonid päris tegevustest.")
                            sinu_jutt("vaena aju muud moodi ei\njõuaks neid ju hoiustada")
                    elif otsus == 2:
                        sinu_jutt("nii et...")
                        sinu_jutt("tere!")
                        jutt("tere?",norm_scared)
                        sinu_jutt("tead mis, ma pole pea\nüldse sinuga rääkinud\nkõikide meie jagatud\nkooliaastate vältel.")
                        sinu_jutt("niisiis täna ma lõhun selle\npikaajalise traditsiooni ja\nütlen sullegi tere")
                        jutt("miks just praegu? miks\njust nüüd?",norm_scared)
                        sinu_jutt("mis muu päev kui mitte\ntäna? tuli tuju ja \nvõttis kätte")
                    jutt("kuule. nii vägagi kui\nma seda vestlust ei\nnaudiks, ma pean nüüd\ntööd edasi tegema",norm_norm)
                    sinu_jutt("segan ma sind siis nii väga?")
                    jutt("mitte just seda...",norm_scared)
                    jutt("kuid harjumatu on et\nsinusugune minuga rääkima\nhakkas",norm_norm)
                    sinu_jutt("harjumatu...")
                    pilt("...",norm_norm,["reageeri solvunult","lohuta"])
                    if otsus == 1:
                        sinu_jutt("või kohe minusugused?")
                        jutt("...",norm_scared)
                        sinu_jutt("minusugused ehk siis?")
                        jutt("sellised, kes julgevad\nastuda igale võõrale ligi\nja alustada nendega vestlust",norm_norm)
                        sinu_jutt("arusaadav. arusaadav tõepoolest")
                    elif otsus == 2:
                        sinu_jutt("a.. ma vabandan, et\nma olen sulle sellise ilme\njätnud.")
                        jutt("ah ei ega see polegi\nmidagi mida sa saad muuta.\nsee on lihtsalt kuidas sa mulle\npaistad",norm_norm)
                        sinu_jutt("aga siiski, tahaksin\nseda muuta.")
                        jutt(" ",norm_happy)
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
                    pilt("ärka üles",norm_angry,["ei","ei","ei"])
