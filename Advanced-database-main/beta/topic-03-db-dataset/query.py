import sqlite3

connection = sqlite3.connect("shopping-list.db")

cursor = connection.cursor()

rows = cursor.execute("select id, description from item")
rows = list(rows)

print(rows)

rows = [ {'id':row[0], 'description':row[1]} for row in rows ]

print(rows)
