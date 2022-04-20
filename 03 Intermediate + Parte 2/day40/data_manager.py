import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/2ca1b0d11e6e3fdba128a4f85418b9e8/flightDeals/prices"
APP_ID = "f0b386d9"
API_KEY = "4808a0931b46b5914adbd27ae3ed2b55"
SECRET_TOKEN = "mPdYcbUK9p)ufxJp"

sheety_bearer_authorization = {
    "Authorization": f"Bearer {SECRET_TOKEN}"
}


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_data = []

    def get_destination_data(self):

        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=sheety_bearer_authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):

        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=sheety_bearer_authorization,
            )
            print(response.text)

    def get_customer_emails(self):

        customers_endpoint = "https://api.sheety.co/2ca1b0d11e6e3fdba128a4f85418b9e8/flightDeals/users"
        response = requests.get(customers_endpoint, headers=sheety_bearer_authorization)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
