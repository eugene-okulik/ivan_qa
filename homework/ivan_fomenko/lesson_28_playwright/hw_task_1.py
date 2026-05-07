from playwright.sync_api import Page, expect


def test_filling_fields(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='username').fill('Sobaka-Babaka')
    page.get_by_role('textbox', name='password').fill('12345')
    page.get_by_role('button', name='Login').click()

    error_msg = page.get_by_text('Your username is invalid!')
    expect(error_msg).to_be_visible()
