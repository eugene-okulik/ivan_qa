my_dict = {'tuple': (1, 2, 3, 4, 5),
           'list': [1, 2, 3, 4, 5],
           'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
           'set': {1, 2, 3, 4, 5}}

# Для того, что хранится под ключом ‘tuple’: выведите на экран последний элемент
print(my_dict['tuple'][-1])

# Для того, что хранится под ключом ‘list’:
# добавьте в конец списка еще один элемент
#  удалите второй элемент списка
new_element_to_list = my_dict['list'].append(6)
pop_element_from_list = my_dict['list'].pop(1)
print(my_dict['list'])

# Для того, что хранится под ключом ‘dict’:
# добавьте элемент с ключом ('i am a tuple',) и любым значением,
# удалите какой-нибудь элемент
my_dict['dict'][('i am a tuple',)] = 999
my_dict['dict'].pop('b')
print(my_dict['dict'])

# Для того, что хранится под ключом ‘set’:
# добавьте новый элемент в множество,
# удалите элемент из множества
my_dict['set'].add(6)
my_dict['set'].remove(2)
print(my_dict['set'])

print(my_dict)
