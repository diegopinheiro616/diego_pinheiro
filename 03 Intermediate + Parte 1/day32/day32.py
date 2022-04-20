""" Day 32 - Send Email (smtplip) & Manage Dates (datetime) """
# Gmail: smtp.gmail.com

# ######## How to Send Emails with Python using SMTP ##########
"""
import smtplib

my_email = "9sagesrpg@gmail.com"
password = "hdJTdE34"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # <---- Segurança. Mensagem fica criptografada
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="ninesagesrpg@yahoo.com",
                        msg="Subject:Hello2\n\nThis is the body of my email.")

my_email = "ninesagesrpg@yahoo.com"
password = "lxnndedvyeodhxmt"

with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()  # <---- Segurança. Mensagem fica criptografada
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="9sagesrpg@gmail.com",
                        msg="Subject:Hello\n\nThis is the body of my email.")
"""
# ######## Working with the datetime Module ##########
"""
import datetime as dt

now = dt.datetime.now()  # <---- Procura no pc dia e hora.
# print(now)  # 2021-12-29 10:37:56.499365
year = now.year
month = now.month
day_of_week = now.weekday()
# print(type(now))  # datetime.datetime
# print(type(year))  # int
# print(day_of_week)  # 2 (0:segunda, 2:quarta) certo!
date_of_birth = dt.datetime(year=1989, month=2, day=18, hour=4)
print(date_of_birth)  # 1989-02-18 04:00:00
"""
# ######## Challenge 1 - Send Motivacional Quotes on Mondays via Email ##########
"""
import smtplib
import datetime as dt
import random

my_email = "9sagesrpg@gmail.com"
password = "hdJTdE34"

now = dt.datetime.now()
# print(now)
weekday = now.weekday()
# print(weekday)

if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    # print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="diegothetal@gmail.com",
                            msg=f"Subject:Monday Motivation\n\n{quote}"
                            )
"""
# ######## Challenge 2 - Automated Birthday Wisher Project Challenge ##########
"""
from datetime import datetime
import pandas
import random
import smtplib

my_email = "9sagesrpg@gmail.com"
password = "hdJTdE34"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # <---- Segurança. Mensagem fica criptografada
        connection.login(my_email, password)  # (user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday\n\n{contents}")
"""
# ######## Run Your Python Code in the Cloud ##########
# """