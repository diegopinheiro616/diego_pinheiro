""" Day 38 """

import os
import requests
from datetime import datetime

APP_ID = "f0b386d9"
API_KEY = "4808a0931b46b5914adbd27ae3ed2b55"
SECRET_TOKEN = "Bearer OtixeMeg##@iifsdsdfeg64653{}"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

bearer_authorization = {
    "Authorization": SECRET_TOKEN
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


exercise_test = input("Tell me which exercises you did: ")

post_request_body = {
    "query": exercise_test,
    "gender": "male",
    "weight_kg": 68.0,
    "height_cm": 159.00,
    "age": 32

}

site_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/2ca1b0d11e6e3fdba128a4f85418b9e8/workoutTracking/workouts"

response = requests.post(url=site_endpoint, json=post_request_body, headers=headers)
result = response.json()
print(result)  # ran 3 miles
# {'exercises': [{'tag_id': 317, 'user_input': 'ran', 'duration_min': 30.02, 'met': 9.8, 'nf_calories': 333.42,
# 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg',
# 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg', 'is_user_uploaded': False},
# 'compendium_code': 12050, 'name': 'running', 'description': None, 'benefits': None}]}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=bearer_authorization)
result = sheet_response.json()
print(result)


