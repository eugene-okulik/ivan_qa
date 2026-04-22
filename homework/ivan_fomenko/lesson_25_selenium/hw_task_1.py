from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)
driver.get('https://www.qa-practice.com/elements/input/simple')

TEST_TEXT = 'Hello_world'

TEXT_AREA = driver.find_element(By.ID, 'id_text_string')
TEXT_AREA.send_keys(TEST_TEXT)
TEXT_AREA.submit()

RESULT_TEXT = driver.find_element(By.ID, 'result-text').text
print(f'Был введен текст: {RESULT_TEXT}')

assert RESULT_TEXT == TEST_TEXT, (
    'Текст некорректный\n'
    f'Ожидаемый текст {TEST_TEXT}\n'
    f'Полученный текст {RESULT_TEXT}'
)
