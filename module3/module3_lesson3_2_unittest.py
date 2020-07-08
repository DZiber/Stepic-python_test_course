import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')


class TestUniqSelectors(unittest.TestCase):
    def test_uniq_selector1(self):
        link = "http://suninjuly.github.io/registration1.html"

        driver.maximize_window()
        actions = ActionChains(driver)
        driver.get(link)
        input1 = driver.find_element_by_css_selector(".first_block .first")
        input1.send_keys("Ivan")
        input2 = driver.find_element_by_css_selector(".first_block .second")
        input2.send_keys("Petrov")
        input3 = driver.find_element_by_css_selector(".form-control.third")
        input3.send_keys("tetst@email.com")

        button = driver.find_element_by_css_selector("button.btn")
        actions.move_to_element(button).perform()
        button.click()

        time.sleep(1)

        welcome_text_elt = driver.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_uniq_selector2(self):
        link = "http://suninjuly.github.io/registration2.html"

        driver.maximize_window()
        actions = ActionChains(driver)
        driver.get(link)
        input1 = driver.find_element_by_css_selector(".first_block .first")
        input1.send_keys("Ivan")
        input2 = driver.find_element_by_css_selector(".first_block .second")
        input2.send_keys("Petrov")
        input3 = driver.find_element_by_css_selector(".form-control.third")
        input3.send_keys("tetst@email.com")

        button = driver.find_element_by_css_selector("button.btn")
        actions.move_to_element(button).perform()
        button.click()

        time.sleep(1)

        welcome_text_elt = driver.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
