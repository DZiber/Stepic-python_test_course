import math
from selenium import webdriver
import os

driver = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
link = "http://suninjuly.github.io/file_input.html"

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    driver.maximize_window()
    driver.get(link)

    first_name = driver.find_element_by_name("firstname")
    first_name.send_keys("Test")
    last_name = driver.find_element_by_name("lastname")
    last_name.send_keys("Tester")
    email_name = driver.find_element_by_name("email")
    email_name.send_keys("test@email.com")
    file_upload = driver.find_element_by_xpath(".//input[@type='file']")
    file_upload.send_keys(file_path)

    button = driver.find_element_by_xpath(".//button[text()='Submit']")
    button.click()

finally:
    driver.quit()
