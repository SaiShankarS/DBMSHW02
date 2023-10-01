import dataset

db = dataset.connect('sqlite:///shopping-list.db')

def get_items(id=None):
    list_table = db["list"]
    if id == None:
        rows = list_table.find()
    else:
        rows = list_table.find(id=id)
    rows = [dict(row) for row in rows]
    return rows

def add_item(description):
    list_table = db["list"]
    list_table.insert({"description":description})

def update_item(id, description):
    list_table = db["list"]
    list_table.update({
        "id":id,
        "description":description
        }, ['id'])

def delete_item(id):
    list_table = db["list"]
    list_table.delete(id=id)

def set_up_database():
    try:
        db["list"].drop()
    except:
        pass
    list_table = db["list"]
    for item in ['apples', 'broccoli', 'pizza', 'tangerine', 'potatoes']:
        list_table.insert({"description":item})

def test_set_up_database():
    print("testing set_up_database()")
    set_up_database()
    list_table = db["list"]
    items = list(list_table.find())
    assert len(items) == 5
    descriptions = [item['description'] for item in items]
    for description in ['apples', 'broccoli', 'pizza', 'tangerine', 'potatoes']:
        assert description in descriptions

def test_get_items():
    print("testing get_items()")
    items = get_items()
    assert type(items) is list
    assert len(items) > 0
    for item in items:
        assert type(item) is dict
        assert 'id' in item
        assert type(item['id']) is int
        assert 'description' in item
        assert type(item['description']) is str
    id = items[0]['id']
    description = items[0]['description']
    items = get_items(id)
    assert type(items) is list
    assert len(items) == 1
    assert items[0]['id'] == id
    assert items[0]['description'] == description

def test_add_item():
    print("testing add_item()")
    set_up_database()
    items = get_items()
    original_length = len(items)
    add_item("mango")
    items = get_items()
    assert len(items) == original_length + 1
    descriptions = [item['description'] for item in items]
    assert "mango" in descriptions

def test_update_item():
    print("testing update_item()")
    set_up_database()
    items = get_items()
    id = items[2]['id']
    description = items[2]['description']
    update_item(id, "chocolate")
    items = get_items()
    assert items[2]['description'] == "chocolate"

def test_delete_item():
    print("testing delete_item()")
    set_up_database()
    add_item("mango")
    items = get_items()
    for item in items:
        if item['description'] == 'mango':
            delete_item(item['id'])
    items = get_items()
    for item in items:
        assert item['description'] != 'mango'

if __name__ == "__main__":
    test_set_up_database()
    test_get_items()
    test_add_item()
    test_update_item()
    test_delete_item()
    print("done.")
