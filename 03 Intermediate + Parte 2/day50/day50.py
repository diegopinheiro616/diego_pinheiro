""" Day 50 """

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# Setup selelnium
ser = Service("C:\Development\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
# Log in to website
driver.get('https://tinder.com/')
time.sleep(1)
log_in = driver.find_element(By.CLASS_NAME, 'button')
log_in.click()
time.sleep(1)
# Get buttons
buttons_pop_up = driver.find_elements(By.CLASS_NAME, 'button')
# Find Facebook login button
for button in buttons_pop_up:
    if button.get_attribute('aria-label') == 'Log in with Facebook':
        button.click()
        time.sleep(3)
        # Handle facebook pop up window
        main_window = driver.window_handles[0]
        child_window = driver.window_handles[1]
        driver.switch_to.window(child_window)
        # print(driver.title)
        # log in to facebook
        email = driver.find_element(By.NAME, 'email')
        email.send_keys('SEND EMAIL')
        password = driver.find_element(By.NAME, 'pass')
        password.send_keys('SEND PASSWORD')
        login_fb = driver.find_element(By.NAME, 'login')
        login_fb.click()
        # switch to main window
        driver.switch_to.window(main_window)
        break
# Find all buttons on tinder page
time.sleep(5)
allow_location = driver.find_elements(By.CLASS_NAME, 'button')
# Find button that allows location
for button in allow_location:
    if button.get_attribute('data-testid') == 'allow':
        print("Found allow location")
        button.click()
        break
# Find button that says NO to notifications
time.sleep(2)
no_notifications = driver.find_elements(By.CLASS_NAME, 'button')
for button in no_notifications:
    if button.get_attribute('data-testid') == 'decline':
        button.click()
        print("no notifications")
        break

accept_tos = driver.find_element(By.XPATH, '//*[@id="q-184954025"]/div/div[2]/div/div/div[1]/button')
accept_tos.click()
print('Accepted TOS')
time.sleep(5)
counter = 0
# Loop like untill dail limit of 100
while counter < 99:
    try:
        # Check if it's first card or not
        if counter == 0:
            like_button = driver.find_element(By.XPATH, '//*[@id="q-184954025"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
            like_button.click()
            # print('Clicked the 1st like')
        else:
            like_button = driver.find_element(By.XPATH, '//*[@id="q-184954025"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
            like_button.click()
            # print('Clicked another like')
    except NoSuchElementException:
        print('No Like Button?')
    try:
        back_out = driver.find_element(By.XPATH, '//*[@id="q-728486218"]/div/div/div[1]/div/div[4]/button')
        back_out.click()
        print('You found a match, plan a date')
    except NoSuchElementException:
        #print("No Match with Person")
        continue
    try:
        # Sometimes tinder asks to add desktop app so this says no
        no_add_app = driver.find_element(By.XPATH, '//*[@id="q36386411"]/div/div/div[2]/button[2]')
        no_add_app.click()
        #print("No add app to desktop")
    except NoSuchElementException:
        print("Add App Pop Up doesn't exist")
    # Don't make tinder ban your bot so wait
    time.sleep(5)
    # Increase counter to stop at daily limit
    counter += 1
print("we finished no errors last line")