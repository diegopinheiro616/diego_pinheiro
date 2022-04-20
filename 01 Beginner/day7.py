"""
Day 7 - Project Hangman

"""
# ################ Step 1 ####################
# Picking a random words and checking answers
"""
word_list = ['avocado', 'dinossaur', 'state']

import random

chosen_word = random.choice(word_list)

guess = input('Guess a letter: ').lower

for letter in chosen_word:
    if letter == guess:
        print('right')
    else:
        print('wrong')
"""
# ################ Step 2 ####################
# Replacing Blanks with Guesses
"""
word_list = ['avocado', 'dinossaur', 'state']

import random

chosen_word = random.choice(word_list)
print(chosen_word)

word_length = len(chosen_word)
display = []
for _ in range(word_length):
    display += '_'
print(display)

guess = input('Guess a letter: ').lower()

for position in range(word_length):
    letter = chosen_word[position]

    if letter == str(guess):
        display[position] = letter

print(display)

"""
# ################ Step 3 ####################
# Checking if the Player has Won
"""
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(display)

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the
# letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

end_of_game = False

while not end_of_game:
    guess = input('Guess a letter: ').lower()
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        # print(f"Current position: {position}\nCurrent letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_of_game = True
        print('You win')
"""

# ################ Step 4 ####################
# Checking if the Player has Won
"""
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.

lives = 6

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter


    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1.
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose.')

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

    print(stages[lives])

"""


# ################ Step 5 ####################
# Improving the User Experience
"""

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
"""

# ################ Step 5 ####################
# How to Add ASCII and Improve the UI
"""
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

import random
from day7_1 import pokemon
chosen_word = random.choice(pokemon)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

from day7_1 import logo

print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f'You have already guessed {guess}.')
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from day7_1 import stages
    print(stages[lives])
    
"""

# ################ Exercise 1 ####################
"""
# Hangman
import random

tentativas = 6
hookman_letters = ''
word_list = ['ardvark', 'baboon', 'camel']
chosen_word_list = []
hookman_letters_list = []
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen

chosen_word = random.choice(word_list)
# str(print(chosen_word))
for letters in chosen_word:
    hookman_letters += '_'
print(hookman_letters)
chosen_word_list = list(chosen_word)
hookman_letters_list = list(hookman_letters)
print(chosen_word_list)
print(hookman_letters_list)

while not hookman_letters_list == chosen_word_list and tentativas >= 1:
    tentativas = tentativas - 1
    guess = str.lower(input('Guess a letter: '))
    # print(guess)
    print(tentativas)
    for letra in range(0, len(chosen_word_list)):
        if guess == chosen_word_list[letra]:
                hookman_letters_list[letra] = guess
        # print(hookman_letters_list)
        # print(''.join(hookman_letters_list))
    print(''.join(hookman_letters_list))
if hookman_letters_list == chosen_word_list:
    print('You did it! 0/\nHookman is safe!\nCongratulations!\n=)')
elif tentativas == int(0):
    print('Oh no!\nHookman is dead!\n=(')



"""

# ################ Exercise 2 ####################


import random
import day7_1
from day7_1 import stages
import os
cls = lambda: os.system('cls')

print(day7_1.logo)

lives = 6

chosen_word_list = []
hookman_letters = ''
hookman_letters_list = []

desafio = str.lower(input('### Pokemon Hangman ###\nEi, treinador! Você manja o nome de todos os primeiros'
                          ' 251 pokemons?\nHora de testar todo o seu conhecimento.\nGostaria de jogar no nível fácil '
                          'ou difícil? '))

if desafio == 'fácil' or desafio == 'facil':
    desafio = 1
elif desafio == 'difícil' or desafio == 'dificil':
    desafio = 2
else:
    desafio = 0

while desafio == 0:
    desafio = str.lower(input('Não entendi. Poderia repetir qual nível de dificuldade gostaria de jogar. '
                        'Fácil ou difícil? '))
    if desafio == 'fácil' or desafio == 'facil':
        desafio = 1
    elif desafio == 'difícil' or desafio == 'dificil':
        desafio = 2
    else:
        desafio = 0

# print(desafio)
chosen_word = str.lower(random.choice(day7_1.pokemon))
# print(chosen_word)
# print(len(chosen_word))
if desafio == 2:
    while len(chosen_word) <= 5:
        chosen_word = str.lower(random.choice(day7_1.pokemon))
        # print(chosen_word)
        # print(len(chosen_word))

elif desafio == 1:
    while len(chosen_word) > 5:
        chosen_word = str.lower(random.choice(day7_1.pokemon))
        # print(chosen_word)
        # print(len(chosen_word))
# print(chosen_word)
# print(len(chosen_word))
for letters in chosen_word:
    hookman_letters += '_'
# print(hookman_letters)
chosen_word_list = list(chosen_word)
hookman_letters_list = list(hookman_letters)
# print(chosen_word_list)
# print(hookman_letters_list)

end_of_game = False

while not end_of_game:
    print(stages[lives])
    print(''.join(hookman_letters_list))
    # print(lives)
    guess = input('Guess a letter: ').lower()
    # cls() <---- Descobrir como fazer o clear funcionar
    # print(guess)
    # print(tentativas)

    if guess not in chosen_word:
        print(''.join(hookman_letters_list))
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(stages[lives])
            print('\n#####################################################################')
            print(f'The answer is {chosen_word}.\nI knew it! You are a fraud!\n=(')

    for letra in range(0, len(chosen_word_list)):
        if guess == chosen_word_list[letra]:
            hookman_letters_list[letra] = guess
            if hookman_letters_list == chosen_word_list:
                end_of_game = True
                print('\n#####################################################################')
                print(f'The answer is {chosen_word}.\nYou really are a pokemon master!\nCongratulations!\n=)')

