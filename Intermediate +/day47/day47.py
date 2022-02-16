import requests

from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com.br/CADEIRA-GAMER-PLAYSTATION-BRANCA-CADGPSBR/dp/B09GW8JJ3D/ref=sr_1_3?__mk_pt_BR=" \
      "%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3R0GZK28IAB6F&keywords=playstation%2B5&qid=1643414464&sprefix=playsta" \
      "tion%2B5%2Caps%2C210&sr=8-3&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0"
                  ".4692.99 Safari/537.36 Edg/97.0.1072.69",
    "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
}
MY_EMAIL = "9sagesrpg@gmail.com"
MY_PASSWORD = "hdJTdE34"


response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(name='span', class_='a-offscreen').get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency.replace(".", "").replace(",", "."))
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 1200

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="diegothetal@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )