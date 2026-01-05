# программа для добавления "ing" в конец каждого слова

# Условия для работы программы:
# знаки препинания не пишутся внутри слов
# если идет запятая или точка после слова, то знак идет после "ing"


my_string = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
             "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
)

# вариант с использованием печати внутри цикла
for word in my_string.split():
    if word[-1] in ',.':
        print(word[:-1] + 'ing' + word[-1], end=' ')
    else:
        print(word + 'ing', end=' ')

# вариант с созданием нового списка
result_str = []
for word in my_string.split():
    if word[-1] in ',.':
        result_str.append(word[:-1] + 'ing' + word[-1])
    else:
        result_str.append(word + 'ing')

print(f"\n\n\nвторой вариант: {' '.join(result_str)}")
