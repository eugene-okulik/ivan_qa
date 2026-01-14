def fibonachi_numbers():
    f1_num = 0
    f2_num = 1
    while True:
        f3_num = f1_num + f2_num
        yield f1_num
        f1_num = f2_num
        f2_num = f3_num


count = 1
for number in fibonachi_numbers():
    if count == 5:
        print(number)
    elif count == 200:
        print(number)
    elif count == 1000:
        print(number)
    elif count == 100000:
        # при печати выбивает ошибку из за ограничения длины строки
        print(number)
        break
    count += 1
