""" Day 53 - Capstone Project """

FORM = "https://docs.google.com/forms/d/e/1FAIpQLSdMcGUSjzZKywFcHoKmFOmp1pW3k_avorySiP9xUygfLszsyg/viewform?usp=sf_link"

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0"
                  ".4692.99 Safari/537.36 Edg/97.0.1072.69",
    "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
}

response = requests.get(
    "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTe"
    "rm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22sou"
    "th%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%"
    "3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%"
    "3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22v"
    "alue%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3"
    "A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds"
    "%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",
    headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

all_link_elements = soup.select(".list-card-top a")

all_links = []
for link in all_link_elements:
    href = link["href"]
    print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)


all_address_elements = soup.select(".list-card-info address")
print(all_address_elements)
all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]
print(all_addresses)


all_price_elements = soup.select(".list-card-heading")
print(all_price_elements)
print(all_price_elements[0])
# <div class="list-card-heading"><div class="list-card-price">$2,995+<abbr class="list-ca
# rd-label"> <!-- -->1 bd</abbr></div><ul class="list-card-details"></ul></div>
print(all_price_elements[0].get_text())  # $2,995+ 1 bd
# """
all_prices = []
for element in all_price_elements:
    # Get the prices. Single and multiple listings have different tag & class structures
    try:
        # Price with only one listing
        price = element.get_text()
        all_prices.append(price)
    except IndexError:
        print('Multiple listings for the card')
        # Price with multiple listings
        price = element.get_text()
        all_prices.append(price)
    # finally:
    #    all_prices.append(price)
print(all_prices)
# ['$2,995+ 1 bd', '$2,950/mo2 bds1 ba1,200 sqft- Apartment for rent', '$2,600+ 1 bd', '$2,300+ 1 bd',
# '$2,800/mo2 bds1 ba1,600 sqft- Apartment for rent', '$2,895/mo1 bd1 ba675 sqft- Apartment for rent',
# '$2,895/mo1 bd1 ba670 sqft- Apartment for rent', '$2,795/mo1 bd1 ba539 sqft- Apartment for rent',
# '$2,595+/mo1 bd1 ba415 sqft- Apartment for rent', '']

# Create Spreadsheet using Google Form
# Substitute your own path here 👇
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

for n in range(len(all_links)):
    # Substitute your own Google Form URL here 👇
    driver.get(FORM)

    time.sleep(2)
    address = driver.find_element(By.XPATH,
                                  '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]'
                                  '/div/div[1]/input')
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/d'
                                          'iv/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/d'
                                         'iv/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()
