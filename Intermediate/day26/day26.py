""" Day 26 - List Comprehension and the NATO Alphabet """

# ################ How to Create Lists using List Comprehension ####################
"""
# numbers = [1, 2, 3]
# new_numbers = [new_item for item in list]
# new_numbers = [n + 1 for n in numbers]
# print(new_numbers) = [2, 3, 4]

# name = "Angela"
# new_list = [letter for letter in name] <---- new_list = ["A", "n", "g", "e", "l", "a"]

# lista = [n*2 for n in range(1, 5)] <---- lista = [2, 4, 6, 8]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [new_item for item in list if test]
# short_names = [name for name in names if len(name) < 5] <---- short_names = ["Alex", "Beth", "Dave"]
long_names = [name.upper() for name in names if len(name) > 5] <---- long_names = ["CAROLINE", "ELEAANOR", "FREDDIE"]
"""
# ################ Exercise 1 - Squaring Numbers ####################
"""
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n**2 for n in numbers]

print(squared_numbers)  # <---- [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
"""
# ################ Exercise 2 - Filtering Even Numbers ####################
"""
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = [num for num in numbers if num % 2 == 0]

print(result)  # <--- [2, 8, 34]
"""
# ################ Exercise 3 - Data Overlap ####################
"""
with open("file1.txt") as file1:
    file_1_data = file1.readlines()
    # ['3\n', '6\n', '5\n', '8\n', '33\n', '12\n', '7\n', '4\n', '72\n', '2\n', '42\n', '13']

with open("file2.txt") as file2:
    file_2_data = file2.readlines()
    # ['3\n', '6\n', '13\n', '5\n', '7\n', '89\n', '12\n', '3\n', '33\n', '34\n', '1\n', '344\n', '42']

result = [int(num) for num in file_1_data if num in file_2_data]  # <--- o int(num) transforma a string 'xx\n' em int!
result2 = [num for num in file_1_data if num in file_2_data]

print(result)  # [3, 6, 5, 33, 12, 7]
print(result2)  # ['3\n', '6\n', '5\n', '33\n', '12\n', '7\n']
"""
# ################ How to Use Dictionary Comprehension ####################
"""
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_score = {student: random.randint(1, 100) for student in names}
# print(student_score) = {'Alex': 21, 'Beth': 59, 'Caroline': 78, 'Dave': 65, 'Eleanor': 20, 'Freddie': 1}

passed_students = {student: score for (student, score) in student_score.items() if score >= 60}  # ".items() qdo dici.
# print(passed_students) = {'Caroline': 78, 'Dave': 65}
"""
# ################ Exercise 4 - Dictionary Comprehension 1 ####################
"""
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# print(sentence.split()) <---- ['What', 'is', 'the', 'Airspeed', 'Velocity', 'of', 'an', 'Unladen', 'Swallow?']

result = {word: len(word) for word in sentence.split()}  # ".split() = converte frase em lista. cada palavra uma str.

print(result)  
# <---- {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}
"""
# ################ Exercise 4 - Dictionary Comprehension 2 ####################
"""
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:((temp_c * 9/5) + 32) for (day, temp_c) in weather_c.items() }
print(weather_f)
# {'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2,
# 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}
"""
# ################ How to Iterate over a Pandas DataFrame ####################
"""
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76,  98]
}
# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key)  # student                   print(value) # ["Angela", "James", "Lily"]
#                 score                                    [56, 76,  98]

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
#   student  score
# 0  Angela     56
# 1   James     76
# 2    Lily     98

# Looping through a DataFrame:
# for (key, value) in student_data_frame.items():
#     print(key)  # print(value)
# student         0    Angela
# score           1     James
#                 2      Lily
#                 Name: student, dtype: object
#                 0    56
#                 1    76
#                 2    98
#                 Name: score, dtype: int64

# Loop through rows of a DataFrame:
for (index, row) in student_data_frame.iterrows():  # <---- Pandas possuem seu ".items()" próprio: ".iterrows()
    print(index)
    # 0
    # 1
    # 2
    print(row)
    # student    Angela
    # score          56
    # Name: 0, dtype: object
    # student    James
    # score         76
    # Name: 1, dtype: object
    # student    Lily
    # score        98
    # Name: 2, dtype: object
    print(row.student)
    # Angela
    # James
    # Lily
    print(row.score)
    # 56
    # 76
    # 98
    if row.student == "Angela":
        print(row.score)
        # 56
"""


