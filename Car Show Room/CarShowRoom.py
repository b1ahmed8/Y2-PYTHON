import json

data = None

with open('data.json', 'r') as file:
    data = json.loads(file.read())

