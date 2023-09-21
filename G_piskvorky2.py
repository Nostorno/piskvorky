# ovladani - sipky / mezernik - obsazeni pole

from turtle import Turtle, Screen
import random, time
from data10x10 import moznosti_hrac_2, moznosti_hrac_3, moznosti_hrac_4
from data10x10 import moznosti_pc_2, moznosti_pc_3, moznosti_pc_4

x_osa = 0  # aktualni pozice hrace v radku (0-9)
y_osa = 0  # sloupci
hraci_seznam_hodnoty = []  # seznam hodnot policek (n,z,c)
tahy_hrace = []  # souradnice vhodnych tahu
prvni_kolo = False  # prvni kolo pc
hraj = False  # zda hrac odehral

# nastaveni hraciho okna
hraci_okno = Screen()
hraci_okno.title("Hrajeme piskvorky")
hraci_okno.setup(width=600, height=600)
hraci_okno.tracer(False)

# nastaveni bodu pc
pc = Turtle()
pc.shape("circle")
pc.penup()
pc.speed(150)
pc.left(90)
pc.setpos(225, 225)

# nastaveni bodu hrace
kurzor = Turtle()
kurzor.shape("circle")
kurzor.penup()
kurzor.speed(150)
kurzor.setpos(-250, 250)

# nastaveni bodu text - vyhodnoceni
info = Turtle()
info.penup()
info.goto(0, 260)
info.color("white")

# vykresleni herniho pole
kurzor.pendown()
kurzor.pensize(5)
for aaa in range(11):
    kurzor.forward(500)
    kurzor.right(90)
    kurzor.forward(aaa * 50)
    kurzor.right(90)
    kurzor.forward(500)
    kurzor.right(90)
    kurzor.forward(aaa * 50)
    kurzor.right(90)
kurzor.right(90)
for aaa in range(11):
    kurzor.forward(500)
    kurzor.left(90)
    kurzor.forward(aaa * 50)
    kurzor.left(90)
    kurzor.forward(500)
    kurzor.left(90)
    kurzor.forward(aaa * 50)
    kurzor.left(90)
kurzor.penup()
kurzor.setpos(-225, 225)


# funkce vytvoreni seznamu hodnot
def vytvoreni_seznamu():
    for cislo in range(10):
        rada = ["n"] * 10
        hraci_seznam_hodnoty.append(rada)


vytvoreni_seznamu()


# vypise hodnoty hraci plochy !! klavesa H !!
def hodnoty():
    for radek in range(0, 10):
        for sloupec in range(0, 10):
            if sloupec < 9:
                print(hraci_seznam_hodnoty[radek][sloupec], end="")
            elif sloupec == 9:
                print(hraci_seznam_hodnoty[radek][sloupec])
    time.sleep(4)


def hrac():  # hrac obsadi policko
    global hraj, nyni_hrac, nyni_pocitac
    tah = hraci_seznam_hodnoty[y_osa][x_osa]
    if tah == "z" or tah == "c":
        print("policko je jiz obsazene!")
    elif tah == "n":
        hraci_seznam_hodnoty[y_osa][x_osa] = "z"
        obarveni_pole_hrac()
        vyhodnoceni()
        hraj = False


def pocitac():
    global prvni_kolo, pc_x_graf, pc_y_graf, hraj, tahy_hrace, budouci, tahy_hrace, nyni_hrac, nyni_pocitac
    nyni_pocitac = 1
    nyni_hrac = 1
    vyhodnoceni()
    budouci = 0  # hrac v dalsim kole
    tahy_hrace = []  # seznam moznych tahu
    tahy_hrace_nutne = []
    hledani_tahu_pc = nyni_hrac  # zapise aktualni pocet
    for hledani in range(500):
        pc_x = random.randint(0, 9)
        pc_y = random.randint(0, 9)
        pc_tah = hraci_seznam_hodnoty[pc_y][pc_x]
        if pc_tah == "n":  # pole je volne, zapise z
            hraci_seznam_hodnoty[pc_y][pc_x] = "z"
            vyhodnoceni()
            hraci_seznam_hodnoty[pc_y][pc_x] = "n"
            if nyni_hrac > hledani_tahu_pc:  # je vyssi nez predchazejici?
                souradnice_hrace = str(pc_x) + str(pc_y)
                tahy_hrace.append(souradnice_hrace)  # ulozi souradnice do seznamu
            if nyni_hrac > (hledani_tahu_pc + 1):
                souradnice_hrace = str(pc_x) + str(pc_y)
                tahy_hrace_nutne.append(souradnice_hrace)
            if budouci < nyni_hrac:  # do budouci zapise nejvyssi nalezeny pocet
                budouci = nyni_hrac
        nyni_hrac = hledani_tahu_pc  # vrati promenou nyni_hrac do puvodniho stavu
    pocitac_odehral = False  # zda PC odehral
    hraj = True
    nenalezeno = 0  # pocet opakovani v pripade nevhodneho tahu
    print(nyni_hrac, nyni_pocitac, budouci)
    print(tahy_hrace)
    print(tahy_hrace_nutne)
    time.sleep(3)
    if (
        nyni_pocitac < nyni_hrac
        or nyni_pocitac == nyni_hrac
        and (budouci - nyni_pocitac) > 1
        or budouci == 5
        and (nyni_pocitac - nyni_hrac) == 1
    ):
        if len(tahy_hrace_nutne) > 0:
            print("nutne")
            pc_x = int(tahy_hrace_nutne[0][0])
            pc_y = int(tahy_hrace_nutne[0][1])
            hraci_seznam_hodnoty[pc_y][pc_x] = "c"
            pc_x_graf = (pc_x * 50) - 225
            pc_y_graf = ((pc_y * 50) - 225) * -1
            obarveni_pole_pc()
            pocitac_odehral = True
            tahy_hrace = []
            tahy_hrace_nutne = []

        else:
            print("pouze pole")
            kolik_tahu_je = len(tahy_hrace)
            aaa = nyni_pocitac
            for bonus in range(kolik_tahu_je):
                pc_x = int(tahy_hrace[bonus][0])
                pc_y = int(tahy_hrace[bonus][1])
                hraci_seznam_hodnoty[pc_y][pc_x] = "c"
                vyhodnoceni()
                if nyni_pocitac > aaa:
                    pc_x_graf = (pc_x * 50) - 225
                    pc_y_graf = ((pc_y * 50) - 225) * -1
                    obarveni_pole_pc()
                    pocitac_odehral = True
                    # vyhodnoceni()
                    # budouci = nyni_hrac
                    tahy_hrace = []
                    tahy_hrace_nutne = []
                    break
                else:
                    hraci_seznam_hodnoty[pc_y][pc_x] = "n"

            if aaa == nyni_pocitac:
                pc_x = int(tahy_hrace[0][0])
                pc_y = int(tahy_hrace[0][1])
                pc_x_graf = (pc_x * 50) - 225
                pc_y_graf = ((pc_y * 50) - 225) * -1
                obarveni_pole_pc()
                hraci_seznam_hodnoty[pc_y][pc_x] = "c"
                pocitac_odehral = True
                vyhodnoceni()
                budouci = nyni_hrac
                tahy_hrace = []
                tahy_hrace_nutne = []

    while not pocitac_odehral:  # hlavni smycka
        if prvni_kolo == False:  # podminka pro prvni tah PC
            pc_x = random.randint(4, 5)
            pc_y = random.randint(4, 5)
            prvni_kolo = True
            pc_x_graf = (pc_x * 50) - 225
            pc_y_graf = ((pc_y * 50) - 225) * -1
            obarveni_pole_pc()
            hraci_seznam_hodnoty[pc_y][pc_x] = "c"
            vyhodnoceni()
            pocitac_odehral = True

        else:  # dalsi kola
            pc_x = random.randint(0, 9)
            pc_y = random.randint(0, 9)
            pc_x_graf = (pc_x * 50) - 225
            pc_y_graf = ((pc_y * 50) - 225) * -1
            souradnice = str(pc_x) + str(pc_y)
            pc_tah = hraci_seznam_hodnoty[pc_y][pc_x]
            if pc_tah == "n":  # kontrola zda je pole volne
                hraci_seznam_hodnoty[pc_y][pc_x] = "c"
                pc_uktualne = nyni_pocitac  # ulozeni aktualniho stavu PC
                vyhodnoceni()

                if nyni_pocitac > pc_uktualne:  # tah vhodny
                    nenalezeno += 1
                    if nenalezeno < 250 and souradnice in tahy_hrace:
                        pocitac_odehral = True
                        nenalezeno = 0
                        obarveni_pole_pc()

                    elif nenalezeno > 250:  # uz jen vhodny
                        pocitac_odehral = True
                        nenalezeno = 0
                        obarveni_pole_pc()

                    else:
                        nyni_pocitac = pc_uktualne
                        hraci_seznam_hodnoty[pc_y][pc_x] = "n"

                else:  # tah je nevhodny, bude generovat novou pozici / pak - 1
                    hraci_seznam_hodnoty[pc_y][pc_x] = "n"
                    nenalezeno += 1
                    if nenalezeno > 500:
                        nenalezeno = 0
                        nyni_pocitac -= 1
            else:  # kdyz je pole obsazene
                nenalezeno += 1


def vyhodnoceni():
    global nyni_hrac, nyni_pocitac
    kombinace = []  # seznam hernich moznosti
    for radky in range(10):  # kombinace radky
        jedna_kombinace = "".join(hraci_seznam_hodnoty[radky][0:10])
        jedna_kombinace = "x" + jedna_kombinace + "x"
        kombinace.append(jedna_kombinace)
    for sloupce in range(10):  # kombinace sloupce
        jedna_kombinace = "".join([seznam[sloupce] for seznam in hraci_seznam_hodnoty])
        jedna_kombinace = "x" + jedna_kombinace + "x"
        kombinace.append(jedna_kombinace)
    jedna_kombinace = ""

    for y in range(4, 10):  # kombinace diagonalni cast 1
        for x in range(y, -1, -1):
            jedna_kombinace += hraci_seznam_hodnoty[x][y - x]
        jedna_kombinace = "x" + jedna_kombinace + "x"
        kombinace.append(jedna_kombinace)
        jedna_kombinace = ""

    for y in range(5):  # kombinace diagonalni cast 2
        for x in range(9, 4 - y, -1):
            jedna_kombinace += hraci_seznam_hodnoty[x][9 - x + 5 - y]
        jedna_kombinace = "x" + jedna_kombinace + "x"
        kombinace.append(jedna_kombinace)
        jedna_kombinace = ""

    for y in range(6):  # kombinace diagonalni cast 3
        pomocna_p = 0
        for x in range(0 + y, 10):
            jedna_kombinace += hraci_seznam_hodnoty[x][pomocna_p]
            pomocna_p += 1
        jedna_kombinace = "x" + jedna_kombinace + "x"
        kombinace.append(jedna_kombinace)
        jedna_kombinace = ""

    pomocna_p = 6  #  kombinace diagonalni cast 4
    for y in range(5):
        pomocna_p -= 1
        for x in range(5 + y):
            jedna_kombinace += hraci_seznam_hodnoty[x][pomocna_p + x]
        jedna_kombinace = "x" + jedna_kombinace + "x"
        kombinace.append(jedna_kombinace)
        jedna_kombinace = ""

    testovaci_hrac = 0
    testovaci_pc = 0

    for seznam in kombinace:  # projde seznam kombinace
        if "c" in seznam:  # pro pc
            nyni_pocitac = 1
        for moznosti2 in moznosti_pc_2:
            if moznosti2 in seznam:
                nyni_pocitac = 2
        for moznosti3 in moznosti_pc_3:
            if moznosti3 in seznam:
                nyni_pocitac = 3
        for moznosti4 in moznosti_pc_4:
            if moznosti4 in seznam:
                nyni_pocitac = 4
        if "ccccc" in seznam:
            nyni_pocitac = 5
        if testovaci_pc < nyni_pocitac:
            testovaci_pc = nyni_pocitac

        if "z" in seznam:  # pro hrace
            nyni_hrac = 1
        for moznosti2 in moznosti_hrac_2:
            if moznosti2 in seznam:
                nyni_hrac = 2
        for moznosti3 in moznosti_hrac_3:
            if moznosti3 in seznam:
                nyni_hrac = 3
        for moznosti4 in moznosti_hrac_4:
            if moznosti4 in seznam:
                nyni_hrac = 4
        if "zzzzz" in seznam:
            nyni_hrac = 5
        if testovaci_hrac < nyni_hrac:
            testovaci_hrac = nyni_hrac

    nyni_hrac = testovaci_hrac
    nyni_pocitac = testovaci_pc


def pohyb_up():  # pohyb po hraci plose
    global x_osa, y_osa
    y = kurzor.ycor()
    y_osa -= 1
    if y >= 225:
        y = -275
        y_osa = 9
    kurzor.sety(y + 50)


def pohyb_down():
    global x_osa, y_osa
    y_osa += 1
    y = kurzor.ycor()
    if y <= -225:
        y = 275
        y_osa = 0
    kurzor.sety(y - 50)


def pohyb_left():
    global x_osa, y_osa
    x_osa -= 1
    x = kurzor.xcor()
    if x <= -225:
        x = 275
        x_osa = 9
    kurzor.setx(x - 50)


def pohyb_right():
    global x_osa, y_osa
    x_osa += 1
    x = kurzor.xcor()
    if x >= 225:
        x = -275
        x_osa = 0
    kurzor.setx(x + 50)


# obarveni pole hrace (grafika)
def obarveni_pole_hrac():
    kurzor.pensize(1)
    kurzor.forward(21)
    kurzor.pendown()
    kurzor.left(90)
    kurzor.fillcolor("green")
    kurzor.begin_fill()
    kurzor.circle(21)
    kurzor.end_fill()
    kurzor.left(90)
    kurzor.penup()
    kurzor.forward(21)
    kurzor.left(180)
    kurzor.fillcolor("black")


# obarveni pole pc (grafika)
def obarveni_pole_pc():
    pc.setpos(pc_x_graf, pc_y_graf)
    pc.pensize(1)
    pc.backward(21)
    pc.pendown()
    pc.right(90)
    pc.fillcolor("red")
    pc.begin_fill()
    pc.circle(21)
    pc.end_fill()
    pc.left(90)
    pc.penup()
    pc.forward(21)
    pc.left(180)
    pc.fillcolor("black")


def zobrazeni_vyherce():  # zobrazeni vysledku hry
    info.clear()
    info.color("black")
    info.write(vyherce, align="center", font=("Arial", 25, "normal"))
    info.color("white")


# kliknutim na klavesy
hraci_okno.listen()
hraci_okno.onkeypress(pohyb_right, "Right")
hraci_okno.onkeypress(pohyb_left, "Left")
hraci_okno.onkeypress(pohyb_down, "Down")
hraci_okno.onkeypress(pohyb_up, "Up")
hraci_okno.onkeypress(hrac, "space")
hraci_okno.onkeypress(hodnoty, "h")

# hlavni cyklus
# global nyni_hrac, nyni_pocitac, budouci
for pocet_kol in range(50):
    pocitac()
    if nyni_pocitac == 5:
        vyherce = "VYHRAL POCITAC"
        zobrazeni_vyherce()
        hraci_okno.update()
        break
    while hraj == True:
        if nyni_hrac == 5:
            break
        time.sleep(0.1)
        print(
            f"x:{x_osa} y:{y_osa} hrac:{nyni_hrac} pocitac: {nyni_pocitac} budouci: {budouci}"
        )
        hraci_okno.update()
    if nyni_hrac == 5:
        vyherce = "ZVITEZIL JSI"
        zobrazeni_vyherce()
        hraci_okno.update()
        break

hraci_okno.exitonclick()
# print(f"x:{x_osa} y:{y_osa} hrac:{nyni_hrac} pocitac: {nyni_pocitac} budouci: {budouci}")
