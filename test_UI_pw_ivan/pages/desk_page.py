from pages.base_page import BasePage
from pages.locators import desk_locators as loc
from playwright.sync_api import expect


class DeskPage(BasePage):
    PAGE_URL = '/shop/category/desks-1'
    BREADCRUMBS_LOC = loc.breadcrumbs

    def count_of_products(self, expected_count=9):
        count_on_page = self.page.locator(loc.count_of_products)
        expect(count_on_page).to_have_count(expected_count)

    def verify_attributes(self, expected_text):
        super().verify_text(loc.list_of_attributes, expected_text)

    def customize_desk(self, expected_text):
        self.page.locator(loc.checkbox_steel).click()

        # 1. Разделяем входную строку на имя и цену
        product_name, expected_price = expected_text.split("\n")

        # 2. Сужаем локатор по его названию внутри тега <a>
        target_product = self.page.locator(loc.customize_desk).filter(
            has=self.page.locator("a[itemprop='name']", has_text=product_name)
        )

        # 3. Ассерт проверяет только цену внутри этой карточки
        expect(target_product.locator(
            "span.oe_currency_value")).to_have_text(expected_price)

    def customization_desk(self):
        self.page.locator(loc.checkbox_steel).click()
        self.page.locator(loc.customize_desk).click()
        self.page.locator(loc.checkbox_black).click()
        self.page.locator(loc.add_to_card).click()
