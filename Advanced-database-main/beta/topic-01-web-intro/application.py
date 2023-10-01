from bottle import route, post, run, template, redirect, request

import sqlite3

connection = sqlite3.connect("shopping-list.db")

@route("/")
def get_index():
    return("hello from the shopping list app.")

@route("/list")
def get_list():
    cursor = connection.cursor()
    rows = cursor.execute("select id, description from item")
    rows = list(rows)
    rows = [ {'id':row[0], 'description':row[1]} for row in rows ]
    return template("list.tpl", shopping_list=rows)

@route("/add")
def get_add():
    return template("add_item.tpl")

@post("/add")
def post_add():
    description = request.forms.get("description")
    cursor = connection.cursor()
    cursor.execute(f"insert into item (description) values ('{description}')")
    connection.commit()
    redirect("/list")

@route("/delete/<id>")
def get_delete(id):
    cursor = connection.cursor()
    rows = cursor.execute(f"delete from item where id={id}")
    connection.commit()
    redirect("/list")

@route("/update/<id>")
def get_update(id):
    cursor = connection.cursor()
    rows = cursor.execute(f"select id, description from item where id={id}")
    rows = list(rows)
    if len(rows) != 1:
        redirect("/list")
    rows = [ {'id':row[0], 'description':row[1]} for row in rows ]
    description = rows[0]['description']
    return template("update_item.tpl", id=id, description=description)

@post("/update")
def post_update():
    description = request.forms.get("description")
    id = request.forms.get("id")
    cursor = connection.cursor()
    cursor.execute(f"update item set description='{description}' where id={id}")
    connection.commit()
    redirect("/list")

run(host='localhost', port=8080)