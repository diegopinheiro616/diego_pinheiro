""" Day 36 """
import requests
from twilio.rest import Client

VIRTUAL_TWILIO_NUMBER = "+13074481980"
VERIFIED_NUMBER = "+5511962246633"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "T84QELV4W77RK1WG"
NEWS_API_KEY = "857587525c614d469a8b431a975c6aac"

account_sid = "AC7d73be5d658c6cecb2c54d5e62b28557"
auth_token = "243999bc62e820cbe8ad99123fecc48c"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
# e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
# print(response.json())
# {'Meta Data': {'1. Information': 'Daily Prices (open, high, low, close) and Volumes', '2. Symbol': ...1686'}}}
data = response.json()["Time Series (Daily)"]
# print(data)
# {'2022-01-03': {'1. open': '1147.7500', '2. high': '1201.0700', '3. low': '1136.0400', ...686'}}
data_list = [value for (key, value) in data.items()]
# print(data_list)
# [{'1. open': '1147.7500', '2. high': '1201.0700', '3. low': '1136.0400', '4. close': '1199.7800', '5. volume':...6'}]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
# print(yesterday_closing_price)  # 1199.7800

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
# print(day_before_yesterday_closing_price)  # 1056.7800


#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
# Hint: https://www.w3schools.com/python/ref_func_abs.asp


difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
# print(difference)  # 143.0

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day
# before yesterday.
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
# print(diff_percent)  # 11.918851789494742

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
# if diff_percent > 5:
    # print("Get News")  # Get News

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if abs(diff_percent) > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    # print(news_response)  # <Response [200]>
    # print(news_response.json())
    # {'status': 'ok', 'totalResults': 10, 'articles': [{'source': {'id': 'reuters', 'name': 'Reuters'}, 'author':..'}]}
    articles = news_response.json()["articles"]
    # print(articles)
    # [{'source': {'id': 'reuters', 'name': 'Reuters'}, 'author': None, 'title': 'Tesla, Southwest Airlines, ....]'}]


    #TODO 7. - Use Python slice operator to create a list that contains the first 3 articles.
    # Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    # Understanding slice notation
    # a[start:stop]  # items start through stop-1
    # a[start:]      # items start through the rest of the array
    # a[:stop]       # items from the beginning through stop-1
    # a[:]           # a copy of the whole array

    three_articles = articles[:3]
    # print(three_articles)
    # [{'source': {'id': 'reuters', 'name': 'Reuters'}, 'author': None, 'title': 'Tesla, Southwest Airlines,....'}]
    # clicar no botão do "4: Run" "Soft-Wrap"
    # Vai aparecer informações a mais, inclusive urls, etc...

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

    #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: " \
                          f"{article['description']}" for article in three_articles]

    #TODO 9. - Send each article as a separate message via Twilio.
    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )



    #Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to 
file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height 
of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to
 file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height
  of the coronavirus market crash.
"""

