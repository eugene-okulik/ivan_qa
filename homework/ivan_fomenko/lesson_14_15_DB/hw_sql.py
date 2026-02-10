import mysql.connector as mysql


# добавляем студента
# добавляем группу
# определяем добавленного студента в нашу группу
# создаем в базе 2 книги
# выдаем студенту эти книги
# создаем учебные предметы subjects
# создаем ПО 2 урока для КАЖДОГО из предметов
# ставим оценки студенту за эти уроки


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl',
)

cursor = db.cursor(dictionary=True)

# добавляем студента
add_student_query = '''
INSERT INTO students (name, second_name, group_id)
VALUES ('Гриба', 'Бас', 1);
'''
cursor.execute(add_student_query)
student_id = cursor.lastrowid
print(f'Добавлен студент с id: {student_id}')


# добавляем книги студенту
add_book_query_1 = '''
INSERT INTO books (title, taken_by_student_id)
VALUES ('Анегдоты про грибы', {student_id});'''
cursor.execute(add_book_query_1.format(student_id=student_id))
book_1_id = cursor.lastrowid
print(f'Добавлена первая книга с id: {book_1_id}')

add_book_query_2 = '''
INSERT INTO books (title, taken_by_student_id)
VALUES ('Грибы в лесу', {student_id});'''
cursor.execute(add_book_query_2.format(student_id=student_id))
book_2_id = cursor.lastrowid
print(f'Добавлена вторая книга с id: {book_2_id}')


# добавляем группу
add_group_query = '''
INSERT INTO `groups` (title, start_date, end_date)
VALUES ('Лесные грибы', '2024-01-01', '2029-12-31');'''
cursor.execute(add_group_query)
group_id = cursor.lastrowid
print(f'Добавлена группа с id: {group_id}')


# определяем студента в группу
assign_group_query = '''
UPDATE students
SET group_id = {group_id}
WHERE id = {student_id};'''
cursor.execute(
    assign_group_query.
    format(group_id=group_id, student_id=student_id)
    )
print(cursor.lastrowid)
print(f'Студент с id {student_id} добавлен в группу с id {group_id}')


# создаем учебные предметы subjects
add_subject_query_1 = '''
INSERT INTO subjects (title)
VALUES ('Какие грибы есть первыми?');
'''
cursor.execute(add_subject_query_1)
subject_1_id = cursor.lastrowid
print(f'Добавлен предмет с id: {subject_1_id}')

add_subject_query_2 = '''
INSERT INTO subjects (title)
VALUES ('Какие грибы есть вторыми?');
'''
cursor.execute(add_subject_query_2)
subject_2_id = cursor.lastrowid
print(f'Добавлен предмет с id: {subject_2_id}')


# создаем ПО 2 урока для КАЖДОГО из предметов
add_lesson_query_1 = '''
INSERT INTO lessons (title, subject_id)
VALUES ('Урок 1', {subject_id});'''
cursor.execute(add_lesson_query_1.format(subject_id=subject_1_id))
lesson_1_id = cursor.lastrowid
print(f'Добавлен урок с id: {lesson_1_id}, для предмета с id: {subject_1_id}')

add_lesson_query_2 = '''
INSERT INTO lessons (title, subject_id)
VALUES ('Урок 2', {subject_id});'''
cursor.execute(add_lesson_query_2.format(subject_id=subject_1_id))
lesson_2_id = cursor.lastrowid
print(f'Добавлен урок с id: {lesson_2_id}, для предмета с id: {subject_1_id}')


add_lesson_query_3 = '''
INSERT INTO lessons (title, subject_id)
VALUES ('Урок 3', {subject_id});'''
cursor.execute(add_lesson_query_3.format(subject_id=subject_2_id))
lesson_3_id = cursor.lastrowid
print(f'Добавлен урок с id: {lesson_3_id}, для предмета с id: {subject_2_id}')

add_lesson_query_4 = '''
INSERT INTO lessons (title, subject_id)
VALUES ('Урок 4', {subject_id});'''
cursor.execute(add_lesson_query_4.format(subject_id=subject_2_id))
lesson_4_id = cursor.lastrowid
print(f'Добавлен урок с id: {lesson_4_id}, для предмета с id: {subject_2_id}')


# ставим оценки студенту за эти уроки
add_mark_query_1 = '''
INSERT INTO marks (value, lesson_id, student_id)
VALUES (10, {lesson_id}, {student_id});'''
cursor.execute(
    add_mark_query_1.format(lesson_id=lesson_1_id, student_id=student_id)
)

add_mark_query_2 = '''
INSERT INTO marks (value, lesson_id, student_id)
VALUES (9, {lesson_id}, {student_id});'''
cursor.execute(
    add_mark_query_2.
    format(lesson_id=lesson_2_id, student_id=student_id)
)

add_mark_query_3 = '''
INSERT INTO marks (value, lesson_id, student_id)
VALUES (8, {lesson_id}, {student_id});
'''
cursor.execute(
    add_mark_query_3.
    format(lesson_id=lesson_3_id, student_id=student_id)
)

add_mark_query_4 = '''
INSERT INTO marks (value, lesson_id, student_id)
VALUES (7, {lesson_id}, {student_id});
'''
cursor.execute(
    add_mark_query_4.format(lesson_id=lesson_4_id, student_id=student_id)
)

db.commit()

db.close()
