#################################################################
# FILE : hello_turtle.py
# WRITER : Yair Shtern
# EXERCISE : intro2cs1 ex1 2020
# DESCRIPTION: A simple program that draw a bed of 3 flowers.
#################################################################
import turtle
def draw_petal():
    # Turtle draw one petal.
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)


def draw_flower():
    # Turtle draw one flower using 4 petals.
    turtle.left(45)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(135)
    turtle.forward(150)


def draw_flower_and_advance():
    # Turtle draw flower and advance.
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()


def draw_flower_bed():
    # Turtle draw bad of 3 flowers by using the previous functionsand.
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()

    draw_flower_and_advance()
    draw_flower_and_advance()
    draw_flower_and_advance()

if __name__ == "__main__":
    draw_flower_bed()
    turtle.done()