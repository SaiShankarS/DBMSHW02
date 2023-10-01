import sqlite3

connection = sqlite3.connect("shopping-list.db")

def get_items(id=None):
    cursor = connection.cursor()
    if id == None:
        rows = cursor.execute("select id, description from item")
    else:
        rows = cursor.execute(f"select id, description from item where id={id}")

    rows = list(rows)
    rows = [ {'id':row[0], 'description':row[1]} for row in rows ]
    return rows

def setup_database():
    cursor = connection.cursor()
    try:
        cursor.execute("drop table item")
    except:
        pass
    cursor.execute("create table item(id integer primary key, description text)")
    for item in ['apples', 'broccoli', 'pizza', 'tangerines', 'potatoes']:
        cursor.execute(f"insert into item (description) values ('{item}')")
    connection.commit()

def add_item(description):
    cursor = connection.cursor()
    cursor.execute(f"insert into item (description) values ('{description}')")
    connection.commit()

def delete_item(id):
    cursor = connection.cursor()
    rows = cursor.execute(f"delete from item where id={id}")
    connection.commit()

def update_item(id, description):
    cursor = connection.cursor()
    cursor.execute(f"update item set description='{description}' where id={id}")
    connection.commit()

def test_get_items():
    print("testing get_items()")
    items = get_items()
    assert type(items) is list
    assert len(items) > 0
    for item in items:
        assert 'id' in item
        assert type(item['id']) is int
        assert 'description' in item
        assert type(item['description']) is str
    example_id = items[0]['id']
    example_description = items[0]['description']
    items = get_items(example_id)
    assert len(items) == 1
    assert example_id == items[0]['id']
    assert example_description == items[0]['description']

def test_setup_database():
    print("testing setup_database()")
    setup_database()
    items = get_items()
    assert len(items) == 5
    descriptions = [item['description'] for item in items]
    for description in ['apples', 'broccoli', 'pizza', 'tangerines', 'potatoes']:
        assert description in descriptions

def test_add_item():
    print("testing add_item()")
    setup_database()
    items = get_items()
    original_length = len(items)
    add_item("licorice")
    items = get_items()
    assert len(items) == original_length + 1
    descriptions = [item['description'] for item in items]
    assert "licorice" in descriptions

def test_delete_item():
    print("testing delete_item()")
    setup_database()
    items = get_items()
    original_length = len(items)
    deleted_description = items[1]['description']
    deleted_id = items[1]['id']
    delete_item(deleted_id)
    items = get_items()
    assert len(items) == original_length - 1
    for item in items:
        assert item['id'] != deleted_id
        assert item['description'] != deleted_description

def test_update_item():
    print("testing update_item()")
    setup_database()
    items = get_items()
    original_description = items[1]['description']
    original_id = items[1]['id']
    update_item(original_id,"new-description")
    items = get_items()
    found = False
    for item in items:
        if item['id'] == original_id:
            assert item['description'] == "new-description"
            found = True
    assert found

if __name__ == "__main__":
    test_get_items()
    test_setup_database()
    test_add_item()
    test_delete_item()
    test_update_item()
    print("done.")
