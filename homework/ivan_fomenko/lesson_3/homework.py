# Даны 2 числа a и b. Получить их сумму, разность и произведение.
a = 5
b = 5

summ_nembers = a + b
diff_numbers = a - b
prod_numbers = a * b

print(f'Сумма: {summ_nembers}')
print(f'Разность: {diff_numbers}')
print(f'Произведение: {prod_numbers}')


# Даны числа x и y. Получить x − y / 1 + xy
x = 10
y = 5

expr_result = (x - y) / (1 + x * y)

print(f'Результаты выражения: {expr_result}')


# Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел.
c = 5
b = 7

arithmetic_mean = (c + b) / 2
geometric_mean = (c * b) ** 0.5

print(f'Среднее арифметическое равно {arithmetic_mean}')
print(f'Среднее геометрическое равно {geometric_mean}')


# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь/
katet_1 = 4
katet_2 = 5

gipotenuza = (katet_1**2 + katet_2**2) ** 0.5
ploshad = katet_1 * katet_2 / 2

print(f'Гипотенуза прямоугольного треугольника равна {gipotenuza}')
print(f'Площадь прямоугольного треугольника равна {ploshad}')
