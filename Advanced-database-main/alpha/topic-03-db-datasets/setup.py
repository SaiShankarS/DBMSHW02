import sqlite3

connection = sqlite3.connect("shopping-list.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table list")
except:
    pass

cursor.execute("create table list(id integer primary key, description text)")

for item in ['apples', 'broccoli', 'pizza', 'tangerine', 'potatoes']:
    cursor.execute(f"insert into list (description) values ('{item}')")

connection.commit()
connection.close()
print("done.")
