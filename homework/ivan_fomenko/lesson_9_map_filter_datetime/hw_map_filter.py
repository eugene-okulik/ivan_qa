temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34,
    30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31,
    33, 31, 30, 32, 30, 28, 24, 23
]


# для себя написал черновой вариант
list_temp = []


def calc_date(example_list):
    for x in example_list:
        if x > 28:
            list_temp.append(x)


calc_date(temperatures)
print(f'список дней через функцию {list_temp}')


# MAP
# так не решить задачу судя по всему
# возвращает True False
hot_days_map = map(lambda x: x > 28, temperatures)
print(f'список через map {list(hot_days_map)}')

# FILTER
hot_days_filter = list(filter(lambda x: x > 28, temperatures))
print(f'список через filter {hot_days_filter}')


# min max avg temperature
print(f'Самая высокая температура в жарких днях: {max(hot_days_filter)}')
print(f'Самая низкая температура в жарких днях: {min(hot_days_filter)}')
print(f'Средняя температура в жарких днях: {round(sum(hot_days_filter) / len(hot_days_filter), 2)}')
