from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--start-maximized')
    chrome_driver = webdriver.Chrome(options=options)

    yield chrome_driver
    chrome_driver.quit()


def test_add_to_card(driver):
    driver.get('http://testshop.qa-practice.com/')
    wait = WebDriverWait(driver, 15)
    action = ActionChains(driver)

    # ищем товар, открываем в новой вкладке
    first_supply = driver.find_element(By.CLASS_NAME, 'oe_product')
    action.key_down(Keys.CONTROL)
    action.click(first_supply)
    action.key_up(Keys.CONTROL)
    action.perform()

    # переключаемся на новую вкладку
    driver.switch_to.window(driver.window_handles[1])

    # кликаем на Add to Cart + сохраняем название товара
    NAME_ITEM = driver.find_element(By.CSS_SELECTOR, '[itemprop="name"]').text
    print(NAME_ITEM)
    add_to_card = wait.until(
        EC.element_to_be_clickable((By.ID, 'add_to_cart'))
    )
    add_to_card.click()

    # ждем модалку и кликаем на Continue Shopping
    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.modal-content')
        )
    )
    continue_btn = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.btn.btn-secondary')
        )
    )
    continue_btn.click()
    # driver.close()

    # возвращаемся на 1 страницу
    driver.switch_to.window(driver.window_handles[0])

    # кликаем на корзину
    card_icon = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'o_wsale_my_cart'))
    )
    card_icon.click()

    # проверяем, что товар в корзине
    card_item = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, 'flex-grow-1'))
    )
    assert NAME_ITEM in card_item.text
