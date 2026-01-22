# Задание на декораторы 3
# Напишите программу: Есть функция которая делает одну из арифметических операций с переданными
# ей числами (числа и операция передаются в аргументы функции). Функция выглядит примерно так:

# def calc(first, second, operation):
#     if operation == '+':
#         return first + second
#     elif .....
# Программа спрашивает у пользователя 2 числа (вне функции)

# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:

# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение

first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
# operation = input('Введите арифимитечкий оператор: ')


def choice_operator(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            operation = '*'
            return func(first, second, operation)
        elif first == second:
            operation = '+'
            return func(first, second, operation)
        elif first > second:
            operation = '-'
            return func(first, second, operation)
        elif first < second:
            operation = '/'
            return func(first, second, operation)
        else:
            print('Для таких чисел нет арифмитического действия')
    return wrapper


@choice_operator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second
    else:
        print('Не знаю такого оператора')


print(calc(first, second, ''))
