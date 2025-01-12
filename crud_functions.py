import sqlite3

connection = sqlite3.connect('tg_bot.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE  IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    )
    ''')
    connection.commit()

def add_product(title_product, description_product, price_product, id_product):
    check = cursor.execute('SELECT * FROM Products WHERE title=?', (title_product,))
    if check.fetchone() is None:
        cursor.execute(f'''INSERT INTO Products('title', 'description', 'price', 'id') VALUES (?, ?, ?, ?) ''', (f'{title_product}', f'{description_product}', f'{price_product}', f'{id_product}'))
    connection.commit()

def get_all_products():
    cursor.execute('''SELECT title, description, price FROM Products''')
    all_prod = cursor.fetchall()
    return all_prod


initiate_db()

add_product("Product1", "описание1", 100, 1)
add_product("Product2", "описание2", 200, 2)
add_product("Product3", "описание3", 300, 3)
add_product("Product4", "описание4", 400, 4)
prod = get_all_products()

connection.commit()
connection.close()