import json

data = {
    'first_name': 'Eugene',
    'last_name': 'Petrov',
    'age': 35,
    'hobbies': [
        'guitar',
        'cars',
        'mountains',
        'adventures'
    ]
}

# конвертація словника у рядок формату JSON
json_data = json.dumps(data)
print(json_data)

# конвертація словника у рядок формату JSON та записом даного тексту у файл.
with open('data/output.json', 'w') as f:
    # передаємо словник (що хочемо конвертувати в JSON) та файловий дескриптор
    # (куди хочемо записати)
    json.dump(data, f, indent=4)
