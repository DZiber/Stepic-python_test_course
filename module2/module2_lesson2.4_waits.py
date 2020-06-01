import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.maximize_window()
    actions = ActionChains(driver)
    driver.get(link)

    WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = driver.find_element_by_id("book")
    button.click()

    x_elem = driver.find_element_by_id("input_value")
    capcha_answer = calc(x_elem.text)
    answer = driver.find_element_by_id("answer")
    answer.send_keys(capcha_answer)

    button = driver.find_element_by_xpath(".//button[text()='Submit']")
    actions.move_to_element(button).perform()
    button.click()

finally:
    driver.quit()
