import math

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
link = "http://suninjuly.github.io/selects1.html"

try:
    driver.maximize_window()
    actions = ActionChains(driver)
    driver.get(link)

    x_elem = driver.find_element_by_id("num1")
    y_elem = driver.find_element_by_id("num2")
    capcha_answer = int(x_elem.text) + int(y_elem.text)

    select = Select(driver.find_element_by_id("dropdown"))
    select.select_by_value(str(capcha_answer))

    button = driver.find_element_by_xpath(".//button[text()='Submit']")
    actions.move_to_element(button).perform()
    button.click()

finally:
    driver.quit()
