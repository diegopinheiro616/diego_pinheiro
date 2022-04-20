"""
Day 8 - Functions with Inputs
"""
"""
# review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print('Hellllo')
    print('I want a burger! A simple one.')
    print('Ok little fella. Do you wanna a coke too?')

greet()
"""
# Function that allow for input
"""

def greet_with_name(name):
    print(f'Hello {name}.')
    print(f'How do you do {name}?')

greet_with_name("Billie")


Parameter -----> Name = Billie <----- Argument
"""
# Function with more than 1 input
"""
def greet_name_location(name, location):
    print(f'Client: {name}.')
    print(f'Address: {location}.')

greet_name_location('Diego', 'Mooca')
"""
# Function with keword arguments
"""
def greet_with(a, b, c):
    print(f'Client: {a}.')
    print(f'Address: {b}.')
    print(f'Age: {c}.')
a = 'Diego'
b = 'Mooca'
c = '32 years old'
greet_with(a, b, c)

# or
def greet_with(a, b, c):
    print(f'Client: {a}.')
    print(f'Address: {b}.')
    print(f'Age: {c}.')
# or
greet_with(b='mooca', c='32 years old', a='Diego')
"""

# ################ Exercise 1 ####################
# Paint Area Calculator - Opção 1
"""
import math
def paint_calc(height, width, cover):
    cans = math.ceil(((test_h * test_w) / cover))
    print(f"You'll need {cans} cans of paint.")

# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
"""
# ################ Exercise 1 ####################
# Paint Area Calculator - Opção 2
"""
import math
def paint_calc(height, width, cover):
    cans = (height * width) / cover
    cans_1 = math.ceil(cans)
    print(f"You'll need {cans_1} cans of paint.")

# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
height = int(input("Height of wall: "))
width = int(input("Width of wall: "))
cover = 5
paint_calc(height, width, cover)
"""
# ################ Exercise 2 ####################
# Prime Number Checker - Opção 1
"""
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
n = int(input("Check this number: "))
prime_checker(number=n)
"""
# ################ Exercise 3 ####################
# Caesar Cipher - Opção 1

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")



CÓDIGO MORTO
"""

def cesar(plain_text, shift_amount):
    plain_text = list(plain_text)  # <---- transforma string em lista: dog == ['D', 'o', 'g']
    
    if direction == 'encode':
        for letter in range(len(plain_text)):
            # print(alphabet.index(plain_text[letter]))  # <---- Localiza a posição de uma str em uma list: [3, 14, 6]
            plain_text[letter] = alphabet[alphabet.index(plain_text[letter]) + shift_amount]  # <---- shift 3 == ['g', 'r', 'j']
            # print(text_list)
            new_text = (''.join(plain_text))  # <---- lista para string: ['g', 'r', 'j'] == grj


    elif direction == 'decode':
        for letter in range(len(plain_text)):
            # print(alphabet.index(plain_text[letter]))  # <---- Localiza a posição de uma str em uma list: [6, 17, 9]
            plain_text[letter] = alphabet[alphabet.index(plain_text[letter]) - shift_amount]  # <---- shift 3 == ['d', 'o', 'g']
            # print(text_list)
            new_text = (''.join(plain_text))  # <---- lista para string: ['d', 'o', 'g'] == dog
    print(f'The encoded text is {new_text}.')

cesar(plain_text = text, shift_amount = shift)

"""


