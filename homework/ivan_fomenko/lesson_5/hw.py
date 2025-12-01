person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

# Задание 1
# распаковка списка person в переменные:
# name, last_name, city, phone, country

name = person[0]
last_name = person[1]
phone = person[2]
city = person[3]
country = person[4]


# Задание 2
# Получить число из строки

test_str_1 = 'результат операции: 42'
test_str_2 = 'результат операции: 514'
test_str_3 = 'результат работы программы: 9'

# Реализовал через список, но понял что это не то что нужно было
# str_1_plus = int(test_str_1.split()[-1]) + 10
# str_2_plus = int(test_str_2.split()[-1]) + 10
# str_3_plus = int(test_str_3.split()[-1]) + 10

# print(f'Значение 1: {str_1_plus}, значение 2: {str_2_plus}, значение 3: {str_3_plus}')


# Реализовал через index(), добавил 2 чтобы пропустить ":  "
index_1 = test_str_1.index(':') + 2
index_2 = test_str_2.index(':') + 2
index_3 = test_str_3.index(':') + 2

num_1 = int(test_str_1[index_1:]) + 10
num_2 = int(test_str_2[index_2:]) + 10
num_3 = int(test_str_3[index_3:]) + 10

print(f'Значение 1: {num_1}, значение 2: {num_2}, значение 3: {num_3}')


# Задание 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

# первый пришедший вариант, показался не универсальным
print(f'Students {students[0]}, {students[1]}, {students[2]} study these subjects: {subjects[0]}, {subjects[1]}, {subjects[2]}')

# второй вариант выглядит лучше на мой взгляд
students_str = ', '.join(students)
subjects_str = ', '.join(subjects)
print(f'Students {students_str} study these subjects: {subjects_str}')
