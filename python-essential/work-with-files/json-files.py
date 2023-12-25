import json

filename = 'my-files/my_file.json'

with open(filename, 'r') as file:
    data = json.load(file)
print(data)

data.append({"name": 'Alex', "age": 45})
print(data)

with open('my-files/my_file2.json', 'w') as file:
    json.dump(data, file)
