import mysql.connector as mysql



db = mysql.connect(
    user = 'st-onl',
    passwd = 'AVNS_tegPDkI5BlB2lW5eASC',
    host = 'db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port = 25060,
    database = 'st-onl',
)

cursor = db.cursor(dictionary=True)
# cursor.execute('SELECT * FROM students LIMIT 10;')
# data = cursor.fetchall()
# print(data)
# for student in data:
#     [print(student['name'])]


# cursor.execute('SELECT * FROM students WHERE id = 22202;')
# data2 = cursor.fetchone()
# print(data2)


## иньекции
# f"SELECT * FROM users WHERE user = {user} AND password = {passwd}"
# query = "SELECT * FROM students WHERE name = '{0}' AND second_name = '{1}'"

# cursor.execute(query.format(input('name'), input('second_name')))


cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES ('Ivan', 'Privet', '1');")
student_id = cursor.lastrowid
cursor.execute(f"SELECT * FROM students WHERE id = {student_id};")
print(cursor.fetchone())

db.commit()
# print(cursor.fetchall())
db.close()