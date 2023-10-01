from bottle import route, post, run, template, redirect, request

import database

@route("/")
def get_index():
    redirect("/list")

@route("/list")
def get_list():
    rows = database.get_items()
    return template("list.tpl", shopping_list=rows)

@route("/add")
def get_add():
    return template("add_item.tpl")

@post("/add")
def post_add():
    description = request.forms.get("description")
    database.add_item(description)
    redirect("/list")

@route("/delete/<id>")
def get_delete(id):
    database.delete_item(id)
    redirect("/list")

@route("/update/<id>")
def get_update(id):
    rows = database.get_items(id)
    if len(rows) != 1:
        redirect("/list")
    description = rows[0]['description']
    return template("update_item.tpl", id=id, description=description)

@post("/update")
def post_update():
    description = request.forms.get("description")
    id = request.forms.get("id")
    database.update_item(id, description)
    redirect("/list")

run(host='localhost', port=8080)