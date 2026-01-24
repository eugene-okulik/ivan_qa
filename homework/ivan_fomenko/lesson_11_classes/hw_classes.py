class Book:
    material_page = 'Бумага'
    exist_text = True

    def __init__(
            self,
            book_name,
            author,
            pages,
            ISBN,
            reserved):
        self.book_name = book_name
        self.author = author
        self.pages = pages
        self.ISBN = ISBN
        self.reserved = reserved


# пишу список книг
Dostoevskyi_idiot = Book(
    'Idiot',
    'Dostoevskyi',
    350,
    '978-5-94708-243-2',
    True)

Tolkien_lord_of_the_ring = Book(
    'LOR',
    'Tolkien',
    1500,
    '978-5-17-106077-0',
    False)

Chehov_toska = Book(
    'Toska',
    'Chehov',
    550,
    '888-5-94708-243-8',
    False)

Gogol_igroki = Book(
    'Igroki',
    'Gogol',
    1050,
    '777-5-94708-243-8',
    False)

Pushin_osen = Book(
    'Osen',
    'Pushkin',
    2110,
    '111-5-94708-243-2',
    True)

# создаю список из книг
books_list = [
    Dostoevskyi_idiot,
    Tolkien_lord_of_the_ring,
    Chehov_toska,
    Gogol_igroki,
    Pushin_osen
]

# print в зависимости от reserved
for book in books_list:
    if book.reserved:
        print((f'Название: {book.book_name}, Автор: {book.author}, '
               f'страниц: {book.pages}, материал: {book.material_page}, '
               'зарезервинована'))
    else:
        print(f'Название: {book.book_name}, Автор: {book.author}, '
              f'страниц: {book.pages}, материал: {book.material_page}')


# 2 Задание


class SchoolBooks(Book):

    def __init__(
            self,
            book_name,
            author,
            pages,
            ISBN,
            reserved,
            school_predmet,
            school_class,
            school_homework):
        super().__init__(
            book_name,
            author,
            pages,
            ISBN,
            reserved)
        self.school_predmet = school_predmet
        self.school_class = school_class
        self.school_homework = school_homework


school_book_first = SchoolBooks(
    'Математика для школьников',
    'Иванова А.А.',
    301,
    '111-222-333',
    False,
    'Математика',
    '7 класс',
    False)

school_book_second = SchoolBooks(
    'История для школьников',
    'Петров А.А.',
    101,
    '000-42-333',
    True,
    'История',
    '10 класс',
    True)

school_book_list = [school_book_first, school_book_second]

# print в зависимости от reserved
for book in school_book_list:
    if book.reserved:
        print(f'Название: {book.book_name}, Автор: {book.author}, '
              f'страниц: {book.pages}, предмет: {book.school_predmet}, '
              f'класс: {book.school_class}, зарезервирована')
    else:
        print(f'Название: {book.book_name}, Автор: {book.author}, '
              f'страниц: {book.pages}, предмет: {book.school_predmet}, '
              f'класс: {book.school_class}')
