import pytest
import allure
from common.base import BasePage as Base
from pages.homePage import HomePage

# to link the setup in conftest.py
@pytest.mark.usefixtures("test_setup")
class Test_Homepage():
    @allure.description("Validate items in the home page")

    def test_search_field_tc1(self,base_url):
        HomePage.verify_searchField(self,base_url)

    def test_search_result__tc2(self,base_url):
        HomePage.search_text(self,"Dress",base_url)

    def test_search_and_resultVerify__tc3(self,base_url):
        HomePage.search_text(self,"Top", base_url)
        HomePage.search_text_verifyResults(self)

    def test_search_result__tc3(self,base_url):
        HomePage.search_text(self,"Jeans",base_url)
        HomePage.search_text_verifyResults(self)

    def test_search_and_resultVerify__tc4(self,base_url):
        HomePage.search_text(self,"Pasta",base_url)
        HomePage.search_text_verifyResults(self)

    def test_search_and_resultVerify__tc66(self,base_url):
        HomePage.search_text(self,"Noodles",base_url)
        HomePage.search_text_verifyResults(self)





