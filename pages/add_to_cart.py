import allure
import allure_commons

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.base import BasePage

from locators.locators import pdp
import time

#https://www.digitalocean.com/community/tutorials/how-to-use-logging-in-python-3
import logging
logging.basicConfig(level = logging.INFO)
logger = logging.getLogger()

class AddtoCart(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Verify Add to cart')
    def verify_add_to_cart_button(self):
        BasePage.is_element_visible(self, *pdp._add_to_cart)

    @allure.step('Add to cart')
    def add_to_cart_button(self):
        self.driver.switch_to.frame(self.driver.find_element(*pdp._frame))
        BasePage.wait_for_element_present(self, *pdp._add_to_cart)
        BasePage.highlight(self.driver.find_element(*pdp._add_to_cart))
        self.driver.find_element(*pdp._add_to_cart).click()
        time.sleep(5)
        self.driver.switch_to.default_content()

    def click_proceed_to_checkout(self):
        BasePage.wait_for_element_present(self, *pdp._proceed_to_checkout)
        self.driver.find_element(*pdp._proceed_to_checkout).click()
        time.sleep(5)


