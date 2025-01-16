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

cursor.execute('''DELETE FROM Users ''')

for i in range(10):
    cursor.execute('''INSERT INTO Users (username, age, email, balance) VALUES (?, ?, ?, ?)''', (f'User{i+1}', f'{(i+1)*10}', f'example{i+1}@gmail.com', '1000'))


for j in range(1, 11, 2):
    cursor.execute('''UPDATE Users SET balance = ? WHERE id = ? ''', ('500', j))


for k in range(1, 11, 3):
    cursor.execute('''DELETE FROM Users WHERE id = ?''', (f'{k}',))


cursor.execute('''SELECT username, email, age, balance FROM Users WHERE age != ?''', ('60',))
users = cursor.fetchall()
for user in users:
    print(user)


connection.commit()
connection.close()
