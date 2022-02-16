"""
Day 4 - Radomisation and Python lists
Mersenne Twister

$$$$$$$$$$$$$$$ Tipos Random $$$$$$$$$$$$$$$
https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

$$$$$$$$$$$$$$$ Tipos Lista $$$$$$$$$$$$$$$
https://docs.python.org/3/tutorial/datastructures.html

import random
import day4_1 # <--- informação vinda de outro arquivo. Necessita importar.

random_integer = random.randint(1, 10)
print(random_integer)
print(day4_1.pi)

import random
import day4_1

random_float = random.random()
print(random_float * 5)

love_score = random.randint(1, 100)
print(f'Your love score is {love_score}')

# ################ Exercise 1 ####################
# Cara ou Coroa - Opção 1

import random

a = ['Heads', 'Tails']
for i in range(1):
    print(random.choice(a))

# ################ Exercise 1 ####################
# Cara ou Coroa - Opção 2

cara_ou_coroa = random.randint(0, 1)
if cara_ou_coroa == 1:
    print('Heads')
else:
    print('Tails')

# Lists

#                         0             1           2
states_of_america = ['Delaware', 'Pennsylvania', 'Texas']
print(states_of_america[0])
print(states_of_america [-1]) # <- Começa do final e vai ordem reversa.

states_of_america[1] = 'Alalalala' # <- Substitui o item
print(states_of_america)

states_of_america.extend(['Angelgard', 'Crazyland']) # <- Adiciona itens a lista
print(states_of_america)

# Existe vários tipos de lista no Python. Acessar link acima para ver outros tipos.

# ################ Exercise 2 ####################
# Banker Roulette

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#print(names)
#print(len(names))  # Identifica quantos items há dentro do vetor 'names'
segunda_entrada = len(names) - 1
#print(segunda_entrada)

azarado = random.randint(0, segunda_entrada)
print(f'{names[azarado]} is going to buy the meal today!')

# dirty_dozen = ['Strawberries', 'Spinach', 'Kale', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears', 'Tomatoes', 'Celery', 'Potatoes']

fruits = ['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears']
vegetables = ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# ################ Exercise 3 ####################
# Treasure Map - Opção 1

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

if position == '11':
    row1[0] = "X"
elif position == '21':
    row1[1] = "X"
elif position == '31':
    row1[2] = "X"
elif position == '12':
    row2[0] = "X"
elif position == '22':
    row2[1] = "X"
elif position == '32':
    row2[2] = "X"
elif position == '13':
    row3[0] = "X"
elif position == '23':
    row3[1] = "X"
elif position == '33':
    row3[2] = "X"

print(f"{row1}\n{row2}\n{row3}")

# ################ Exercise 3 ####################
# Treasure Map - opção 2

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

#  23
horizontal = int(position[0])  #2
vertical = int(position[1])  #3

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")


# ################ QUIZ ####################

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])

print(dirty_dozen)
# Then print out:

print(dirty_dozen[0])
print(dirty_dozen[1])
# To see what happens at the next stage print out:

print(dirty_dozen[1][2])
print(dirty_dozen[1][3])

# ################ Exercise 4 ####################
# Rock, Paper and Scissors - Opção 1

import random

player_choice = input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ')
# print(type(player_choice))

computer_choice = str(random.randint(0, 2))

if computer_choice == '0':
    computer_choise1 = 'Rock'
elif computer_choice == '1':
    computer_choise1 = 'Paper'
else:
    computer_choise1 = 'Scissors'
# print(player_choice)


print(f'Computer\'s choice: {computer_choise1}.')

fight = [player_choice + computer_choice]
# print(fight)

'''
Rock(0) < Paper(1) < Sc2issor(2) < Rock(0)
'''

if fight[0] == '01':  # pedra x papel
    print('Computer wins!')
elif fight[0] == '02':  # pedra x tesoura
    print('Player wins!')
elif fight[0] == '00':  # perdra x pedra
    print('Draw!')
elif fight[0] == '11':
    print('Draw!')
elif fight[0] == '12':  # papel x tesoura
    print('Computer wins!')
elif fight[0] == '10': # papel x pedra
    print('Player wins!')
elif fight[0] == '21':  # tesoura x papel
    print('Player wins!')
elif fight[0] == '22':
    print('Draw!')
elif fight[0] == '20':  # tesoura x pedra
    print('Computer wins!')

"""

# ################ Exercise 4 ####################
# Rock, Paper and Scissors - Opção 2

import random

game_images = ['Rock', 'Paper', 'Scissors']

player_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. '))
# print(type(player_choice))
if player_choice >= 3 or player_choice <= -1:
    print('You typed an invalid number, you lose!')
else:
    print(game_images[player_choice])

    computer_choice = random.randint(0, 2)
    print(game_images[computer_choice])

    if computer_choice == player_choice:
        print('Draw!')
    elif player_choice == 0 and computer_choice == 2:
        print('You win!')
    elif computer_choice == 0 and player_choice == 2:
        print('You lose!')
    elif computer_choice > player_choice:
        print('You lose!')
    elif computer_choice < player_choice:
        print('You win!')





