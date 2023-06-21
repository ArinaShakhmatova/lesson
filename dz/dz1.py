
# import sqlite3
# from pprint import pprint
#
#
# def users_gen():
#     gender, name, blood_type, citizenship = "", "", "", ""
#     return User(gender, name, blood_type, citizenship)
#
#
# class User:
#     def __init__(self, gender, name, blood_type, citizenship):
#         self.gender = gender
#         self.name = name
#         self.blood_type = blood_type
#         self.citizenship = citizenship
#
#
# def create_table_users(cursor):
#     command = """
#     CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY,
#     gender TEXT,
#     name TEXT,
#     blood_type TEXT,
#     citizenship TEXT
#     )
#     """
#
#     cursor.execute(command)
#
#
# def add_user(cursor, user):
#     command = """
#     INSERT INTO users(gender, name, blood_type, citizenship) VALUES (?, ?, ?, ?);
#     """
#
#     cursor.execute(command, (user.gender, user.name, user.blood_type, user.citizenship))
#
#
# def print_users(cursor):
#     command = """
#     SELECT * FROM users WHERE gender = 'мальчик'
#     """
#     result = cursor.execute(command)
#     users = result.fetchall()
#     pprint(users)
#
#
# with sqlite3.cogitnnect('database.db') as cursor:
#     create_table_users(cursor)
#     add_user(cursor, User("мальчик", "Толя", "III", "Монгольская Империя"))
#     add_user(cursor, User("девочка", "Диана", "IV", "Римская империя"))
#     add_user(cursor, User("девочка", "Маша", "II", "Единый Орден"))
#     add_user(cursor, User("мальчик", "Матвей", "III", "Арстоцка"))
#     print_users(cursor)

# try:
# connection = sqlite3.connect('database.db')
# cursor = connection.cursor()
# except sqlite3.DatabaseError:
# print("Connection error")
# finally:
# connection.close()

def g(n):
    if n == n[::-1]:
        return True
    else:
        return False

n = str(input())
l = g(n)
print(l)

