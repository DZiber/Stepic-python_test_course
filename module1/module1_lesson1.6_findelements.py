from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
link = "http://suninjuly.github.io/huge_form.html"

try:
    driver.maximize_window()
    actions = ActionChains(driver)
    driver.get(link)

    elements = driver.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("Test")
    button = driver.find_element_by_css_selector("button.btn")
    actions.move_to_element(button).perform()
    button.click()

finally:
    driver.quit()
