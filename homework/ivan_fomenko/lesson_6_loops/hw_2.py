# программа для перебора последовательности от 1 до 100

# условия для работы программы:
# для кратных 3 должна писать "Fuzz" вместо числа
# для кратных 5 должна писать "Buzz" вместо числа
# для кратных 3 и 5 должна писать "FuzzBuzz" вместо числа
# иначе должна писать само число

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('FuzzBuzz', end=' ')
    elif number % 5 == 0:
        print('Buzz', end=' ')
    elif number % 3 == 0:
        print('Fuzz', end=' ')
    else:
        print(number, end=' ')
