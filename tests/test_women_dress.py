import pytest
import allure
from common.base import BasePage as Base
from page.homePage import HomePage
from page.womenDressPage import WomenDressPage

# to link the setup in conftest.py
@pytest.mark.usefixtures("test_setup")
class Test_Women_dress():

    @allure.description("Validate items in the home page")

    def test_search_field_tc1(self,base_url):
        WomenDressPage.verify_searchField(self,base_url)

    def test_search_result__tc2(self):
        WomenDressPage.search_text(self)




