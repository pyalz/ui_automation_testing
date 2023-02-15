from selenium.webdriver.common.by import By

class HomeLocators:
    # All the object of the home page.
    _search_text_field = (By.ID, 'search_query_top')
    _search_button = (By.NAME, 'submit_search')
    _search_results = (By.XPATH, "//span[@class='available-now']")
    _quick_view = (By.XPATH, "//div[@class='product-container']")


class WomenDressLocators:
    _women_Button = (By.XPATH, "//a[@class='sf-with-ul'][contains(text(),'Women')]")
    _cat_name = (By.CLASS_NAME, 'cat-name')
    _sort_drop_down = (By.ID, 'selectProductSort')

class pdp:
    _frame = (By.CLASS_NAME,"fancybox-iframe")
    _add_to_cart = (By.XPATH, "//span[contains(text(),'Add to cart')]")
    _proceed_to_checkout = (By.XPATH, "//span[contains(text(),'Proceed to checkout')]")

class CartSummary:
    _total_price = (By.XPATH,"//td[@id='total_price_container']")
    _total_tax = (By.XPATH, "//td[@id='total_tax']")



