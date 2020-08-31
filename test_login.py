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



