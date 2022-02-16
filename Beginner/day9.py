"""
Day 9 - Dictionaries and Nesting
"""
# ################ Dictionary ####################
"""
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    }

# Retrieving items from dictionary.
print(programming_dictionary["Bug"])

# Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Creating a new dictionary.
emply_dictionary = {}

# Wipe an existing dictionary.
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in dictionary.
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary["Bug"])

# Loop through a dictionary.
for key in programming_dictionary:
    print(key)  # <--- Print Key list
    print(programming_dictionary[key])  # <--- Print Value of the Key List
"""
# ################ Exercise 1 ####################
# Grading Program
"""
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
    }

student_grades = {}

for student in student_scores:  # <---- chama cada 'key' na biblioteca 'student_scores' de student.
    score = student_scores[student]  # <---- cria uma atribuição de ponte usando as informações da biblioteca.
    if score > 90:
        student_grades[student] = "Outstanding"  # <---- copia as key de uma biblioteca para outra. E substitui seu
    elif score > 80:                             # 'value' pela da condição ao lado.
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
"""
# ################ Nesting ####################
"""
# Nesting
capitals = {
    'France': 'Paris',
    'Germany': 'Berlin',
}

# Nesting a List in a Dictionary
travel_log = {
    'France': ['Paris', 'Lille', 'Dijon'],
    'Germany': ['Berlin', 'Hamburg', 'Stuttgart']
}

# Nesting a dictionary in a Dictionary
travel_log = {
    'France': {'cities_visited': ['Paris', 'Lille', 'Dijon'], 'total_visits': 12},
    'Germany': {'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'], 'total_visits': 7},
}

# Nesting a dictionary in a List
travel_log = [
    {
        'Country': 'France',
        'cities_visited': ['Paris', 'Lille', 'Dijon'],
        'total_visits': 12
    },
    {
        'Country': 'Germany',
     'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'],
      'total_visits': 7
      },
]
"""
# ################ Exercise 2 ####################
# Dictionary in List
"""
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(name, number_of_visits, name_of_cities):
    new_country = {}  # <---- adiciona novo dicionário a lista
    new_country["country"] = name  # <---- dentro do dicionário estabelece a key country e qual sera seu value
    new_country["visits"] = number_of_visits
    new_country["cities"] = name_of_cities
    travel_log.append(new_country)  # <---- utiliza comando de adição de item a lista

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
"""
# ################ QUIZ ####################
"""
Question 1:
Which line of code will change the starting_dictionary to the final_dictionary?

starting_dictionary = {
    "a": 9,
    "b": 8,
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

Right answer:
starting_dictionary["c"] = 7  # <---- adiciona no key e value ao dicionário
final_dictionary = starting_dictionary

Question 2:
Which line of code will produce an error?

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

a) dict["c"] = [1, 2, 3]  # <---- vai redefinir o value de uma key (NÃO vai dar erro)
b) for key in dict:
     dict[key] += 1  # <--- vai redefinir o value de toda as chaves (NÃO vai dar erro)
c) dict[1] = 4  # <---- como não há key '1' no dic., vai adicionar nova key. Uma quarta, nesse caso (NÃO vai dar erro)
d) print(dict[1])  # <---- vai dar erro, pois não há key 1 no dicionario.

Question 3:
Which line of code will print "Steak"?

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

a) print(order["main"][2][0])  # <---- vai print = Steak   Resposta CERTA
b) print(order["main"][2])  # <---- vai print = ['Steal']  Resposta ERRADA

"""
# ################ Exercise 3 ####################
# The Secret Auction Program - opção Dr.
"""
from day9_1 import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
"""
# ################ Exercise 3 ####################
# The Secret Auction Program - opção Eu
"""
from day9_1 import logo


def nome_valor():
    nome = input('What\'s your name?: ')
    valor = int(input('What\'s your bid?: $'))
    apostadores[nome] = valor

def selecionar_vencedor(registro_apostadores):  # <---- Essa merda é um nome inventado que equivale ao apostadores.
    maior_aposta = 0
    vencedor = ""
    for apostas in registro_apostadores:  # apostadores == registro_apostadores / apostas tb é um termo inventado.
        ultima_aposta = registro_apostadores[apostas]
        if ultima_aposta > maior_aposta:
            maior_aposta = ultima_aposta
            vencedor = apostas
    print(f'The winner is {vencedor} with a bid of ${maior_aposta}.')

print(logo)
print('Welcome to the secret auction program.')

apostadores = {}
final_apostadores = False

while final_apostadores == False:
    nome_valor()
    comecar_aposta = input("Are there any other bidders? Type 'yes' or 'no'.")
    if comecar_aposta == 'no':
        final_apostadores = True
selecionar_vencedor(apostadores)
"""