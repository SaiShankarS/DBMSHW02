import sqlite3

connection = sqlite3.connect("shopping-list.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table item")
except:
    pass

cursor.execute("create table item(id integer primary key, description text)")

for item in ['apples', 'broccoli', 'pizza', 'tangerines', 'potatoes']:
    cursor.execute(f"insert into item (description) values ('{item}')")

connection.commit()
connection.close()
