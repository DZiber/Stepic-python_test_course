import math

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.maximize_window()
    actions = ActionChains(driver)
    driver.get(link)

    x_elem = driver.find_element_by_id("treasure")
    capcha_answer = calc(x_elem.get_attribute("valuex"))

    answer = driver.find_element_by_id("answer")
    answer.send_keys(capcha_answer)
    checkbox = driver.find_element_by_id("robotCheckbox")
    checkbox.click()
    radio = driver.find_element_by_id("robotsRule")
    radio.click()

    button = driver.find_element_by_xpath(".//button[text()='Submit']")
    actions.move_to_element(button).perform()
    button.click()

finally:
    driver.quit()


