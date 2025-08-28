import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
soup = BeautifulSoup(response.text, "html.parser")

addresses = [address.getText().replace("|", "").strip() for address in soup.find_all(name ="a", class_="StyledPropertyCardDataArea-anchor")]

prices = [price.getText().split("+")[0].replace("/mo", "").strip() for price in soup.find_all(name = "span", class_="PropertyCardWrapper__StyledPriceLine")]

links= [link["href"] for link in soup.find_all(name ="a", class_="StyledPropertyCardDataArea-anchor")]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

for i in range(len(addresses)):

    driver = webdriver.Chrome()
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfHO0dZ8OUXpR_xs_JLRH7IU2f0Lgh2E5FTIqGQzOqSO3YW6g/viewform?usp=dialog")
    time.sleep(3)

    fill_address = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    fill_address.send_keys(addresses[i])

    fill_link = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    fill_link.send_keys(prices[i])

    fill_price = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    fill_price.send_keys(links[i])

    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

    time.sleep(2)