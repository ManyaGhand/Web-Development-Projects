from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

cookie = driver.find_element(By.XPATH, value = '//*[@id="bigCookie"]')

upgrade_interval = 5
upgrade_time = time.time() + upgrade_interval

# Set time to stop program execution
stop_time = time.time() + 300
while True:
    cookie.click()
    if time.time() >= upgrade_time:
        products = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
        print(products)

        if products:
            products[len(products) - 1].click()
        upgrade_time = time.time() + upgrade_interval

    # Stop program execution
    if time.time() >= stop_time:
        break

# Print out cookies per second
print(driver.find_element(By.XPATH, "//*[@id='cookies']/div").text)

driver.quit()