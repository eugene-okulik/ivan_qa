from random import choice, randrange

salary = int(input('Enter your salary: '))
bonus = choice([True, False])
final_salary = salary

# проверяю есть ли бонус
print(f'salary: {salary}, bonus: {bonus}')

# расчитываем итоговую зп. flake8 жаловался, что я ставлю bonus == True
if bonus:
    final_salary = salary + randrange(5000, 15000)
    print(f'Salary with bonus: {final_salary}')
else:
    print(f'Salary without bonus: {final_salary}')
