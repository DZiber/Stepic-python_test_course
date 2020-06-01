import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')

try:
    driver.maximize_window()
    actions = ActionChains(driver)

    driver.get("https://stepik.org/lesson/25969/step/12")
    time.sleep(5)

    textarea = driver.find_element_by_css_selector(".textarea")

    textarea.send_keys("get()")
    time.sleep(5)

    submit_button = driver.find_element_by_css_selector(".submit-submission")
    actions.move_to_element(submit_button).perform()
    submit_button.click()

finally:
    driver.quit()
