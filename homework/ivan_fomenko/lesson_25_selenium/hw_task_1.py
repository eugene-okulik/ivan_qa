from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)
driver.get('https://www.qa-practice.com/elements/input/simple')

TEST_TEXT = 'Hello_world'

text_area = driver.find_element(By.ID, 'id_text_string')
text_area.send_keys(TEST_TEXT)
text_area.submit()

result_text = driver.find_element(By.ID, 'result-text').text
print(f'Был введен текст: {result_text}')

assert result_text == TEST_TEXT, (
    'Текст некорректный\n'
    f'Ожидаемый текст {TEST_TEXT}\n'
    f'Полученный текст {result_text}'
)
