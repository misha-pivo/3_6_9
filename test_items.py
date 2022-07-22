from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_language_from_command_line(browser):
    browser.get(link)
    time.sleep(30)
    add_basket=browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    assert add_basket, 'o my god... button, where you?'
