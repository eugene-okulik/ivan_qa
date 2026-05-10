from playwright.sync_api import Page, expect, BrowserContext


def test_click_new_page(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    link = page.locator('#new-page-button')
    with page.context.expect_page() as new_page:
        link.click()
    expected_text = new_page.value.locator('#result-text')
    expect(expected_text).to_have_text('I am a new page in a new tab')
