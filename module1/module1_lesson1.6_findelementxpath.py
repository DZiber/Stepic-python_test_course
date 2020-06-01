import math

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
link = "http://suninjuly.github.io/find_xpath_form"

try:
    driver.maximize_window()
    actions = ActionChains(driver)
    driver.get(link)

    input1 = driver.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = driver.find_element_by_id("country")
    input4.send_keys("Russia")
    button = driver.find_element_by_xpath(".//button[text()='Submit']")
    actions.move_to_element(button).perform()
    button.click()

finally:
    driver.quit()
