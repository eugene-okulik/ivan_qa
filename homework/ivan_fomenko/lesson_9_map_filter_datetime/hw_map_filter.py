temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

#С помощью функции map или filter создайте из этого списка новый список с жаркими днями. Будем считать жарким всё, что выше 28.

# Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.

# для себя написал черновой вариант
list_temp = []
def calc_date(example_list):
    for x in example_list:
        if x > 28:
            list_temp.append(x)

calc_date(temperatures)
print(f'список дней через функцию {list_temp}')


# MAP
# пообщался с чатомГПТ понял, что этот вариант плохой и нельзя так решить задачу
hot_days_map = map(lambda x: x > 28, temperatures)
print(f'список через map {list(hot_days_map)}')


# FILTER
hot_days_filter = list(filter(lambda x: x > 28, temperatures))
print(f'список через filter {hot_days_filter}')
