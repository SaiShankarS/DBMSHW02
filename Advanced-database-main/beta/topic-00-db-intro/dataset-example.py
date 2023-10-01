import dataset

db = dataset.connect('sqlite:///pets.db')

pet_table = db["pet"]

data = [dict(item) for item in pet_table.find()]

print(data)
