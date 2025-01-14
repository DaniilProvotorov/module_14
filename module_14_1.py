import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
#for i in range(10):
#    cursor.execute('''INSERT INTO Users (username, age, email, balance) VALUES (?, ?, ?, ?)''', (f'User{i+1}', f'{(i+1)*10}', f'example{i+1}@gmail.com', '1000'))

# a = 1
# for i in range(1, 11, 2):
#     cursor.execute('''UPDATE Users SET balance = ? WHERE id = ?''', ('500', a))
#     a += 2

# n = 1
# for i in range(1, 11, 3):
#     cursor.execute('''DELETE FROM Users WHERE id = ?''', (f'{n}',))
#     n += 3

cursor.execute('''SELECT username, email, age, balance FROM Users WHERE age != ?''', ('60',))
users = cursor.fetchall()
for user in users:
    print(user)


connection.commit()
connection.close()
