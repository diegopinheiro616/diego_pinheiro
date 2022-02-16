"""
Day 5

### For Loop ###

fruits = ['Apple', 'Peach', 'Pear']
for fruit in fruits:  # atribui uma variável para cada item na lista (vetor)
    print(fruit)     # Aí todos os membros da lista fruits ganham atributo variável(var)
    print(fruit + 'Pie')  # Loooooooop. Rola repetição para cada item da lista fruits
    print(fruits)
print(fruits)

# ################ Exercise 1 ####################
# Average Height - opção 1 (Sem 'len' e 'sum')

student_heights = input("Input a list of student heights ").split()  # <---divide uma string em uma lista
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# print(n)
total_alturas = 0
total_estudantes = n + 1
# print(total_estudantes)


for n in student_heights:
    # print(n)
    # print(type(n))
    total_alturas += int(0 + n)
    # print(total_alturas)
resultado = int(total_alturas / total_estudantes)
print(resultado)

# ################ Exercise 1 ####################
# Average Height - opção 2 (Sem 'len' e 'sum')

student_heights = input("Input a list of student heights ").split()  # <---divide uma string em uma lista
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(average_height

# ################ Exercise 1 ####################
# Average Height - opção 3 (Com 'len' e 'sum')

student_heights = input("Input a list of student heights ").split()  # <---divide uma string em uma lista
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# print(len(student_heights))  # Conta número de variáveis
# print(sum(student_heights))  # Soma o valor das variáveis

soma_alturas = sum(student_heights)
# print(type(soma_alturas))
numero_estudantes = len(student_heights)
# print(type(numero_estudantes))
media_altura = int(soma_alturas / numero_estudantes)

print(media_altura)

# ################ Exercise 2 ####################
# Highest Score

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)


# print(type(student_scores[n]))
highest_score = 0

for score in student_scores:
    # print(score)
    if score > highest_score:
        highest_score = score
print(f'The highest score in the class is: {highest_score}')

# ### FOR LOOP #####

fruits = ['Apple', 'Peach', 'Pear']
for fruit in fruits:
    print(fruit)
    print(fruit + 'Pie')

# ### FOR LOOP WITH RANGE function #####

# for number in range(a, b):
# print(number)

# for number in range(1, 11):
#   print(number)

for number in range(1, 11, 3):  # <-Pulando 3 números
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)

# ################ Exercise 3 ####################
# Adding Even Number - Opção 1

total = 0
for number in range(2, 101, 2):
    # print(number)
    total += number
    # print(total)
print(total)

# ################ Exercise 3 ####################
# Adding Even Number - Opção 2

alternative_sum = 0
for number in range(1, 101):
    if number % 2 == 0:
        # print(number)
        alternative_sum += number
print(alternative_sum)

# ################ Exercise 4 ####################
# FizzBuzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        number = 'FizzBuzz'
    elif number % 3 == 0:
        number = 'Fizz'
    elif number % 5 == 0:
        number = 'Buzz'
    print(number)

# ################ Exercise 5 ####################
# PyPassword Generator - Opção 1

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  # 52
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # 10
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']  # 9

new_letters = []
new_numbers = []
new_symbols = []

print("Welcome to the PyPassword Generator!")
nr_letters = int(input('How many letters would you like in your password?\n'))
nr_numbers = int(input(f'How many numbers would you like in your password?\n'))
nr_symbols = int(input(f'How many symbols would you like in your password?\n'))


for letter in range(0, nr_letters):  # <---Transformar números do input acima em lista valores random. 3 => [1, 10, 4]
    letter = random.randint(0, 51)
    letter = letters[letter]  # <---Transformar o número em um correspondente dentro da lista 'letters' ex. 0 = a
    # print(letter)
    new_letters.extend([letter])
# print(new_letters)

for number in range(0, nr_numbers):
    number = random.randint(0, 9)
    number = numbers[number]
    # print(number)
    new_numbers.extend([number])
# print(new_numbers)

for symbol in range(0, nr_symbols):
    symbol = random.randint(0, 8)
    symbol = symbols[symbol]
    # print(symbol)
    new_symbols.extend([symbol])
# print(new_symbols)

all = new_letters + new_numbers + new_symbols  # <---Une as três listas em uma.
# print(all)

all_random = []

for random_one in range(0, len(all)):  # <---Repete as etapas acima, mas limitando a lista de referencia a 'all'
    random_one = random.randint(0, len(all) - 1)
    random_one = all[random_one]
    # print(random_one)
    all_random.extend([random_one])
# print(all_random)
final_password = ''.join(all_random)
print(final_password)


# ################ Exercise 5 ####################
# PyPassword Generator - Opção 2

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

"""

# ################ Exercise 5 ####################
# PyPassword Generator - Opção 3

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))
  print(password_list)

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")

