
""" Day 33 - API (Application Programming Interface) Endpoints & API Parameters - ISS Overhead Notifier """

# ######### API Endpoints and Making API Calls ##########
"""
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)  # <Response [200]>
"""
# ######### Working with Responses: HTTP Codes, Exceptions & JSON Data ##########
"""
# 1XX: Hold On, 2XX: Here You Go, 3XX: Go Away, 4XX: You Screwed Up, 5XX: I Screwed Up, 404: Not Found
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)  # <Response [200]>
# print(response.status_code)  # 200 (Sucess!!)
response.raise_for_status()  # Se não for um código 200, ele vai levantar exceções.

data = response.json()
# print(data)  # {'iss_position': {'longitude': '130.1801', 'latitude': '-43.5273'},
#               'message': 'success', 'timestamp': 1640864144}
# data = response.json()["iss_position"]
# print(data)  # {'longitude': '139.7327', 'latitude': '-38.2430'}
# data = response.json()["iss_position"]["latitude"]
# print(data)  # -35.5324
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)  # ('151.2774', '-29.1148')

# latlong.net/geo-tools
"""
# ######### Challenge - Build a Kanye Quotes App using the Kanye Rest API ##########
"""
# https://api.kanye.rest
from tkinter import *
import requests

def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250,
                                font=("Arial", 16, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
"""
# ######### Understand API Parameters: Match Sunset Times with the Current Time ##########
"""
import requests
from datetime import datetime

MY_LAT = "-23.5489"
MY_LONG = "-46.6388"

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()  # Se não for um código 200, ele vai levantar exceções.

# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)

# print(iss_position)

parameters = {
    "lag": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
# print(data)  # {'results': {'sunrise': '9:04:25 AM', 'sunset': '9:14:02 PM', 'solar_noon': '3:09:13 PM',
#               'day_length': '12:09:37', 'civil_twilight_begin': '8:43:07 AM', 'civil_twilight_end': '9:35:20 PM',
#             'nautical_twilight_begin': '8:16:58 AM', 'nautical_twilight_end': '10:01:29 PM',
#             'astronomical_twilight_begin': '7:50:41 AM', 'astronomical_twilight_end': '10:27:46 PM'}, 'status': 'OK'}
# sunrise = data["results"]["sunrise"]
# sunset = data["results"]["sunset"]

# print(sunrise)  # .                      9:14:02 PM ("formatted":1)          2021-12-30T09:04:25+00:00 ("formatted":0)
# print(sunrise.split("T"))  # .                                        ['2021-12-30', '09:04:25+00:00'] ("formatted":0)
# print(sunrise.split("T")[1].split(":"))  # .                               ['09', '04', '25+00', '00'] ("formatted":0)
# print(sunrise.split("T")[1].split(":")[0]) # .                                                      09 ("formatted":0)

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)  # 09
print(sunset)  # 21

time_now = datetime.now()

print(time_now)  # 2021-12-30 09:25:40.693975
print(time_now.hour)  # 9
"""
# ######### ISS Overhead Notifier Project ##########
# """
import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -23.5489  # Your latitude
MY_LONG = -46.6388  # Your longitude
MY_EMAIL = "9sagesrpg@gmail.com"
MY_PASSWORD = "hdJTdE34"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="9sagesrpg@gmail.com",
            msg="Subject: Look Up\n\nThe ISS is above you in the sky."
        )

# """


