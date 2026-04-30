from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--start-maximized')
    chrome_driver = webdriver.Chrome(options=options)

    # chrome_driver.implicitly_wait(10)

    yield chrome_driver
    chrome_driver.quit()


def test_check_adding_to_card(driver):
    driver.get('http://testshop.qa-practice.com/')
    action = ActionChains(driver)
    wait = WebDriverWait(driver, 15)

    # наводим курсор на товар, жмем корзину
    TEXT_SUPPLY = driver.find_element(By.CLASS_NAME, 'text-primary').text
    icon_supply = driver.find_element(By.CLASS_NAME, 'oe_product')
    print(TEXT_SUPPLY)
    icon_card = driver.find_element(By.CSS_SELECTOR, "a.a-submit")
    action.move_to_element(icon_supply)
    action.move_to_element(icon_card)
    action.click()
    action.perform()

    # проверяем что это правильный товар
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, 'product-name'))
    )
    name_item = driver.find_element(By.CLASS_NAME, 'product-name').text
    assert TEXT_SUPPLY in name_item, 'Проверьте название товара'
