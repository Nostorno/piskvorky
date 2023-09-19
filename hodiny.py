from turtle import Turtle, Screen
import time, random

cas = 0.0

minuty = ["čtvrt", "půl", "třičtvrtě", "cela"]
hodiny_15_45 = [
    "jednu",
    "dvě",
    "tři",
    "čtyři",
    "pět",
    "šest",
    "sedm",
    "osm",
    "devět",
    "deset",
    "jedenáct",
    "dvanáct",
]
hodiny_30 = [
    "jedné",
    "druhé",
    "třetí",
    "čtvrté",
    "páté",
    "šesté",
    "sedmé",
    "osmé",
    "deváté",
    "desáté",
    "jedenácté",
    "dvanácté",
]

mala = Turtle()  # mala raficka - hodinova
mala.shape("circle")
mala.color("red")
velka = Turtle()  # velka raficka - minutova
velka.shape("circle")
velka.color("blue")

spravne_spatne = Turtle()  # titulek / vysledek
spravne_spatne.penup()
spravne_spatne.goto(0, 310)

informace = Turtle()  # zadany cas pro nastaveni
informace.penup()
informace.goto(0, -340)

okno = Screen()  # nastavei okna
okno.title("hodiny pro holky")
okno.setup(width=620, height=720)
okno.bgpic("hodinky.gif")
okno.tracer(False)


def move_right():
    spravne_spatne.clear()
    global cas
    cas = cas + 0.25
    if cas > 12:
        cas = 0.25
    mala.clear()
    velka.clear()
    uhel = -7.5
    mala.left(uhel)
    mala.pensize(20)
    mala.forward(180)
    mala.backward(180)
    uhel = -90
    velka.left(uhel)
    velka.pensize(10)
    velka.forward(270)
    velka.backward(270)


def move_left():
    spravne_spatne.clear()
    global cas
    cas = cas - 0.25
    if cas < 0:
        cas = 11.75
    mala.clear()
    velka.clear()
    uhel = 7.5
    mala.left(uhel)
    mala.pensize(20)
    mala.forward(180)
    mala.backward(180)
    uhel = 90
    velka.left(uhel)
    velka.pensize(10)
    velka.forward(270)
    velka.backward(270)


def vysledek():
    spravne_spatne.clear()
    if cas != final_cas:
        spravne_spatne.color("red")
        spravne_spatne.write("Špatně", align="center", font=("Arial", 30, "normal"))

    if cas == final_cas:
        spravne_spatne.color("green")
        spravne_spatne.write("Správně", align="center", font=("Arial", 30, "normal"))

    spravne_spatne.color("white")


def novy_cas():
    spravne_spatne.clear()
    informace.clear()
    informace.color("black")
    global final_cas
    cas_minuty = random.choice(minuty)
    if cas_minuty == "čtvrt":
        c_m = 0.25
        c_h = random.randint(0, 11)
        cas_hodina = hodiny_15_45[c_h]
        final = str(cas_minuty) + " na " + str(cas_hodina)
        final_cas = c_h + c_m
    elif cas_minuty == "půl":
        c_m = 0.5
        c_h = random.randint(0, 11)
        cas_hodina = hodiny_30[c_h]
        final = str(cas_minuty) + " " + str(cas_hodina)
        final_cas = c_h + c_m
    elif cas_minuty == "třičtvrtě":
        c_m = 0.75
        c_h = random.randint(0, 11)
        cas_hodina = hodiny_15_45[c_h]
        final = str(cas_minuty) + " na " + str(cas_hodina)
        final_cas = c_h + c_m
    else:
        c_h = random.randint(0, 11)
        cas_hodina = hodiny_15_45[c_h]
        final = str(cas_hodina) + " hodin/y "
        final_cas = c_h + 1

    informace.write(final, align="center", font=("Arial", 25, "normal"))
    informace.color("white")


okno.listen()  # ovladaci klavesy
okno.onkeypress(move_right, "Right")
okno.onkeypress(move_left, "Left")
okno.onkeypress(vysledek, "Return")
okno.onkeypress(novy_cas, "space")

# startovni pozice raficek
velka.left(90)
velka.pensize(10)
velka.forward(270)
velka.backward(270)
mala.left(90)
mala.pensize(20)
mala.forward(180)
mala.backward(180)

novy_cas()


while True:
    time.sleep(0.01)
    okno.update()

okno.exitonclick()  # okno se musi vypnout
