from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
link = "http://suninjuly.github.io/registration2.html"

try:
    driver.maximize_window()
    actions = ActionChains(driver)
    driver.get(link)
    input1 = driver.find_element_by_css_selector(".first_block .first")
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_css_selector(".first_block .second")
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_css_selector(".form-control.third")
    input3.send_keys("tetst@email.com")

    # Отправляем заполненную форму
    button = driver.find_element_by_css_selector("button.btn")
    actions.move_to_element(button).perform()
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()
