def check_student_in_db(student_info_list, cursor):

    # вытаскиваем данные из списка
    (
        name, second_name, group_title, book_title,
        subject_title, lesson_title, mark_value
    ) = student_info_list

    # Словарь для накопления результатов проверок
    results = {
        'student_name': f'{name} {second_name}',
        'checks': []
    }

    # 1 проверяем таблицу students
    sql_query_students = '''
    SELECT * FROM students
    WHERE name = %s AND second_name = %s;
    '''

    cursor.execute(sql_query_students, (name, second_name))
    student_result = cursor.fetchall()
    if student_result:
        results['checks'].append({
            'name': 'студент',
            'passed': True,
            'message': (
                f'Студент {name} {second_name}'
                f'найден в таблице students'
            )
        })
    else:
        results['checks'].append({
            'name': 'студенты',
            'passed': False,
            'message': (
                f'Студент {name} {second_name}'
                f'не найден в таблице students'
            )
        })
        return results  # Нет смысла проверять остальное, если студента нет

    # 2 проверяем таблицу groups и сверяем с group_id в students
    sql_query_groups = '''
    SELECT g.title FROM `groups` AS g
    JOIN students AS s
        ON s.group_id = g.id
    WHERE s.name = %s AND s.second_name = %s AND g.title = %s;
    '''
    cursor.execute(sql_query_groups, (name, second_name, group_title))
    group_result = cursor.fetchall()
    if group_result:
        results['checks'].append({
            'name': 'группы',
            'passed': True,
            'message': f'Группа {group_title} найдена'
        })
    else:
        results['checks'].append({
            'name': 'группы',
            'passed': False,
            'message': f'Группа {group_title} не найдена'
        })

    # 3 проверяем таблицу books и сверяем с taken_by_student_id в students
    sql_query_books = '''
    SELECT b.title FROM books AS b
    JOIN students AS s
        ON s.id = b.taken_by_student_id
    WHERE s.name = %s AND s.second_name = %s AND b.title = %s;
    '''
    cursor.execute(sql_query_books, (name, second_name, book_title))
    book_result = cursor.fetchall()
    if book_result:
        results['checks'].append({
            'name': 'книги',
            'passed': True,
            'message': f'Книга {book_title} найдена'
        })
    else:
        results['checks'].append({
            'name': 'книги',
            'passed': False,
            'message': f'Книга {book_title} не найдена'
        })

    # 4 проверяем таблицу subjects и сверяем с subject_id в lessons
    sql_query_subjects = '''
    SELECT sub.title FROM subjects AS sub
    JOIN lessons AS l
        ON l.subject_id = sub.id
    WHERE l.title = %s AND sub.title = %s;
    '''
    cursor.execute(sql_query_subjects, (lesson_title, subject_title))
    subject_result = cursor.fetchall()
    if subject_result:
        results['checks'].append({
            'name': 'предметы',
            'passed': True,
            'message': (
                f'Предмет {subject_title}'
                f'найден для урока {lesson_title}')
        })
    else:
        results['checks'].append({
            'name': 'предметы',
            'passed': False,
            'message': (
                f'Предмет {subject_title} не найден '
                f'для урока {lesson_title}'
            )
        })

    # 5 проверяем таблицу marks и сверяем lesson_id и value
    sql_query_marks = '''
    SELECT m.value FROM marks AS m
    JOIN lessons AS l
        ON l.id = m.lesson_id
    WHERE m.value = %s AND l.title = %s;
    '''
    cursor.execute(sql_query_marks, (mark_value, lesson_title))
    mark_result = cursor.fetchall()
    if mark_result:
        results['checks'].append({
            'name': 'оценки',
            'passed': True,
            'message': f'Оценка {mark_value} найдена для урока {lesson_title}'
        })
    else:
        results['checks'].append({
            'name': 'оценки',
            'passed': False,
            'message': f'НЕТ оценки {mark_value} для урока {lesson_title}'
        })
    return results


def print_check_results(check_result):
    student_name = check_result['student_name']
    failed_checks = [
        check for check in check_result['checks'] if not check['passed']
    ]

    print(f"\n{'='*60}")
    print(f"Студент: {student_name}")
    print(f"{'='*60}")

    for check in check_result['checks']:
        status = 'OK' if check['passed'] else 'НЕТ ДАННЫХ'
        print(f"{status} - {check['message']}")

    if failed_checks:
        failed_names = ', '.join([ch['name'] for ch in failed_checks])
        print(
            f"\nДля студента {student_name}",
            f"не были найдены данные: {failed_names}"
        )
    else:
        print(f"\nВсе проверки пройдены успешно для {student_name}")
    print(f"{'='*60}\n")
