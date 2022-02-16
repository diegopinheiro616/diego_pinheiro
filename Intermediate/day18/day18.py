"""
Day 18 - Turtle & The Graphical User Interface (GUI)
"""
# ################ Turtle ####################
"""
from turtle import Turtle, Screen  # Moduleee

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("circle")
timmy_the_turtle.color("yellow")

screen = Screen()
screen.exitonclick()
"""
# ################ Exercise 1 ###################
# Draw a Square
"""
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")

# for _ in range(4):
#    timmy_the_turtle.forward(100)
#    timmy_the_turtle.left(90)

tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)
"""
# ################ Basic Import ###################
"""
#import turle
# tim = turtle.Turtle()

# from turtle import Turtle
# tim = Turtle()
# tom = Turtle()
# Tia = Turtle()

from turtle import *  # <---- Importa tudo(modules)!!!! Evitar!
# tim = Turtle()
"""
# ################ Aliasing Modules ###################
"""
import turtle as t
tim = t.Turlte()
"""
# ################ Installing Modules ###################
"""
import heroes  # Dá para instalar direto do pycharm. Só clicar na lâmpada vermelha e clicar.
print(heroes.gen())
"""
# ################ Exercise 2 ###################
# Draw a Dashed Line
"""
import turtle as t
tim = t.Turtle()

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.penup()
"""
# ################ Exercise 3 ###################
# Drawing differents Shapes
"""
import turtle as t
import random

tim = t.Turtle()

colours = ["red", "blue", "yellow", "black"]

num_sides = 3

def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shapes_side_n in range(3,11):
    tim.color(random.choice(colours))
    draw_shapes(shapes_side_n)
"""
# ################ Exercise 4 ###################
# Drawing a Random Walk
"""
import turtle as t
import random

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")
for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))
"""
# ################ Python Tuples and How to Generate Random RGB Colours ###################
"""
# Python Tuples lembra uma lista

# my_tuple = (1, 3, 8) <---- Não pode editar. Carved in Stone... Immutable

# list(my_tuple) <---- Aí o Tuple vira List!

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
"""
# ################ Exercise 5 ###################
# Draw a Spirograph
"""
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.speed("fastest")
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(3)

screen = t.Screen()
screen.exitonclick()
"""
# ################ Exercise 6 ###################
# The Hirst Painting Project - Parte 1 - Colorgram - Extraindo cores
"""
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 6)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

# colors = (242, 240, 237), (244, 245, 247), (245, 240, 243), (237, 244, 241), (174, 21, 47), (179, 78, 35)

# site verificação das cores ---> https://www.w3schools.com/colors/colors_rgb.asp
"""
# ################ Exercise 6 ###################
# The Hirst Painting Project - Parte 2 - Quadro
"""
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(137, 186, 237), (244, 188, 54), (236, 20, 21), (204, 89, 160), (174, 21, 47), (179, 223, 35)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
"""