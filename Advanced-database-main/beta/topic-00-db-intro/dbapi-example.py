import sqlite3
connection = sqlite3.connect("pets.db")

cursor = connection.cursor()

result = cursor.execute("select * from pet")

print(result)

data = result.fetchall()
print(data)

names = [item[0] for item in list(result.description)]
print(names)

print(dict(zip(names, data[0])))

data = [dict(zip(names, item)) for item in data]

