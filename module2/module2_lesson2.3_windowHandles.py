import math

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.maximize_window()
    actions = ActionChains(driver)
    driver.get(link)

    button = driver.find_element_by_tag_name("button")
    button.click()

    base_window = driver.window_handles[0]
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    x_elem = driver.find_element_by_id("input_value")
    capcha_answer = calc(x_elem.text)
    answer = driver.find_element_by_id("answer")
    answer.send_keys(capcha_answer)

    button = driver.find_element_by_xpath(".//button[text()='Submit']")
    actions.move_to_element(button).perform()
    button.click()

finally:
    driver.quit()
