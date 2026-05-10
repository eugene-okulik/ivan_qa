from playwright.sync_api import Page, expect
import re


def test_check_color_btn(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    change_color_btn = page.locator('#colorChange')
    expect(change_color_btn).to_have_class(
        re.compile(r'text-danger'), timeout=6000
    )
    change_color_btn.click()
