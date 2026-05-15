from playwright.sync_api import Page, expect, Route
import re
import json


def test_iphone_17(page: Page):

    def change_response(route: Route):
        response = route.fetch()
        data = response.json()
        digital_mat = data['body']['digitalMat'][0]
        digital_mat['familyTypes'][0]['productName'] = 'Яблокофон 17 Про'
        route.fulfill(
            status=response.status,
            body=json.dumps(data, ensure_ascii=False)
        )

    page.route(re.compile(r'/shop/api/digital-mat'), change_response)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('button', has_text='iPhone 17 Pro Max').click()
    test_locator = page.locator('[data-autom="DigitalMat-overlay-header-0-0"]')
    print(test_locator.text_content())
    expect(
        page.locator(
            '[data-autom="DigitalMat-overlay-header-0-0"]')
        ).to_have_text('Яблокофон 17 Про')
