"""
Day 24 - Files, Directories and Paths
"""
# ################ How to open, Read and Write to Files using the  "with" Keyword ###################
"""
# with open("y_files.txt") as file:  # <---- by default open("my_files.txt", mode="r") (r)ead
#    contents = file.read()
#    print(contents)

# with open("my_files.txt", mode="w") as file:  # <---- (w)rite       Substitui to_do o texto do arquivo
#    file.write("New text. =O")

# with open("my_files.txt", mode="a") as file:  # <---- (a)ppend        Adiciona texto ao arquivo
#    file.write("\n My name is Ramza")

with open("todinho.txt", mode="w") as file:  # <---- Se não tiver um arquivo com esse nome, o software cria
    file.write("\n My name is Ramza")
"""
# ################ Understanding Relatives and Absolute File Paths ###################
"""
# with open("/Users/Usuario/Desktop/data.txt") as file:  # <---- Absolute Path
# with open("../../../../Desktop/data.txt") as file:  # <---- Relative Path
    contents = file.read()
    print(contents)
"""
# ################ Quiz ###################
"""
Question 1:
If you are writing code inside the main.py file to open the quiz.txt what would be the relative file path?
Answer: "quiz.txt" <---- Although you can also write this as "./quiz.txt", the "./" is optional.

Question 2:
When writing Python code, what is the absolute path to get to quiz.txt?
On a Mac, Macintosh HD is the root, on a PC it is usually the C:/ drive. So it might look like this:
Answer: open("/Users/my_project/quiz.txt") <---- O "Drive C" ou "MacintoshHD" são o Root e podem ser ocultados.

Question 3:
If you are writing code inside main.py, what is the relative file path to open quiz.txt?
Answer: open("../my_files/quiz_files/quiz.txt") <---- This is the right answer. The .. 
                                                      goes up one folder into all_files then down to my_files/etc...
"""
# ################ Jogo da Cobrinha 2.0 ###################

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()

