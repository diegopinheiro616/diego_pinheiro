"""
Object Oriented Programming (OOP)
"""

# ################ Constructing Objects ####################
"""
import another_module

print(another_module.another_variable)

import turtle

timmy = turtle.Turtle()  # <---- Class Turtle

from turtle import Turtle

timmy = Turtle()
print(timmy)
"""
# ################ Object Attributes ####################
"""
# car.speed 'car' = object 'speed' = attribute

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)

my_screen = Screen()
print(my_screen.canvheight)
"""
# ################ Object Methods ####################
"""
# car.stop() # 'car' = object, 'stop()' = method
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
"""
# ################ Add library ####################

# IMPORTAR BIBLIOTECA = Settings > "Projeto" > Python Interpreter > + > "Escolher biblioteca" > Instalar.
"""
from prettytable import PrettyTable

table = PrettyTable()  # Class(Blueprint)
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander", "Bulbasaur"])  # Methods
table.add_column("Type", ["Eletric", "Water", "Fire", "Grass/Poison"])  # Methods
table.align = "l"  # Attributes

print(table)
"""
# ################ Quiz ####################
"""
Question 1:
In OOP what is the name of the blueprint for creating objects?
Answer: Class

Question 2:
Given a Class blueprint for a Car has the following attributes and methods,
which line of code in the answers will produce an error?
Attributes:

num_of_seats

speed

Methods:

drive()

brake()

a) car.drive() OK!
b) car.num_of_seats = 2 OK!
c) car.brake = 0 <----- WRONG! RESPOSTA
d) print(car.speed) OK!

Question 3:
    my_toyota = Car()
    my_fiat = Car()
What word would you use to describe what's inside my_toyota and my_fiat?
a) Class: This is a blueprint used to create objects. <----- WRONG!
b) Attribute: This is a variable associated with an object. <----- WRONG!
c) Variable: Although my_toyota and my_fiat are variables, they each contain a Car object. <----- WRONG!
d) Object: Correct! my_toyota and my_fiat are variables and each contains a Car object. OK!
e) Method: This is a function associated with an object. <----- WRONG!
"""
# ################ Exercise 1 ####################
# Coffee Machine in OOP

# Program Requirements
# 1. Print report
# 2. Check resources sufficient?
# 3. Process coins
# 4. Check transation successful?
# 5. Make Coffee

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maquina_dinheiro = MoneyMachine()  # <---- Blueprint da maquina de dinheiro
maquina_cafe = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f'What would you like? ({options}): ')
    if choice == "off":
        is_on = False
    elif choice == 'report':
        maquina_dinheiro.report()
        maquina_cafe.report()
    else:
        drink = menu.find_drink(choice)
        if maquina_cafe.is_resource_sufficient(drink) and maquina_dinheiro.make_payment(drink.cost):
            maquina_cafe.make_coffee(drink)






