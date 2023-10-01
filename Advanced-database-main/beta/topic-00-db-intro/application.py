from bottle import route, run, template
import sqlite3
connection = sqlite3.connect("pets.db")

# @route('/hello/<name>')
# def index(name):
#     return template('<b>Hello {{name}}</b>!', name=name)

@route("/")
def get_index():
    return "Hello, there!"

@route("/hello/<name>")
def get_hello(name):
    return template("hello.tpl", name=name) 

# pets = [
#     {'id':1, "name":"Dorothy", "kind":"dog"},
#     {'id':2, "name":"Casey", "kind":"dog"},
#     {'id':3, "name":"Flipper", "kind":"fish"},
#     {'id':4, "name":"Cowabelle", "kind":"cow"}
# ]

@route("/pets")
def get_pets():
    cursor = connection.cursor()
    result = cursor.execute("select * from pet")
    data = result.fetchall()
    names = [item[0] for item in list(result.description)]
    pets = [dict(zip(names, item)) for item in data]
    return template("pets.tpl", pets=pets) 



run(host='localhost', port=8080)
