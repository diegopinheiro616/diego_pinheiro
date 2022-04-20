""" Day 48 """
# ########## SELENIUM ############
"""
from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com.br/CADEIRA-GAMER-PLAYSTATION-BRANCA-CADGPSBR/dp/B09GW8JJ3D/ref=sr_1_3?__mk_pt_BR=" \
#      "%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3R0GZK28IAB6F&keywords=playstation%2B5&qid=1643414464&sprefix=playsta" \
#      "tion%2B5%2Caps%2C210&sr=8-3&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147&th=1")  # Abre o url
# price = driver.find_element_by_class_id("XXX")
# print(price.text)

driver.get("https://www.python.org/")  # Abre o url

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))  # search

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)  # {'height': 82, 'width': 290}

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)  # docs.python.org

bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)  # Submit Website Bug

# https://www.w3schools.com/xml/xpath_intro.asp  <---- Documentação do XPath

# driver.close()  # Fecha o url
driver.quit()  # Fecha o url e to do browser
"""
# ########## USE SELENIUM TO SCRAPE WEBSITE DATA ############
"""
from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")  # Abre o url

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)
# {0: {'time': '2022-02-05', 'name': 'PyCascades ... 4: {'time': '2022-04-11', 'name': 'PyCon DE & PyData Berlin 2022'}}
"""
# ########## USE SELENIUM IN A BLANK PROJECT & SCRAPE A DIFFERENT PIECE OF DATA ############
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)  # 6,446,198
# article_count.click()  # <---- Clica no link

all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# all_portals.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)  # <---- Qualquer tecla no teclado pode ser replicada aqui.
"""
# ########## USE SELENIUM IN A SIGN IN SITE ############
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://secure-retreat-92358.herokuapp.com")
first_name = driver.find_element(By.NAME, "fname")
first_name.send_keys("Diego")
last_name = driver.find_element(By.NAME, "lname")
last_name.send_keys("Pinheiro")
email = driver.find_element(By.NAME, "email")
email.send_keys("diegothetal@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()
"""
# ########## CLICK COOKIE PROJECT ############
# """
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on.
cookie = driver.find_element(By.ID, "cookie")

# Get upgrade item ids.
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Get all upgrade <b> tags
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break

