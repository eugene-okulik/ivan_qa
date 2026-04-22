from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--start-maximized')
    chrome_driver = webdriver.Chrome(options=options)

    chrome_driver.implicitly_wait(10)
    chrome_driver.get('https://demoqa.com/automation-practice-form')

    yield chrome_driver
    chrome_driver.quit()


def test_fill_form(driver):
    wait = WebDriverWait(driver, 10)

    # базовые поля
    driver.find_element(By.ID, 'firstName').send_keys('Ivan')
    driver.find_element(
        By.CSS_SELECTOR, "input[placeholder='Last Name']"
    ).send_keys('Ivanov')
    driver.find_element(
        By.CSS_SELECTOR, "input[placeholder='name@example.com']"
    ).send_keys('ivanov@example.com')
    driver.find_element(
        By.ID, 'gender-radio-1'
    ).click()
    driver.find_element(
        By.XPATH, '//input[@placeholder="Mobile Number"]'
    ).send_keys('1234567890')

    # subj, hobbie, address
    SUBJECT_FIELD = driver.find_element(
        By.ID, 'subjectsInput')
    SUBJECT_FIELD.send_keys('Maths')
    SUBJECT_FIELD.send_keys(Keys.ENTER)

    # hobbies, address
    driver.find_element(
        By.CSS_SELECTOR, "input[value='3']"
    ).click()
    driver.find_element(
        By.ID, 'currentAddress'
    ).send_keys('ул. Пушкина. Дом колотушкина')

    # state
    STATE = driver.find_element(
        By.ID, 'react-select-3-input'
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", STATE)
    STATE.send_keys('NCR', Keys.ENTER)

    # city
    driver.find_element(
        By.ID, 'react-select-4-input'
    ).send_keys('Delhi', Keys.ENTER)

    # submit
    SUBMIT = driver.find_element(By.ID, 'submit')
    driver.execute_script("arguments[0].scrollIntoView(true);", SUBMIT)
    driver.execute_script("arguments[0].click();", SUBMIT)

    # ждем форму и проверяем результат
    wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, 'example-modal-sizes-title-lg'),
            'Thanks for submitting the form'
        )
    )

    CHECK_RESULT = wait.until(
        EC.presence_of_element_located((By.ID, 'example-modal-sizes-title-lg'))
    )
    assert CHECK_RESULT.text == 'Thanks for submitting the form'

    # печатаем результат
    rows = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '.table-responsive tbody tr')
        )
    )

    # print(f'что это {rows}')
    result_data = {}
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        if len(cells) == 2:
            label = cells[0].text.strip()
            value = cells[1].text.strip()
            result_data[label] = value
    print(f'Проверка данных: {result_data}')
