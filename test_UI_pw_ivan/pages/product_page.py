from pages.base_page import BasePage
from pages.locators import product_locators as loc
from playwright.sync_api import expect


class ProductPage(BasePage):
    PAGE_URL = '/shop/furn-9999-office-design-software-7?category=9'
    BREADCRUMBS_LOC = loc.breadcrumbs

    def verify_text_of_product(self, expected_text):
        self.verify_text(loc.name_of_product, expected_text)

    def verify_price_of_product(self, expected_price):
        self.verify_text(loc.price_of_product, expected_price)

    def add_product_to_cart(self):
        self.page.locator(loc.add_to_cart).click()

    def go_to_cart(self):
        self.page.locator(loc.btn_view_cart).click()

    def verify_product_in_cart(self, expected_product, expected_price):
        expect(self.page.locator(
            loc.product_in_cart)).to_contain_text(expected_product)
        expect(self.page.locator(
            loc.product_in_cart)).to_contain_text(expected_price)
