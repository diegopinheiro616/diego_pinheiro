"""
Day 20 - Build the snake game - Part 1: Animation & Coordinates
"""
# ################ Intro ###################
"""
Construção em 7 partes:
Day 1 - Create a snake body
        Move the snake
        Create snake food
Day 2 - Dectect collision with food
        Create a scoreboard
        Detect collision with wall
        Detect collision with tail
"""
# ################ Screen Setup and Creating Snake Body ###################
"""
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jogo da Cobrinha")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)

screen.exitonclick()
"""
# ################ Animating the Snake Segments on Screen ###################
"""
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jogo da Cobrinha")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):  # start= len(segments) -1, stop = 0, step = -1
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

screen.exitonclick()
"""
# ################ Create a Snake Class & Move to OOP ###################
"""
# Criar três classes: Snakes, Food, Scoreboard

from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jogo da Cobrinha")
screen.tracer(0)  # Desliga animação da tartaruga (movimentação)

snake = Snake()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
"""
# ################ How to Control the Snake with the a Keypress ###################
"""
# Criar três classes: Snakes, Food, Scoreboard

from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jogo da Cobrinha")
screen.tracer(0)  # Desliga animação da tartaruga (movimentação)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")  # <----Inicial Maiuscula pois é uma tecla do teclado
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
"""
"""
Day 21 - Build the snake game - Part 2: Inheritance & List Slicing
"""
# ################ Class Inheritance ###################
"""
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()  # <---- ATIVA a Superclass Animal

    def swim(self):
        print("Moving in water.")

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
"""
# ################ Quiz ###################
"""
Question 1:
Given the following:

class Dog:
    def __init__(self):
        self.temperament = "loyal"
 
    def bark(self):
        print("Woof, woof!")
        
How do you create a class called Labrador (the subclass) that inherits from the Dog class (the superclass)?

Answer:
class Labrador(Dog):
    def __int__(self):
        self.temperament = "friendly"  <---- The call to "super()" in the initialiser is recommended, but not strictly
                                             reguired.

Question 2:
Given this:

class Dog:
    def __init__(self):
        self.temperament = "loyal"
 
class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.temperament = "gentle"


What will this code print?

doggo = Dog()
print(f"A dog is {doggo.temperament}")
 
sparky = Labrador()
print(f"Sparky is {sparky.temperament}")

Answer: A dog is loyal
        Spark is gentle
        
Question 3:
Given this code:

class Dog:
    def __init__(self):
        self.temperament = "loyal"
 
    def bark(self):
        print("Woof, woof!")
 
class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.is_a_good_boy = True
 
    def bark(self):
        super().bark()
        print("Greetings, good sir. How do you do?")


What will this print?

sparky = Labrador()
sparky.bark()

Answer: Woof, woof!                          <---- Correct. We are extending the functionality of the bark() method.
        Greetings, good sir. How do you do?
"""
# ################ Detect Collisions with Food ###################
"""
from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jogo da Cobrinha")
screen.tracer(0)  # Desliga animação da tartaruga (movimentação)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")  # <----Inicial Maiuscula pois é uma tecla do teclado
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()


screen.exitonclick()
"""
# ################ Create a Scoreboard and Keep Score ###################
"""
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jogo da Cobrinha")
screen.tracer(0)  # Desliga animação da tartaruga (movimentação)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")  # <----Inicial Maiuscula pois é uma tecla do teclado
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()

screen.exitonclick()
"""
# ################ Detect Collisions with a Wall ###################
"""
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jogo da Cobrinha")
screen.tracer(0)  # Desliga animação da tartaruga (movimentação)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")  # <----Inicial Maiuscula pois é uma tecla do teclado
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
"""
# ################ Detect Collisions with your own tail ###################
"""
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jogo da Cobrinha")
screen.tracer(0)  # Desliga animação da tartaruga (movimentação)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")  # <----Inicial Maiuscula pois é uma tecla do teclado
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 295 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collison with your own tail.
    for segments in snake.segments:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
"""
# ################ How to Slice Lists & Tuples in Python ###################

# piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
# piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

# print(piano_keys[2:5])  # <----- ["c", "d", "e"]
# print(piano_keys[2:])  # <----- ["c", "d", "e", "f", "g"]
# print(piano_keys[:5])  # <----- ["a", "b", "c", "d", "e"]
# print(piano_keys[2:5:2])  # <----- ["c", "e"] # Exclui o segundo item"
# print(piano_keys[::2])  # <----- ["a", "c", "e", "g"]
# print(piano_keys[::-1])  # <----- ["g", "f", "e", "d", "c", "b", "a"]

# print(piano_tuple[2:5])  # <----- ("mi", "fa", "so")

# ################ Final Stage of the Exercise ###################

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jogo da Cobrinha")
screen.tracer(0)  # Desliga animação da tartaruga (movimentação)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")  # <----Inicial Maiuscula pois é uma tecla do teclado
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 295 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collison with your own tail.
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
