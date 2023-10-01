from bottle import route, run, template
import sqlite3
connection = sqlite3.connect("pets.db")

# @route('/hello/<name>')
# def index(name):
#     return template('<b>Hello {{name}}</b>!', name=name)

@route("/")
def get_index():
    return template("<b>Yo, there {{name}}!!!</b>", name="index")

pets = [
    {'id':1, "name":"Dorothy", "kind":"dog"},
    {'id':2, "name":"Casey", "kind":"dog"},
    {'id':3, "name":"Flipper", "kind":"fish"},
    {'id':4, "name":"Cowabelle", "kind":"cow"}
]

@route("/hello/<name>")
def get_hello(name):
    return template("hello.tpl", name=name)

@route("/pets")
def get_pets():
    cursor = connection.cursor()
    result = cursor.execute("select * from pet")
    data = result.fetchall()
    names = [item[0] for item in list(cursor.description)]
    return template("pets.tpl", names=names, data=data)

run(host='localhost', port=8080)