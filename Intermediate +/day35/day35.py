""" Day 35 """
"""
# http://api.openweathermap.org/data/2.5/weather?q=london,UK&appid=8cbfc48f2e0cb9fc01890c385bd59e81

# {"coord":{"lon":-0.1257,"lat":51.5085},"weather":[{"id":803,"main":"Clouds","description":"broken clouds",
# "icon":"04d"}],"base":"stations","main":{"temp":283.72,"feels_like":282.92,"temp_min":282.64,"temp_max":284.4,
# "pressure":1008,"humidity":80},"visibility":10000,"wind":{"speed":4.12,"deg":240},"clouds":{"all":75},
# "dt":1641217356,"sys":{"type":2,"id":2019646,"country":"GB","sunrise":1641197149,"sunset":1641225821},
# "timezone":0,"id":2643743,"name":"London","cod":200}
"""
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

API_KEY = "8cbfc48f2e0cb9fc01890c385bd59e81"
LAT = "-23.550520"
LONG = "-46.633308"

account_sid = "AC7d73be5d658c6cecb2c54d5e62b28557"
auth_token = "243999bc62e820cbe8ad99123fecc48c"

weather_params = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
# print(response.status_code)  # 200 <---- "OK" HTTPS STATUS
response.raise_for_status()
weather_data = response.json()
# print(weather_data["hourly"][0]["weather"])
# [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}]
# print(weather_data["hourly"][0]["weather"][0])
# {'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}
# print(weather_data["hourly"][0]["weather"][0]["id"])
# 501
weather_data_slice = weather_data["hourly"][:12]  # <---- Slice

will_rain = False

# for hour_data in weather_data_slice:
#    print(hour_data["weather"])
# [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}]
# [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]
# [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]
# [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]
# [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}]
# [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}]
# [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}]
# [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}]
# [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}]
# [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}]
# [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}]
# [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}]

# for hour_data in weather_data_slice:
#    print(hour_data["weather"][0])
# {'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}
# {'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}
# {'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}
# {'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}
# {'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}
# {'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}
# {'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}
# {'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}
# {'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}
# {'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}
# {'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}
# {'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}

# for hour_data in weather_data_slice:
#    print(hour_data["weather"][0]["id"])
# 501
# 802
# 803
# 803
# 501
# 501
# 501
# 501
# 500
# 500
# 500
# 500

for hour_data in weather_data_slice:
    # print(hour_data["weather"][0]["id"])
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_="+13074481980",
        to="+5511962246633"
    )
print(message.status)

# (478) 412-7282   #  +14784127282
# 5511962246633