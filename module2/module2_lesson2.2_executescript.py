import math

from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.maximize_window()
    driver.get(link)

    x_elem = driver.find_element_by_id("input_value")
    capcha_answer = calc(x_elem.text)

    answer = driver.find_element_by_id("answer")
    answer.send_keys(capcha_answer)
    checkbox = driver.find_element_by_id("robotCheckbox")
    checkbox.click()
    radio = driver.find_element_by_id("robotsRule")
    driver.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    button = driver.find_element_by_xpath(".//button[text()='Submit']")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    driver.quit()


