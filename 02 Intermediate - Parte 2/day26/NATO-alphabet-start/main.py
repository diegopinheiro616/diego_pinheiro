""" Exemplo """
"""
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass
"""
# ######### NATO Alphabet Project ###########

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
""""""
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)
# {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', ... , 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'}

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
# Enter a word: mae
# ['Mike', 'Alfa', 'Echo']

