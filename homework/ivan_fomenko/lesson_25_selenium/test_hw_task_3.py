from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--start-maximized')
    chrome_driver = webdriver.Chrome(options=options)

    chrome_driver.implicitly_wait(10)
    yield chrome_driver


def test_clicking(driver):
    driver.get("https://www.qa-practice.com/elements/select/single_select")

    # find selector
    CHOOSE_LANG = driver.find_element(By.ID, 'id_choose_language')
    SELECT = Select(CHOOSE_LANG)
    SELECT.select_by_visible_text('JavaScript')

    # submit
    driver.find_element(By.CSS_SELECTOR, "input[name='submit']").click()

    # find modal window
    result = driver.find_element(By.ID, 'result')

    assert 'JavaScript' in result.text

    print(result.text)


def test_check_start_btn(driver):
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')

    # start btn
    START_BTN = driver.find_element(By.CSS_SELECTOR, '#start button')
    START_BTN.click()

    # wait until end
    wait.until(EC.text_to_be_present_in_element(
        (By.XPATH, "//div[@id='finish']/h4"),
        "Hello World!")
    )

    FINISH_TEXT = driver.find_element(By.XPATH, "//div[@id='finish']/h4")
    assert FINISH_TEXT.text == 'Hello World!'
