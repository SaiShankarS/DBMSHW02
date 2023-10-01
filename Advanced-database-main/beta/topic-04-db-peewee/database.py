from peewee import *

db = SqliteDatabase('shopping-list.db')
db.connect()

class Item(Model):
    description = CharField()
    class Meta:
        database = db # this model uses the "people.db" database


def setup_database():
    Item.drop_table(safe=True)
    Item.create_table()
    for description in ['apples', 'broccoli', 'pizza', 'tangerines', 'potatoes']:
        add_item(description)

def get_items(id=None):
    if id == None:
        items = Item.select()
    else:
        items = Item.select().where(Item.id == id)
    items = [
        { 
            "id" : item.id,
            "description" : item.description
        }
        for item in items
    ]
    return items


def add_item(description):
    item = Item(description=description)
    item.save()

def delete_item(id):
    item = Item.select().where(Item.id == id).get()
    item.delete_instance()

def update_item(id, description):
    # item = Item.select().where(Item.id == id).get()
    # item.description = description
    # item.save()
    Item.update({Item.description: description}).where(Item.id == id).execute()

def test_setup_database():
    print("testing setup_database()")
    setup_database()
    items = get_items()
    assert len(items) == 5
    descriptions = [item['description'] for item in items]
    for description in ['apples', 'broccoli', 'pizza', 'tangerines', 'potatoes']:
        assert description in descriptions

def test_get_items():
    print("testing get_items()")
    setup_database()
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
    test_setup_database()
    test_get_items()
    test_add_item()
    test_delete_item()
    test_update_item()
    print("done.")
