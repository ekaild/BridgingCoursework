from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E
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

delay = 3

try:
    myE = WebDriverWait(browser, delay).until(E.presence_of_element_located((By.ID, 'a')))
    print ("Ready")
except TimeoutException:
        print ("Timeout")

browser.get('http://127.0.0.1:8000')

try:
    tab_title_correct = WebDriverWait(browser, 3).until(
        E.title_contains("Bogdan")
    )
    print(browser.title)
    assert "Bogdan" in browser.title

    create = WebDriverWait(browser, 3).until(
        E.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Create"))
    )
    browser.find_element_by_partial_link_text('Create').click()

    blog_title_present_4 = WebDriverWait(browser, 3).until(
        E.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Bogdan"))
    )
    browser.find_element_by_link_text("Bogdan's Blog").click()

    test_post_title_present_2 = WebDriverWait(browser, 3).until(
        E.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Future"))
    )
    browser.find_element_by_partial_link_text("Future").click()


    edit = WebDriverWait(browser, 3).until(
        E.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Edit"))
    )
    browser.find_element_by_partial_link_text("Edit").click()

    save = WebDriverWait(browser, 3).until(
        E.visibility_of_element_located((By.TAG_NAME, 'button'))
    )
    blog = WebDriverWait(browser, 3).until(
        E.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Bogdan"))
    )
    browser.find_element_by_link_text("Bogdan's Blog").click()



    print("Everything works.", end="\n")
except AssertionError:
    print("A test failed.", end="\n")
except TimeoutException:
    print("Timeout exception!", end="\n")
except Exception:
    print("Unknown exception.", end="\n")
finally:
    browser.quit()