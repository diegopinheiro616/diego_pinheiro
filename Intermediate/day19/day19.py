"""
Day 19 - More Turtle Graphics, Event Listeners, State and Multiple Instances
"""
# ################ Python Higher Order Functions & Events Listeners ###################
# function as imput
"""
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)  # <----  function as imput
screen.exitonclick()
"""
# ################ Exercise 1 ###################
# Make an Etch-A-Sketch App
"""
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
"""
# ################ Exercise 2 ###################
# Turtle Coordinate System - Parte 1
"""
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet: ", prompt="Which tutle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
print(user_bet)

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_position[turtle_index])

screen.exitonclick()
"""
# ################ Quiz ###################
"""
Question 1:
What's the heading of the following turtle?
🐢
Answer: 180 <---- E = 0, N = 90, W=180, S = 270

Question 2:
On the following 600px by 600px screen, what is the coordinate of the purple turtle?
Hint: All turtles by default have a height of 20px and width of 20px.
Answer = (x=-300,y=0) <---- The height and width are there to mislead you.
                            All turtle positions are measured from their center.
Question 3:
A turtle starts at position (0, 0) after the following line of code is executed, where will the turtle be?
turtle.goto(-150, 150)
Answer: A
"""
# ################ Exercise 2 ###################
# Aaaand, we're off to the races - Parte 2
"""
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet:", prompt="Which tutle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []
print(user_bet)

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()  # <---- pois a função color apresenta dois inputs. E só precisamos de 1
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
"""
