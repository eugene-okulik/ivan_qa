import os
import csv
import dotenv
import mysql.connector as mysql
from checker_db import check_student_in_db, print_check_results

# загружаем .env файл
dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

# создаем путь к файлу Евгения
base_path = os.path.dirname((__file__))
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_path = os.path.join(
    homework_path, 'eugene_okulik', 'lesson_16', 'hw_data', 'data.csv'
)


# читаем csv файл
with open(eugene_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Пропускаем заголовок

    for row in csv_reader:
        results = check_student_in_db(row, cursor)
        print_check_results(results)
