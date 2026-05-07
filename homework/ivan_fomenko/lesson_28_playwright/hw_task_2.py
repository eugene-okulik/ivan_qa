from playwright.sync_api import Page, expect


def test_filling_full_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_placeholder('First Name').fill('Dratuti')
    page.get_by_placeholder('Last Name').fill('Dratututovich')
    page.locator('#userEmail').fill('pocket@gmail.com')
    page.locator('#gender-radio-1').check()
    page.get_by_placeholder('Mobile Number').fill('1234567890')
    page.locator('#dateOfBirthInput').fill('01 Jan 2000')

    subj = page.locator('#subjectsInput')
    subj.fill('English')
    subj.press('Enter')

    page.locator('#hobbies-checkbox-1').check()
    page.get_by_placeholder('Current Address').fill('Itlay, Freedom Square, 1')

    state = page.locator('#react-select-3-input')
    state.fill('NCR')
    state.press('Enter')

    city = page.locator('#react-select-4-input')
    city.fill('Delhi')
    city.press('Enter')

    page.get_by_role('button', name='submit').click()

    expect_msg = 'Thanks for submitting the form'
    expect(page.get_by_text(expect_msg)).to_be_visible()
