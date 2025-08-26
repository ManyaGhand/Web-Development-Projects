from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
import os
import time

ACCOUNT_EMAIL = "student@test.com"
ACCOUNT_PASSWORD = "password123"

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")
wait = WebDriverWait(driver, 2)

def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            time.sleep(1)
    return None

def login():
    time.sleep(12)
    login_btn = wait.until(ec.element_to_be_clickable((By.ID ,"login-button")))
    login_btn.click()

    time.sleep(3)
    email = wait.until(ec.element_to_be_clickable((By.ID ,"email-input")))
    email.send_keys(ACCOUNT_EMAIL)

    time.sleep(3)
    password = wait.until(ec.element_to_be_clickable((By.ID ,"password-input")))
    password.send_keys(ACCOUNT_PASSWORD)

    time.sleep(3)
    submit_btn = driver.find_element(By.ID ,"submit-button")
    submit_btn.click()

    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))


retry(login, description="login")

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

booked_count = 0
waitlist_count = 0
already_booked_count = 0

for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    if "Wed" in day_title:
        class_time = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in class_time:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            button.click()


            if button.text =="Booked":
                print(f"✓ {class_name} Class is already booked for {day_title}")
                already_booked_count = +1
            elif button.text =="Waitlisted":
                print(f"✓ {class_name} Class is waitlisted for {day_title}")
                already_booked_count = +1
            elif button.text =="Book Class":
                button.click()
                print(f" ✓ {class_name} Class is booked for {day_title}")
                booked_count = +1
            elif button.text == "Join Waitlist":
                button.click()
                print(f"✓ Joined waitlist for {class_name} on {day_title}")
                waitlist_count = +1
            break

print("\n--- BOOKING SUMMARY ---")
print(f"Classes booked: {booked_count}")
print(f"Waitlists joined: {waitlist_count}")
print(f"Already booked/waitlisted: {already_booked_count}")
print(f"Total Tuesday 6pm classes processed: {booked_count + waitlist_count + already_booked_count}")
