#This is only one test. I made another just to make sure it works and to better understand it.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


from django.contrib.auth import authenticate

browser = webdriver.Firefox()

#Get site
browser.get('http://127.0.0.1:8000/admin')

#Login
username_element = browser.find_element_by_name("username")
username_element.send_keys("bogdan")
password_element = browser.find_element_by_name("password")
password_element.send_keys("123456")
password_element.send_keys(Keys.RETURN)

#One attempt at finding something on the page
try:
    header_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "header"))
    )

    footer_element = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.ID, "footer"))
    )
except TimeoutException:
    print("No element found")
finally:
    print("Elements found. Proof:")
    print(header_element)
