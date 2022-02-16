""" Day 51 """
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

PROMISED_DOWN = 100
PROMISED_UP = 50
CHROME_DRIVER_PATH = YOUR CHROE DRIVER PATH
TWITTER_EMAIL = YOUR TWITTER EMAIL ADDRESS
TWITTER_PASSWORD = YOUR TWITTER PASSWORD


class InterNetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.download_speed = None
        self.upload_speed = None
        self.driver = webdriver.Chrome(driver_path)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        # Press GO button to check the internet speed
        sleep(5)
        go_button = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                      '1]/a/span[4]')
        go_button.click()

        # Catch the download speed after 45 secs
        sleep(45)
        self.download_speed = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
            '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
            '2]/div/div[2]/span').text
        # Catch the upload speed
        self.upload_speed = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div['
            '3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    def tweet_at_provider(self, email_id, password):
        self.driver.get("https://twitter.com/login")

        sleep(5)  # Click on "Sign in with Google Account" button
        google_login_button = self.driver.find_element_by_css_selector(
            ".S9gUrf-YoZ4jf iframe")  # Couldn't figure out the way to work with Xpath.
        google_login_button.click()

        sleep(3)  # Switch the driver to "Google sign-in" window
        base_window = self.driver.window_handles[0]
        google_signin_window = self.driver.window_handles[1]
        self.driver.switch_to.window(google_signin_window)

        sleep(2)  # Pass in user Email ID and press enter to go password page
        login_field = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        login_field.send_keys(email_id)
        login_field.send_keys(Keys.ENTER)

        sleep(2)  # Pass in the password and press enter to sign in to Twitter
        password_field = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        password_field.send_keys(password)
        password_field.send_keys(Keys.ENTER)

        sleep(3)  # Switch the driver back to main window.
        self.driver.switch_to.window(base_window)

    def tweet_issue(self, tweet):
        sleep(3)
        tweet_field = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div['
            '2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_field.send_keys(tweet)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div['
                                                         '2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                                                         '1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_button.click()


bot = InterNetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()  # Checks the internet speed

# Captures current internet download and upload speed.
download = float(bot.download_speed)
upload = float(bot.upload_speed)

if download < PROMISED_DOWN or upload < PROMISED_UP:
    bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD)  # Log in to Twitter account
    tweet = f"Hey Internet Provider, why is my internet speed {download}down/{upload}up when I pay 1000rs for 10down/5up? "
    bot.tweet_issue(tweet)

    sleep(10)  # Quit the program after 10 secs
    bot.driver.quit()
else:
    sleep(10)  # Quit the program after 10 secs
    bot.driver.quit()
"""
