import pytest
import allure
from common.base import BasePage as Base
from pages.homePage import HomePage
from pages.add_to_cart import AddtoCart
from pages.Summary import Summary

# to link the setup in conftest.py
@pytest.mark.usefixtures("test_setup")
class Test_Homepage():
    @allure.description("Check out a product")

    def test_search_result__tc1(self,base_url):
        HomePage.search_text(self,"Dress",base_url)
        HomePage.search_text_verifyResults(self)
        HomePage.click_product(self)
        AddtoCart.add_to_cart_button(self)
        AddtoCart.click_proceed_to_checkout(self)
        Summary.validate_total_tax_is_present(self)


    def test_search_result__tc2(self,base_url):
        HomePage.search_text(self,"Printed Dress",base_url)
        HomePage.search_text_verifyResults(self)
        HomePage.click_product(self)
        AddtoCart.add_to_cart_button(self)
        AddtoCart.click_proceed_to_checkout(self)
        Summary.validate_total_tax_is_present(self)


    def test_search_result__tc3(self,base_url):
        HomePage.search_text(self,"Top",base_url)
        HomePage.search_text_verifyResults(self)
        HomePage.click_product(self)
        AddtoCart.add_to_cart_button(self)
        AddtoCart.click_proceed_to_checkout(self)
        Summary.validate_total_tax_is_present(self)
        Summary.validate_total_tax_is_present(self)

    def test_search_result__tc4(self,base_url):
        HomePage.search_text(self,"T-Shirt",base_url)
        HomePage.search_text_verifyResults(self)
        HomePage.click_product(self)
        AddtoCart.add_to_cart_button(self)
        AddtoCart.click_proceed_to_checkout(self)
        Summary.validate_total_tax_is_present(self)

    def test_search_result__tc4(self, base_url):
        HomePage.search_text(self, "Blouse", base_url)
        HomePage.search_text_verifyResults(self)
        HomePage.click_product(self)
        AddtoCart.add_to_cart_button(self)
        AddtoCart.click_proceed_to_checkout(self)
        Summary.validate_total_tax_is_present(self)

    def test_search_result__tc5(self, base_url):
        HomePage.search_text(self, "Invalid", base_url)
        HomePage.search_text_verifyResults(self)
        HomePage.click_product(self)
        AddtoCart.add_to_cart_button(self)
        AddtoCart.click_proceed_to_checkout(self)
        Summary.validate_total_tax_is_present(self)





