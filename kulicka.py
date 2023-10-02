from turtle import Turtle, Screen
import random, time

start = False
poloha_desky = 0
score = 0
bonus = False
poloha_bonus_x = None
rychlost = 0.025
deska = 5
velikost_textu = 50
text_bonusu = "ZAČÍNÁME"

# hlavni hraci okno
hlavni_okno = Screen()
hlavni_okno.bgcolor("black")
hlavni_okno.title("xxx")
hlavni_okno.setup(width=540, height=900)
hlavni_okno.bgpic("vektor.gif")
hlavni_okno.tracer(False)

# hraci kulicka
kulicka = Turtle()
kulicka.shape("circle")
kulicka.color("yellow")
kulicka.penup()
kulicka.right(45)

# hraci desticka
desticka = Turtle()
desticka.shape("square")
desticka.turtlesize(stretch_wid=0.5, stretch_len=deska)
desticka.color("red")
desticka.penup()
desticka.goto(0, -410)
desticka.move = "stop"


game_ove = Turtle()
game_ove.hideturtle()
game_ove.penup()
game_ove.goto(0, 275)
game_ove.color("lightgreen")

# pocet bodu
body = Turtle()
body.hideturtle()
body.penup
body.goto(0, 92)
body.color("yellow")
body.write(score, align="center", font=("Arial", 60, "normal"))
hlavni_okno.update()

# kulicka + / -
bonus_kulicka = Turtle()
bonus_kulicka.shape("circle")
bonus_kulicka.color("lightgreen")
bonus_kulicka.penup()
bonus_kulicka.goto(0, 470)

# textove pole / info bonus
bonus_text = Turtle()
bonus_text.hideturtle()
bonus_text.penup()
bonus_text.left(90)
bonus_text.color("yellow")
bonus_text.goto(0, 290)


# nastaveni na reakci klaves
def move_right():
    desticka.move = "right"


def move_left():
    desticka.move = "left"


def move_stop():
    desticka.move = "stop"


# pohyb desky
def move():
    global poloha_desky
    if desticka.move == "left":
        poloha_desky = desticka.xcor()
        if poloha_desky <= -220:
            poloha_desky = -216
        desticka.setx(poloha_desky - 4)
        poloha_desky -= 3

    if desticka.move == "right":
        poloha_desky = desticka.xcor()
        if poloha_desky >= 220:
            poloha_desky = 216
        desticka.setx(poloha_desky + 4)
        poloha_desky += 3


def vygenerovani_bonusu():
    global bonus, poloha_bonus_x
    if bonus == False:
        nahoda = random.randint(0, 101)
        if nahoda < 33:
            bonus = True
            poloha_bonus_x = random.randint(-250, 250)
            bonus_kulicka.goto(poloha_bonus_x, 460)


# kdyz seberu bonus
def bonus_postih():
    global rychlost, deska, velikost_textu, text_bonusu
    neco = random.randint(1, 4)
    velikost_textu = 45
    if neco == 1:
        rychlost += 0.005
        bonus_text.color("lightgreen")
        desticka.color("lightgreen")
        text_bonusu = "RYCHLOST"
        if rychlost > 0.065:
            rychlost = 0.65

    if neco == 2:
        rychlost -= 0.005
        desticka.color("red")
        bonus_text.color("red")
        text_bonusu = "RYCHLOST"
        if rychlost < 0:
            rychlost = 0

    if neco == 3:
        deska -= 1
        if deska < 1:
            deska = 1
        desticka.color("red")
        bonus_text.color("red")
        text_bonusu = "DESKA"
        desticka.turtlesize(stretch_wid=0.5, stretch_len=deska)

    if neco == 4:
        deska += 1
        if deska > 10:
            deska = 10
        desticka.color("lightgreen")
        bonus_text.color("lightgreen")
        text_bonusu = "DESKA"
        desticka.turtlesize(stretch_wid=0.5, stretch_len=deska)


def score_rychlost():
    global score, rychlost, text_bonusu, velikost_textu
    score += 1
    body.clear()
    body.write(score, align="center", font=("Arial", 60, "normal"))
    if score % 10 == 0:
        rychlost -= 0.005
        text_bonusu = "LEVEL"
        velikost_textu = 45


# akcni klavesy
hlavni_okno.listen()
hlavni_okno.onkeypress(move_right, "Right")
hlavni_okno.onkeypress(move_left, "Left")
hlavni_okno.onkeypress(move_stop, "space")


# jadro
def pozadi():
    global start, poloha_desky, score, bonus, rychlost, velikost_textu, text_bonusu
    while start == False:
        jede = True
        vygenerovani_bonusu()
        while jede == True:
            bonus_text.clear()
            if velikost_textu > 1:
                velikost_textu -= 1
                bonus_text.write(
                    text_bonusu,
                    align="center",
                    font=("Arial", velikost_textu, "normal"),
                )

            if bonus == True:
                y = bonus_kulicka.ycor()
                bonus_kulicka.sety(y - 10)
                if (y - 10) < -390 and abs(poloha_desky - poloha_bonus_x) <= (
                    10 * deska
                ):
                    bonus_kulicka.goto(0, 470)
                    bonus = False
                    bonus_postih()
                    score_rychlost()
                if y < -460:
                    bonus_kulicka.goto(0, 470)
                    bonus = False

            stara_x = round(kulicka.xcor())
            stara_y = round(kulicka.ycor())
            kulicka.forward(5)
            nova_x = round(kulicka.xcor())
            nova_y = round(kulicka.ycor())
            # print(poloha_desky, nova_x, nova_y, bonus, poloha_bonus_x, rychlost, deska)
            if nova_y > 440 and stara_x < nova_x:
                kulicka.right(90)
                jede = False
            elif nova_y > 440 and stara_x > nova_x:
                kulicka.left(90)
                jede = False

            elif nova_y < -450:
                jede = False
                start = True

            elif nova_y < -390 and stara_x > nova_x and nova_y > -396:
                if abs(poloha_desky - nova_x) <= (10 * deska):
                    kulicka.right(90)
                    score_rychlost()

            elif nova_y < -390 and stara_x < nova_x and nova_y > -396:
                if abs(poloha_desky - nova_x) <= (10 * deska):
                    kulicka.left(90)
                    score_rychlost()

            elif nova_x > 250 and stara_y < nova_y:
                kulicka.left(90)
                jede = False
            elif nova_x > 250 and stara_y > nova_y:
                kulicka.right(90)
                jede = False
            elif nova_x < -260 and stara_y < nova_y:
                kulicka.right(90)
                jede = False
            elif nova_x < -260 and stara_y > nova_y:
                kulicka.left(90)
                jede = False

            move()
            hlavni_okno.update()
            time.sleep(rychlost)
    kulicka.forward(2000)


for cas in range(5, 0, -1):
    game_ove.clear()
    game_ove.write(cas, align="center", font=("Arial", 50, "normal"))
    hlavni_okno.update()
    time.sleep(1)
game_ove.clear()

pozadi()

game_ove.write("Game over", align="center", font=("Arial", 50, "normal"))


hlavni_okno.exitonclick()
