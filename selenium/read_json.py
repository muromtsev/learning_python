import json

with open('selenium/result.json', 'r') as file:
    data = json.load(file)

def read_json(json_data):
    for d in json_data:
        print(d['Name'])
        print(d['Price'])

read_json(data)
