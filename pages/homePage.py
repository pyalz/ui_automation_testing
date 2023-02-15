import allure
import allure_commons

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.base import BasePage
from locators.locators import HomeLocators
from locators.locators import HomeLocators
from locators.locators import pdp
import time

#https://www.digitalocean.com/community/tutorials/how-to-use-logging-in-python-3
import logging
logging.basicConfig(level = logging.INFO)
logger = logging.getLogger()

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Login and check the homepage has search field')
    def verify_searchField(self,base_url):
        self.driver.get(base_url)
        is_present = BasePage.is_element_visible(self, *HomeLocators._search_text_field)
        logger.info('Logged INFO message')
        logger.warning('Logged WARNING message')
        logger.info(time.time())
        time.sleep(3)
        logger.info(time.time())
        assert is_present, "Search field is missing"


    @allure.step('Search for Dress')
    def search_text(self,clothType,base_url):
        self.driver.get(base_url)
        self.driver.find_element(*HomeLocators._search_text_field).click()
        self.driver.find_element(*HomeLocators._search_text_field).send_keys(clothType)
        self.driver.find_element(*HomeLocators._search_button).click()

    @allure.step('Verify the results')
    def search_text_verifyResults(self):
        BasePage.wait_for_element_present(self,*HomeLocators._search_results)
        obj = self.driver.find_elements(*HomeLocators._search_results)
        print(len(obj))
        if len(obj) == 0:
            raise Exception("test case failed search_text_verifyResults")

    @allure.step('Click on 1st product')
    def click_product(self):
        self.driver.find_elements(*HomeLocators._quick_view)[0].click()

