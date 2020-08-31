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

footer_element_exists = False
try:
    footer_element = browser.find_element_by_id("footer")
    footer_element_exists = True
except NoSuchElementException:
    print("Footer not found!")
finally:
    print("Footer found. Proof: ")
    print(footer_element_exists)
    browser.quit()


if footer_element_exists:
    footer_element = browser.find_element_by_id("footer")
    try:
        view_element = footer_element.find_element_by_tag_name('e')
        ActionChains(browser).move_to_element(view_element).click().perform()
    except NoSuchElementException:
        print("Failed to identify element.")