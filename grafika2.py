from turtle import Turtle, Screen  # import Turtle,Screen
import random

# zmena barevneho modu
import turtle

turtle.colormode(255)


tommy = Turtle()  # vytvorim zelvu objekt tommy
tommy.shape("turtle")  # shape - jak bude vypadat


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


tommy.pencolor("white")
tommy.forward(300)
tommy.right(90)
tommy.pencolor("black")
tommy.forward(200)
tommy.right(90)
tommy.forward(600)
tommy.right(90)
tommy.forward(400)
tommy.right(90)
tommy.forward(600)
tommy.right(90)
tommy.forward(200)
tommy.right(90)
tommy.pencolor("white")
tommy.forward(300)
tommy.pencolor("blue")
tommy.right(90)

# velikost okna je 600 * 400
# zelva kouka na 12ku

start_uhel = 45  # random.randint(1, 90)

tommy.speed(0)
tommy.right(start_uhel)

for jeden_tah in range(30):
    tommy.pencolor(random_color())
    jede = True
    print(jeden_tah)
    while jede == True:
        stara_x = round(tommy.xcor())
        stara_y = round(tommy.ycor())

        tommy.forward(2)
        nova_x = round(tommy.xcor())
        nova_y = round(tommy.ycor())
        if nova_y > 199 and stara_x < nova_x:
            tommy.right(90)
            jede = False
        elif nova_y > 199 and stara_x > nova_x:
            tommy.left(90)
            jede = False
        elif nova_y < -199 and stara_x > nova_x:
            tommy.right(90)
            jede = False
        elif nova_y < -199 and stara_x < nova_x:
            tommy.left(90)
            jede = False

        elif nova_x > 299 and stara_y < nova_y:
            tommy.left(90)
            jede = False
        elif nova_x > 299 and stara_y > nova_y:
            tommy.right(90)
            jede = False
        elif nova_x < -299 and stara_y < nova_y:
            tommy.right(90)
            jede = False
        elif nova_x < -299 and stara_y > nova_y:
            tommy.left(90)
            jede = False


# tommy.forward(10)
# x = round(tommy.xcor())
# y = round(tommy.ycor())
# print(x, y)

my_screen = Screen()  # do my_screen ulozi obrazovku
my_screen.exitonclick()  # okno se musi vypnout
