import allure
import allure_commons

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.base import BasePage

from locators.locators import CartSummary
import time

#https://www.digitalocean.com/community/tutorials/how-to-use-logging-in-python-3
import logging
logging.basicConfig(level = logging.INFO)
logger = logging.getLogger()

class Summary(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def validate_total_tax_is_present(self):
        BasePage.wait_for_element_present(self, *CartSummary._total_price)
        BasePage.wait_for_element_present(self, *CartSummary._total_tax)
        BasePage.highlight(self.driver.find_element(*CartSummary._total_price))



