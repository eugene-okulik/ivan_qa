from random import choice, randrange

salary = int(input('Fill your salary: '))
bonus = choice([True, False])
final_salary = salary

print(f'salary: {salary}, bonus: {bonus}')

if bonus == True:
    final_salary = salary + randrange(5000, 15000)
    print(f'Salary with bonus: {final_salary}')
else:
    print(f'Salary without bonus: {final_salary}')
