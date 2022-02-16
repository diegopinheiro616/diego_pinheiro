"""
Day 13 - Debbugging
"""
# ##########DEBUGGING#####################

# ################ Exercise 1 ####################
# Describe Problem
"""
def my_function():
    for i in range(1, 21):  # <---- raio entre 1 e 21. Incluindo o 1 e excluindo o 21. Logo, 20 números, não 21.
        # print(i)
        # print(type(i))
        if i == 20:
            print("You got it")
my_function()
"""
# ################ Exercise 2 ####################
# Reproduce the Bug
"""
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])
# print(dice_num)
"""
# ################ Exercise 3 ####################
# Play Computer
"""
year = int(input("What's your year of birth? "))
if year >= 1980 and year <= 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")
else:
    print("You are a mummy.")
"""
# ################ Exercise 4 ####################
# Fix the Errors
"""
age = int(input("How old are you? "))
if age >= 18:
    print(f"You can drive at age {age}.")
"""
# ################ Exercise 5 ####################
# Print is Your Friend
"""
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# print(pages)
# print(type(pages))
word_per_page = int(input("Number of words per page: "))
# print(type(word_per_page))
# print(word_per_page)
total_words = pages * word_per_page
print(total_words)
"""
# ################ Exercise 6 ####################
# Use a Debugger
"""
# Pythontutor == BIG GUN!!!!
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)
mutate([1,2,3,5,8,13])
"""
# ################ Exercise 7 ####################
"""
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
"""
# ################ Exercise 8 ####################
"""
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
"""
# ################ Exercise 9 ####################
"""
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print([number])
"""
