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
# for i in range(10):
#     cursor.execute('''UPDATE Users SET balance = ? WHERE id = ?''', ('500', a))
#     a += 2

# n = 1
# for i in range(10):
#     cursor.execute('''DELETE FROM Users WHERE id = ?''', (f'{n}',))
#     n += 3

# cursor.execute('''SELECT username, email, age, balance FROM Users WHERE age != ?''', ('60',))
# users = cursor.fetchall()
# for user in users:
#     print(user)

cursor.execute('''DELETE FROM Users WHERE id = ?''', ('6',))
cursor.execute('''SELECT COUNT(*) FROM Users ''')
total_users = cursor.fetchone()[0]
print(f"всего людей: {total_users}")
cursor.execute('''SELECT SUM(balance) FROM Users''')
all_balance = cursor.fetchone()[0]
print(f'общий баланс: {all_balance}')
print(f'средний баланс: {all_balance/total_users}')




connection.commit()
connection.close()

