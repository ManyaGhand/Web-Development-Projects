import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

PROMISED_DOWN = 100
PROMISED_UP = 10

TWITTER_EMAIL = os.getenv("EMAIL")
TWITTER_PASSWORD = os.getenv("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InternetSpeedBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options= chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/result/18144801311")
        time.sleep(15)

        continue_popup = self.driver.find_element(By.XPATH, value= '//*[@id="onetrust-accept-btn-handler"]')
        continue_popup.click()

        go_button = self.driver.find_element(By.XPATH, value = '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a/span[4]')
        go_button.click()
        time.sleep(60)
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div/div[2]/span').text
        print(f"UPLOADING SPEED: {self.up}")
        print(f"DOWNLOADING SPEED: {self.down}")
        self.driver.quit()


'''Note: 
Originally, this project was intended to automatically tweet internet speed
results using Selenium. However, Twitter/X has become almost bot-free and 
blocks most Selenium-based login attempts.'''

   # def tweet_at_provider(self):
   #     self.driver.get("https://x.com/login")
   #    time.sleep(3)
   #
   #     email = self.driver.find_element(By.XPATH,
   #                                      value='//*[@id="container-div"]/div/div[2]/div[1]/div[2]/div')
   #     password = self.driver.find_element(By.XPATH,
   #                                        value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
   #    email.send_keys(TWITTER_EMAIL)
   #    email.send_keys(Keys.ENTER)
   #    password.send_keys(TWITTER_PASSWORD)
   #    time.sleep(2)
   #    password.send_keys(Keys.ENTER)
   #
   #    time.sleep(5)
   #     tweet_compose = self.driver.find_element(By.XPATH,
   #                                              value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
   #
   #    tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
   #     tweet_compose.send_keys(tweet)
   #     time.sleep(3)
   #
   #     tweet_button = self.driver.find_element(By.XPATH,
   #                                             value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
   #     tweet_button.click()
   #     time.sleep(2)
   #     self.driver.quit()


Bot = InternetSpeedBot()
Bot.get_internet_speed()
