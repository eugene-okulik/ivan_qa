from pages.base_page import BasePage
from pages.locators import cart_locators as loc


class CartPage(BasePage):
    PAGE_URL = '/shop/cart'
    BREADCRUMBS_LOC = loc.breadcrumbs

    def verify_empty_cart(self, expected_text):
        self.verify_text(loc.text_is_empty, expected_text)
