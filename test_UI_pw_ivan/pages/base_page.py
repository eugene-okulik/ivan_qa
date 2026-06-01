import re
from typing import Optional
from playwright.sync_api import Page, expect


class BasePage:
    BASE_URL = 'http://testshop.qa-practice.com'
    PAGE_URL = ''
    BREADCRUMBS_LOC: Optional[str] = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        if self.PAGE_URL:
            self.page.goto(f'{self.BASE_URL}{self.PAGE_URL}')
        else:
            self.page.goto(self.BASE_URL)

    def verify_title(self, expected_title):
        expect(self.page).to_have_title(expected_title)

    def verify_breadcrumbs(self, expected_breadcrumbs):
        if self.BREADCRUMBS_LOC is None:
            raise ValueError('BREADCRUMBS_LOC must be defined in subclass')

        pattern = ".*".join(expected_breadcrumbs.split("\n"))
        expect(self.page.locator(self.BREADCRUMBS_LOC)).to_have_text(
            re.compile(pattern, re.DOTALL)
        )

    def verify_text(self, locator, expected_text):
        expect(self.page.locator(locator)).to_have_text(expected_text)
