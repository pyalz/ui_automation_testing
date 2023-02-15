import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import (ElementNotVisibleException,
                                        NoSuchElementException,
                                        StaleElementReferenceException,
                                        TimeoutException
)
import urllib3
from pytest_base_url.plugin import base_url
import time


class BasePage():
    # -----------------completed-------------------------------------------------------------------------
    def __init__(self, driver):
        self.driver = driver

    def open_homepage(self,base_url):
        self.driver.get(base_url)

    def is_element_visible(self, *locator):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except (ElementNotVisibleException, NoSuchElementException):
            return False

    def is_element_present(self, *locator):
        """
        Return true if the element at the specified locator is present in the DOM.
        Note: It returns false immediately if the element is not found.
        """
        self.driver.implicitly_wait(0)
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
        finally:
            # set the implicit wait back
            self.driver.implicitly_wait(30)

    def wait_for_element_present(self, *locator):
        count = 0
        timeout = 15
        while not BasePage.is_element_present(self, *locator):
            count += 1
            if count == timeout:
                raise Exception(
                    'Could not find what we were looking for after {} seconds'.format(count))
#-----------------completed-------------------------------------------------------------------------
    def wait_for_element_not_present(self, *locator):
        """Wait for the element at the specified locator to be not present in the DOM."""
        self.selenium.implicitly_wait(0)
        timeout = 20
        try:
            WebDriverWait(self.selenium, timeout).until(lambda s: len(self.find_elements(*locator)) < 1)
            return True
        except TimeoutException:
            assert not TimeoutException, 'Page Timeout'
        finally:
            self.selenium.implicitly_wait(timeout)

    def wait_for_element_visible(self, *locator):
        """Wait for the element at the specified locator to be visible in the browser."""
        count = 0
        timeout = 10
        while not self.is_element_visible(*locator):
            time.sleep(1)
            count += 1
            if count == timeout:
                raise Exception("{} was not visible after {time} seconds".format(*locator, time=timeout))

    def wait_for_element_to_load( self, *locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(*locator)
        )

    def highlight(element, effect_time=2, color="red", border=5):
        """Highlights (blinks) a Selenium Webdriver element"""
        driver = element._parent

        desired_y = (element.size['height'] / 2) + element.location['y']
        current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script(
            'return window.pageYOffset')
        scroll_y_by = desired_y - current_y
        driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)

        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                  element, s)

        original_style = element.get_attribute('style')
        apply_style("border: {0}px solid {1};".format(border, color))
        time.sleep(effect_time)
        apply_style(original_style)

