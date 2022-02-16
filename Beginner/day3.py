'''
Day 3

water_level = 50
if water_level > 80:
    print('Drain water')
else:
    print('Continue')

    print('Welcome to the rollercoaster!')
height = int(input('What is your height in cm? '))

if height >= 120:
    print('You can ride the rollercoaster!')
else:
    print('Sorry, you have to grow taller before you can ride.')

Operator    Meaning
   >        Greater than
   <        Less than
   >=       Greater than or equal to
   <=       Less than or equal to
   ==       Equal to
   !=       Not equal to

print('Welcome to the rollercoaster!')
height = int(input('What is your height in cm? '))

if height != 120:
    print('You can ride the rollercoaster!')
else:
    print('Sorry, you have to grow taller before you can ride.')

print(40 % 3) <- % Module

print(40 % 3)

# Nested if / else

if condition:
    if another condition:
    else:
        do this
else: do this



print('Welcome to the rollercoaster!')
height = int(input('What is your height in cm? '))

if height >= 120:
    print('You can ride the rollercoaster!')
    age = int(input('What is your age? '))
    if age <= 18:
        print('Please pay $7.')
    else:
        print('Please pay $12.')
else:
    print('Sorry, you have to grow taller before you can ride.')

print('Welcome to the rollercoaster!')
height = int(input('What is your height in cm? '))

if height >= 120:
    print('You can ride the rollercoaster!')
    age = int(input('What is your age? '))
    if age <= 12:
        print('Please pay $5.')
    elif age <= 18:   # <--- Else if
        print('Please pay $7.')
    else:
        print('Please pay $12.')
else:
    print('Sorry, you have to grow taller before you can ride.')


# ################ Exercise 1 ####################
# Calculadora Índice de Massa Corpórea

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2) # <- Int

if bmi < 18.5:
    print(f'Your BMI is {bmi}, you are underweight.')
elif bmi < 25:
    print(f'Your BMI is {bmi}, you have a normal weight.')
elif bmi < 30:
    print(f'Your BMI is {bmi}, you are slightly overweight.')
elif bmi < 35:
    print(f'Your BMI is {bmi}, you are obese.')
else:
    print(f'Your BMI is {bmi}, you are clinically obese.')

# ################ Exercise 2 ####################
# Calculadora Ano bissexto

year = int(input("Which year do you want to check? "))

ver_1 = float(year % 4)
ver_2 = float(year % 100)
ver_3 = float(year % 400)


if ver_1 == 0:

      if ver_2 == 0:
        if ver_3 == 0:
            print('Leap year.')
        else:
            print('Not leap year.')
      else:
        print('Leap year.')

else:
    print('Not leap year.')

# print(f'[{ver_1}], [{ver_2}] e [{ver_3}].')

# ############# Montanha Russa com adicional foto ###############

print('Welcome to the rollercoaster!')
height = int(input('What is your height (cm)? '))
bill = 0

if height >= 120:
    print('You can ride the rollercoaster!')
    age = int(input('What is your age? '))
    if age < 12:
        bill = 5
        print('Child tickets is $5.')
    elif age <= 18:
        bill = 7
        print('Youth tickets are $7.')
    else:
        bill = 12
        print('Adult tickets is $12')

    wants_photo = input('Photo? yes or no. ')
    if wants_photo == 'yes':
        bill += 3
        print(f'Your final bill is {bill}.')
    else:
        print(f'Your final bill is {bill}.')

else:
    print('Sorry, you have to grow taller before you can ride')


# ################ Exercise 3 ####################
# Python Pizza - Opção 1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == 'S':
    bill += 15
    if add_pepperoni == 'Y':
        bill += 2
elif size == 'M':
    bill += 20
    if add_pepperoni == 'Y':
        bill += 3
elif size == 'L':
    bill += 25
    if add_pepperoni == 'Y':
        bill += 3
if extra_cheese == 'Y':
    bill += 1

print(f'Your final bill is: ${bill}.')

# ################ Exercise 3 ####################
# Python Pizza Opção 2

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == 'S':
    bill = 15
elif size == 'M':
    bill += 20
else:
    bill += 25

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'Y':
    bill += 1

print(f'Your final bill is: ${bill}.')

# ############# Montanha Russa de graça para idosos entre 45 e 55 ###############

print('Welcome to the rollercoaster!')
height = int(input('What is your height (cm)? '))
bill = 0

if height >= 120:
    print('You can ride the rollercoaster!')
    age = int(input('What is your age? '))

    if age < 12:
        bill = 5
        print('Child tickets is $5.')
    elif age <= 18:
        bill = 7
        print('Youth tickets are $7.')
    elif age >= 45 and age <= 55:
        print('Old man, have a free ride!')
    else:
        bill = 12
        print('Adult tickets is $12')

    wants_photo = input('Photo? yes or no. ')
    if wants_photo == 'yes':
        bill += 3
        print(f'Your final bill is {bill}.')
    else:
        print(f'Your final bill is {bill}.')

else:
    print('Sorry, you have to grow taller before you can ride')

    # ################ Exercise 4 ####################
# Calculadora do Amor

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_low = str.lower(name1)
# print(name1_low)
name2_low = str.lower(name2)
# print(name2_low)
both_names = (f'{name1_low} {name2_low}')
# print(both_names)

t = both_names.count('t')
# print(f'T = {t}')
r = both_names.count('r')
# print(f'R = {r}')
u = both_names.count('u')
# print(f'U = {u}')
e = both_names.count('e')
# print(f'E = {e}')

l = both_names.count('l')
# print(f'L = {l}')
o = both_names.count('o')
# print(f'O = {o}')
v = both_names.count('v')
# print(f'V = {v}')

fist_number = t + r + u + e
# print(fist_number)
second_number = l + o + v + e
# print(second_number)

love = int(f'{fist_number}{second_number}')
# print(love)

if (love <= 10) or (love >= 90):
    print(f'Your score is {love}, you go together like coke and mentos.')
elif love >= 40 and love <= 50:
    print(f'Your score is {love}, you are alright together.')
else:
    print(f'Your score is {love}.')

'''

    # ################ Exercise 5 ####################
# Treasure Island
print('Welcome to Treasure Island.\nYour mission is to find the treasure.')
decisao_1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right': ")
if decisao_1 == 'right':
    decisao_2 = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ')
    if decisao_2 == 'wait':
        decisao_3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ')
        if decisao_3 == 'yellow':
            print('You win!')
        elif decisao_3 == 'red':
            print('Burned by fire. Game Over.')
        elif decisao_3 == 'blue':
            print('Burned by fire. Game Over.')
        else:
            print('Game over.')
    else:
        print('Attacked by trout. Game Over.')

else:
    print('You fall into a hole. Game Over.')

