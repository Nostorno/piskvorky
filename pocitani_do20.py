from turtle import Turtle, Screen
import random, time

start = False
zadany_vysledek = ""
vypocet_dobre = 0
vypocet_spatne = 0
odehral = False

hlavni_okno = Screen()
hlavni_okno.title("Učíme se počítat do dvaceti")
hlavni_okno.setup(width=540, height=600)
hlavni_okno.bgpic("pozadi_matematika.gif")
hlavni_okno.tracer(False)

# kulicka na uvitaci obrazovce
kresleni = Turtle()
kresleni.shape("circle")
kresleni.color("yellow")
kresleni.penup()
kresleni.right(45)


def zacatek():
    global start
    start = True
    return start


hlavni_okno.listen()
hlavni_okno.onkeypress(zacatek, "space")


# kulicka na pozadi
def pozadi():
    global start
    while start == False:
        jede = True
        while jede == True:
            stara_x = round(kresleni.xcor())
            stara_y = round(kresleni.ycor())

            kresleni.forward(20)
            nova_x = round(kresleni.xcor())
            nova_y = round(kresleni.ycor())
            if nova_y > 280 and stara_x < nova_x:
                kresleni.right(90)
                jede = False
            elif nova_y > 280 and stara_x > nova_x:
                kresleni.left(90)
                jede = False
            elif nova_y < -280 and stara_x > nova_x:
                kresleni.right(90)
                jede = False
            elif nova_y < -280 and stara_x < nova_x:
                kresleni.left(90)
                jede = False

            elif nova_x > 250 and stara_y < nova_y:
                kresleni.left(90)
                jede = False
            elif nova_x > 250 and stara_y > nova_y:
                kresleni.right(90)
                jede = False
            elif nova_x < -250 and stara_y < nova_y:
                kresleni.right(90)
                jede = False
            elif nova_x < -250 and stara_y > nova_y:
                kresleni.left(90)
                jede = False
            time.sleep(0.03)
            hlavni_okno.update()
    kresleni.forward(2000)


pozadi()


hlavni_okno.bgpic("kalkulacka.gif")

priklad = Turtle()
priklad.hideturtle()
priklad.penup()
priklad.goto(-190, 165)

spravne = Turtle()
spravne.hideturtle()
spravne.penup()
spravne.goto(10, -193)
spravne.color("lightgreen")
spravne.write(vypocet_dobre, align="center", font=("Arial", 30, "normal"))

spatne = Turtle()
spatne.hideturtle()
spatne.penup()
spatne.goto(10, -275)
spatne.color("red")
spatne.write(vypocet_spatne, align="center", font=("Arial", 30, "normal"))

spravne_v = Turtle()
spravne_v.hideturtle()
spravne_v.penup()
spravne_v.goto(140, -203)
spravne_v.color("lightgreen")

spatne_v = Turtle()
spatne_v.hideturtle()
spatne_v.penup()
spatne_v.goto(140, -284)
spatne_v.color("red")

v_vysledku = Turtle()
v_vysledku.hideturtle()
v_vysledku.penup
v_vysledku.goto(0, 0)


def vygeneruj_priklad():
    novy = True
    while novy == True:
        cislo_prvni = random.randint(0, 20)
        cislo_druhe = random.randint(0, 20)
        pro_znamenko = random.randint(0, 100)
        if pro_znamenko < 51:
            znamenko = "+"
        else:
            znamenko = "-"

        if znamenko == "+":
            vysledek = cislo_prvni + cislo_druhe
            if vysledek > 20:
                novy = True
            else:
                novy = False

        if znamenko == "-":
            vysledek = cislo_prvni - cislo_druhe
            if vysledek < 0:
                novy = True
            else:
                novy = False

    zadani = str(cislo_prvni) + str(znamenko) + str(cislo_druhe) + str("=")

    return zadani, vysledek


def vykresleni_prikladu(zadani, zadany_vysledek):
    priklad.clear()
    priklad.color("black")
    priklad.write(
        f"{zadani}{zadany_vysledek}",
        align="left",
        font=("Arial", 65, "normal"),
    )


def zpocitat():
    global zadany_vysledek, vypocet_dobre, vypocet_spatne, vysledek, odehral
    if vysledek == int(zadany_vysledek):
        vypocet_dobre += 1
        spravne.clear()
        spravne.write(vypocet_dobre, align="center", font=("Arial", 30, "normal"))
        v_vysledku.color("lightgreen")
        v_vysledku.write("správně", align="center", font=("Arial", 80, "normal"))
        hlavni_okno.update()
        time.sleep(4)
        v_vysledku.clear()

    if vysledek != int(zadany_vysledek):
        vypocet_spatne += 1
        spatne.clear()
        spatne.write(vypocet_spatne, align="center", font=("Arial", 30, "normal"))
        spravne_v.write(vysledek, align="center", font=("Arial", 45, "normal"))
        spatne_v.write(zadany_vysledek, align="center", font=("Arial", 45, "normal"))
        v_vysledku.color("red")
        v_vysledku.write("špatně", align="center", font=("Arial", 80, "normal"))
        hlavni_okno.update()
        time.sleep(10)
        spatne_v.clear()
        spravne_v.clear()
        v_vysledku.clear()
    odehral = True
    zadany_vysledek = ""
    vysledek = 0


def vyhodnoceni_klavesy(x, y):
    global zadany_vysledek
    if y > 73 and y < 139:
        if x > -218 and x < -146:
            zadany_vysledek = zadany_vysledek + str(1)
        if x > -126 and x < -57:
            zadany_vysledek = zadany_vysledek + str(2)
        if x > -37 and x < 35:
            zadany_vysledek = zadany_vysledek + str(3)
        if x > 55 and x < 126:
            zadany_vysledek = zadany_vysledek + str(4)
        if x > 150 and x < 218:
            zadany_vysledek = zadany_vysledek + str(5)
    if y > -14 and y < 52:
        if x > -218 and x < -146:
            zadany_vysledek = zadany_vysledek + str(6)
        if x > -126 and x < -57:
            zadany_vysledek = zadany_vysledek + str(7)
        if x > -37 and x < 35:
            zadany_vysledek = zadany_vysledek + str(8)
        if x > 55 and x < 126:
            zadany_vysledek = zadany_vysledek + str(9)
        if x > 150 and x < 218:
            zadany_vysledek = zadany_vysledek + str(0)
    if y > -100 and y < -38:
        if x > -215 and x < -10:
            delka = len(zadany_vysledek)
            if delka > 0:
                zadany_vysledek = zadany_vysledek[:-1]
        if x > 13 and x < 220:
            zpocitat()


hlavni_okno.onscreenclick(vyhodnoceni_klavesy)


for cislo_prikladu in range(1, 11):
    odehral = False
    zadani, vysledek = vygeneruj_priklad()
    while odehral == False:
        vykresleni_prikladu(zadani, zadany_vysledek)
        hlavni_okno.update()
        time.sleep(0.2)


hlavni_okno.delay()
