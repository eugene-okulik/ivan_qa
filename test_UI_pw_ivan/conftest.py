import pytest
from playwright.sync_api import BrowserContext
from pages.cart_page import CartPage
from pages.desk_page import DeskPage
from pages.product_page import ProductPage


@pytest.fixture()
def page(context: BrowserContext, playwright):
    playwright.selectors.set_test_id_attribute("id")
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture()
def cart_page(page):
    return CartPage(page)


@pytest.fixture()
def desk_page(page):
    return DeskPage(page)


@pytest.fixture()
def product_page(page):
    return ProductPage(page)
