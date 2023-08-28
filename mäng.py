import sys
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
    hetkene_koht = "kool"
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
            koha_tekst = tehniline_font.render(hetkene_koht, True, "black")
            ekraan.blit(koha_tekst, (610, 10))
            nadala_tekst = tehniline_font.render(str(nadal), True, "black")
            ekraan.blit(nadala_tekst, (325, 15))
        if paus_olek == False:
            ekraan.fill("light gray")
            ekraan.blit(tuju, (400, 100))
            ekraan.blit(layout, (0, 0))
            koha_tekst = tehniline_font.render(hetkene_koht, True, "black")
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
            koha_tekst = tehniline_font.render(hetkene_koht, True, "black")
            ekraan.blit(koha_tekst, (610, 10))
            nadala_tekst = tehniline_font.render(str(nadal), True, "black")
            ekraan.blit(nadala_tekst, (325, 15))
            automaatne_jargmine_rida(raakimine, 55, 150, 30, "black",paks)
        elif paus_olek == False:
            ekraan.fill("light gray")
            ekraan.blit(tuju, (400, 100))
            ekraan.blit(layout, (0, 0))
            koha_tekst = tehniline_font.render(hetkene_koht, True, "black")
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
        koha_tekst = tehniline_font.render(hetkene_koht, True, "black")
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
        paks = False
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
    prom = False
    help = False
    dancing = False
    story = False
    while mangib:
        #nädal 1
        uks_nadal = True
        if nadal == 1:
            if usaldus == 1:
                while uks_nadal:
                    jutt(" ", pop_norm)
                    sinu_jutt(" ")
                    jutt("hey! heyyyy! over here!",pop_norm)
                    sinu_jutt("yeah? What’s up man?")
                    jutt("So, i have a proposal for you.",pop_norm)
                    sinu_jutt("listen, i cant keep trading my homework for your lunches. You cant become so reliant on those kinds of things")
                    jutt("wow wow, who told you that i forgot about the history assignment today",pop_norm)
                    sinu_jutt("no one, but thats just how these things usually go")
                    jutt("well not today amigo. I have some sandwich news for you",pop_norm)
                    sinu_jutt("well shoot")
                    jutt("so, good news, you get to go with someone else to the prom, yay!",pop_norm)
                    sinu_jutt("eh? what? the prom that’s this friday?")
                    jutt("exactly! Because, unfortunate news, I can’t go with you",pop_norm)
                    sinu_jutt("dude.")
                    jutt("But but, now some more good news, I got asked out! And I couldn’t really refuse because..",pop_norm)
                    sinu_jutt("Because?")
                    jutt("It was Lydia, you know, my crush of some sorts",pop_norm)
                    sinu_jutt("Bummer..")
                    jutt("But that’s where the proposal comes in, I want you to ask Lydias sister Misty to go with you",pop_norm)
                    sinu_jutt("Let me get this straight, you blow me off and then want me to ask a girl, that I’ve never talked to, out to for the prom?")
                    pilt("Yes. you are correct",pop_norm,["act offended","agree with the plan"])
                    if otsus == 1:
                        sinu_jutt("what do you take me for, a chaparone? an escort?")
                        jutt("Listen listen, I have good motive for this. It’s doing me and lydia a favor but also you because we do go together every year and it be good to.. free you up?",pop_norm)
                        sinu_jutt("You’re so full of shit.")
                        jutt("Fine. it may be so. But if you do, I’ll give you something to be grateful for", pop_norm)
                        sinu_jutt("and that would be?")
                        jutt("My old motorcycle! So you wouldn’t have to come by bus every morning.", pop_norm)
                        sinu_jutt("Wait you’re for real?")
                        jutt("cross my heart and hope to die", pop_norm)
                        sinu_jutt("and better stick a needle in yoiur eye as well while you’re at it")
                        jutt("hey! that’ s mean.", pop_norm)
                        sinu_jutt("and you aren’t ?")
                        jutt("toche. but i’m getting a new ride anyways and I have nothing to do with three vehicles",pop_norm)
                        sinu_jutt("Can’t imagine why.")
                        jutt("And my heart would be at ease knowing it’s in trusted hands.", pop_norm)
                        sinu_jutt("ugh")
                        pilt("pleaseeeee?", pop_norm,["yes","no"])
                        if otsus == 1:
                            sinu_jutt("Well everyone else already have dates so, i guess i’ll give it a shot")
                            jutt("thats the spirit", pop_norm)
                            sinu_jutt(" I better get ahead of my game then, do you know where she’s at?")
                            jutt("The last i cheked, misty is sitting on the brick wall at the moment", pop_norm)
                            sinu_jutt("good to know. well give me the boot and wish me luck, im off")
                            jutt("Good luck! You can do it", pop_norm)
                        elif otsus == 2:
                            sinu_jutt("but.. it feels wrong")
                            jutt("what does? You asking out someone who clearly never parties?", pop_norm)
                            jutt("you’re doing them a favor!", pop_norm)
                            sinu_jutt("am i really though? I’ m still a bit bummed i cant go with you")
                            jutt("so am i, but that life.  please? just this once?", pop_norm)
                            sinu_jutt("I just might go solo for this one pal")
                            jutt("well it was worth asking.", pop_norm)
                            sinu_jutt("am i still getting the motorcycle or-")
                            jutt("not even in your dreams", pop_norm)
                            sinu_jutt("fair game.")
                            jutt("yeah well, happens.", pop_norm)
                            mangib = False
                            uks_nadal = False
                            break
                    elif otsus == 2:
                        sinu_jutt("Well I guess, a new friend wouldn´t hurt?")
                        jutt(
                            "That’s the spirit! Take it as a challenge perhaps because Misty was never the party goer type.",
                            pop_norm)
                        sinu_jutt("So this is just an extra hard task for me?")
                        jutt("Yeah...", pop_norm)
                        jutt("But but, if you do do it, I’ll give you my old motorcycle for your efforts", pop_norm)
                        sinu_jutt("wait, are you for real?")
                        jutt("cross my heart and hope to die", pop_norm)
                        sinu_jutt("well shit. now i might even consider taking you up on that offer")
                        jutt(
                            "Yes! please do. I’m getting a new ride anyways and what does a girl do with three bikes anyways.",
                            pop_norm)
                        sinu_jutt("I’m too poor to even fathom owning anything like that")
                        jutt(
                            "That’s why I’m here. Besides, you’ll not only be doing me and yourself a favor but also Lydia because she kind of asked me to set this thing up",
                            pop_norm)
                        sinu_jutt(" you sneaky bastard")
                        jutt(
                            "Thank you in advance. But i suggest you to start scheming a masterplan because the prom is indeed in four days.",
                            pop_norm)
                        sinu_jutt(
                            "Look at you bossing me around, but you're right. Do you know where misty is right now?")
                        jutt("I believe she’s at the brick wall the last i checked.", pop_norm)
                        sinu_jutt("Thanks. I guess I'll go shoot my shot then.")
                        jutt("Good luck! and again, thank you again", pop_norm)

                    ekraan.blit(mitmes_nadal, (0, 0))
                    nadala_tekst = tehniline_font.render(str(nadal), True, "white")
                    ekraan.blit(nadala_tekst, (400, 300))
                    koha_tekst = tehniline_font.render(hetkene_koht, True, "black")
                    ekraan.blit(koha_tekst, (610, 10))
                    pg.display.update()
                    pg.time.wait(1500)

                    sinu_jutt("hey! misty right?")
                    jutt("?", norm_write)
                    sinu_jutt("i’m-")
                    jutt("i know who you are.", norm_write)
                    sinu_jutt("awesome, less introductions")
                    pilt("...", norm_write,["prom?","homework?"])
                    if otsus == 1:
                        prom = True
                        sinu_jutt("so, let me get right to it. I’d like to ask you out for prom")
                        jutt("why?", norm_write)
                        sinu_jutt("well i dont have a date for it and to my knowledge you don’t either")
                        jutt("I don’t. and don’t need one either", norm_write)
                        sinu_jutt("how come?")
                        jutt("I’m simply not going. So you can go off to pester some other poor soul ", norm_write)
                        sinu_jutt("am i really pestering you?")
                        jutt("not yet but probably soon it will come to it", norm_write)
                        sinu_jutt("I’ll try my best not to then")
                        jutt("or just don’t", norm_write)
                        sinu_jutt("why so hostile?")
                        jutt("i have no reason to bother being nice", norm_write)
                        sinu_jutt("but if i make it worth the bother?")
                        pilt("guess we’ll wait and see", norm_write,["writing?","why not prom"])
                        if otsus == 1:
                            sinu_jutt("what will you do in the meanwhile then?")
                            jutt("in the meanwhile I'll be working on the assignment", norm_write)
                            sinu_jutt("Oh, the one for the history class?")
                            pilt("you’re correct", norm_write,["prom night plans?","help with homework"])
                            if otsus == 1:
                                sinu_jutt("what were your plans for the prom night then?")
                                jutt("Just go home and watch a movie most likely", norm_write)
                                sinu_jutt("Instead of going to prom?")
                                jutt("There’s always next year. Maybe my sister won’t ditch me then", norm_write)
                                sinu_jutt("Well i know how you feel. My friend left me hanging as well")
                                jutt("You mean your Friend? The one Lydia asked out?", norm_write)
                                sinu_jutt("Yeah that one")
                                jutt("hm.", norm_write)
                                sinu_jutt("And just because you couln’t go with your sister, you’re not going at all?")
                                jutt("I’m not a party person. never was never will be. She convinced me to go",
                                     norm_write)
                                sinu_jutt("see? you were convinced once so why not again?")
                                jutt("fool me once, shame on you, fool me twice, shame on me", norm_write)
                                sinu_jutt(
                                    "that’s true. But why not take the chance again? I mean there are only so many proms you get to attend")
                                jutt("and those are plenty. if i even go to those", norm_write)
                                sinu_jutt("and let this be one of the plenty and go with me")
                                jutt("we’ll see", norm_write)
                                jutt("I have to get to class so good luck convincing anyone else to go with you",
                                     norm_write)
                                sinu_jutt("i’ve got my eyes set on the target")
                                jutt("good for you", norm_write)
                                sinu_jutt("I’ll come by tomorrow as well")
                                jutt("You do that, I have to get to class. ", norm_write)
                                sinu_jutt("well, bye!")
                                jutt("bye.", norm_write)
                                nadal += 1
                                uks_nadal = False
                            elif otsus == 2:
                                help = True
                                sinu_jutt(" do you think you’ll need any help with that?")
                                jutt("as in, you don’t believe i can do it myself?", norm_write)
                                sinu_jutt(
                                    "no not that, just mine is already finished and it would be easier for you to have a reference of some sorts")
                                jutt("well-", norm_write)
                                sinu_jutt("there")
                                jutt("well.. thank you", norm_write)
                                sinu_jutt("you’re the most welcome.")
                                jutt("didn’t take you for someone who did all their homework", norm_write)
                                sinu_jutt(
                                    "heh, the thing is, that i usually let Friend copy off of me and she’ll give me her lunch")
                                jutt("ohh, you’re a friend of Friends then?", norm_write)
                                sinu_jutt("that i am")
                                jutt("the girl my sister abandoned me for?", norm_write)
                                sinu_jutt("that’s the one")
                                jutt(" good to know", norm_write)
                                sinu_jutt(
                                    "if it helps then for your information, Friend blew me off as well. we we’re supposed to go together")
                                jutt("I know exactly how you feel", norm_write)
                                sinu_jutt("so why don’t we get revenge and go together?")
                                jutt("because I don’t really know you", norm_write)
                                sinu_jutt("we still have three days to get to know each other")
                                jutt("one less if you consider today, which I do.", norm_write)
                                sinu_jutt(
                                    "But think about it, how many proms are you going to get anyways in your life time?")
                                jutt("The prom happens every year.", norm_write)
                                sinu_jutt(
                                    "See? more the reason you should try going with someone else. If you don’t like it you can always ditch the next ones")
                                jutt("I’ll think about it", norm_write)
                                sinu_jutt("That’s good, I’ll keep on trying")
                                jutt("do try.", norm_write)
                                jutt(
                                    "But do that tomorrow as I’m going to head to class now. Thank you for the homework.",
                                    norm_write)
                                sinu_jutt("Thanks for taking a chance on me")
                                jutt("I said i’ll think about it", norm_write)
                                sinu_jutt(
                                    "well tomorrow you will have thought about it and my chances grow with each passing day")
                                jutt("see you tomorrow then", norm_write)
                                sinu_jutt("Bye then")
                                nadal += 1
                                uks_nadal = False
                                usaldus = 2
                        elif otsus == 2:
                            sinu_jutt("why don’ you want to go?")
                            jutt("well my sister, who i was supposed to go with, ditched me for some other girl",
                                 norm_write)
                            sinu_jutt(
                                "well what a coincidence, the same thing happened to me. But in my case it was just a friend.")
                            jutt("are you a friend of... Friends?", norm_write)
                            sinu_jutt("The one and only")
                            jutt("good to know", norm_write)
                            sinu_jutt("you know her?")
                            jutt("I know of her. Lydia has told me some things", norm_write)
                            sinu_jutt("oo i wanna know, tell me")
                            jutt("I’m not up for gossip", norm_write)
                            sinu_jutt("It’s not gossip. It’s relaying information")
                            jutt(
                                "All you need to know is that my sister has liked Friend for a while now and i encouraged her to do something about it",
                                norm_write)
                            sinu_jutt("and look where you ended up")
                            jutt("you’re not really in a better situation", norm_write)
                            sinu_jutt("true. that’s why we have to team up and go together, you know, to get revenge")
                            jutt("how would that help anything", norm_write)
                            sinu_jutt(
                                "well, you’ll get to have fun and she’ll be jealous because you’re having so much fun without her")
                            pilt(
                                "I think it will only assure her that she did the right thing and that i’m fine by myself",
                                norm_write,["you're not fine by yourself?","try it though"])
                            if otsus == 1:
                                sinu_jutt("are you not by yourself then?")
                                jutt("kind of a personal question", norm_write)
                                sinu_jutt("you brought it up")
                                jutt("and you pointed it out", norm_write)
                                sinu_jutt("because im curious. and im on a mission")
                                jutt("mission being?", norm_write)
                                sinu_jutt("convincing you to go to prom with me")
                                jutt("feel a bit invasive, don’t you think?", norm_write)
                                sinu_jutt(
                                    "perhaps. but now back to the topic at hand, why don’t you want your sister to think you’ll be alright by yourself?")
                                jutt("i dont think im comfortable sharing that with you", norm_write)
                                jutt("i still don’t know you", norm_write)
                                sinu_jutt("that’s my bad. but you’re not asking about me either")
                                jutt("my mistake.", norm_write)
                                jutt("but not really, you’re the one to initiate the conversation", norm_write)
                                sinu_jutt("conversation is a two way street")
                                jutt("depends", norm_write)
                                sinu_jutt("depends?")
                                jutt("depends on how invested the people are in the conversation", norm_write)
                                sinu_jutt("but so far so good? you haven’t ignored me so i take it as a win")
                                jutt("if you so wish. ", norm_write)
                                sinu_jutt("well i do want to keep getting to know you so i will")
                                jutt("you’re persistent, aren’t you?", norm_write)
                                sinu_jutt("you’re the judge")
                                jutt("maybe some other day, i’ll have to get to class", norm_write)
                                sinu_jutt("will you be here tomorrow?")
                                jutt("will you be?", norm_write)
                                sinu_jutt("for sure")
                                jutt("then i guess we’ll see tomorrow", norm_write)
                                sinu_jutt("see you")
                                jutt("bye", norm_write)
                                uks_nadal = False
                                nadal += 1
                                usaldus = 2
                            elif otsus == 2:
                                sinu_jutt(
                                    " and if you end up being fine then you’ll have found a new way to have fun, where´s the downside?")
                                jutt(
                                    "that maybe i wont be fine. Maybe i wont like the prom at all and will have a worse time than i would’ve had at home",
                                    norm_write)
                                sinu_jutt("and then you’ll know not to go next year! easy")
                                jutt(
                                    "why risk it. the possibility of me liking it will still exist if i dont go, if i do then it will be a certainty",
                                    norm_write)
                                sinu_jutt("isn’t it worth it for the knowledge?")
                                jutt("maybe, maybe not. i didn’t plan on giving it a second thought", norm_write)
                                sinu_jutt("now perhaps you will")
                                jutt("thanks to you, ive had to. and i still side with a comfortable movie night",
                                     norm_write)
                                sinu_jutt("can i try to convince you otherwise?")
                                jutt("I have a feeling you will try to that nonetheless", norm_write)
                                sinu_jutt("that’s true.")
                                jutt("but your efforts are better waste on someone else, i’ve got to go to class",
                                     norm_write)
                                sinu_jutt("will you be here tomorrow?")
                                jutt("most likely. and im assuming you as well?", norm_write)
                                sinu_jutt("certainly")
                                jutt("well then see you later", norm_write)
                                sinu_jutt("bye misty!")
                                uks_nadal = False
                                nadal += 1
                    elif otsus == 2:
                        sinu_jutt("what are you working on?")
                        jutt("history assignment", norm_write)
                        sinu_jutt("that’s exciting")
                        pilt("to some, perhaps.", norm_write,["help with homework","do you like history?"])
                        if otsus == 1:
                            help = True
                            sinu_jutt("well mine is finished so, if you want to you could take it as a reference")
                            jutt("do you think i can’t do it by myself?", norm_write)
                            sinu_jutt("oh no, not that. just thought it might be helpful")
                            jutt("no need.", norm_write)
                            sinu_jutt("if you say so")
                            sinu_jutt("But if you do need any assistance then i’d love to help.")
                            jutt("I’m sure a teacher would be just fine", norm_write)
                            sinu_jutt("True that is an option, but i’ve been told i’m an excellent tutor")
                            jutt("I don’t need your help", norm_write)
                            sinu_jutt("Alright, i understand")
                            pilt("good", norm_write,["do you like history?","what are your hobbies?"])
                            if otsus == 2:
                                sinu_jutt("so what are your hobbies?")
                                jutt("why do you care to ask?", norm_write)
                                sinu_jutt("just want to get to know you more")
                                pilt("the reason being?", norm_write,["lie","be honest"])
                                if otsus == 1:
                                    sinu_jutt(
                                        "i just haven’t talked to you at all and we’ve been in the same year for ages now so why not")
                                    jutt("plenty of reasons why not to", norm_write)
                                    sinu_jutt("such as?")
                                    jutt("we’ve never talked before, why start now?", norm_write)
                                    sinu_jutt("for the exact same reason. why not get some more friends")
                                    jutt("and you think we’ll ever be that, friends?", norm_write)
                                    sinu_jutt("there’s always a chance")
                                    jutt("a slim one", norm_write)
                                    sinu_jutt("but it’s still there")
                                    jutt("sure", norm_write)
                                    sinu_jutt("would you be against some conversation with me?")
                                    jutt("no not that. just that i don’t usually get approached like that",
                                         norm_write)
                                    sinu_jutt("like what?")
                                    jutt("no one really approaches me with the intention to be friends", norm_write)
                                    sinu_jutt("well they should, they’re missing out")
                                    jutt("really? like what?", norm_write)
                                    sinu_jutt("that’s what im here to find out")
                                    jutt("so you spoke out of turn as you don’t know me yourself", norm_write)
                                    sinu_jutt("maybe only a little")
                                    jutt("or maybe a lot", norm_write)
                                    sinu_jutt("alright then. tell me about yourself then")
                                    jutt("Maybe some other time, I’ve got to get to class", norm_write)
                                    sinu_jutt("Will you be here tomorrow?")
                                    jutt("Sure", norm_write)
                                    sinu_jutt("Awesome, I’ll ask you about it then!")
                                    jutt("If I can’t avoid it then sure", norm_write)
                                    sinu_jutt("See you later!")
                                    jutt("Bye", norm_write)
                                    nadal += 1
                                    uks_nadal = False
                                elif otsus == 2:
                                    sinu_jutt("well I kind of lost my date for the prom")
                                    jutt("who?", norm_write)
                                    sinu_jutt("Friend")
                                    jutt("ohh. I might know why", norm_write)
                                    sinu_jutt("do tell")
                                    jutt("my sister Lydia asked her out", norm_write)
                                    sinu_jutt("oh darn it.")
                                    jutt("things like that happen", norm_write)
                                    sinu_jutt("that’s true. but now I've got no one to go with")
                                    jutt("me neither", norm_write)
                                    sinu_jutt("just an idea, let’s go together then?")
                                    jutt("uh.. no?", norm_write)
                                    sinu_jutt("why not?")
                                    jutt("I don’t know you", norm_write)
                                    sinu_jutt("there’s still four days ahead of us, maybe i’ll convince you otherwise")
                                    jutt("hardly", norm_write)
                                    sinu_jutt("doesn’t hurt to try")
                                    jutt("depends", norm_write)
                                    sinu_jutt("depends on what?")
                                    jutt("if the convincing part will be annoying or not", norm_write)
                                    sinu_jutt("I’ll try my best to not make it so")
                                    jutt("go on. i don’t think i can stop you", norm_write)
                                    sinu_jutt("well thank you, i will try")
                                    jutt("but you have to do that tomorrow, i’ve got to go to class", norm_write)
                                    sinu_jutt("well will you be here tomorrow?")
                                    jutt("most likely", norm_write)
                                    sinu_jutt("awesome, i’ll see you then?")
                                    jutt("most probably", norm_write)
                                    sinu_jutt("bye misty!")
                                    jutt("bye", norm_write)
                                    nadal += 1
                                    uks_nadal = False
                            elif otsus == 1:
                                sinu_jutt("do you like history?")
                                jutt("In general or the subject?", norm_write)
                                sinu_jutt(" let’s say the subject")
                                jutt("i’m fond of it.", norm_write)
                                sinu_jutt("how come?")
                                jutt(
                                    "i like listening to the teacher. reminds me of bed time stories. just with less loopholes",
                                    norm_write)
                                sinu_jutt(
                                    "that sounds sweet. i think the best way to learn about history is to listen someone tell you about it")
                                jutt("i agree. though it’s not always the most reliable.", norm_write)
                                sinu_jutt(
                                    "to some extent nothing is about history. we only know a fraction of the real events")
                                jutt("so there´s always something more to discover", norm_write)
                                sinu_jutt("that’s for certain")
                                jutt("but researching something unattainable really isn’t my style", norm_write)
                                sinu_jutt("what then?")
                                jutt("writing. sure it’s limitless but it can be whatever you decide for it to be",
                                     norm_write)
                                sinu_jutt("oh, so creative writing?")
                                jutt("more or less", norm_write)
                                sinu_jutt(
                                    "i’ve always found myself enjoying writing about some clear subject easier.  there is a clear direction, more tangible")
                                jutt("guess i like to stroll more than follow a fixed path", norm_write)
                                sinu_jutt("do you have any creative pieces to showcase?")
                                jutt("I do.", norm_write)
                                sinu_jutt("can i read them?")
                                jutt("I don’t have them with me", norm_write)
                                sinu_jutt("how about later?")
                                jutt("we’ll see.", norm_write)
                                sinu_jutt("i’ll look forward to it")
                                jutt("well you’ll have to wait quite a bit as i’m off to class", norm_write)
                                sinu_jutt("will you be here tomorrow?")
                                jutt("most likely", norm_write)
                                sinu_jutt("I’ll come by and say hi then")
                                jutt("I’m sure you will. But bye until then", norm_write)
                                sinu_jutt("Bye!")
                                uks_nadal = False
                                nadal += 1
                                usaldus = 2
                        elif otsus == 2:
                            sinu_jutt("do you like history?")
                            jutt("In general or the subject?", norm_write)
                            sinu_jutt(" let’s say the subject")
                            jutt("i’m fond of it.", norm_write)
                            sinu_jutt("how come?")
                            jutt(
                                "i like listening to the teacher. reminds me of bed time stories. just with less loopholes",
                                norm_write)
                            sinu_jutt(
                                "that sounds sweet. i think the best way to learn about history is to listen someone tell you about it")
                            jutt("i agree. though it’s not always the most reliable.", norm_write)
                            sinu_jutt(
                                "to some extent nothing is about history. we only know a fraction of the real events")
                            jutt("so there´s always something more to discover", norm_write)
                            sinu_jutt("that’s for certain")
                            jutt("but researching something unattainable really isn’t my style", norm_write)
                            sinu_jutt("what then?")
                            jutt("writing. sure it’s limitless but it can be whatever you decide for it to be",
                                 norm_write)
                            sinu_jutt("oh, so creative writing?")
                            jutt("more or less", norm_write)
                            sinu_jutt(
                                "i’ve always found myself enjoying writing about some clear subject easier.  there is a clear direction, more tangible")
                            jutt("guess i like to stroll more than follow a fixed path", norm_write)
                            sinu_jutt("do you have any creative pieces to showcase?")
                            jutt("I do.", norm_write)
                            sinu_jutt("can i read them?")
                            jutt("I don’t have them with me", norm_write)
                            sinu_jutt("how about later?")
                            jutt("we’ll see.", norm_write)
                            sinu_jutt("i’ll look forward to it")
                            jutt("well you’ll have to wait quite a bit as i’m off to class", norm_write)
                            sinu_jutt("will you be here tomorrow?")
                            jutt("most likely", norm_write)
                            sinu_jutt("I’ll come by and say hi then")
                            jutt("I’m sure you will. But bye until then", norm_write)
                            sinu_jutt("Bye!")
                            uks_nadal = False
                            nadal += 1
                            usaldus = 2
        elif nadal == 2:
            ekraan.blit(mitmes_nadal, (0, 0))
            nadala_tekst = tehniline_font.render(str(nadal), True, "white")
            ekraan.blit(nadala_tekst, (400, 300))
            koha_tekst = tehniline_font.render(hetkene_koht, True, "black")
            ekraan.blit(koha_tekst, (610, 10))
            pg.display.update()
            pg.time.wait(1500)
            if usaldus == 1:
                while uks_nadal == True:
                    sinu_jutt("heyy!")
                    jutt("and there you are again", norm_write)
                    sinu_jutt("just like i promised")
                    jutt("didn’t think you’d bother", norm_write)
                    sinu_jutt("well i dont give up that easy")
                    jutt("i can see that yes", norm_write)
                    sinu_jutt("so what are you up to?")
                    jutt("writing", norm_write)
                    sinu_jutt("whatcha writing?")
                    jutt("still the history assignment", norm_write)
                    sinu_jutt("oh that’s tough")
                    pilt("it really is", norm_write,["need any help?","what are your hobbies?"])
                    if otsus == 1:
                        if help == True:
                            sinu_jutt("well mine is finished so if you’d like you could have it for a reference")
                            jutt("you think I can’t do it by myself?", norm_write)
                            sinu_jutt("no not that, it would just maybe be a little helpful")
                        elif help == False:
                            sinu_jutt("You sure you don’t want mine for a reference?")
                            jutt("it wouldn’t be fair to you if I just copied it", norm_write)
                            sinu_jutt("no not copy, just reference for the structure and such")
                        jutt("well-", norm_write)
                        sinu_jutt("it’s seriously wouldn’t be a problem on my part")
                        jutt("if you say so", norm_write)
                        sinu_jutt("so there, you can have it for the time being")
                        jutt("thank you", norm_write)
                        sinu_jutt("you’re the most welcome")
                        jutt("didn’t take you for someone who did all their homework", norm_write)
                        sinu_jutt(
                            "heh, the thing is, that i usually let Friend copy off of me and she’ll give me her lunch")
                        jutt("ohh, you’re a friend of Friends then?", norm_write)
                        sinu_jutt("that i am")
                        jutt("the girl my sister abandoned me for?", norm_write)
                        sinu_jutt("that’s the one")
                        jutt(" good to know", norm_write)
                        sinu_jutt(
                            "if it helps then for your information, Friend blew me off as well. we we’re supposed to go together")
                        jutt("I know exactly how you feel", norm_write)
                        sinu_jutt("so why don’t we get revenge and go together?")
                        jutt("because..I’m not sure even", norm_write)
                        sinu_jutt("you still have time to decide, two days is plenty of time")
                        jutt("one less if you consider today, which I do.", norm_write)
                        sinu_jutt("but think about it, how many proms are you going to get anyways in your life time?")
                        jutt("the prom happens every year.", norm_write)
                        sinu_jutt(
                            "see? more the reason you should try going with someone else. If you don’t like it you can always ditch the next ones")
                        jutt("I’ll think about it", norm_write)
                        sinu_jutt("good, I’m glad.")
                    mitu_korda = ["dancing?","weird question","writing?"]
                    sinu_jutt("so do tell me about yourself, do you have hobbies of any kind?")
                    jutt("you couldn’t come up with anything more original?", norm_write)
                    sinu_jutt("i have to know the basics before i can baffle you with any philosophical questions")
                    jutt("fine", norm_write)
                    sinu_jutt("so again, what are some of your hobbies?")
                    jutt("schoolwork, creative writing, ballroom dancing, and just reading", norm_write)
                    while len(mitu_korda) != 1:
                        pilt("...", norm_write,mitu_korda)
                        if otsus == 1 and mitu_korda[0]=="dancing?":
                            sinu_jutt("you do ballroom dancing?")
                            jutt("just like i said", norm_write)
                            sinu_jutt("that’s perfect")
                            jutt("why so?", norm_write)
                            sinu_jutt("you could give me lessons, I’m rubbish at dancing")
                            jutt("i’d have to think about it", norm_write)
                            sinu_jutt("why?")
                            if prom == True:
                                jutt("i have feeling that would be your way of convincing me to go to prom",
                                     norm_write)
                                sinu_jutt("maybe")
                                jutt("not gonna happen", norm_write)
                            elif prom == False:
                                jutt("i have feeling that you aren’t the best student", norm_write)
                                sinu_jutt("ouch")
                                jutt("you seem to be more of an academic kind", norm_write)
                            sinu_jutt("alright then, not gonna be pushy about it. why do you do it then?")
                            jutt("what, dancing?", norm_write)
                            sinu_jutt("yes!")
                            jutt("well, I like it. It’s a form of expression, but orderly. Beautiful really", norm_write)
                            sinu_jutt("I haven’t really seen it in action before but I believe you. You’re the professional after all")
                            jutt("Not particularly. I just dabble in it once a week", norm_write)
                            sinu_jutt("that’s pretty good though")
                            jutt("other’s do it twice a week and attend tournaments", norm_write)
                            sinu_jutt("why don’t you do it?")
                            jutt("I’ve never danced for the approvement for others, I do it for me", norm_write)
                            sinu_jutt("very cheesy of you")
                            jutt("oh shut up. that’s just my reasoning, which you asked for", norm_write)
                            sinu_jutt("I'm not complaining")
                            sinu_jutt("how did you get into it then")
                            pilt("family. my sister had done it for years so the advised me to also get into it",norm_write,["do your parents dance?","perfect for prom!"])
                            if otsus == 1:
                                sinu_jutt("oh that sounds awesome, do your parents dance as well?")
                                jutt("no not really. maybe they’ll manage to stay standing during slow waltz but otherwise no.",
                                     norm_write)
                                jutt("I’m pretty sure they live out their dream though us, or at least my mom", norm_write)
                                sinu_jutt("that must suck")
                                jutt("but it’s alright. I've learned to love it in my own way", norm_write)
                                sinu_jutt("do you compete?")
                                jutt(
                                    "oh definitely not. my sister is into tournaments and such but not me. I just do it out of my love for it",
                                    norm_write)
                                sinu_jutt("those are indeed the best hobbies. what do you like about it?")
                                jutt("hard to summarize. I think dance is the best physical type of self expression.",
                                     norm_write)
                                jutt(
                                    "creative writing nourishes the soul but with dance you get to just go wild but in an orderly manner",
                                    norm_write)
                                jutt("if that makes sense", norm_write)
                                sinu_jutt("no no i get it. the ability to express yourself using only your body is amazing")
                                sinu_jutt("that’s why I want to learn ASL someday")
                                jutt("ASL? sign language? Yeah I could see why you’d associate the two", norm_write)
                                sinu_jutt("both forms of communication")
                                jutt("one of them feels much more direct in that sense but sure", norm_write)
                                sinu_jutt("that’s for certain. but both are very valid")
                                jutt("not arguing that", norm_write)
                            elif otsus == 2:
                                if prom == False:
                                    sinu_jutt("you guys would kill it at prom")
                                    jutt("oh yeah, prom..", norm_write)
                                    sinu_jutt("you’re going right?")
                                    jutt("that was the plan but my sister ditched me for some girl named Friend", norm_write)
                                    sinu_jutt("oh that’s rough. but i’m kind of the same position")
                                    jutt("how come?", norm_write)
                                    sinu_jutt(
                                        "well i was supposed to go with Friend but she got asked out by some girl named Lydia")
                                    jutt("ohh.", norm_write)
                                    sinu_jutt("exactly.")
                                    jutt("...", norm_write)
                                    sinu_jutt("hey but this gives me an idea")
                                    jutt("an idea?", norm_write)
                                    sinu_jutt("why don’t we go together? you know, to get revenge and such?")
                                    jutt("i don’t think it will be a good idea", norm_write)
                                    sinu_jutt(
                                        "why not? you already know how to dance so that wouldn’t be a problem. and prom doesn’t come around that often")
                                    jutt("well yes but i hardly know you", norm_write)
                                    sinu_jutt("and what stops you from changing that?")
                                    jutt("the intent of not doing it?", norm_write)
                                    sinu_jutt("so you don’t want to be friends with me?")
                                    jutt("no not that-", norm_write)
                                    sinu_jutt("then there’s no harm in getting to know each other some more at the prom")
                                    jutt("it feels weird going with a..stranger?", norm_write)
                                    sinu_jutt("a little, but i’ll try my hardest to not make it awkward")
                                    jutt("I’ll think about it", norm_write)
                                    sinu_jutt("awesome! glad to hear that")
                                    jutt("of course you are", norm_write)
                                    prom = True
                                elif prom == True:
                                    sinu_jutt("i get why you would’ve wanted to with your sister then, you guys would’ve been the stars of the prom")
                                    jutt("heh, perhaps. we do love it when we get to show off moves", norm_write)
                                    sinu_jutt(
                                        "I get that you’re not all into the idea but If you’re willing you could teach me some basic moves and we could try to do the same")
                                    jutt("sweet thought, it would have to be much slower though", norm_write)
                                    sinu_jutt("yeah your right, but I won’t know until I’ve tried it")
                                    jutt("I see that you like risking it in life", norm_write)
                                    sinu_jutt("that is my specialty. my motto is ,,why not")
                                    jutt("I could be the one to tell you all the reasons why not to do something", norm_write)
                                    sinu_jutt("eyy, your ying to my yan")
                                    jutt("something like that, my expertise is in pessimism", norm_write)
                                    sinu_jutt("i’ve taken a notice yeah")
                                    jutt("is it really that obvious?", norm_write)
                                    sinu_jutt("oh no. i just have sherlock holmes brain and could deduce it")
                                    jutt("sure, i believe you", norm_write)
                                    sinu_jutt("as you should, i’m the brightest witch of our generation, a little genius or so")
                                    jutt("who can’t get themselves a date for the prom?", norm_write)
                                    sinu_jutt("i’m still working on that part")
                                    jutt("and you’re hard at work on it.", norm_write)
                                    sinu_jutt("is it working?")
                                    jutt("a little", norm_write)
                                    sinu_jutt("ahaa! So there’s a chance i could take you to prom?")
                                    jutt("there’s always a chance", norm_write)
                                    sinu_jutt("soo could you be my date for the prom?")
                                    jutt("maybe ask me later? I really don’t know about that", norm_write)
                                    sinu_jutt("I’ll ask tomorrow again then")
                                    jutt("I’m sure you will", norm_write)
                                    usaldus = 2
                            mitu_korda.remove("dancing?")
                            dancing = True
                        elif otsus == 1 and mitu_korda[0]=="weird question" or otsus == 2 and mitu_korda[1]=="weird question":
                            sinu_jutt("alright but now an off topic question")
                            jutt("I won’t protest", norm_write)
                            sinu_jutt("for what in your life do you feel the most grateful?")
                            jutt("now that’s a bit of a deep question", norm_write)
                            sinu_jutt("perhaps, but I’m curious")
                            jutt(" I’d have to say, my living situation", norm_write)
                            sinu_jutt("so you like your home?")
                            jutt(
                                "not only. I am grateful I was born into a family where there’s always food on the table and a roof over my head",
                                norm_write)
                            jutt(
                                "that there’s free education and I get to have hobbies of any variety. grateful to be born here",
                                norm_write)
                            sinu_jutt("so you’re happy about your privileged life?")
                            jutt("that’s one way to put it", norm_write)
                            sinu_jutt(
                                "I guess I haven’t really though about that. I was assuming you’d say ´my family´) or ´my friends´ or something of that sorts")
                            jutt("you’re not all that great at guessing huh", norm_write)
                            sinu_jutt("I do try")
                            jutt("well everyone does that, try to make sense of the world, you’re not that special",
                                 norm_write)
                            sinu_jutt("ouch")
                            jutt(
                                "I’m just being honest. assumptions are useful only to the extent that they don’t disturb your view of reality",
                                norm_write)
                            sinu_jutt("that’s good to know")
                            jutt("you’re welcome", norm_write)
                            mitu_korda.remove("weird question")
                        elif otsus == 3 and mitu_korda[2]=="writing?" or otsus == 2 and mitu_korda[1] == "writing?":
                            sinu_jutt("you write?")
                            jutt("creative writing yeah", norm_write)
                            sinu_jutt("do you have an examples of your work?")
                            jutt("I mean yeah", norm_write)
                            sinu_jutt("may I see them?")
                            jutt("ah better not, I don’t like to showcase my work", norm_write)
                            sinu_jutt("totally understandable, but why do you write then?")
                            sinu_jutt(
                                "isn’t writings whole point that now it’s recorded somewhere and someone can view it?")
                            jutt("yes, but the one that can view it is me. that’s all I need", norm_write)
                            sinu_jutt("will you ever publish your works?")
                            jutt("I don’t see a need to. I write for myself", norm_write)
                            sinu_jutt("what do you write about then?")
                            jutt("anything that comes to mind. blank piece of paper is my canvas", norm_write)
                            sinu_jutt("damn. I don’t think I could ever really do that.")
                            sinu_jutt(
                                "I’ve always enjoyed writing for school projects. there’s a clear direction and objective to the writing and it makes it easier")
                            jutt("well I guess i just like to stroll rather than take a beaten path", norm_write)
                            sinu_jutt("to each their own. but again, are there stories that you’re working on right now?")
                            jutt(
                                "well as i prefer short stories then there are quite a few. most of them more ideas than fleshed out chapters",
                                norm_write)
                            sinu_jutt("well shoot, I'd love to hear about them")
                            jutt("it’s hard to describe them outright", norm_write)
                            jutt(
                                "just like with poems, you can’t give the full effect of the poem by describing it, you’d have to indulge yourself in it.",
                                norm_write)
                            sinu_jutt(
                                "oh alright, I get it. is there even a slight possibility that I’d get to read them someday?")
                            jutt("maybe. if I’ve grown to trust you enough", norm_write)
                            sinu_jutt("I’ll try my best to make it happen then")
                            jutt("good luck", norm_write)
                            mitu_korda.remove("writing?")
                    jutt("hey, it was lovely talking to you again but I’ve got to go to class now",
                         norm_write)
                    sinu_jutt("So do I, can I send you to your class?")
                    jutt("oh no, we’re having an outdoor class today", norm_write)
                    sinu_jutt("oh really? for what?")
                    jutt("art class. we’ll be drawing live fauna and so", norm_write)
                    sinu_jutt("sounds fun, I hope you’ll enjoy!")
                    jutt("I hope so to. but I’ll see you tomorrow", norm_write)
                    sinu_jutt("see you!")
                    nadal += 1
                    uks_nadal = False
            elif usaldus == 2:
                while uks_nadal == True:
                    sinu_jutt("hello!")
                    jutt("hey there!",norm_norm)
                    sinu_jutt("how are you?")
                    pilt("...",norm_norm)
                    if help == True:
                        jutt("quite well actually", norm_norm)
                        jutt("you know your assignment really helped me. I hope I’ll get a good grade", norm_norm)
                        sinu_jutt("that’s wonderful! I’m happy I could help you with it")
                        jutt("yeah! i got a free morning thanks to you", norm_norm)
                        sinu_jutt("what have you been up to then?")
                        jutt("I’ve just been working on a personal project of mine", norm_norm)
                        sinu_jutt("and what’s that?")
                        jutt(
                            "a short story. I’ve had the idea for it for a while now so I thought I’d get it down somewhere",
                            norm_norm)
                        sinu_jutt("oh! can I read it?")
                        jutt("well, sure. I’ll give it to you but don’t read it while I’m near please", norm_norm)
                        sinu_jutt("why not? are you embarrassed?")
                        jutt("it feels weird letting someone read something so creatively personal", norm_norm)
                        sinu_jutt("alright alright, I get it. I guess I’m just used to other people reading my papers")
                        jutt("well if they’re copying off of you then certainly", norm_norm)
                        sinu_jutt("I do it all for food")
                        jutt("of course you do", norm_norm)
                        story = True
                    elif help == False:
                        jutt("I’m a bit tired from trying to finish the history assignment", norm_norm)
                        sinu_jutt("was it that rough?")
                        jutt("just a little, got through it this morning. wish I could’ve done anything else",
                             norm_norm)
                        sinu_jutt("like what?")
                        jutt("writing", norm_norm)
                        sinu_jutt("writing what?")
                        jutt("I’ve got an idea for a short story but well, I don’t have the time to write it out",
                             norm_norm)
                        sinu_jutt("ooh, what’s the story about then?")
                        jutt("kind of personal, if I ever finish it then I might let you read it", norm_norm)
                        sinu_jutt("I’d honestly would love that")
                        jutt("I’m glad", norm_norm)
                    mitu_korda = ["ask about prom","ask about plans","ask about dancing"]
                    while len(mitu_korda) != 1:
                        pilt("...",norm_norm,mitu_korda)
                        if otsus == 1 and mitu_korda[0]=="ask about prom":
                            if prom == True:
                                sinu_jutt("but hey, about prom-")
                                jutt(
                                    "I get that you really want to go. I’m just still uncertain on how it would even go",
                                    norm_norm)
                                sinu_jutt(
                                    "I mean so far we’ve gotten to talk quite a bit, so the dry conversations wouldn’t be the problem")
                                sinu_jutt("so why not try it?")
                                jutt("I’m not a party person", norm_norm)
                                sinu_jutt("but it’s barely a party. more like...")
                                sinu_jutt("a dance.. gathering?")
                                jutt("sounds like a party to me", norm_norm)
                                sinu_jutt("you don’t even want to check it out?")
                                jutt("well.. maybe", norm_norm)
                                sinu_jutt(
                                    "you could just go in, look around a bit and then get out before it gets on your nerves")
                                jutt("but getting ready takes forever", norm_norm)
                                sinu_jutt("it doesn’t have to. besides if you do it with someone it could be quite fun")
                                jutt("I’m still not sure", norm_norm)
                                sinu_jutt("that’s alright. I’ll ask tomorrow again, for the last time")
                                jutt("thanks", norm_norm)
                                sinu_jutt("for what?")
                                jutt(
                                    "for even trying to convince me, I assumed you’d give up after the first rejection",
                                    norm_norm)
                                sinu_jutt("I’m determined, I blame my upbringing")
                                jutt("heh, always blaming the parents", norm_norm)
                                sinu_jutt("well they shouldn’t always be at fault then!")
                                jutt("fair enough", norm_norm)
                                usaldus = 3
                            elif prom == False:
                                sinu_jutt("but hey, the prom is coming up")
                                jutt("oh is it now?", norm_norm)
                                jutt("in like.. two days right?", norm_norm)
                                sinu_jutt("I think so yeah")
                                jutt("do you have a date for it?", norm_norm)
                                sinu_jutt(
                                    "well no.. my friend Friend with whom I was supposed to go with, blew me off for some girl named Lydia")
                                jutt("oh- Lydia as in my sister Lydia?", norm_norm)
                                sinu_jutt("ohh she’s your sister")
                                jutt("well yeah. we planned on going together as well", norm_norm)
                                sinu_jutt("what happened then that changed her mind?")
                                jutt(
                                    "she has always liked Friend and when we talked about it, I encouraged her to do something about it",
                                    norm_norm)
                                jutt("they must’ve gotten to talking and it went all downhill from there", norm_norm)
                                sinu_jutt("would make sense yeah.")
                                sinu_jutt("wait so you’re basically to blame for us not having dates?")
                                jutt("maybe", norm_norm)
                                sinu_jutt("well dang")
                                jutt("kind of sucks. prom looked inviting", norm_norm)
                                sinu_jutt("but hey, here’s an idea")
                                sinu_jutt("what if we went together? like to get revenge or something of that sorts")
                                jutt("me and you?", norm_norm)
                                jutt("we don’t really know each other tho", norm_norm)
                                sinu_jutt("I mean we’ve gotten along so far, what’s just one more prom night as well?")
                                jutt("that’s true", norm_norm)
                                sinu_jutt("so come on, let’s go!")
                                jutt("I’ll think about it, okay?", norm_norm)
                                sinu_jutt("works for me")
                                prom = True
                            mitu_korda.remove("ask about prom")
                        elif otsus == 1 and mitu_korda[0]=="ask about plans" or otsus == 2 and mitu_korda[1]=="ask about plans":
                            sinu_jutt("so do you have any other plans for the week? or weekend?")
                            jutt(
                                "besides the short story, I’m not even sure. though I did promise my sister I’d help her prepare for the bake sale on monday",
                                norm_norm)
                            sinu_jutt("there’s a bake sale on monday?")
                            jutt(
                                "in the town square yeah, Lydia has volunteered to help with bigger projects so they offered her a free space at the bake sale",
                                norm_norm)
                            sinu_jutt("oh dang. can she even bake then?")
                            jutt("besides grilled cheese? not really. that’s why I’m there", norm_norm)
                            sinu_jutt("and you can bake?")
                            jutt(
                                "I’m the one that makes most of the family dinners and celebration cakes so I’d say so",
                                norm_norm)
                            sinu_jutt("so you always do the cooking in the family?")
                            pilt("family of five, I arrive the earliest so I just got into the habit of it", norm_norm,["offer to help out","offer to cook for her","ask her to teach you"])
                            if otsus == 1:
                                sinu_jutt("if you are willing, I’d love to help out with the baking")
                                jutt("that’s very sweet of you. but I’m not sure what you could even do to help",
                                     norm_norm)
                                jutt("I’ve always managed to get by myself", norm_norm)
                                sinu_jutt(
                                    "exactly. get by. and I’d be there to make it be fun and easy. clean the dishes or something")
                                jutt("that would actually be helpful. baking is like 50% baking 50% cleaning",
                                     norm_norm)
                                sinu_jutt("oh that sounds rough")
                                jutt("sure but I usually do it while I wait. there’s so much waiting", norm_norm)
                                sinu_jutt("I could keep you company")
                                jutt(
                                    "I already have a sister who will do the dirty jobs for me. maybe some other time though",
                                    norm_norm)
                                sinu_jutt("I’d be down")
                                jutt("cool, I’m sure we’ll figure something out when the time comes", norm_norm)
                                sinu_jutt("can’t wait")
                            elif otsus == 2:
                                sinu_jutt("hey, if you are free on any upcoming weekends, I’d love to cook for you")
                                jutt("you- what?", norm_norm)
                                sinu_jutt(
                                    "I mean you always do most of the work for your family so why not let someone else treat you")
                                jutt("I’m not sure", norm_norm)
                                sinu_jutt("that’s alright, I won’t be pushy. but I’m not all that bad myself")
                                jutt("you aren’t?", norm_norm)
                                sinu_jutt("that was uncalled for but yes, I like to cook from time to time")
                                jutt("rice and meatballs?", norm_norm)
                                sinu_jutt("more like bologna or lasagna. I’ve been on a weird Italian mood lately")
                                jutt("well if you’re offering. I won’t turn down a free dinner", norm_norm)
                                sinu_jutt("that’s the spirit. so if any of your weekends open up, let me know")
                                jutt("for sure", norm_norm)
                                usaldus = 3
                            elif otsus == 3:
                                sinu_jutt("oh damn you have to teach me sometime")
                                jutt("if you’re up for it", norm_norm)
                                sinu_jutt(
                                    "now that I think about it, I might just end up watching you do all the baking while I snack on something")
                                jutt(
                                    "that’s usually how those kind of things so. I assume how this weekend will end up as well",
                                    norm_norm)
                                sinu_jutt("that happens when you’re too good at something")
                                jutt("maybe. but then again, it’s not the same with like painting", norm_norm)
                                sinu_jutt(
                                    "I’d argue otherwise. people enjoy looking at others finished projects more than do it themselves")
                                jutt("true. but also art is more about the journey and not the destination", norm_norm)
                                jutt(
                                    "baking is also in some ways but in the end, it’s how to pastry turns out. and then it gets eaten in a fraction of the time it got made in",
                                    norm_norm)
                                sinu_jutt(
                                    "well yes, you wouldn’t necessarily eat art, but they still devour the painting with a single glance and don’t usually come back to it again")
                                jutt("fair enough. different mediums, same problem", norm_norm)
                                sinu_jutt("would you even enjoy someone helping you out in the kitchen?")
                                jutt(
                                    "I’m not sure I would. they’d likely end up in the way. besides baking is usually 50% cleaning, 50% actually doing something",
                                    norm_norm)
                                sinu_jutt("sounds fun")
                                jutt("not really. I really should hire myself a dishwasher", norm_norm)
                                sinu_jutt("do the other family members not help with that?")
                                jutt(
                                    "I usually do the cleaning up myself while I wait so there’s not really a need for them",
                                    norm_norm)
                                sinu_jutt("but maybe you could ask next time? would make your life a bit easier")
                                jutt("that’s true, perhaps I will", norm_norm)
                                sinu_jutt("good luck with that")
                                jutt("thanks", norm_norm)
                            mitu_korda.remove("ask about plans")
                        elif otsus == 2 and mitu_korda[1]=="ask about dancing" or otsus == 3 and mitu_korda[2] == "ask about dancing":
                            sinu_jutt("so what else do you like to do for fun?")
                            jutt("well I read a bit and I do ballroom dancing", norm_norm)
                            sinu_jutt("you do what?")
                            jutt("ballroom dancing, it’s like a very fancy way of doing simple dances", norm_norm)
                            sinu_jutt("but that sounds awesome, do you compete?")
                            jutt("oh definitely not. I do it more out of the love for dance not a need of approval",
                                 norm_norm)
                            sinu_jutt("why do you love it then so much?")
                            jutt(
                                "well my sister competes, she likes wearing those shiny uniforms and dolling herself up for big events",
                                norm_norm)
                            jutt("but I love the self expression aspect of it. ", norm_norm)
                            jutt(
                                "with writing, it’s a mental release, but dancing is like physical creativity with rules and regulation",
                                norm_norm)
                            jutt("if you understand", norm_norm)
                            sinu_jutt("yeah I do, I get it. a form of self expression for your body")
                            jutt("exactly, and i love it because of it", norm_norm)
                            sinu_jutt("that’s interesting to hear. I’m not a dancer myself so I wouldn’t know")
                            jutt("yeah true. it’s not really like other physical sports", norm_norm)
                            sinu_jutt("it really isn’t. but I like hearing you talk about it")
                            jutt("thank you", norm_norm)
                            sinu_jutt("think you could ever teach me a few steps?")
                            jutt("maybe, if you can keep up", norm_norm)
                            sinu_jutt("oh don’t you worry about that. I run track so-")
                            jutt("not that kind of speed, more like dexterity rather than straight forward running",
                                 norm_norm)
                            sinu_jutt("well whenever one of your classes free up, I’d love to come and watch")
                            jutt("maybe you’ll even learn something", norm_norm)
                            sinu_jutt("perhaps")
                            mitu_korda.remove("ask about dancing")
                            dancing = True
                    jutt("hey, it was lovely talking to you again but I’ve got to go to class now", norm_norm)
                    sinu_jutt("So do I, can I send you to your class?")
                    jutt("oh no, we’re having an outdoor class today", norm_norm)
                    sinu_jutt("oh really? for what?")
                    jutt("art class. we’ll be drawing live fauna and so", norm_norm)
                    sinu_jutt("sounds fun, I hope you’ll enjoy!")
                    jutt("I hope so to. but I’ll see you tomorrow", norm_norm)
                    sinu_jutt("see you!")
                    nadal += 1
                    uks_nadal = False
        elif nadal == 3:
            if usaldus == 1:
                while uks_nadal == True:
                    sinu_jutt("hey there!")
                    jutt("hi again", norm_mus)
                    sinu_jutt("so what are you up to?")
                    jutt("well I don’t have a lot of time right now.", norm_mus)
                    pilt("but to answer your question, I’m just listening to music", norm_mus,["ask about music","ask about prom"])
                    if otsus == 1:
                        sinu_jutt("what kind?")
                        jutt("japanese metal if that say’s anything to you", norm_mus)
                        sinu_jutt("oh like babymetal and such?")
                        jutt("not a fan of that particular band but yes", norm_mus)
                        sinu_jutt("who do you usually listen to then?")
                        jutt("well I don’t always listen to japanese metal, just was in the mood.", norm_mus)
                        jutt("I don’t actually even know any real bands or singers from that genre", norm_mus)
                        sinu_jutt("woow, what a fake fan")
                        jutt("oh don’t start with that", norm_mus)
                        sinu_jutt("alright alright I won’t")
                        jutt("thank you", norm_mus)
                    if prom == True:
                        sinu_jutt("but hey so, prom is tomorrow")
                        jutt("oh this again", norm_mus)
                        sinu_jutt("will you go to the prom with me?")
                        jutt("I thought about it", norm_mus)
                        if dancing == True:
                            sinu_jutt("you’d be the belle of the ball with your dancing")
                            jutt("well maybe but-", norm_mus)
                            sinu_jutt("it would be just one night. one single prom night")
                            jutt("alright so. I won’t go there with you. but I will pop by for just a little.",
                                 norm_mus)
                            jutt("I’ll say hi to my sister and that’s it", norm_mus)
                            sinu_jutt("heyy that’s awesome. I’ll be waiting for you there then")
                            jutt("but again, I’ll only be there for a short while", norm_mus)
                            sinu_jutt("that totally works for me")
                            jutt("I do have to run now.", norm_mus)
                            sinu_jutt("but I’ll see you tomorrow then right?")
                            jutt("yes, yes you will", norm_mus)
                            sinu_jutt("byee Misty!")
                            jutt("bye!", norm_mus)
                            nadal += 1
                            uks_nadal = False
                            usaldus = 2
                        elif dancing == False:
                            sinu_jutt("you’ll get to have so much fun, you’d still kind of be there with your sister")
                            sinu_jutt("and besides, it’s a party! it will be cool!")
                            jutt("listen. I did think about it. but i honestly don’t think I’ll go.", norm_mus)
                            jutt("definitely not with you and otherwise as well", norm_mus)
                            sinu_jutt("really? but it would be awesome with you there")
                            jutt("that’s just too bad, because I’m really not a party person", norm_mus)
                            sinu_jutt("dang it")
                            jutt("I do hope you’ll have fun though", norm_mus)
                            sinu_jutt("don’t know if I will now though, going all alone")
                            jutt("it won’t be that bad. trust me.", norm_mus)
                            sinu_jutt("if you say so")
                            jutt("but I do have to run now, I´ll see you around", norm_mus)
                            sinu_jutt("see you Misty")
                            jutt("bye!", norm_mus)
                            nadal += 1
                            uks_nadal = False
                    elif prom == False:
                        sinu_jutt("hey, you know there’s the prom coming up")
                        jutt("tomorrow yes", norm_mus)
                        sinu_jutt("and well, I don’t still have a date so I was wondering if you’d like to go with me")
                        jutt("what?", norm_mus)
                        sinu_jutt(
                            "I was supposed to go with my friend Friend but she told me that Lydia, your sister, has asked her out")
                        sinu_jutt("so now we both technically don’t have dates")
                        jutt("yeah true..", norm_mus)
                        sinu_jutt("so why not go together and have all the fun ourselves?")
                        jutt("because I don’t want to", norm_mus)
                        sinu_jutt("why on earth not?")
                        jutt(
                            "I’ve already made plans for tomorrow night and I’m definitely not in the mood to do the whole prom thing",
                            norm_mus)
                        sinu_jutt("it won’t be anything big, we wouldn’t even have to stay there for long")
                        jutt("yes that’s true, but my answer is still no", norm_mus)
                        sinu_jutt("oh dang it")
                        jutt("yeah, and also I have to run now, I’m kind of running late", norm_mus)
                        sinu_jutt("well, I guess I’ll just see you around")
                        jutt("same back to you, have fun at prom", norm_mus)
                        sinu_jutt("thanks, have fun at your thing")
                        jutt("I will, see you!", norm_mus)
                        sinu_jutt("bye!")
                        nadal += 1
                        uks_nadal = False
            elif usaldus == 2:
                while uks_nadal == True:
                    sinu_jutt("hey Misty!")
                    jutt("hey there!", norm_mus)
                    jutt("also just a heads up, I don’t really have the time to talk today", norm_mus)
                    jutt(" I’m in a bit of a rush", norm_mus)
                    sinu_jutt("oh this won’t take long")
                    jutt("alright, shoot", norm_mus)
                    if story == True:
                        sinu_jutt("first off, here’s your story back")
                        jutt("oh thank you", norm_mus)
                        sinu_jutt("it was awesome and I loved it")
                        jutt("oh really? that’s lovely to hear", norm_mus)
                        sinu_jutt("but now back on topic")
                    if prom == False:
                        sinu_jutt("hey, you know there’s the prom coming up")
                        jutt("tomorrow yes", norm_mus)
                        sinu_jutt("and well, I don’t still have a date so I was wondering if you’d like to go with me")
                        jutt("what?", norm_mus)
                        sinu_jutt(
                            "I was supposed to go with my friend Friend but she told me that Lydia, your sister, has asked her out")
                        sinu_jutt("so now we both technically don’t have dates")
                        jutt("yeah true..", norm_mus)
                        sinu_jutt("so why not go together and have all the fun ourselves?")
                        jutt("that’s quite a lot to ask though. I really haven’t even thought about it", norm_mus)
                        sinu_jutt("just a little impulsive party")
                        jutt("okay for one, I won’t go there with you. I just don’t know you enough", norm_mus)
                        sinu_jutt("ohh..")
                        jutt("but I will pop by for just a little.", norm_mus)
                        jutt("I’ll say hi to my sister and that’s it", norm_mus)
                        sinu_jutt("heyy that’s awesome. I’ll be waiting for you there then")
                        jutt("but again, I’ll only be there for a short while", norm_mus)
                        sinu_jutt("that totally works for me")
                        jutt("I do have to run now.", norm_mus)
                        sinu_jutt("but I’ll see you tomorrow then right?")
                        jutt("yes, yes you will", norm_mus)
                        sinu_jutt("byee Misty!")
                        jutt("bye!", norm_mus)
                        nadal += 1
                        uks_nadal = False
                    elif prom == True:
                        sinu_jutt("so you know that prom is coming up like tomorrow")
                        jutt("yeah.", norm_mus)
                        sinu_jutt("so I was wondering if you would like to go to the prom with me?")
                        jutt("listen I thought about it and-", norm_mus)
                        if dancing == True:
                            sinu_jutt("you’d be the belle of the ball there! especially with your dancing skills")
                            sinu_jutt("it would be really fun and you’d technically get to be with your sister")
                            jutt("hey! I thought it over", norm_mus)
                            jutt(
                                "and yeah, I think I will go to the prom with you. I’m sure it will be a drag but I will come by for a little at least",
                                norm_mus)
                            sinu_jutt("oh dang really? that’s amazing")
                            jutt("but I’ll leave right away if I don’t enjoy it", norm_mus)
                            sinu_jutt("would make sense")
                            jutt("so yeah. I’ll see you tomorrow there. you better look nice", norm_mus)
                            sinu_jutt("I will, I definitely will")
                            jutt("lovely! but now I truly have to run so, byee!", norm_mus)
                            sinu_jutt("see you Misty!")
                            nadal += 1
                            uks_nadal = False
                            usaldus = 3
                        elif dancing == False:
                            sinu_jutt("you’ll get to have so much fun, you’d still kind of be there with your sister")
                            sinu_jutt("and besides, it’s a party! it will be cool!")
                            jutt("alright so. I won’t go there with you. but I will pop by for just a little.",
                                 norm_mus)
                            jutt("I’ll say hi to my sister and that’s it", norm_mus)
                            sinu_jutt("heyy that’s awesome. I’ll be waiting for you there then")
                            jutt("but again, I’ll only be there for a short while", norm_mus)
                            sinu_jutt("that totally works for me")
                            jutt("I do have to run now.", norm_mus)
                            sinu_jutt("but I’ll see you tomorrow then right?")
                            jutt("yes, yes you will", norm_mus)
                            sinu_jutt("byee Misty!")
                            jutt("bye!", norm_mus)
                            nadal += 1
                            uks_nadal = False
            elif usaldus == 3:
                while uks_nadal == True:
                    sinu_jutt("hi Misty")
                    jutt("oh hi there!", norm_mus)
                    jutt("lovely to see you again", norm_mus)
                    sinu_jutt("it is?")
                    jutt("for sure! but today you’ll have to do quick because I have to run soon", norm_mus)
                    sinu_jutt("oh yeah sure")
                    if story == True:
                        sinu_jutt("so first off, here’s your story back")
                        jutt("oh thank you", norm_mus)
                        sinu_jutt("it was awesome and I loved it")
                        jutt("oh really? that’s lovely to hear", norm_mus)
                        sinu_jutt("but now back on topic")
                    if prom == False:
                        sinu_jutt("hey, you know there’s the prom coming up")
                        jutt("tomorrow yes", norm_mus)
                        sinu_jutt("and well, I don’t still have a date so I was wondering if you’d like to go with me")
                        jutt("what?", norm_mus)
                        sinu_jutt(
                            "I was supposed to go with my friend Friend but she told me that Lydia, your sister, has asked her out")
                        sinu_jutt("so now we both technically don’t have dates")
                        jutt("oh yeah that’s true", norm_mus)
                        sinu_jutt("so I was wondering if you’d like to go to the prom with me?")
                        jutt("well-", norm_mus)
                        sinu_jutt("It would be fun, you’d get to see your sister and we’d just dance through the night")
                        jutt("you haven’t given me really a lot of time to think about it but...", norm_mus)
                        sinu_jutt("but?")
                        jutt("but sure, I’m in. where’s the harm in that", norm_mus)
                        sinu_jutt("oh dang really? that’s amazing!")
                        jutt("yeah. but like, if I don’t like it, I will leave. I’m not really a party person at all",
                             norm_mus)
                        sinu_jutt("yeah thats totally understandable")
                        jutt("so yeah. oh I have to run now but I’ll see you there tomorrow", norm_mus)
                        sinu_jutt("I’ll see you there!")
                        jutt("bye!", norm_mus)
                        nadal += 1
                        uks_nadal = False
                    if prom == True:
                        sinu_jutt("so you know that prom is coming up like tomorrow")
                        jutt("yeah.", norm_mus)
                        sinu_jutt("so I was wondering if you would like to go to the prom with me?")
                        jutt("well you did promise to ask me again", norm_mus)
                        sinu_jutt("and that’s why I’m here")
                        jutt("I thought it over and talked with my sister", norm_mus)
                        jutt("and I say sure, let’s go.", norm_mus)
                        sinu_jutt("really?")
                        jutt(
                            "yeah really. my other plan was to just binge movies all night but I hope this will be a little bit more fun",
                            norm_mus)
                        sinu_jutt("oh I promise you it will be")
                        jutt("cool, I’ll see you there then as I do have to run off now", norm_mus)
                        sinu_jutt("yeah of course, you do your things")
                        jutt("bye!", norm_mus)
                        sinu_jutt("bye Misty!")
                        nadal += 1
                        uks_nadal = False
        elif nadal == 4:
            if usaldus == 1:
                while uks_nadal == True:
                    sinu_jutt("hey Friend!")
                    jutt("hey theree! Long time no see", pop_norm)
                    sinu_jutt("yeah that’s true, I’ve been busy")
                    jutt("talking with Misty, if my eyes have been correct", pop_norm)
                    sinu_jutt("yeahh that’s true")
                    jutt("so, do tell me, how´d it go?", pop_norm)

                    sinu_jutt("okey so, not as well as I thought")
                    jutt("what do you mean?", pop_norm)
                    sinu_jutt("it means she’s not coming at all")
                    jutt("oh dang why’d you scare her off like that?", pop_norm)
                    sinu_jutt("I didn’t do it on purpose")
                    jutt("you’re really bad at this", pop_norm)
                    sinu_jutt("I didn’t think I’d be")
                    jutt("well you’re going to the prom alone and you’ll miss out on a motorcycle", pop_norm)
                    sinu_jutt("yeahh... I know")
                    jutt("sucks to be you", pop_norm)
                    sinu_jutt("the most")
                    jutt("but hey, you’ll still get to party with me and Lydia, don’t worry.", pop_norm)
                    jutt("we won’t push you out", pop_norm)
                    sinu_jutt("thanks Friend")
                    jutt("no problem. but hey, let’s head to class now", pop_norm)
                    nadal += 1
                    uks_nadal = False
                    mangib = False
            elif usaldus == 2:
                while uks_nadal == True:
                    sinu_jutt("hey Friend!")
                    jutt("hey theree! Long time no see", pop_norm)
                    sinu_jutt("yeah that’s true, I’ve been busy")
                    jutt("talking with Misty, if my eyes have been correct", pop_norm)
                    sinu_jutt("yeahh that’s true")
                    jutt("so, do tell me, how´d it go?", pop_norm)

                    sinu_jutt("pretty good I’d have to say")
                    jutt("so you’re going to the prom with Misty?", pop_norm)
                    sinu_jutt("well not that well")
                    jutt("what do you mean?", pop_norm)
                    sinu_jutt("she’ll only pop by to say hello to Lydia and that’s it")
                    jutt("dude, why did you scare her off?", pop_norm)
                    sinu_jutt("I didn’t! at least I thought I didn’t")
                    jutt("well damn. oh well, you’ll still get to hang out with me and Lydia", pop_norm)
                    sinu_jutt("but the bike is still mine right?")
                    jutt(
                        "man, no. popping by isn’t attending, I mean sure it’s something but still, you could do better",
                        pop_norm)
                    sinu_jutt("probably")
                    jutt("so yeah, cut your losses and let’s go to class", pop_norm)
                    sinu_jutt("sure")
                    nadal += 1
                    uks_nadal = False
                    mangib = False
            elif usaldus == 3:
                while uks_nadal == True:
                    sinu_jutt("hey Friend!")
                    jutt("hey theree! Long time no see", pop_norm)
                    sinu_jutt("yeah that’s true, I’ve been busy")
                    jutt("talking with Misty, if my eyes have been correct", pop_norm)
                    sinu_jutt("yeahh that’s true")
                    jutt("so, do tell me, how´d it go?", pop_norm)

                    sinu_jutt("pretty well I’d have to say")
                    jutt("and what does that mean?", pop_norm)
                    sinu_jutt("that I’m going to the prom with Misty")
                    jutt("wait really? you actually did it?", pop_norm)
                    sinu_jutt("fair and square")
                    jutt("well damn. I didn’t think you had it in you", pop_norm)
                    sinu_jutt("well I did and I was great. now please, I’d like my bike")
                    jutt("I don’t have it on me, just come by my place afterwards", pop_norm)
                    sinu_jutt("no problem, piece of cake")
                    jutt("stop swagging", pop_norm)
                    sinu_jutt("when I stop being awesome")
                    jutt("god damn it what have I done", pop_norm)
                    jutt("please just get yourself to class", pop_norm)
                    sinu_jutt("alright alright I will")
                    jutt("good", pop_norm)
                    nadal += 1
                    uks_nadal = False
                    mangib = False

