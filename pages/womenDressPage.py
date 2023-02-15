import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.base import BasePage
import allure
import allure_commons

class WomenDressPage(BasePage):

    _women_Button = (By.XPATH , "//a[@class='sf-with-ul'][contains(text(),'Women')]")
    _cat_name = (By.CLASS_NAME, 'cat-name')
    _sort_drop_down = (By.ID, 'selectProductSort')

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Women Category')
    def verify_searchField(self,base_url):
        self.driver.get(base_url)
        self.driver.find_element(*WomenDressPage._women_Button).click()
        is_present = BasePage.is_element_visible(self, *WomenDressPage._cat_name)
        assert is_present, "Women Category is missing"

    @allure.step('Search text')
    def search_text(self):
        select = Select(self.driver.find_element_by_id('selectProductSort'))
        select.select_by_visible_text('Price: Lowest first')
        time.sleep(10)



