from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()
# #####################################################################################################################

ORIGIN_CITY_IATA = "GRU"

tomorrow_a = datetime.now() + timedelta(days=1)
tomorrow = tomorrow_a.strftime("%d/%m/%Y")
six_months_later = datetime.now() + timedelta(days=6*30)
six_months = six_months_later.strftime("%d/%m/%Y")

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        # #####################################################################################################################
    pprint(f"sheet_data:\n {sheet_data}")
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
    # #####################################################################################################################

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months
    )
    # #####################################################################################################################
    if flight is None:
        continue

    if flight is not None and flight.price < destination["lowestPrice"]:

        users = data_manager.get_customer_emails()
        # #####################################################################################################################
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = f"Low price alert! Only U${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} " \
                  f"to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to " \
                  f"{flight.return_date}."

        if flight.stop_overs > 0:

            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(message)

        link = f'https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.' \
               f'{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}'

        notification_manager.send_emails(emails, message, link)

# Low price alert! Only U$742 to fly from São Paulo-GRU to Amsterdam-AMS, from 2022-02-15 to 2022-03-02.
# Flight has 1 stop over, via Paris.
