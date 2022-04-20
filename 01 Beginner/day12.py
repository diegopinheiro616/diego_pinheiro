"""
Day 12 - Namespaces: Local vs, Global Scope
"""
# ########### Local Scope #############
"""
enemies = 1

def increase_enemies():
    enemies = 2
    print(f'enemies inside function: {enemies}')

increase_enemies()
print(f'enemies outside function: {enemies}')

# Result: inside 2, outside 1

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength) <---- Dá erro!
"""
# ########### Global Scope #############
"""
player_health = 10 

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)
        drink_potion()
"""
# ########### Does Python have Block Scope? #############
"""
# There is no Block Scope

game_level = 3
def create_enemy():
    enemies = ['skeleton', 'zombie', 'alien']
    if game_level < 5:
        new_enemy = enemies[0]
        print(new_enemy)
"""
# ########### How to Modify Variables with Global Scope #############
"""
# Modifying Global Scope
# Ideia 1
enemies = 1

def increase_enemies():
    global enemies  # <----- Bom evitar
    enemies += 1
    print(f'enemies inside function: {enemies}.')

increase_enemies()
print(f'enemies outside function: {enemies}.')

# Ideia 2
enemies = 1

def increase_enemies():
    print(f'enemies inside function: {enemies}.')
    return enemies + 1  # <---- Dessa maneira fica mais fácil.

enemies = increase_enemies()
print(f'enemies outside function: {enemies}.')
"""
# ########### Python Constants & Global Scope #############
"""
# Global Constants
PI = 3.14159  # <---- Bom utilizar quando vc jogar ela uma vez e nunca mais modifica-la. Variável 'fixa'.
URL = 'https://www.google.com'  # <---- DICA: coloque em letra MAIÚSCULA para diferenciá-la de outras variáveis.
TWITTER_HANDLE = '@yu_angela'
"""
# ########### Quiz #############
"""
Question 1:
What will be printed in the console when the following code is run?
DO NOT run the code, just pretend to be a computer:

def a_function(a_parameter):
    a_variable = 15
    return a_parameter
a_function(10)
print(a_variable)

Answer: NameError

Question 2:
What will be printed in the console when the code is run?
DO NOT run the code, just pretend to be a computer.
i = 50
def foo():
    i = 100
    return i
foo()
print(i)

Answer: 50

Question 3:
What will be printed in the console when the following code is run?
DO NOT run the code, just pretend to be a computer.
def bar():
    my_variable = 9
    if 16 > 9:
      my_variable = 16 
    print(my_variable)
bar()
"""
# ################ Exercise 1 ####################
# Number Guessing Game - Dr. Angela Yu
"""
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}")

  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")

game()
"""
# ################ Exercise 1 ####################
# Number Guessing Game - Eu

from random import randint

def comecar_jogo():
    jogar = True
    while jogar:
        print('Bem vindo ao Number Guessing Game!\nEstou pensando em um número entre 1 e 100.')
        dificuldade = input('Escolha a dificuldade. Digite \'easy\' ou \'hard\': ')
        if dificuldade == 'easy':
            jogar = False
            print(f'Você tem 10 tentativas sobrando para advinhar o número.')
            return 10
        elif dificuldade == 'hard':
            jogar = False
            print(f'Você tem 5 tentativas sobrando para advinhar o número.')
            return 5
        else:
            dificuldade = input('Input errado. Escolha a dificuldade. Digite \'easy\' ou \'hard\': ')

def teste_numero():
    fim_do_teste = False
    vidas = comecar_jogo()
    numero_sorteado = randint(1, 100)
    numero_chutado = int(input('Fale um número: '))
    while not fim_do_teste:
        if numero_chutado == numero_sorteado:
            print('Você acertou o número. Parabéns.')
            fim_do_teste = True
            return True
        elif numero_chutado > numero_sorteado:
            vidas -= 1
            numero_chutado = int(input(f'Muito alto.\nVocê ainda tem {vidas} chances.\nEscolha outro número: '))
        elif numero_chutado < numero_sorteado:
            vidas -= 1
            numero_chutado = int(input(f'Muito baixo.\nVocê ainda tem {vidas} chances.\nEscolha outro número: '))
        if vidas == 1:
            print('Você errou o número.\nGame Over.')
            fim_do_teste = True
            return True

def jogar_jogo():
    while not teste_numero() == True:
        teste_numero()

while input('Você gostaria de jogar Guessing Game? \'Sim\' ou \'Não\'? ').lower() == 'sim':
    jogar_jogo() 





