import json


with open('menu_items.json', 'r') as json_file:
    data = json.load(json_file)
    print(type(data))
    print(data)
    for key, value in data.items():
        print(f"{key}:{value} \n")
        print("-------")