from peewee import *

db = SqliteDatabase('shopping-list.db')
db.connect()

class Item(Model):
    description = CharField()
    class Meta:
        database = db # This model uses the "people.db" database.

def set_up_database():
    db.drop_tables([Item], safe=True)
    db.create_tables([Item])
    for description in ['apples', 'broccoli', 'pizza', 'tangerine', 'potatoes']:
        add_item(description)

def get_items(id=None):
    if id==None:
        items = Item.select()
    else:
        items = Item.select().where(Item.id == id)
    items = [
        {
            'id':item.id,
            'description':item.description
        }
        for item in items
    ]
    return items

def add_item(description):
    item = Item(description=description)
    item.save()

def update_item(id, description):
    item = Item.select().where(Item.id == id).get()
    item.description = description
    item.save()

def delete_item(id):
    #Item.delete().where(Item.id == id).execute()
    item = Item.select().where(Item.id == id).get()
    item.delete_instance()


def test_set_up_database():
    print("testing set_up_database()")
    set_up_database()
    items = get_items()
    assert len(items) == 5
    for item in items:
        assert type(item) is dict
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
