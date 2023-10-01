import sqlite3
connection = sqlite3.connect("pets.db")

cursor = connection.cursor()
result = cursor.execute("select * from pet")
data = result.fetchall()
print(data)
names = [item[0] for item in list(cursor.description)]
print(names)

print(list(zip(names, data[0])))