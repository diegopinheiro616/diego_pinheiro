""" Day 25 - Working with CSV Files and analysing Data with Pandas """

# ################ Reading CSV Data in Python ####################
"""
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    print(data)
    temperatures = []
#    for row in data:
#        print(row)
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    # print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
print(data['temp'])  # <---- Imprime só os dados da coluna temp (sem o ´titulo da coluna)
"""
# ################ DataFrames & Series: Working with Rows & Columns ####################
"""
import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))  # <---- class 'pandas.core.frame.DataFrame'  DATAFRAME
# print(type(data["temp"]))  # <---- class 'pandas.core.series.Series'  SERIES (cada coluna é uma das series)

data_dict = data.to_dict()
# print(data_dict)  # <---- {'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday',
#  5: 'Saturday', 6: 'Sunday'}, 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24},
#  'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}

# temp_list = data["temp"].to_list()
# print(temp_list)  # <---- [12, 14, 15, 14, 21, 22, 24]
# print(len(temp_list))  # <---- 7

# average = sum(temp_list) / len(temp_list)
# print(round(average, 0))  # <---- 17.0

# print(data["temp"].mean())  # <---- 17.428571428571427    "mean" Média(average do trecho acima)
# print(data["temp"].max())  # <---- 24 (temperatura máxima)

# Get Data in Columns
# print(data["Condition"])  # <---- (key) não necessita ser uma string com a letra inicial minúscula
# print(data.Condition)  # <---- (object) Transformauma dascoluna em atributo. AmbosPrints dão o mesmo resultado abaixo:
# 0     Sunny
# 1      Rain
# 2      Rain
# 3    Cloudy
# 4     Sunny
# 5     Sunny
# 6     Sunny
# Name: condition, dtype: object

# Get Data in Rows
# print(data[data.day == "Monday"])
#       day  temp Condition
# 0  Monday    12     Sunny
# print(data[data.temp == data.temp.max()])
#       day  temp Condition
# 6  Sunday    24     Sunny

monday = data[data.day == "Monday"]
# print(monday)  # <---- day  temp Condition
#                0  Monday    12     Sunny
# print(monday.Condition)  # <---- 0    Sunny
monday_temp = int(monday.temp)
monday_temp_f = round(monday_temp * 9/5 + 32, 1)
# print(monday_temp_f)  # <---- 53.6

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
    }

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")  # <--- creates: new_data.csv arquivo na mesma pasta com a seguinte formatação:
# ,students,scores
# 0,Amy,76
# 1,James,56
# 2,Angela,65
"""
# ################ The Great Squirrel Census Data Analysis (with Pandas!) ####################
"""
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
# print(grey_squirrels)
#               X  ...                                    Lat/Long
# 2    -73.974281  ...  POINT (-73.97428114848522 40.775533619083)
# 3    -73.959641  ...  POINT (-73.9596413903948 40.7903128889029)
# 4    -73.970268  ...  POINT (-73.9702676472613 40.7762126854894)
# 6    -73.954120  ...  POINT (-73.9541201789795 40.7931811701082)
# 7    -73.958269  ...  POINT (-73.9582694312289 40.7917367820255)
# ...         ...  ...                                         ...
# 3016 -73.966290  ...  POINT (-73.9662895079734 40.7843300758044)
# 3018 -73.963943  ...  POINT (-73.9639431360458 40.7908677445466)
# 3019 -73.970402  ...  POINT (-73.9704015859639 40.7825600069973)
# 3020 -73.966587  ...  POINT (-73.9665871993517 40.7836775064883)
# 3021 -73.963994  ...  POINT (-73.9639941227864 40.7899152327912)
#
# [2473 rows x 31 columns]

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# print(grey_squirrels_count)  # <---- 2473
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count, red_squirrels_count, black_squirrels_count)  # <---- 2473 392 103

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

# ,Fur Color,Count
# 0,Gray,2473
# 1,Cinnamon,392
# 2,Black,103
"""

