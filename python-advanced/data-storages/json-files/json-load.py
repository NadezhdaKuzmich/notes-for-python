import json

json_data = '{"first_name": "Eugene"}'
# конвертація рядка формату JSON на словник (dict).
data = json.loads(json_data)
print(data)
print(data['first_name'])

with open('data/output.json', 'r') as f:
    # конвертація рядка формату JSON, записаного у файлі у словник.
    # полегшує роботу з JSON файлами, щоб не читати вміст самому і не
    # передавати в json.loads, а виконати цю операцію у межах однієї команди.
    data = json.load(f)
    print(data)
