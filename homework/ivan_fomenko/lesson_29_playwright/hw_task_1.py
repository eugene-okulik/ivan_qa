from playwright.sync_api import Page, expect, Dialog


def test_alert(page: Page):
    def accept_dialog(dialog: Dialog):
        print(f'Alert message: {dialog.message}')
        dialog.accept()
    page.on('dialog', accept_dialog)
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.get_by_role('link', name='Click').click()

    result_text = page.locator('#result-text')
    expect(result_text).to_contain_text('Ok')
