from bottle import route, post, run, template, redirect, request
import sqlite3

connection = sqlite3.connect("shopping-list.db")

@route("/")
def get_index():
    return "Hello from the shopping list app"

@route("/list")
def get_list():
    cursor = connection.cursor()
    rows = cursor.execute("select id, description from list")
    rows = list(rows)
    rows = [ {'id' : row[0], 'description': row[1]} for row in rows ]
    return template("list.tpl", shopping_list=rows)

@route("/add")
def get_add():
    return template("add_item.tpl")

@post("/add")
def post_add():
    description = request.forms.get("description")
    cursor = connection.cursor()
    cursor.execute(f"insert into list(description) values ('{description}')")
    connection.commit()
    redirect("/list")    

@route("/update/<id>")
def get_update(id):
    cursor = connection.cursor()
    rows = cursor.execute(f"select id, description from list where id={id}")
    rows = list(rows)
    rows = [ {'id' : row[0], 'description': row[1]} for row in rows ]
    return template("update_item.tpl", item=rows[0])

@post("/update")
def post_update():
    description = request.forms.get("description")
    id = request.forms.get("id")
    cursor = connection.cursor()
    cursor.execute(f"update list set description='{description}' where id={id}")
    connection.commit()
    redirect("/list")    

@route("/delete/<id>")
def get_delete(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from list where id={id}")
    connection.commit()
    redirect("/list")


run(host='localhost', port=8080)