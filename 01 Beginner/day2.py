"""
Day 2


print('Hello'[4])
print(123 + 45)
print('123' + '45')

#Integer (números inteiros)
#Float (números reais)
#Boolean (True or False)

num_char = str(len(input('What is your name? ')))
print('Your name has ' + num_char + ' characters.')

a = float(123)
print(type(a))

nome = input('Qual o seu nome? ')
idade = input('Você é a mãe do Diego? ')
print(f'{nome}, você é a melhor mãe do mundo! =]')

Ordem operações:
1°) ()   2°) **(ex. 3³) 3°) * e / 4°) + e -

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)

print(round(8 / 3, 2))
print(8 // 3)

result = 24 / 2
result /= 2
print(result)

score = 6
score -= 1
score -= 1
print(score)  # 4
score += 2
score += 2
print(score)  # 8

score = 0
height = 1.8
isWinning = True
#f-String
print(f'Your score is {score}, your height is {height}, you are winning is {isWinning}.')

a = int('5') / int(2.7)

print("Agora" + a)
print(f'Agora {a}')
"""

# Tip Calculator
print('Welcome to the tip calculator.')
conta = float(input('What was the total bill? $ '))
gorjeta = float(input('What percentage tip would you like to give? 10%, 12%, or 15%? '))
pessoas = float(input('How many people to split the bill? '))
conta_por_pessoa = (conta * ((100 + gorjeta) / 100)) / pessoas
print(f'Each person should pay ${(conta_por_pessoa):.2f}.')
print(f'Each person should pay ${(round(conta_por_pessoa, 2))}.')
