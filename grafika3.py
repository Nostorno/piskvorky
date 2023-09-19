from turtle import Turtle, Screen  # import Turtle,Screen
import random

# zmena barevneho modu
import turtle

turtle.colormode(255)


tommy = Turtle()  # vytvorim zelvu objekt tommy
tommy.shape("arrow")  # shape - jak bude vypadat


def random_color(vyhodnoceni):
    if vyhodnoceni == 0:
        nova = "black"
    if vyhodnoceni == 1:
        nova = "red"
    if vyhodnoceni == 2:
        nova = "blue"
    if vyhodnoceni == 3:
        nova = "pink"
    if vyhodnoceni == 4:
        nova = "green"
    if vyhodnoceni == 5:
        nova = "violet"
    return nova


barva = 0
# tommy.pencolor("black")
tommy.speed(20)
for tah in range(100):
    tommy.pencolor(random_color(barva))
    tommy.forward(tah)
    tommy.right(60)
    barva += 1
    if barva > 5:
        barva = 0


my_screen = Screen()  # do my_screen ulozi obrazovku
my_screen.exitonclick()  # okno se musi vypnout

# jiny zpusob pomoci modulo !!!

seznam = ["violet", "yellow", "red", "green", "blue", "pink"]  # seznam barev
# v seznamu vybere barvu ( tah deleno 6 = zbytek ( je 0- 5))
tommy.pencolor(seznam[tah % 6])
