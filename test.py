import json

with open('new_dict.json') as file:
    new_dict = json.load(file)

id = "244285"

if id in new_dict:
    print('Все есть')
else:
    print('Нету')