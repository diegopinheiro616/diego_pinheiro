""" Day 30 - Errors, Exceptions and JSON Data:  Improving the Password """
# ######### Cathing Exceptions: The try catch except finally Pattern ##########
"""
# FileNotFound

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["dhuahduah"])
except FileNotFoundError:  # <---- Ele pega "Exceções"
    file = open("a_file.txt", "w")  # <---- Se não achar o arquivo, ela cria.
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message } does not exist.")
else:  # <---- Se der certo o "try" rola o else
    content = file.read()
    print(content)
finally:  # <---- rola independente de dar certo ou não o try, except e else
    file.close()
    print("File was closed.")

"""
# ######### Raising your own Exceptions ##########
"""
# FileNotFound

# try:
#    file = open("a_file.txt")
#    a_dictionary = {"key": "value"}
#    print(a_dictionary["dhuahduah"])
# except FileNotFoundError:  # <---- Ele pega "Exceções"
#    file = open("a_file.txt", "w")  # <---- Se não achar o arquivo, ela cria.
#    file.write("Something")
# except KeyError as error_message:
#    print(f"The key {error_message } does not exist.")
# else:  # <---- Se der certo o "try" rola o else
#    content = file.read()
#    print(content)
# finally:  # <---- rola independente de dar certo ou não o try, except e else
#    raise KeyError("This is an error that I made up.")

# weight = int(input("Weight: "))
# height = float(input("Height: "))

# if height > 3:
#    raise ValueError("Human height should not be over 3 meters.")  # Erro "forçado"

# bmi = weight / height ** 2
# print(bmi)

"""
# ######### Exercise 1 - Index Error Handling ##########
"""
fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")

make_pie(4)

# """
# ######### Exercise 2 - Key Error Handling ##########
"""
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:  # <---- Evita esse tipo de erro. Ao inves de identificar e avisar que um dos elementos não possui
        #                         tal "key", ele ignora e continua a fazer a conta, nesse caso.
        pass

print(total_likes)

"""
# ######### Code Exercise: Exception Handling in the NATO Phonetic Alphabet Project ##########
# """
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()  # <---- É possível colocar a função dentro dela mesma. Mindblowing!
    else:
        print(output_list)

generate_phonetic()
