from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

chrome_webdriver_path = "Your path to your chrome webdriver here"
ser = Service(chrome_webdriver_path)
driver = webdriver.Chrome(service=ser)
driver.get("Enter the URL of the site where you want to save the jobs from (make sure that you have easy"
           "apply filter on)")

driver.maximize_window()

sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()

# SIGN IN

email_bar = driver.find_element(By.ID, "username")
password_bar = driver.find_element(By.ID, "password")
sign_in_button = driver.find_element(By.CLASS_NAME, "btn__primary--large")

sleep(1)

email_bar.send_keys("your email to your linkedin account")
password_bar.send_keys("your password to your linkedin account")
sign_in_button.click()

sleep(1)

# APPLICATION PROCESS

jobs = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")

for job in jobs:
    sleep(1)
    job.click()
    sleep(1)
    save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    save_button_text = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button span")
    print(save_button_text)
    print(save_button_text.text)
    if save_button_text.text == "Save":
        save_button.click()
        print("Hello")
        sleep(1)

