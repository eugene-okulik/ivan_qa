import os
import datetime
import re


# создаем путь к файлу Евгения
base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))

eugene_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
print(eugene_path)


# функция для вытаскивания даты из строки
def get_data(line_str):
    pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{6}'
    match = re.search(pattern, line_str)
    if match:
        data_str = match.group()
        date_obj = datetime.datetime.strptime(data_str, '%Y-%m-%d %H:%M:%S.%f')
        return date_obj
    else:
        print('Дата не найдена')
    return None


# функции для работы с датами
def plus_one_week(date_obj):
    return date_obj + datetime.timedelta(weeks=1)


def day_of_week(date_obj):
    return date_obj.strftime('%A')


def days_ago(date_obj):
    delta = datetime.datetime.now() - date_obj
    return delta.days


# читаем файл
with open(eugene_path, 'r', encoding='utf-8') as okulik_file:
    # записываю все строки файла в список
    list_of_lines = okulik_file.readlines()
    print(f'первая строка: {plus_one_week(get_data(list_of_lines[0]))}')
    print(f'вторая строка: {day_of_week(get_data(list_of_lines[1]))}')
    print(f'третья строка: {days_ago(get_data(list_of_lines[2]))}')
